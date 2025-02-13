import json
import logging
import os
import re
from functools import cached_property
from urllib.parse import urljoin

import importlib_metadata
import importlib_resources
import marshmallow as ma
from flask import current_app, request, url_for
from flask.ctx import RequestContext
from flask.globals import _cv_request
from flask_resources import (
    Resource,
    ResourceConfig,
    from_conf,
    request_parser,
    resource_requestctx,
    response_handler,
    route,
)
from flask_restful import abort
from invenio_base.utils import obj_or_import_string
from invenio_jsonschemas import current_jsonschemas
from invenio_records_resources.proxies import current_service_registry

logger = logging.getLogger("oarepo_runtime.info")


class InfoConfig(ResourceConfig):
    blueprint_name = "oarepo_runtime_info"
    url_prefix = "/.well-known/repository"

    schema_view_args = {"schema": ma.fields.Str()}
    model_view_args = {"model": ma.fields.Str()}

    def __init__(self, app):
        self.app = app

    @cached_property
    def components(self):
        return tuple(
            obj_or_import_string(x)
            for x in self.app.config.get("INFO_ENDPOINT_COMPONENTS", [])
        )


schema_view_args = request_parser(from_conf("schema_view_args"), location="view_args")
model_view_args = request_parser(from_conf("model_view_args"), location="view_args")


class InfoResource(Resource):
    def create_url_rules(self):
        return [
            route("GET", "/", self.repository),
            route("GET", "/models", self.models),
            route("GET", "/schema/<path:schema>", self.schema),
            route("GET", "/models/<model>", self.model),
        ]

    @cached_property
    def components(self):
        return [x(self) for x in self.config.components]

    @response_handler()
    def repository(self):
        """Repository endpoint."""
        links = {
            "self": url_for(request.endpoint, _external=True),
            "models": url_for("oarepo_runtime_info.models", _external=True),
        }
        try:
            import invenio_requests  # noqa
            links["requests"] = api_url_for("requests.search", _external=True)
        except ImportError:
            pass

        ret = {
            "name": current_app.config.get("THEME_SITENAME", ""),
            "description": current_app.config.get("REPOSITORY_DESCRIPTION", ""),
            "version": os.environ.get("DEPLOYMENT_VERSION", "local development"),
            "invenio_version": get_package_version("oarepo"),
            "transfers": [
                "local-file",
                "url-fetch",
                # TODO: where to get these? (permissions?)
                # "direct-s3",
            ],
            "links": links,
        }
        self.call_components("repository", data=ret)
        return ret, 200

    @response_handler(many=True)
    def models(self):
        data = []
        # iterate entrypoint oarepo.models
        for model in importlib_metadata.entry_points().select(group="oarepo.models"):
            package_name, file_name = model.value.split(":")
            model_data = json.loads(
                importlib_resources.files(package_name).joinpath(file_name).read_text()
            )
            model_data = model_data.get("model", {})
            if model_data.get("type") != "model":
                continue

            resource_config_class = self._get_resource_config_class(model_data)
            service = self._get_service(model_data)
            service_class = self._get_service_class(model_data)
            if not service or type(service) != service_class:
                continue

            # check if the service class is inside OAREPO_GLOBAL_SEARCH and if not, skip it
            global_search_models = current_app.config.get('GLOBAL_SEARCH_MODELS', [])
            for global_model in global_search_models:
                if global_model['model_service'] == model_data["service"]["class"]:
                    break
            else:
                continue

            model_features = self._get_model_features(model_data)

            links = {
                "api": self._get_model_api_endpoint(model_data),
                "html": self._get_model_html_endpoint(model_data),
                "schemas": self._get_model_schema_endpoints(model_data),
                "model": self._get_model_model_endpoint(model.name),
                # "openapi": url_for(self._get_model_openapi_endpoint(model_data), _external=True)
            }

            links["published"] = links["api"]
            if "drafts" in model_features:
                links["user_records"] = self._get_model_draft_endpoint(model_data)

            data.append(
                {
                    "name": model_data.get(
                        "model-name", model_data.get("module", {}).get("base", "")
                    ).lower(),
                    "description": model_data.get("model-description", ""),
                    "version": model_data["json-schema-settings"]["version"],
                    "features": model_features,
                    "links": links,
                    # TODO: we also need to get previous schema versions here if we support
                    # multiple version of the same schema at the same time
                    "accept": self._get_model_accept_types(service, resource_config_class),
                }
            )
        self.call_components("model", data=data)
        return data, 200

    @schema_view_args
    @response_handler()
    def schema(self):
        schema = resource_requestctx.view_args["schema"]
        return current_jsonschemas.get_schema(schema, resolved=True), 200

    @model_view_args
    @response_handler()
    def model(self):
        model = resource_requestctx.view_args["model"]
        for _model in importlib_metadata.entry_points().select(
                group="oarepo.models", name=model
        ):
            package_name, file_name = _model.value.split(":")
            model_data = json.loads(
                importlib_resources.files(package_name).joinpath(file_name).read_text()
            )
            return self._remove_implementation_details_from_model(model_data), 200
        abort(404)

    IMPLEMENTATION_DETAILS = re.compile(
        r"""
^(
  class | 
  .*-class |
  base-classes |
  .*-base-classes |
  module |
  generate |
  imports |
  extra-code |
  components |
  .*-args
)$
    """,
        re.VERBOSE,
    )

    def _remove_implementation_details_from_model(self, model):
        if isinstance(model, dict):
            return self._remove_implementation_details_from_model_dict(model)
        elif isinstance(model, list):
            return self._remove_implementation_details_from_model_list(model)
        else:
            return model

    def _remove_implementation_details_from_model_dict(self, model):
        ret = {}
        for k, v in model.items():
            if not self.IMPLEMENTATION_DETAILS.match(k):
                new_value = self._remove_implementation_details_from_model(v)
                if new_value is not None and new_value != {} and new_value != []:
                    ret[k] = new_value
        return ret

    def _remove_implementation_details_from_model_list(self, model):
        ret = []
        for v in model:
            new_value = self._remove_implementation_details_from_model(v)
            if new_value is not None and new_value != {} and new_value != []:
                ret.append(new_value)
        return ret

    def call_components(self, method_name, **kwargs):
        for component in self.components:
            if hasattr(component, method_name):
                getattr(component, method_name)(**kwargs)

    def _get_model_features(self, model):
        features = []
        if model.get("requests", {}):
            features.append("requests")
        if model.get("draft", {}):
            features.append("drafts")
        if model.get("files", {}):
            features.append("files")
        return features

    def _get_model_api_endpoint(self, model):
        try:
            alias = model["api-blueprint"]["alias"]
            return api_url_for(f"{alias}.search", _external=True)
        except:  # NOSONAR noqa
            logger.exception("Failed to get model api endpoint")
            return None

    def _get_model_draft_endpoint(self, model):
        try:
            alias = model["api-blueprint"]["alias"]
            return api_url_for(f"{alias}.search_user_records", _external=True)
        except:  # NOSONAR noqa
            logger.exception("Failed to get model draft endpoint")
            return None

    def _get_model_html_endpoint(self, model):
        try:
            return urljoin(
                self._get_model_api_endpoint(model),
                model["resource-config"]["base-html-url"],
            )
        except:  # NOSONAR noqa
            logger.exception("Failed to get model html endpoint")
            return None

    def _get_model_schema_endpoints(self, model):
        try:
            return {
                'application/json': url_for(
                    "oarepo_runtime_info.schema",
                    schema=model["json-schema-settings"]["name"],
                    _external=True,
                )
            }
        except:  # NOSONAR noqa
            logger.exception("Failed to get model schema endpoint")
            return None

    def _get_model_model_endpoint(self, model):
        try:
            return url_for("oarepo_runtime_info.model", model=model, _external=True)
        except:  # NOSONAR noqa
            logger.exception("Failed to get model model endpoint")
            return None

    def _get_model_accept_types(self, service, resource_config):
        try:
            record_cls = service.config.record_cls
            schema = getattr(record_cls, "schema", None)
            accept_types = []
            for accept_type, handler in resource_config.response_handlers.items():
                curr_item = {'accept': accept_type}
                if handler.serializer is not None and hasattr(handler.serializer, "info"):
                    curr_item.update(handler.serializer.info(service))
                accept_types.append(curr_item)

            return accept_types
        except:  # NOSONAR noqa
            logger.exception("Failed to get model schemas")
        return {}


    def _get_resource_config_class(self, model_data):
        model_class = model_data['resource-config']['class']
        return obj_or_import_string(model_class)()

    def _get_service(self, model_data):
        service_id = model_data["service-config"]["service-id"]
        try:
            service = current_service_registry.get(service_id)
        except KeyError:
            return None
        return service

    def _get_service_class(self, model_data):
        service_id = model_data["service"]["class"]
        return obj_or_import_string(service_id)


def create_wellknown_blueprint(app):
    """Create blueprint."""
    config_class = obj_or_import_string(
        app.config.get("INFO_ENDPOINT_CONFIG", InfoConfig)
    )
    return InfoResource(config=config_class(app)).as_blueprint()


def get_package_version(package_name):
    """Get package version."""
    from pkg_resources import get_distribution

    try:
        return re.sub(r"\+.*", "", get_distribution(package_name).version)
    except Exception:  # NOSONAR noqa
        logger.exception(f"Failed to get package version for {package_name}")
        return None


def api_url_for(endpoint, _external=True, **values):
    """API url_for."""
    try:
        api_app = current_app.wsgi_app.mounts["/api"]
    except:
        api_app = current_app

    site_api_url = current_app.config["SITE_API_URL"]
    site_url = current_app.config["SITE_UI_URL"]
    current_request_context = _cv_request.get()
    try:
        new_context = RequestContext(app=api_app, environ=request.environ)
        _cv_request.set(new_context)
        base_url = api_app.url_for(endpoint, **values, _external=_external)
        if base_url.startswith(site_api_url):
            return base_url
        if base_url.startswith(site_url):
            return base_url.replace(site_url, site_api_url)
        raise ValueError(
            f"URL {base_url} does not start with {site_url} or {site_api_url}"
        )
    finally:
        _cv_request.set(current_request_context)

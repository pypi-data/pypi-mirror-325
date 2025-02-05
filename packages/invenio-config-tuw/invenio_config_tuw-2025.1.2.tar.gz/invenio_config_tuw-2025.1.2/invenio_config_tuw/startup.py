# -*- coding: utf-8 -*-
#
# Copyright (C) 2022-2024 TU Wien.
#
# Invenio-Config-TUW is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Invenio-Config-TUW hacks and overrides to be applied on application startup.

This module provides a blueprint whose sole purpose is to execute some code exactly
once during application startup (via ``bp.record_once()``).
These functions will be executed after the Invenio modules' extensions have been
initialized, and thus we can rely on them being already available.
"""

from logging import ERROR
from logging.handlers import SMTPHandler

import importlib_metadata
from flask.config import Config
from invenio_rdm_records.services.search_params import MyDraftsParam
from invenio_requests.proxies import current_request_type_registry

from .curations import TUWCurationRequest
from .logs import DetailedFormatter


class TUWConfig(Config):
    """Override for the Flask config that evaluates the SITE_{API,UI}_URL proxies."""

    @classmethod
    def from_flask_config(cls, config):
        """Create a clone of the given config."""
        if isinstance(config, TUWConfig):
            return config

        return cls(config.root_path, config)

    def __getitem__(self, key):
        """Return config[key], or str(config[key]) if key is 'SITE_{UI,API}_URL'."""
        value = super().__getitem__(key)

        # give special treatment to the URL configuration items:
        # enforce their evaluation as strings
        if key in ("SITE_UI_URL", "SITE_API_URL"):
            value = str(value)

        return value


def register_smtp_error_handler(app):
    """Register email error handler to the application."""
    handler_name = "invenio-config-tuw-smtp-error-handler"

    # check reasons to skip handler registration
    error_mail_disabled = app.config.get("CONFIG_TUW_DISABLE_ERROR_MAILS", False)
    if app.debug or app.testing or error_mail_disabled:
        # email error handling should occur only in production mode, if not disabled
        return

    elif any([handler.name == handler_name for handler in app.logger.handlers]):
        # we don't want to register duplicate handlers
        return

    elif "invenio-mail" not in app.extensions:
        app.logger.warning(
            (
                "The Invenio-Mail extension is not loaded! "
                "Skipping registration of SMTP error handler."
            )
        )
        return

    # check if mail server and admin email(s) are present in the config
    # if not raise a warning
    if app.config.get("MAIL_SERVER") and app.config.get("MAIL_ADMIN"):
        # configure auth
        username = app.config.get("MAIL_USERNAME")
        password = app.config.get("MAIL_PASSWORD")
        auth = (username, password) if username and password else None

        # configure TLS
        secure = None
        if app.config.get("MAIL_USE_TLS"):
            secure = ()

        # initialize SMTP Handler
        mail_handler = SMTPHandler(
            mailhost=(app.config["MAIL_SERVER"], app.config.get("MAIL_PORT", 25)),
            fromaddr=app.config["SECURITY_EMAIL_SENDER"],
            toaddrs=app.config["MAIL_ADMIN"],
            subject=app.config["THEME_SITENAME"] + " - Failure",
            credentials=auth,
            secure=secure,
        )
        mail_handler.name = handler_name
        mail_handler.setLevel(ERROR)
        mail_handler.setFormatter(DetailedFormatter())

        # attach to the application
        app.logger.addHandler(mail_handler)

    else:
        app.logger.warning(
            "Mail configuration missing: SMTP error handler not registered!"
        )


def override_search_drafts_options(app):
    """Override the "search drafts" options to show all accessible drafts."""
    # doing this via config is (currently) not possible, as the `search_drafts`
    # property can't be overridden with a config item (unlike `search`, above it)
    # cf. https://github.com/inveniosoftware/invenio-rdm-records/blob/maint-10.x/invenio_rdm_records/services/config.py#L327-L332
    try:
        service = app.extensions["invenio-rdm-records"].records_service
        service.config.search_drafts.params_interpreters_cls.remove(MyDraftsParam)
    except ValueError:
        pass


def register_menu_entries(app):
    """Register the curation setting endpoint in Flask-Menu."""
    menu = app.extensions["menu"].root()
    menu.submenu("settings.curation").register(
        "invenio_config_tuw_settings.curation_settings_view",
        '<i class="file icon"></i> Curation',
        order=1,
    )


def customize_curation_request_type(app):
    """Override the rdm-curations request type with our own version."""
    current_request_type_registry.register_type(TUWCurationRequest(), force=True)


def override_flask_config(app):
    """Replace the app's config with our own override.

    This evaluates the ``LocalProxy`` objects used for ``SITE_{API,UI}_URL`` by
    casting them into strings (which is their expected type).
    """
    app.config = TUWConfig.from_flask_config(app.config)


def patch_flask_create_url_adapter(app):
    """Patch Flask's {host,subdomain}_matching with 3.1 behavior.

    See: https://github.com/pallets/flask/pull/5634

    This can be removed once we get Flask 3.1+ in.
    """
    flask_version = importlib_metadata.version("flask").split(".", 2)
    major = int(flask_version[0])
    minor = int(flask_version[1])
    if (major == 3 and minor >= 1) or (major > 3):
        app.logger.info(
            f"Flask version is {flask_version} (>= 3.1). "
            "Skipping monkey patching app.create_url_adapter()."
        )
        return

    def create_url_adapter(self, request):
        """Create a URL adapter for the given request.

        This function is from Flask 3.1, which is licensed under the 3-clause BSD.
        """
        if request is not None:
            subdomain = None
            server_name = self.config["SERVER_NAME"]

            if self.url_map.host_matching:
                # Don't pass SERVER_NAME, otherwise it's used and the actual
                # host is ignored, which breaks host matching.
                server_name = None
            elif not self.subdomain_matching:
                # Werkzeug doesn't implement subdomain matching yet. Until then,
                # disable it by forcing the current subdomain to the default, or
                # the empty string.
                subdomain = self.url_map.default_subdomain or ""

            return self.url_map.bind_to_environ(
                request.environ, server_name=server_name, subdomain=subdomain
            )

        # Need at least SERVER_NAME to match/build outside a request.
        if self.config["SERVER_NAME"] is not None:
            return self.url_map.bind(
                self.config["SERVER_NAME"],
                script_name=self.config["APPLICATION_ROOT"],
                url_scheme=self.config["PREFERRED_URL_SCHEME"],
            )

        return None

    app.create_url_adapter = create_url_adapter.__get__(app, type(app))

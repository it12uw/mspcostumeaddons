# Copyright 2018 Creu Blanca
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from threading import current_thread
from flectra import api, models, SUPERUSER_ID
from flectra.service import wsgi_server


class ResUsers(models.Model):
    _inherit = "res.users"

    # HACK https://github.com/flectra/flectra/issues/24183
    # TODO Remove in v12, and use normal flectra.http.request to get details
    @api.model_cr
    def _register_hook(self):
        """🐒-patch XML-RPC controller to know remote address."""
        super()._register_hook()
        original_fn = wsgi_server.application_unproxied

        def _patch(environ, start_response):
            current_thread().environ = environ
            return original_fn(environ, start_response)

        wsgi_server.application_unproxied = _patch

    @classmethod
    def _auth_check_remote(cls, login, method):
        """Force a method to raise an AccessDenied on falsey return."""
        with cls.pool.cursor() as cr:
            env = api.Environment(cr, SUPERUSER_ID, {})
            remote = env["res.users"].remote
            if remote:
                remote.ensure_one()
        return method()

    # Override all auth-related core methods
    @classmethod
    def _login(cls, db, login, password):
        return cls._auth_check_remote(
            login,
            lambda: super(ResUsers, cls)._login(db, login, password),
        )

    @classmethod
    def authenticate(cls, db, login, password, user_agent_env):
        return cls._auth_check_remote(
            login,
            lambda: super(ResUsers, cls).authenticate(
                db, login, password, user_agent_env),
        )

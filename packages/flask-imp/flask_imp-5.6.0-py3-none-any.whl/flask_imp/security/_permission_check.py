import typing as t
from functools import partial
from functools import wraps

from flask import abort
from flask import flash
from flask import redirect
from flask import session
from flask import url_for

from ._private_funcs import _check_against_values_allowed


def permission_check(
    session_key: str,
    values_allowed: t.Union[t.List[t.Union[str, int, bool]], str, int, bool],
    fail_endpoint: t.Optional[str] = None,
    endpoint_kwargs: t.Optional[t.Dict[str, t.Union[str, int]]] = None,
    message: t.Optional[str] = None,
    message_category: str = "message",
    abort_status: int = 403,
) -> t.Callable[..., t.Any]:
    """
    A decorator that checks if the specified session key exists and its value(s) match the specified value(s).

    *Example*::

        @bp.route("/admin-page", methods=["GET"])
        @login_check('logged_in', True, 'blueprint.login_page')
        @permission_check('permissions', ['admin'], fail_endpoint='www.index', message="Failed message")
        def admin_page():
            ...

    :param session_key: the session key to check for
    :param values_allowed: a list of or singular value(s) that the session key must contain
    :param fail_endpoint: the endpoint to redirect to if the
                          session key does not exist or does not contain the
                          specified values
    :param endpoint_kwargs: a dictionary of keyword arguments to pass to the redirect endpoint
    :param message: if a message is specified, a flash message is shown
    :param message_category: the category of the flash message
    :param abort_status: the status code to abort with if the session key does not exist or match the pass_value
    :return: The decorated function, or abort(abort_status) response
    """

    def permission_check_wrapper(func: t.Any) -> t.Callable[..., t.Any]:
        @wraps(func)
        def inner(*args: t.Any, **kwargs: t.Any) -> t.Any:
            skey = session.get(session_key)

            def setup_flash(
                _message: t.Optional[str], _message_category: t.Optional[str]
            ) -> None:
                if _message:
                    partial_flash = partial(flash, _message)
                    if _message_category:
                        partial_flash(_message_category)
                    else:
                        partial_flash()

            if skey:
                if _check_against_values_allowed(skey, values_allowed):
                    return func(*args, **kwargs)

            setup_flash(message, message_category)

            if fail_endpoint:
                if endpoint_kwargs:
                    return redirect(
                        url_for(
                            fail_endpoint,
                            _anchor=None,
                            _method=None,
                            _scheme=None,
                            _external=None,
                            **endpoint_kwargs,
                        )
                    )

                return redirect(url_for(fail_endpoint))

            return abort(abort_status)

        return inner

    return permission_check_wrapper

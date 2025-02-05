from functools import wraps
from typing import Any, Callable

from dlt.common.typing import TFun

from dlt_plus.common.constants import LICENSE_PUBLIC_KEY

from .license import (
    validate_license,
    discover_license,
    ensure_scope,
    get_scopes,
    ensure_feature_scope,
)


def require_license(scope: str) -> Callable[[TFun], TFun]:
    """Decorator that requires a valid license to execute the decorated function.

    Args:
        scope (str): The scope of the license required to execute the function.
            It is always a feature scope in form package.feature ie. `dlt_plus.sources.mssql`

    Returns:
        TFun: A decorator function that validates the license before executing the function.

    Raises:
        DltLicenseNotFoundException: If no license is found in environment or secrets.toml
        DltLicenseExpiredException: If the license has expired
        DltLicenseSignatureInvalidException: If the license signature is invalid
    """
    ensure_feature_scope(scope)

    def decorator(func: TFun) -> TFun:
        @wraps(func)
        def wrapper_func(*args: Any, **kwargs: Any) -> Any:
            license_string = discover_license()
            license = validate_license(LICENSE_PUBLIC_KEY, license_string)
            scopes = get_scopes(license)
            ensure_scope(scopes, scope)
            return func(*args, **kwargs)

        return wrapper_func  # type: ignore[return-value]

    return decorator

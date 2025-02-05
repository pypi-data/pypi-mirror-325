import os
import re

from typing import Any, Dict

from dlt.common.typing import REPattern
from dlt.common.utils import map_nested_in_place


class InterpolateEnvironmentVariables:
    # TODO: use the same interpolation as rest api source: {var_name} which is more Pythonic
    # TOOO: introduce late binding for secrets, currently we resolve ENV VARS when loading
    _DEFAULT_PATTERN = re.compile(r"\$\{([^}^{]+)\}")  # Find ${VAR_NAME}

    def __init__(self, extra_vars: Dict[str, Any] = None, pattern: REPattern = None):
        if pattern is None:
            pattern = self._DEFAULT_PATTERN
        self.pattern = pattern
        self.extra_vars = extra_vars or {}

    def interpolate(self, data: Dict[str, Any]) -> Dict[str, Any]:
        # two pass so we can replace vars with vars and then with values
        data = map_nested_in_place(self._replace_env_vars, data)
        return map_nested_in_place(self._replace_env_vars, data)

    def _replace_var(self, var_name: str) -> Any:
        return os.getenv(var_name, self.extra_vars.get(var_name, ""))

    def _replace_env_vars(self, value: Any) -> Any:
        if isinstance(value, str):
            return self.pattern.sub(lambda match: self._replace_var(match.group(1)), value)
        return value

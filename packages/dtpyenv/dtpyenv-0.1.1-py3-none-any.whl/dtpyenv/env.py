import os
import logging
from functools import lru_cache


class Env:
    _allowed_variables = set()

    @staticmethod
    def load_file(file_path: str, override: bool = False, fail_on_missing: bool = False):
        """
        Load environment variables from a file. Each line should be in the format: VAR=VALUE.

        Args:
            file_path (str): Path to the environment file.
            override (bool): Whether to override the existing environment variables.
            fail_on_missing (bool): Whether to throw an exception or log a warning when the file doesn't exist.
        """
        if not os.path.exists(file_path):
            if fail_on_missing:
                raise FileNotFoundError(f"The file {file_path} does not exist.")
            logging.warning(f"Environment file {file_path} not found. Skipping loading.")
            return

        with open(file_path, 'r') as file:
            for line in file:
                if '=' in line:
                    key, value = line.strip().split('=', 1)
                    key = key.strip()
                    value = value.strip()
                    if key in Env._allowed_variables:
                        if override or key not in os.environ:
                            os.environ[key] = value

                    else:
                        logging.warning(f"Skipping unallowed environment variable {key}.")

    @staticmethod
    def register(variables: list | set):
        """
        Register the allowed environment variables that can be accessed by the class.

        Args:
            variables (list or set): List or set of allowed variable names.
        """
        Env._allowed_variables.update(variables)

    @staticmethod
    @lru_cache(maxsize=128)
    def get(key: str):
        """
        Retrieve an environment variable, using caching to speed up subsequent lookups.

        Args:
            key (str): The name of the environment variable.

        Returns:
            str: The value of the environment variable, or None if not found.
        """
        return os.getenv(key)

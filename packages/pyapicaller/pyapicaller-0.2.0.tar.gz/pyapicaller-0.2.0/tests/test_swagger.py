import sys
import unittest

from apicaller.swagger import SwaggerCaller


class TestSwaggerCaller(unittest.TestCase):
    def setUp(self):
        # Initialize SwaggerCaller with necessary setups
        self.swagger_caller = SwaggerCaller(swagger_client="test_client")

    def test_get_module_with_valid_module_name(self):
        # Test `_get_module` with a valid module name
        module_name = "math"  # Use a built-in Python module
        self.swagger_caller._path = "."  # Current directory
        self.swagger_caller._client_package = ""  # Empty since we're not using a custom package

        try:
            self.swagger_caller._get_module(module_name)
        except ModuleNotFoundError:
            self.fail(f"_get_module raised ModuleNotFoundError unexpectedly for {module_name}")

    def test_get_module_with_invalid_module_name(self):
        # Test `_get_module` with an invalid module name
        module_name = "invalid_module"
        self.swagger_caller._path = "./non_existent_path"
        self.swagger_caller._client_package = "non_existent_package"

        with self.assertRaises(ValueError):
            self.swagger_caller._get_module(module_name)

    def test_get_module_with_empty_module_name(self):
        # Test `_get_module` when no module name is given
        self.swagger_caller._path = "./example_path"
        self.swagger_caller._client_package = "example_package"

        with self.assertRaises(ModuleNotFoundError):
            self.swagger_caller._get_module()

    def test_get_module_inserts_path_to_sys_path(self):
        # Test if `_get_module` adds the path to sys.path
        self.swagger_caller._path = "./new_path"
        self.swagger_caller._client_package = "example_package"

        try:
            self.swagger_caller._get_module("dummy_module")
        except ModuleNotFoundError:
            pass

        self.assertIn("./new_path", sys.path)


if __name__ == '__main__':
    unittest.main()
import os
import unittest
import unittest.mock

import iker.setup
from iker_tests import resources_directory


class Test(unittest.TestCase):

    def test_read_version_tuple(self):
        major, minor, patch = iker.setup.read_version_tuple(os.path.join(resources_directory, "unittest/setup"),
                                                            version_file="VERSION",
                                                            patch_env_var="DUMMY_BUILD")
        self.assertEqual(major, 1)
        self.assertEqual(minor, 2)
        self.assertEqual(patch, 3)

    def test_read_version_tuple__excessive_patch(self):
        major, minor, patch = iker.setup.read_version_tuple(os.path.join(resources_directory, "unittest/setup"),
                                                            version_file="VERSION_EXCESSIVE_PATCH",
                                                            patch_env_var="DUMMY_BUILD")
        self.assertEqual(major, 1)
        self.assertEqual(minor, 2)
        self.assertEqual(patch, 3)

    def test_read_version_tuple__no_patch(self):
        major, minor, patch = iker.setup.read_version_tuple(os.path.join(resources_directory, "unittest/setup"),
                                                            version_file="VERSION_NO_PATCH",
                                                            patch_env_var="DUMMY_BUILD")
        self.assertEqual(major, 1)
        self.assertEqual(minor, 2)
        self.assertEqual(patch, 0)

    def test_read_version_tuple__env_patch(self):
        with unittest.mock.patch.dict(os.environ, {"DUMMY_BUILD": "12345"}):
            major, minor, patch = iker.setup.read_version_tuple(os.path.join(resources_directory, "unittest/setup"),
                                                                version_file="VERSION_NO_PATCH",
                                                                patch_env_var="DUMMY_BUILD")
        self.assertEqual(major, 1)
        self.assertEqual(minor, 2)
        self.assertEqual(patch, 12345)

    def test_read_version_tuple__patch_out_of_range(self):
        with unittest.mock.patch.dict(os.environ, {"DUMMY_BUILD": "123456789"}):
            major, minor, patch = iker.setup.read_version_tuple(os.path.join(resources_directory, "unittest/setup"),
                                                                version_file="VERSION_NO_PATCH",
                                                                patch_env_var="DUMMY_BUILD")
        self.assertEqual(major, 1)
        self.assertEqual(minor, 2)
        self.assertEqual(patch, 999999)

    def test_version_string_local(self):
        version_string = iker.setup.version_string_local(os.path.join(resources_directory, "unittest/setup"),
                                                         version_file="VERSION",
                                                         patch_env_var="DUMMY_BUILD")
        self.assertEqual(version_string, "1.2.3")

    def test_version_string_local__excessive_patch(self):
        version_string = iker.setup.version_string_local(os.path.join(resources_directory, "unittest/setup"),
                                                         version_file="VERSION_EXCESSIVE_PATCH",
                                                         patch_env_var="DUMMY_BUILD")
        self.assertEqual(version_string, "1.2.3")

    def test_version_string_local__no_patch(self):
        version_string = iker.setup.version_string_local(os.path.join(resources_directory, "unittest/setup"),
                                                         version_file="VERSION_NO_PATCH",
                                                         patch_env_var="DUMMY_BUILD")
        self.assertEqual(version_string, "1.2.0")

    def test_version_string_local__env_patch(self):
        with unittest.mock.patch.dict(os.environ, {"DUMMY_BUILD": "12345"}):
            version_string = iker.setup.version_string_local(os.path.join(resources_directory, "unittest/setup"),
                                                             version_file="VERSION_NO_PATCH",
                                                             patch_env_var="DUMMY_BUILD")
        self.assertEqual(version_string, "1.2.12345")

    def test_version_string_local__patch_out_of_range(self):
        with unittest.mock.patch.dict(os.environ, {"DUMMY_BUILD": "123456789"}):
            version_string = iker.setup.version_string_local(os.path.join(resources_directory, "unittest/setup"),
                                                             version_file="VERSION_NO_PATCH",
                                                             patch_env_var="DUMMY_BUILD")
        self.assertEqual(version_string, "1.2.999999")

import unittest

from app import describe_release


class DescribeReleaseTest(unittest.TestCase):
    def test_parses_yaml_and_builds_request_without_network(self):
        self.assertEqual(
            describe_release("name: demo\nversion: 1.2.3\n"),
            ("demo 1.2.3", "https://example.invalid/demo"),
        )

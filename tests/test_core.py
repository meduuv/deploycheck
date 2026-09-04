import unittest

from deploycheck import validate


class DeployCheckTests(unittest.TestCase):
    def test_valid_service(self):
        self.assertEqual(validate([{"name": "api", "image": "python", "replicas": 2}]), [])

    def test_reports_missing_fields(self):
        errors = validate([{}])
        self.assertIn("service[0]: missing name", errors)
        self.assertIn("service[0]: missing image", errors)


if __name__ == "__main__":
    unittest.main()

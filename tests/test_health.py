import importlib
import os
import unittest
from unittest.mock import patch


class TestHealth(unittest.TestCase):

    def test_health_returns_ok(self):
        env = {
            "DATABASE_URL": "postgresql://test:test@localhost/test",
            "AUTH_SERVICE_URL": "http://localhost:8001",
        }

        with (
            patch.dict(os.environ, env),
            patch("psycopg2.pool.SimpleConnectionPool"),
        ):
            service = importlib.import_module("app")
            response = service.app.test_client().get("/health")

            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.get_json(), {"status": "ok"})


if __name__ == "__main__":
    unittest.main()

import unittest
import json

from api import app


class Tests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_empty_body(self):
        expected_response = {
            "error": 1,
            "message": "No array was received or was not sent properly"
        }
        response = self.app.post('/api/check-array')
        self.assertEqual(400, response.status_code)
        self.assertDictEqual(response.get_json(), expected_response)

    def test_invalid_array_string(self):
        expected_response = {
            "error": 1,
            "message": "Bad request, please send a valid array"
        }
        request_body = json.dumps({"array": "Not an array"})
        response = self.app.post(
            '/api/check-array', headers={"Content-Type": "application/json"}, data=request_body)
        self.assertEqual(400, response.status_code)
        self.assertDictEqual(response.get_json(), expected_response)

    def test_invalid_array_small(self):
        expected_response = {
            "error": 1,
            "message": "Bad request, please send a valid array"
        }
        request_body = json.dumps({"array": [1, 2]})
        response = self.app.post(
            '/api/check-array', headers={"Content-Type": "application/json"}, data=request_body)
        self.assertEqual(400, response.status_code)
        self.assertDictEqual(response.get_json(), expected_response)

    def test_not_separable_array(self):
        expected_response = {
            "error": 2,
            "message": "The array cannot be separated in 2 parts that give the same sum result"
        }
        request_body = json.dumps({"array": [2, 3, 3, 1, 5, 1, 3]})
        response = self.app.post(
            '/api/check-array', headers={"Content-Type": "application/json"}, data=request_body)
        self.assertEqual(200, response.status_code)
        self.assertDictEqual(response.get_json(), expected_response)

    def test_valid(self):
        expected_response = {"result": {"index": 10, "value": 1, "sum": 33}}
        request_body = json.dumps(
            {"array": [2, 2, 2, 2, 2, 2, 2, 6, 10, 3, 1, 5, 2, 5, 3, 1, 3, 14]})
        response = self.app.post(
            '/api/check-array', headers={"Content-Type": "application/json"}, data=request_body)
        self.assertEqual(200, response.status_code)
        self.assertDictEqual(response.get_json(), expected_response)


if __name__ == '__main__':
    unittest.main()

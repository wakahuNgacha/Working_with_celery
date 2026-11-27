import json

from django.test import TestCase
from django.urls import reverse


class MultiplayerApiTests(TestCase):
    def test_post_returns_multiplication_answer(self):
        response = self.client.post(
            reverse("multiplayer"),
            data=json.dumps({"r": 3, "x": 4}),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"answer": 12})

    def test_invalid_json_returns_bad_request(self):
        response = self.client.post(
            reverse("multiplayer"), data="{", content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())

    def test_non_post_request_is_not_allowed(self):
        response = self.client.get(reverse("multiplayer"))

        self.assertEqual(response.status_code, 405)

from django.test import Client, TestCase


class TestMainView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_context_has_all_weather_data(self):
        url = "/main"

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

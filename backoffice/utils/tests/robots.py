from django.test import TestCase


class RobotsViewTestCase(TestCase):

    def test_success_response(self):
        resp = self.client.get('/robots.txt')
        self.assertEqual(resp.status_code, 200)

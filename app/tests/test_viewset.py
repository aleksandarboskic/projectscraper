from django.test import TestCase, Client

class ApiTest(TestCase):
    def test_get_all_articles(self):
        c = Client()
        response = c.get("/api/articles/")
        self.assertEqual(response.status_code, 200)

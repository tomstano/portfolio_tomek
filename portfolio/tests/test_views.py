from django.test import TestCase


class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get('http://127.0.0.1:8000/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, '<h1><a href="/">Home</a></h1>')

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')

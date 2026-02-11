from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve

from shoppinglist.views import home_page

# It was my first test.
# class SmokeTest(TestCase):
#     def test_bad_math(self):
#         self.assertEqual(1+1, 3)

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_return_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>SHOPPING LIST</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))

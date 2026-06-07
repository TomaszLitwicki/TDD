from django.test import TestCase
# from django.http import HttpRequest
# from lists.views import home_page

# class SmokeTest(TestCase):
#     def test_bad_maths(self):
#         self.assertEqual(1+1, 2)

class Home_Page_Test(TestCase):
    # def test_home_page_returns_correct_html(self):
    #     request = HttpRequest()
    #     response = home_page(request)
    #     html : str = response.content.decode('utf8')

    #     self.assertIn('<title>To-Do lists</title>', html)
    #     self.assertTrue(html.startswith("<html>"))
    #     self.assertTrue(html.endswith("</html>"))

    # def test_renders_home_page_content(self):
    #     response = self.client.get('/')
    #     self.assertContains(response, "<title>To-Do lists</title>")

    def test_uses_home_page_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, "home.html")
    
    def test_renders_input_form(self):
        response = self.client.get('/')
        self.assertContains(response, '<form method="POST">')
        self.assertContains(response, '<input name="item_text"')

    def test_can_saved_a_POST_request(self):
        response = self.client.post("/", data={"item_text": "A new list item"})
        self.assertContains(response, 'A new list item')
        self.assertTemplateUsed(response, "home.html")
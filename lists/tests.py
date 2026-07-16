from django.test import TestCase
from lists.models import Item
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
        self.assertContains(response, '<form method="POST" action="/">')
        self.assertContains(response, '<input name="item_text"')

    def test_can_saved_a_POST_request(self):
        self.client.post("/", data={"item_text": "A new list item"})

        self.assertEqual(Item.objects.count(), 1)
        first_item = Item.objects.first()
        self.assertEqual(first_item.text, "A new list item")

        # self.assertContains(response, 'A new list item')
        # self.assertTemplateUsed(response, "home.html")

    def test_redirect_after_POST(self):
        response = self.client.post("/", data={"item_text": "A new list item"})
        self.assertRedirects(response, "/lists/the-only-list-on-the-world/")

    # def test_can_save_multiple_items(self):
    #     self.client.post("/", data = {"item_text": "first item"})
    #     response = self.client.post("/", data={"item_text": "second item"})

    #     self.assertContains(response, "first item")
    #     self.assertContains(response, "second item")

    def test_only_saves_items_when_necessary(self):
        self.client.get("/")
        self.assertEqual(Item.objects.count(), 0)

class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = "The first item"
        first_item.save()

        second_item = Item()
        second_item.text = "The second item"
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]

        self.assertEqual(first_saved_item.text, "The first item")
        self.assertEqual(second_saved_item.text, "The second item")

class ListViewTest(TestCase):
    def test_renders_input_form(self):
        response = self.client.get('/lists/the-only-list-on-the-world/')
        self.assertContains(response, '<form method="POST" action="/">')
        self.assertContains(response, '<input name="item_text"')

    def test_display_all_list_items(self):
        Item.objects.create(text="itemey 1")
        Item.objects.create(text="itemey 2")

        response = self.client.get("/lists/the-only-list-on-the-world/")

        self.assertContains(response, "itemey 1")
        self.assertContains(response, "itemey 2")
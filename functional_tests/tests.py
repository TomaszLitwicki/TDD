import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException
import time

MAX_TIME = 5

class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
    
    def wait_for_row_in_list_table(self, data_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element(By.ID, "id_list_table")
                rows = table.find_elements(By.TAG_NAME, "tr")
                self.assertIn(data_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException):
                if time.time() - start_time > MAX_TIME:
                    raise
                time.sleep(0.5)


    def test_can_start_a_todo_list(self):
        # Edith has heard about a cool new online to-do app.
        # She goes to check out its homepage
        self.browser.get(self.live_server_url)

        # She notices the page title and header mention to-do lists
        self.assertIn("To-Do", self.browser.title)
        
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("To-Do", header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element(By.ID, "id_new_element")
        self.assertEqual(inputbox.get_attribute("placeholder"), "Enter a to-do item")
        
        # She types "Buy peacock feathers" into a text box
        # (Edith's hobby is tying fly-fishing lures)
        inputbox.send_keys("Buy peacock feathers")

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        ###time.sleep(1)

        ###table = self.browser.find_element(By.ID, "id_list_table")
        ###rows = self.browser.find_elements(By.TAG_NAME, "tr")
        self.wait_for_row_in_list_table("1: Buy peacock feathers") 

        # There is still a text box inviting her to add another item.
        # She enters "Use peacock feathers to make a fly" (Edith is very methodical)
        inputbox = self.browser.find_element(By.ID, "id_new_element")
        inputbox.send_keys("Use peacock feathers to make a fly")
        inputbox.send_keys(Keys.ENTER)
        ###time.sleep(1)

        # The page updates again, and now shows both items on her list
        self.wait_for_row_in_list_table("2: Use peacock feathers to make a fly") 
        self.wait_for_row_in_list_table("1: Buy peacock feathers") 

        # Satisfied, she goes back to sleep
        #self.fail("Finish the test!")

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Edith starts a new to-do list
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element(By.ID, "id_new_element")
        inputbox.send_keys("Kup pawie pióra")
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Kup pawie pióra")
        
        # She notice that her list has a unique URL
        edith_list_url = self.browser.current_url
        print(f"\n\nMOJE UWAGI: {edith_list_url} \n\n")
        self.assertRegex(edith_list_url, "/lists/.+")

        # now a new user, Francis, comes along to the site.

        ## DELETE ALL THE BROWSER'S COOKIES
        ## as a way of simulating a brand new user sesion.
        self.browser.delete_all_cookies()

        # Francis visits the home page.
        # There is no sign od Edith's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element(By.TAG_NAME, "body").text
        self.assertNotIn("1: Kup pawie pióra", page_text)

        # Francis starts a new list by entering a new item
        # He is less interesting than Edith...
        inputbox = self.browser.find_element(By.ID, "id_new_element")
        inputbox.send_keys("Kupić mleko")
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Kupić mleko")

        # Grancis gets his own unique URL
        francis_list_url = self.browser.current_url
        print(f"\n\nMOJE UWAGI edith: {edith_list_url} \n\n")
        print(f"\n\nMOJE UWAGI francis: {francis_list_url} \n\n")
        self.assertRegex(francis_list_url, "/lists/.+")
        self.assertNotEqual(francis_list_url, edith_list_url)

        # Again, there is na trace of Edith's list
        page_text = self.browser.find_element(By.TAG_NAME, "body").text
        self.assertNotIn("Kup pawie pióra", page_text)
        self.assertIn("Kupić mleko", page_text)

        # Satisfied, they both go back to sleep.
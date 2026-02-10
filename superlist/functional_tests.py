from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #Strona główna aplikacji
        self.browser.get('http://localhost:8000')

        #Tytuł strony i nagłówek zawierają słowo "SHOPPING LIST"
        self.assertIn('SHOPPING LIST', self.browser.title)
        self.fail('Zakończenie testu')

#Pole tekstowe do wpisania produktu
#Wpisanie produktu: MLEKO
#Enter
#Aktualizacja strony
#Wyświetlanie wpisanego produktu i pole tekstowe do wprowadzenia następnego
#Wpisanie produktu: KAWA ROZPUSZCZALNA
#Enter
#Aktualizacja strony
#Wyświetlanie wpisanych produktów i pole tekstowe do wprowadzenia kolejnego
#Wygenerowany adres URL + info z instrukcją
#Przejście pod wygenerowany LINK URL - wyświetla się lista zakupowa

if __name__ == '__main__':
    unittest.main(warnings='ignore')
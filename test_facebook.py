'''
Scenariusz testowy:
Rejestracja na stronie https://pl-pl.facebook.com/

Warunki wstepne:
Przeglądarka otwarta na stronie https://pl-pl.facebook.com/

Przypadek testowy:
Użytkownik nie podaje daty urodzenia.

Kroki:
1. Wprowadz imię
2. Wprowadź nazwisko
3. Wpisz adres e-mail
4. Potwierdź adres e-mail
5. Wpisz hasło
6. Pomiń podanie daty urodzenia
7. Wybierz płeć kobieta
8. Kliknij Zarejestruj


Oczekiwany rezultat:
1. Użytkownik dostaje informację "Podaj prawdziwą datę urodzin".
'''


import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep



class FacebookRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://pl-pl.facebook.com/")

    def testNoBirthdayDate(self):
        driver = self.driver

        # 1. Wprowadź imię
        name_field = WebDriverWait(driver, 60)\
        .until(EC.presence_of_element_located((By.NAME, 'firstname')))
        name_field.send_keys("Anna")

        # 2. Wprowadź nazwisko
        lastname_field = driver.find_element_by_name('lastname')
        lastname_field.send_keys("Barbara")

        # 3. Wpisz adres e-mail
        email = driver.find_element_by_name('reg_email__')
        email.send_keys("email@email.com")

	    # 4. Potwiedź adres e-mail
        email_confirmation = driver.find_element_by_name('reg_email_confirmation__')
        email_confirmation.send_keys("email@email.com")

        # 5. Wpisz hasło
        password=driver.find_element_by_css_selector('input[data-type="password"]')
        password.send_keys('haslO-7')

	    # 6. Pomiń podanie daty urodzenia

        # 7. Wybierz płeć kobieta
        sex = driver.find_element_by_name('sex')
        sex.click()
        sex.get_attribute('value') == 1

        # 8. Kliknij Zarejestruj
        registration = driver.find_element_by_id('u_0_15').click()

	    # Screenshot
        driver.save_screenshot("screenshot.png")

    visible_errors=[]
    for e in errors:
        if e.is_displayed():
            visible_errors.append(e)

    # Sprawdzenie czy widoczny jest jeden błąd
    assert len(visible_errors) == 1

    # Sprawdzenie treści błędu
    assert visible_errors[0].text == "Wygląda na to, że podano nieprawidłowe informacje. Podaj prawdziwą datę urodzin."

    sleep(25)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


class TestPythonOrg(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")

    def test_searchbar_python(self):
        driver = self.driver
        driver.get("https://www.python.org/")
        self.assertIn("Python", driver.title)
        elem = driver.find_element(By.NAME, "q")
        elem.send_keys("Pip")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
        sleep(5)  # To make the Chrome browser not close instantly

    def test_fill_donation_form(self):
        driver = self.driver
        driver.get("https://psfmember.org/civicrm/contribute/transact/?reset=1&id=2")
        self.assertIn("Donation for the PSF", driver.page_source)

        other_amount = driver.find_element(By.NAME, 'price_47')
        other_amount.send_keys("110")

        email = driver.find_element(By.NAME, "email-5")
        email.send_keys("someemail@email.com")

        sleep(5)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

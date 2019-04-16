import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

szukanie_sport = "Sport"
szukanie_elektronika = "Elektronika"
url = 'https://buggy-testingcup.pgs-soft.com/'


class zadanieDrugie(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(executable_path=r'C:\driver_selenium\ChromeDrive_73\chromedriver.exe')
        self.driver = webdriver.Firefox(executable_path=r'C:\driver_selenium\FirefoxDrive_24\geckodriver.exe')
        self.driver.maximize_window()
        self.driver.get(url + 'task_2')


    def tearDown(self):
        self.driver.quit()

    def test_WybranieDowolnegoProduktu(self):
        driver = self.driver
        # driver.find_element_by_xpath("//span[contains(@class,'placeholder')]").click()
        # driver.find_element_by_xpath("//input[@autocorrect='off']").send_keys(szukanie_sport)
        # driver.find_element_by_xpath("//input[@autocorrect='off']").send_keys(Keys.ENTER)
        # sleep(3)
        # driver.find_element_by_xpath("//span[@title='Sport']").click()
        # driver.find_element_by_xpath("//input[@autocorrect='off']").send_keys(szukanie_elektronika)
        # driver.find_element_by_xpath("//input[@autocorrect='off']").send_keys(Keys.ENTER)

        select = Select(driver.find_element_by_class_name("js-category-select"))
        select .select_by_value("Firma i usługi")
        select.click()
        #
        # select = Select(driver.find_element_by_class_name("js-category-select"))
        # select.select_by_index(1)
        #
        # select = Select(driver.find_element_by_class_name("js-category-select"))
        # select.select_by_visible_text("Firma i usługi")



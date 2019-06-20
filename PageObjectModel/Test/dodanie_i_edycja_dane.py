import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

url = 'https://buggy-testingcup.pgs-soft.com/'


class zadanieDrugie(unittest.TestCase):

    def setUp(self, browser="chrome"):
        if browser == "chrome":
            self.driver = webdriver.Chrome(executable_path=r'../Drivers/ChromeDrive_74/chromedriver.exe')
            self.driver.maximize_window()
            self.driver.get(url + 'task_3')
        elif browser == "mozilla":
            self.driver = webdriver.Firefox(executable_path=r'../Drivers/FirefoxDrive_24/geckodriver.exe')
            self.driver.maximize_window()
            self.driver.get(url + 'task_3')
        else:
            print("Brak przeglądarki")
            raise Exception("Brak przeglądarki")
        return self.driver


    def tearDown(self):
        self.driver.close()
        self.driver.quit()

    def test_add_and_edition_data(self):
        driver = self.driver
        driver.find_element_by_class_name("menu-border").click()
        #driver.find_element_by_class_name("dropdown-toggle").click()
        driver.find_element_by_xpath(".//*[@id='menu1']/li[1]/a").click()
        # driver.find_element_by_xpath(".//*[@id='start-edit']").click()
        sleep(5)
        # driver.find_element_by_id("start-edit").click()
        # driver.find_element_by_id("in-name").clear()
        # driver.find_element_by_id("in-name").send_keys("Lukasz")
        # driver.find_element_by_id("in-surname").clear()
        # driver.find_element_by_id("in-surname").send_keys("Blaszkowski")
        # driver.find_element_by_id("in-notes").clear()
        # driver.find_element_by_id("in-notes").send_keys("to jest text testowy")
        # driver.find_element_by_id("in-phone").clear()
        # driver.find_element_by_id("in-phone").send_keys("10981234098")
        # driver.find_element_by_id("save-btn").click()
        #
        # driver.find_element_by_class_name("menu-border").click()
        # #driver.find_element_by_class_name("dropdown-toggle").click()
        # driver.find_element_by_xpath(".//*[@id='menu1']/li[1]/a").click()
        # driver.find_element_by_xpath(".//*[@id='start-edit']").click()
        # #driver.find_element_by_id("start-edit").click()
        # driver.find_element_by_id("in-name").clear()
        # driver.find_element_by_id("in-name").send_keys("Jan")
        # driver.find_element_by_id("in-surname").clear()
        # driver.find_element_by_id("in-surname").send_keys("Nowak")
        # driver.find_element_by_id("in-notes").clear()
        # driver.find_element_by_id("in-notes").send_keys("może tak a może nie")
        # driver.find_element_by_id("in-phone").clear()
        # driver.find_element_by_id("in-phone").send_keys("0000000000000")
        # driver.find_element_by_id("in-file").clear()
        # driver.find_element_by_id("in-file").send_keys("C:\\ASTA\\img\\lwy_serce.jpge")
        # driver.find_element_by_id("save-btn").click()








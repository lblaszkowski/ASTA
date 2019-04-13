# -*- coding:utf-8 -*-

import unittest
from selenium import webdriver
from time import sleep




class zadaniePierwsze(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Chrome(executable_path=r'C:\driver_selenium\ChromeDrive_73\chromedriver.exe')
        self.driver = webdriver.Firefox(executable_path=r'C:\driver_selenium\FirefoxDrive_24\geckodriver.exe')
        # self.driver.maximize_window()
        # self.driver.get("https://buggy-testingcup.pgs-soft.com/")

    def tearDown(self):
        self.driver.quit()


    def test_open_page(self):
        self.driver.maximize_window()
        self.driver.get("https://buggy-testingcup.pgs-soft.com/")
        # self.driver.find_element_by_xpath("//*[@class='col-md-6']//*[text()='Zadanie 1']").click()

    def test_Dodanie_Do_Koszyka_Glasses(self):
        driver = self.driver
        self.test_open_page()
        # driver.find_element_by_xpath("//*[@class='col-md-6']//*[text()='Zadanie 1']").click()
        driver.find_element_by_css_selector("div:nth-child(1)>div:nth-child(1)>div>div>div>input").click()
        driver.find_element_by_css_selector("div:nth-child(1)>div:nth-child(1)>div>div>div>input").clear()
        driver.find_element_by_css_selector("div:nth-child(1)>div:nth-child(1)>div>div>div>input").send_keys("3")
        driver.find_element_by_xpath("//button[@data-product-name='Okulary']").click()

    def test_Dodanie_do_koszyka_Pilka(self):
        driver = self.driver
        self.test_open_page()
        # driver.find_element_by_xpath("//*[@class='col-md-6']//*[text()='Zadanie 1']").click()
        driver.find_element_by_css_selector("div:nth-child(1)>div:nth-child(2)>div>div>div>input").click()
        driver.find_element_by_css_selector("div:nth-child(1)>div:nth-child(2)>div>div>div>input").clear()
        driver.find_element_by_css_selector("div:nth-child(1)>div:nth-child(2)>div>div>div>input").send_keys("2")
        driver.find_element_by_xpath("//button[@data-product-price='39.22']").click()

if __name__ == "__main__":
    unittest.main()


        # driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div[1]/form/div[3]/div[3]/div/div/div/input").clear()
        # driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div[1]/form/div[3]/div[3]/div/div/div/input").send_keys("1")
        # driver.find_element_by_xpath("//button[@data-product-name='Zeszyt']").click()
        # driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div[1]/form/div[3]/div[4]/div/div/div/input").clear()
        # driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div[1]/form/div[3]/div[4]/div/div/div/input").send_keys("4")
        # driver.find_element_by_xpath("//button[@data-product-name='Kostka']").click()
        # driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div[1]/form/div[2]/div[2]/div/div/div/input").clear()
        # driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div[1]/form/div[2]/div[2]/div/div/div/input").send_keys("8")
        # driver.find_element_by_xpath("//button[@data-product-name='Kamera']").click()
        # driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div[1]/form/div[2]/div[1]/div/div/div/input").clear()
        # driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div[1]/form/div[2]/div[1]/div/div/div/input").send_keys("5")
        # driver.find_element_by_xpath("//button[@data-product-name='Słuchawki']").click()
        # driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div[1]/form/div[1]/div[4]/div/div/div/input").clear()
        # driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div[1]/form/div[1]/div[4]/div/div/div/input").send_keys("7")
        # driver.find_element_by_xpath("//button[@data-product-name='Kabel']").click()
        # driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div[1]/form/div[2]/div[3]/div/div/div/input").clear()
        # driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div[1]/form/div[2]/div[3]/div/div/div/input").send_keys("9")
        # driver.find_element_by_xpath("//button[@data-product-name='Aparat']").click()


import unittest
from selenium import webdriver
from time import sleep

url = 'https://buggy-testingcup.pgs-soft.com/'


class zadaniePierwsze(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(executable_path=r'C:\driver_selenium\ChromeDrive_73\chromedriver.exe')
        self.driver = webdriver.Firefox(executable_path=r'C:\driver_selenium\FirefoxDrive_24\geckodriver.exe')
        self.driver.maximize_window()
        self.driver.get(url + 'task_1')


    def tearDown(self):
        self.driver.quit()


    def test_dodanie_do_koszyka(self):
        driver = self.driver
        okulary = driver.find_element_by_css_selector("div:nth-child(1)>div:nth-child(1)>div>div>div>input").click()
        okulary.clear()
        okulary.send_keys("3")
        driver.find_element_by_xpath("//button[@data-product-name='Okulary']").click()

        driver.find_element_by_css_selector("div:nth-child(1)>div:nth-child(2)>div>div>div>input").click()
        driver.find_element_by_css_selector("div:nth-child(1)>div:nth-child(2)>div>div>div>input").clear()
        driver.find_element_by_css_selector("div:nth-child(1)>div:nth-child(2)>div>div>div>input").send_keys("2")
        driver.find_element_by_xpath("//button[@data-product-price='39.22']").click()
        driver.find_element_by_css_selector("div:nth-child(3)>div:nth-child(3)>div>div>div>input").clear()
        driver.find_element_by_css_selector("div:nth-child(3)>div:nth-child(3)>div>div>div>input").send_keys("1")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.find_element_by_xpath("//button[@data-product-name='Zeszyt']").click()
        driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div[1]/form/div[3]/div[4]/div/div/div/input").clear()
        driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div[1]/form/div[3]/div[4]/div/div/div/input").send_keys("4")
        driver.find_element_by_xpath("//button[@data-product-name='Kostka']").click()
        driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div[1]/form/div[2]/div[2]/div/div/div/input").clear()
        driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div[1]/form/div[2]/div[2]/div/div/div/input").send_keys("8")
        driver.find_element_by_xpath("//button[@data-product-name='Kamera']").click()
        driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div[1]/form/div[2]/div[1]/div/div/div/input").clear()
        driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div[1]/form/div[2]/div[1]/div/div/div/input").send_keys("5")
        driver.find_element_by_xpath("//button[@data-product-name='Słuchawki']").click()
        driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div[1]/form/div[1]/div[4]/div/div/div/input").clear()
        driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div[1]/form/div[1]/div[4]/div/div/div/input").send_keys("7")
        driver.find_element_by_xpath("//button[@data-product-name='Kabel']").click()
        driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div[1]/form/div[2]/div[3]/div/div/div/input").clear()
        driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div[1]/form/div[2]/div[3]/div/div/div/input").send_keys("9")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.find_element_by_xpath("//button[@data-product-name='Aparat']").click()
        sleep(5)

if __name__ == "__main__":
    unittest.main()




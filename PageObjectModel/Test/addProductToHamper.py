import unittest
from selenium import webdriver
from time import sleep

url = 'https://buggy-testingcup.pgs-soft.com/'


class AddProductToHamperPage(unittest.TestCase):


    def setUp(self, browser="mozilla", task="task_1"):
        if browser == "chrome":
            self.driver = webdriver.Chrome(executable_path=r'../Drivers/ChromeDrive_74/chromedriver.exe')
            self.driver.maximize_window()
            self.driver.get(url + task)
        elif browser == "mozilla":
            self.driver = webdriver.Firefox(executable_path=r'../Drivers/FirefoxDrive_24/geckodriver.exe')
            self.driver.maximize_window()
            self.driver.get(url + task)
        else:
            print("Brak przeglądarki")
            raise Exception("Brak przeglądarki")
        return self.driver


    def tearDown(self):
        self.driver.close()
        self.driver.quit()

    def test_AddProductToHamper(self):
        driver = self.driver
        okulary = driver.find_element_by_css_selector("div:nth-child(1)>div:nth-child(1)>div>div>div>input")
        okulary.clear()
        okulary.send_keys("3")
        driver.find_element_by_xpath("//button[@data-product-name='Okulary']").click()

        pilka = driver.find_element_by_css_selector("div:nth-child(1)>div:nth-child(2)>div>div>div>input")
        pilka.clear()
        pilka.send_keys("2")
        driver.find_element_by_xpath("//button[@data-product-price='39.22']").click()

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        zeszyt = driver.find_element_by_css_selector("div:nth-child(3)>div:nth-child(3)>div>div>div>input")
        zeszyt.clear()
        zeszyt.send_keys("1")
        driver.find_element_by_xpath("//button[@data-product-name='Zeszyt']").click()

        kostka = driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div[1]/form/div[3]/div[4]/div/div/div/input")
        kostka.clear()
        kostka.send_keys("4")
        driver.find_element_by_xpath("//button[@data-product-name='Kostka']").click()

        kamera = driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div[1]/form/div[2]/div[2]/div/div/div/input")
        kamera.clear()
        kamera. send_keys("8")
        driver.find_element_by_xpath("//button[@data-product-name='Kamera']").click()

        sluchawki = driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div[1]/form/div[2]/div[1]/div/div/div/input")
        sluchawki.clear()
        sluchawki.send_keys("5")
        driver.find_element_by_xpath("//button[@data-product-name='Słuchawki']").click()

        kabel = driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div[1]/form/div[1]/div[4]/div/div/div/input")
        kabel.clear()
        kabel.send_keys("7")
        driver.find_element_by_xpath("//button[@data-product-name='Kabel']").click()

        aparat = driver.find_element_by_xpath("html/body/div[1]/div/div[2]/div[1]/form/div[2]/div[3]/div/div/div/input")
        aparat.clear()
        aparat.send_keys("9")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.find_element_by_xpath("//button[@data-product-name='Aparat']").click()
        sleep(5)

        print(driver.find_element_by_css_selector("div.col-md-12.basket-summary>p:nth-child(1)>span").text)
        assert driver.find_element_by_css_selector("div.col-md-12.basket-summary>p:nth-child(1)>span").text == "36"

        print(driver.find_element_by_css_selector("div.col-md-12.basket-summary>p:nth-child(2)>span").text)
        assert driver.find_element_by_css_selector("div.col-md-12.basket-summary>p:nth-child(2)>span").text == "1317.33 zł"



if __name__ == "__main__":
    unittest.main()




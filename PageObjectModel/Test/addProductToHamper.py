import unittest
from selenium import webdriver
from time import sleep
from PageObjectModel.Pages.addProductToHamperPage import AddProductToHamperPage


url = 'https://buggy-testingcup.pgs-soft.com/'


class AddProductToHamper_Page(unittest.TestCase):

    @classmethod
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

    @classmethod
    def tearDown(self):
        self.driver.close()
        self.driver.quit()

    def test_AddProductToHamper(self):
        addProduct = AddProductToHamperPage(self.driver)
        addProduct.glasses_product()
        addProduct.ball__product()
        addProduct.notebook_product()
        addProduct.ankle_product()
        addProduct.camera_product()
        addProduct.headphones_product()
        addProduct.cable_product()
        addProduct.theCamera_product()


if __name__ == "__main__":
    unittest.main()




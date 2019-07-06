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
        addProduct.glasses_product("3")
        addProduct.ball_product("2")
        addProduct.notebook_product("1")
        addProduct.ankle_product("4")
        addProduct.camera_product("8")
        addProduct.headphones_product("5")
        addProduct.cable_product("7")
        addProduct.theCamera_product("9")
        addProduct.theTotalNumberOf_products()
        addProduct.toPay()

if __name__ == "__main__":
    unittest.main()




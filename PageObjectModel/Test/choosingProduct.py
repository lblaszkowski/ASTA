import unittest
from selenium import webdriver
from PageObjectModel.Pages.addChoosingProductPage import AddChoosingProductPage

url = 'https://buggy-testingcup.pgs-soft.com/'

class ChoosingProductPage(unittest.TestCase):

    def setUp(self, browser="ff",  task="task_2"):
        if browser == "chrome" or browser == "ch":
            self.driver = webdriver.Chrome(executable_path=r'../Drivers/ChromeDrive_74/chromedriver.exe')
            self.driver.maximize_window()
            self.driver.get(url + task)
        elif browser == "mozilla" or browser == "ff":
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

    def test_ChoosingProduct(self):
        SearchElement = AddChoosingProductPage(self.driver)
        SearchElement.elementSelectionInPage()
        SearchElement.searchInSportPage("Sport")








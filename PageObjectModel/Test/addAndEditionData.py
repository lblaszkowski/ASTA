import unittest
from selenium import webdriver
from PageObjectModel.Pages.addAndEditionDataPage import AddAndEditionData_Page
from time import sleep


url = 'https://buggy-testingcup.pgs-soft.com/'

class AddAndEditionDataPage(unittest.TestCase):

    def setUp(self, browser="mozilla", task="task_3"):
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

    def test_AddAndEditionData(self):
        AddandEditionData = AddAndEditionData_Page(self.driver)
        AddandEditionData.menuButtonClick()
        AddandEditionData.dropdownMenuClick()
        AddandEditionData.editFile()
        AddandEditionData.fieldName("Jan")
        AddandEditionData.fieldSurname("Nowak")
        AddandEditionData.fieldNotes("Testowy napis")
        AddandEditionData.fieldPhone("10981234098")
        AddandEditionData.fieldImage()
        AddandEditionData.saveButton()






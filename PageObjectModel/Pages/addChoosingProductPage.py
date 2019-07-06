from PageObjectModel.Locators.locators_addChoosingProductPage import Locators
from selenium.webdriver.common.keys import Keys


class AddChoosingProductPage():

    def __init__(self, driver):
        self.driver = driver

    def elementSelectionInPage(self):
        elementSelection = self.driver.find_element_by_xpath(Locators.elementSelection_xpath)
        elementSelection.click()

    def searchInSportPage(self, search_Sport):
        searchInSport = self.driver.find_element_by_xpath(Locators.searchInSport_xpath)
        searchInSport.send_keys(search_Sport)
        searchInSport.send_keys(Keys.ENTER)


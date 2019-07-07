from PageObjectModel.Locators.locators_AddAndEditionDataPage import Locators


class AddAndEditionData_Page():

    def __init__(self, driver):
        self.driver = driver

    def menuButtonClick(self):
        menuClick = self.driver.find_element_by_class_name(Locators.menuClick_css_selector)
        menuClick .click()

    def dropdownMenuClick(self):
        dropdownClick = self.driver.find_element_by_xpath(Locators.dropdownClick_css_selector)

    # def editFile(self):
    #     # editFileClick = self.driver.find_element_by_xpath(Locators.editFileClick_Id)
    #     editFileClick = self.driver.find_element_by_xpath(Locators.editFileClick_xpath)
    #     editFileClick.click()

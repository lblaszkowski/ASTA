from PageObjectModel.Locators.locators_AddAndEditionDataPage import Locators


class AddAndEditionData_Page():

    def __init__(self, driver):
        self.driver = driver

    def menuButtonClick(self):
        menuClick = self.driver.find_element_by_class_name(Locators.menuClick_css_selector)
        menuClick.click()

    def dropdownMenuClick(self):
        dropdownClick = self.driver.find_element_by_xpath(Locators.dropdownClick_css_selector)

    def editFile(self):
        editFileClick = self.driver.execute_script(Locators.editFileClick_script)

    def fieldName(self, fieldname):
        field_name = self.driver.find_element_by_id(Locators.field_name_id)
        field_name .clear()
        field_name.send_keys(fieldname)

    def fieldSurname(self, fieldsurname):
        field_surname = self.driver.find_element_by_id(Locators.field_surname_id)
        field_surname .clear()
        field_surname.send_keys(fieldsurname)

    def fieldNotes(self, fieldnotes):
        field_notes = self.driver.find_element_by_id(Locators.field_notes)
        field_notes.clear()
        field_notes.send_keys(fieldnotes)

    def fieldPhone(self, fieldphone):
        field_phone = self.driver.find_element_by_id(Locators.field_phone_id)
        field_phone.clear()
        field_phone.send_keys(fieldphone)

    def fieldImage(self):
        field_image = self.driver.find_element_by_id(Locators.field_image_id)
        field_image.send_keys(Locators.field_imageid)

    def saveButton(self):
        save_button = self.driver.find_element_by_id(Locators.save_button_id)
        save_button.click()

from PageObjectModel.Locators.locators_addProductToHamperPage import Locators

class AddProductToHamperPage():

    def __init__(self, driver):
        self.driver = driver


    def glasses_product(self, quantity_glasses):
        add_glasses = self.driver.find_element_by_css_selector(Locators.add_glasses_css_selector)
        add_glasses.clear()
        add_glasses.send_keys(quantity_glasses)
        glasses_click = self.driver.find_element_by_xpath(Locators.glasses_click_xpath)
        glasses_click.click()

    def ball_product(self, quantity_ball):
        add_ball = self.driver.find_element_by_css_selector(Locators.add_ball_css_selector)
        add_ball.clear()
        add_ball.send_keys(quantity_ball)
        ball_click = self.driver.find_element_by_xpath(Locators.ball_click_xpath )
        ball_click.click()

    def notebook_product(self,quantity_notebook):
        self.driver.execute_script(Locators.execute_script)
        add_notebook = self.driver.find_element_by_css_selector(Locators.add_notebook_css_selector)
        add_notebook.clear()
        add_notebook.send_keys(quantity_notebook)
        notebook_click = self.driver.find_element_by_xpath(Locators.notebook_click_xpath)
        notebook_click.click()

    def ankle_product(self,quantity_ankle):
        add_ankle = self.driver.find_element_by_xpath(Locators.add_ankle_xpath)
        add_ankle.clear()
        add_ankle.send_keys(quantity_ankle)
        ankle_click = self.driver.find_element_by_xpath(Locators.ankle_click_xpath)
        ankle_click .click()

    def camera_product(self, quantity_camera):
        add_camera = self.driver.find_element_by_xpath(Locators.add_camera_xpath)
        add_camera.clear()
        add_camera.send_keys(quantity_camera)
        camera_click = self.driver.find_element_by_xpath(Locators.camera_click_xpath)
        camera_click.click()

    def headphones_product(self,quantity_headphones):
        add_headphones = self.driver.find_element_by_xpath(Locators.add_headphones_xpath)
        add_headphones.clear()
        add_headphones.send_keys(quantity_headphones)
        headphones_click = self.driver.find_element_by_xpath(Locators.headphones_click_xpath)
        headphones_click.click()

    def cable_product(self,quantity_cable):
        add_cable = self.driver.find_element_by_xpath(Locators.add_cable_xpath)
        add_cable.clear()
        add_cable.send_keys(quantity_cable)
        cable_click = self.driver.find_element_by_xpath(Locators.cable_click_xpath)
        cable_click.click()

    def theCamera_product(self, quantity_theCamera):
        add_theCamera = self.driver.find_element_by_xpath(Locators.add_theCamera_xpath)
        add_theCamera.clear()
        add_theCamera.send_keys(quantity_theCamera)
        self.driver.execute_script(Locators.execute_script)
        theCamera_click = self.driver.find_element_by_xpath(Locators.theCamera_click_xpath)
        theCamera_click.click()

    def theTotalNumberOf_products(self):
        print(self.driver.find_element_by_css_selector(Locators.theTotalNumberOf_products_text).text)
        assert self.driver.find_element_by_css_selector(Locators.theTotalNumberOf_products_text).text == "36"

    def toPay(self):
        print(self.driver.find_element_by_css_selector(Locators.toPay_text).text)
        assert self.driver.find_element_by_css_selector(Locators.toPay_text).text == "1317.33 zł"




















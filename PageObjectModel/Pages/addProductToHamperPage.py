from PageObjectModel.Locators.locators_addProductToHamperPage import Locators

class AddProductToHamperPage():

    def __init__(self, driver):
        self.driver = driver


    def glasses_product(self):
        add_glasses = self.driver.find_element_by_css_selector(Locators.add_glasses_css_selector)
        add_glasses.clear()
        add_glasses.send_keys("3")
        glasses_click = self.driver.find_element_by_xpath(Locators.glasses_click_xpath)
        glasses_click.click()

    def ball__product(self):
        add_ball = self.driver.find_element_by_css_selector(Locators.add_ball_css_selector)
        add_ball.clear()
        add_ball.send_keys("2")
        ball_click = self.driver.find_element_by_xpath(Locators.ball_click_xpath )
        ball_click.click()

    def notebook_product(self):
        self.driver.execute_script(Locators.execute_script)
        add_notebook = self.driver.find_element_by_css_selector(Locators.add_notebook_css_selector)
        add_notebook.clear()
        add_notebook.send_keys("1")
        notebook_click = self.driver.find_element_by_xpath(Locators.notebook_click_xpath)
        notebook_click.click()
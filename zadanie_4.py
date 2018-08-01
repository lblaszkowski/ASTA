from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://buggy-testingcup.pgs-soft.com/")
driver.find_element_by_xpath("//h2[contains(.,'Zadanie 4')]").click()
driver.find_element_by_xpath("//button[contains(@class,'btn btn-primary btn-block js-open-window')]").click()


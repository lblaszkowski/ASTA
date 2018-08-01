from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://buggy-testingcup.pgs-soft.com/")
driver.find_element_by_xpath("//h2[contains(.,'Zadanie 5')]").click()







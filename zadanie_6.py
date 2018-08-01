from selenium import webdriver
import time



driver = webdriver.Chrome()
driver.get("https://buggy-testingcup.pgs-soft.com/")
driver.find_element_by_xpath("//h2[contains(.,'Zadanie 6')]").click()
driver.find_element_by_id("LoginForm__username").clear()
driver.find_element_by_id("LoginForm__username").send_keys("tester")
driver.find_element_by_id("LoginForm__password").clear()
driver.find_element_by_id("LoginForm__password").send_keys("123-xyz")
driver.find_element_by_id("LoginForm_save").click()
driver.find_element_by_xpath("//a[contains(.,'Pobierz plik')]").click()
time.sleep(5)
driver.find_element_by_id("logout").click()



print("test jest ok :)")
driver.quit()
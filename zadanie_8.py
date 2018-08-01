from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
#driver.maximize_window()
#driver.manage().window().maximize()

driver.get("https://buggy-testingcup.pgs-soft.com/")
driver.find_element_by_xpath("//h2[contains(.,'Zadanie 8')]").click()
select = Select(driver.find_element_by_id("task8_form_cardType"))
select .select_by_value("ae")
driver.find_element_by_id("task8_form_name").clear()
driver.find_element_by_id("task8_form_name").send_keys("Łukasz Błaszkowski")
driver.find_element_by_id("task8_form_cardNumber").click()
driver.find_element_by_id("task8_form_cardNumber").send_keys("378282246310005")
driver.find_element_by_id("task8_form_cardCvv").click()
driver.find_element_by_id("task8_form_cardCvv").send_keys("012")
select = Select(driver.find_element_by_id("task8_form_cardInfo_month"))
select.select_by_index(4)
select = Select(driver.find_element_by_id("task8_form_cardInfo_year"))
select.select_by_visible_text("2018")
driver.find_element_by_name("task8_form[save]").click()
print("test jest ok :)")
driver.quit()
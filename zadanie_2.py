from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

szukanie_sport = "Sport"
szukanie_elektronika = "Elektronika"

driver = webdriver.Chrome()
driver.get("https://buggy-testingcup.pgs-soft.com/")
driver.find_element_by_xpath("//h2[contains(.,'Zadanie 2')]").click()
driver.find_element_by_xpath("//span[contains(@class,'placeholder')]").click()
driver.find_element_by_xpath("//input[@autocorrect='off']").send_keys(szukanie_sport)
driver.find_element_by_xpath("//input[@autocorrect='off']").send_keys(Keys.ENTER)
# time.sleep(3)
driver.find_element_by_xpath("//span[@title='Sport']").click()
driver.find_element_by_xpath("//input[@autocorrect='off']").send_keys(szukanie_elektronika)
driver.find_element_by_xpath("//input[@autocorrect='off']").send_keys(Keys.ENTER)

select = Select(driver.find_element_by_class_name("js-category-select"))
select .select_by_value("Firma i usługi")

select = Select(driver.find_element_by_class_name("js-category-select"))
select.select_by_index(1)


select = Select(driver.find_element_by_class_name("js-category-select"))
select.select_by_visible_text("Firma i usługi")

print("test ok")
driver.quit()

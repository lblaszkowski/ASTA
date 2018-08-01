from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://buggy-testingcup.pgs-soft.com/")
driver.find_element_by_xpath("//h2[contains(.,'Zadanie 9')]").click()
time.sleep(3)
driver.find_element_by_css_selector("i.jstree-icon").click()
driver.find_element_by_css_selector("#j1_2 > i.jstree-icon").click()
driver.find_element_by_id("j1_3_anchor").click()

#driver.find_element_by_css_selector("ul.vakata-context.jstree-contextmenu.jstree-default-contextmenu >li ")
#driver.find_element_by_link_text("Zmień nazwę").click()


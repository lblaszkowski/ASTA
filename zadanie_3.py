from selenium import webdriver




driver = webdriver.Chrome()
driver.get("https://buggy-testingcup.pgs-soft.com/")
driver.find_element_by_xpath("//h2[contains(.,'Zadanie 3')]").click()
driver.find_element_by_class_name("menu-border").click()
#driver.find_element_by_class_name("dropdown-toggle").click()
driver.find_element_by_xpath(".//*[@id='menu1']/li[1]/a").click()
driver.find_element_by_xpath(".//*[@id='start-edit']").click()
#driver.find_element_by_id("start-edit").click()
driver.find_element_by_id("in-name").clear()
driver.find_element_by_id("in-name").send_keys("Lukasz")
driver.find_element_by_id("in-surname").clear()
driver.find_element_by_id("in-surname").send_keys("Blaszkowski")
driver.find_element_by_id("in-notes").clear()
driver.find_element_by_id("in-notes").send_keys("to jest text testowy")
driver.find_element_by_id("in-phone").clear()
driver.find_element_by_id("in-phone").send_keys("10981234098")
driver.find_element_by_id("save-btn").click()

driver.find_element_by_class_name("menu-border").click()
#driver.find_element_by_class_name("dropdown-toggle").click()
driver.find_element_by_xpath(".//*[@id='menu1']/li[1]/a").click()
driver.find_element_by_xpath(".//*[@id='start-edit']").click()
#driver.find_element_by_id("start-edit").click()
driver.find_element_by_id("in-name").clear()
driver.find_element_by_id("in-name").send_keys("Jan")
driver.find_element_by_id("in-surname").clear()
driver.find_element_by_id("in-surname").send_keys("Nowak")
driver.find_element_by_id("in-notes").clear()
driver.find_element_by_id("in-notes").send_keys("może tak a może nie")
driver.find_element_by_id("in-phone").clear()
driver.find_element_by_id("in-phone").send_keys("0000000000000")
driver.find_element_by_id("in-file").clear()
driver.find_element_by_id("in-file").send_keys("C:\\Users\\Uzytkownik\\Desktop\\Kurs spadochronowy AG - pdf\\WP_20170812_13_24_00_Pro.jpg")
driver.find_element_by_id("save-btn").click()








print("test jest ok :)")
driver.quit()
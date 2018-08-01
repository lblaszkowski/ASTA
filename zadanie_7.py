from selenium import webdriver
from selenium.webdriver import ActionChains




driver = webdriver.Chrome()
driver.get("https://buggy-testingcup.pgs-soft.com/")
driver.find_element_by_xpath("//h2[contains(.,'Zadanie 7')]").click()

#driver.maximize_window()
#driver.manage().window().maximize()


# element = driver.find_element_by_class_name("img-circle")
# target = driver.find_element_by_class_name("place-to-drop ")
# action_chains = ActionChains(driver)
# action_chains.drag_and_drop(element, target);


#ui-droppable
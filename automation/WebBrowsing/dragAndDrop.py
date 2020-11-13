from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

url = 'http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

source1 = driver.find_element_by_xpath('//*[@id="box1"]')
destination1 = driver.find_element_by_xpath('//*[@id="box101"]')
actions1 = ActionChains(driver)
actions1.drag_and_drop(source1, destination1).perform()

source2 = driver.find_element_by_xpath('//*[@id="box2"]')
destination2 = driver.find_element_by_xpath('//*[@id="box102"]')
actions2 = ActionChains(driver)
actions2.drag_and_drop(source2, destination2).perform()

source3 = driver.find_element_by_xpath('//*[@id="box3"]')
destination3 = driver.find_element_by_xpath('//*[@id="box103"]')
actions3 = ActionChains(driver)
actions3.drag_and_drop(source3, destination3).perform()

source4 = driver.find_element_by_xpath('//*[@id="box4"]')
destination4 = driver.find_element_by_xpath('//*[@id="box104"]')
actions4 = ActionChains(driver)
actions4.drag_and_drop(source4, destination4).perform()

source5 = driver.find_element_by_xpath('//*[@id="box5"]')
destination5 = driver.find_element_by_xpath('//*[@id="box105"]')
actions5 = ActionChains(driver)
actions5.drag_and_drop(source5, destination5).perform()

source6 = driver.find_element_by_xpath('//*[@id="box6"]')
destination6 = driver.find_element_by_xpath('//*[@id="box106"]')
actions6 = ActionChains(driver)
actions6.drag_and_drop(source6, destination6).perform()

source7 = driver.find_element_by_xpath('//*[@id="box7"]')
destination7 = driver.find_element_by_xpath('//*[@id="box107"]')
actions7 = ActionChains(driver)
actions7.drag_and_drop(source7, destination7).perform()

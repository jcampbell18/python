from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
messageField.send_keys('Hello Jason')
showMessageButton = driver.find_element_by_xpath('//*[@id="get-input"]/button')
showMessageButton.click()
additionalField1 = driver.find_element_by_xpath('//*[@id="sum1"]')
additionalField1.send_keys('10')
additionalField2 = driver.find_element_by_xpath('//*[@id="sum2"]')
additionalField2.send_keys('11')
getTotalButton = driver.find_element_by_xpath('//*[@id="gettotal"]/button')
getTotalButton.click()

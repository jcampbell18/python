from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

url = 'https://www.google.com/earth/'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

xPath = '/html/body/header/div/nav[1]/ul[2]/li[2]/a/span/span'
wait = WebDriverWait(driver, 20)
launchEarthButton = wait.until(ec.element_to_be_clickable((By.XPATH, xPath)))
launchEarthButton.click()

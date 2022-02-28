import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

ser = Service("D:\Training\Selenium\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=ser)
driver.get("https://www.amazon.com/")

driver.maximize_window()
driver.implicitly_wait(30)

accSingIn = driver.find_element(By.ID,"nav-link-accountList")
hover = ActionChains(driver)
hover.move_to_element(accSingIn).perform()

driver.find_element(By.LINK_TEXT,"Account").click()
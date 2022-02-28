import time

from selenium import webdriver
#New Comment
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\Training\Selenium\Drivers\chromedriver.exe")
driver.get("https://qaotis.rescue.org/Home/Login")

driver.maximize_window()
driver.implicitly_wait(20)

driver.find_element(By.ID,"username").send_keys("Shimulah")

driver.find_element(By.ID,"password").send_keys("X7emy88cc")

driver.find_element(By.NAME,"login-submit").click()

driver.find_element(By.LINK_TEXT,"Support For Refugees").click()

driver.find_element(By.LINK_TEXT,"Documents").click()

driver.find_element(By.CSS_SELECTOR,"#container > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div > button.btn.btn-primary").click()

driver.find_element(By.XPATH,"//input[@type='file']").send_keys("D:\Training\QA\QA\Documents\SDLC.jpg")


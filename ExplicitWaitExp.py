from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
import time

from selenium import webdriver

from selenium.webdriver.common.by import By

ser = Service("D:\Training\Selenium\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=ser)
driver.get("https://qaotis.rescue.org/Home/Login")

driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element(By.ID,"username").send_keys("Shimulah")

driver.find_element(By.ID,"password").send_keys("X7emy88cc")

driver.find_element(By.NAME,"login-submit").click()

driver.back()
driver.forward()
driver.refresh()

while(True):
    try:
        driver.find_element(By.LINK_TEXT, "New").click()
        break
    except:
        time.sleep(2)
        continue
#expwait = WebDriverWait(driver,5)
#expwait.until(expected_conditions.invisibility_of_element_located((By.XPATH,"//h1[text()='Please wait...']")))



driver.find_element(By.LINK_TEXT,"Opportunity").click()

progAreaDD = driver.find_element(By.NAME,"ProgramAreaId")
dd = Select(progAreaDD)
dd.select_by_visible_text("CRRD")

wait = WebDriverWait(driver,5)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"#SubmittingOrganizationalUnit > option:nth-child(2)")))

leadUnit = driver.find_element(By.ID,"SubmittingOrganizationalUnit")
leadUnitDD = Select(leadUnit)
leadUnitDD.select_by_index(1)

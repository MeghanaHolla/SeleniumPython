from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


ser = Service("D:\Training\Selenium\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=ser)
driver.get("https://the-internet.herokuapp.com/")

driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element(By.LINK_TEXT,"Multiple Windows").click()

driver.find_element(By.LINK_TEXT,"Click Here").click()

windows = driver.window_handles

driver.switch_to.window(windows[1])

actualText = driver.find_element(By.CSS_SELECTOR,"body > div.example > h3").text

expectedText = "New Window"

if actualText == expectedText:
    print("Pass")
else:
    print("Fail")

driver.close()

driver.switch_to.window(windows[0])

driver.close()
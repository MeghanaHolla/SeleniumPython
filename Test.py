import pytest
from selenium import webdriver


def test_VerifyFBTitle():
    driver = webdriver.Chrome(executable_path="D:\Training\Selenium\Drivers\\chromedriver.exe")
    driver.get("https://www.facebook.com")
    actualTitle = driver.title
    expectedTitle = "Facebook – log in or sign up"
    assert actualTitle == expectedTitle
    driver.close()

def test_VerifyFBTitle2():
    driver = webdriver.Chrome(executable_path="D:\Training\Selenium\Drivers\\chromedriver.exe")
    driver.get("https://www.facebook.com")
    actualTitle = driver.title
    expectedTitle = "Facebook – log in o sign up"
    assert actualTitle == expectedTitle
    driver.close()

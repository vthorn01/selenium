from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

se = Service(executable_path="C:\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=se)

driver.get("http://demostore.supersqa.com/")
time.sleep(5000)
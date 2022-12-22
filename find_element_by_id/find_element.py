from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
import pdb

se = Service(executable_path="C:\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=se)

driver.get("http://demostore.supersqa.com/")

cart = driver.find_element(By.ID, "site-header-cart")
cart.click()
pdb.set_trace()
time.sleep(5000)
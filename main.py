import time, random, datetime
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

delay = 10

USERNAME = "ubaid_meo_ahmed"
PASSWORD = "alpha_code@123"


date = datetime.datetime.now().strftime("%Y-%m-%d")
delay = 10
POST_LIKE = 5

driver = webdriver.Firefox()
driver.get("https://www.instagram.com/accounts/login/?hl=en")
time.sleep(2)
username = driver.find_element_by_name("username")
username.send_keys(USERNAME)
time.sleep(3)
password = driver.find_element_by_name("password")
password.send_keys(PASSWORD)
time.sleep(2)
login_btn = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
login_btn.click()
time.sleep(3)
try:
    #click save information
    not_now_btn = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/section/div/button'))) 
    not_now_btn.click()
    time.sleep(2)
    #click no notification btn
    notfy_on = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')))
    notfy_on.click()
except:
    pass
# login complete 
# git update 
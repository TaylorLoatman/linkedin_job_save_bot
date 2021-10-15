from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import os

PASSWORD = os.environ.get('PASSWORD_LINKEDIN')

chrome_driver_path = "/Users/TaylorLoatman/chromedriver"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)


driver.get('https://www.linkedin.com/jobs/search/?distance=25&f_AL=true&f_WT=2&geoId=106224388&keywords=python%20developer&location=Atlanta%2C%20Georgia%2C%20United%20States&locationId=&sortBy=R')
driver.maximize_window()
sign_in = driver.find_element(By.CSS_SELECTOR, '.nav__button-secondary')
sign_in.click()
time.sleep(3)

email_input = driver.find_element(By.NAME, 'session_key')
email_input.send_keys('taylor.loatman@yahoo.com')
pw_input = driver.find_element(By.NAME, 'session_password')
pw_input.send_keys(PASSWORD)
get_in = driver.find_element(By.CSS_SELECTOR, '.from__button--floating')
get_in.click()
time.sleep(3)

try:
    jobs = driver.find_elements(By.CSS_SELECTOR, '.mt5 .jobs-save-button')
    for job in jobs:
        print(job.text)
        # job.click()
        # time.sleep(3)
        # remove_from_search = driver.find_element(By.CSS_SELECTOR, '.job-card-container__action-container button')
        # remove_from_search.click()
        # time.sleep(3)
except NoSuchElementException:
    pass

# driver.quit()
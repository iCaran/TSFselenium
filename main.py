import os
from selenium import webdriver
from selenium.webdriver.common.by import By

os.environ['PATH'] += r"C:/SeleniumDrivers"
driver = webdriver.Chrome()

print("#\tTEST\tRESULT")

# HOME PAGE
driver.get("https://www.thesparksfoundationsingapore.org/")
print("1.\tHome Page Loads:\tOK")

# LOGO
logo = driver.find_element(By.CSS_SELECTOR, ".navbar-brand > img")
print("1.\tLogo on Home Page Header:\tOK")

# NAVBAR
nav_test="About Us\nPolicies and Code\nPrograms\nLINKS\nJoin Us\nContact Us"
nav = driver.find_element(By.CLASS_NAME, "navbar-nav")
#nav_items = nav.find_element(By.TAG_NAME, "li")
#print(repr(nav.text))
if (nav.text==nav_test):
    print("1.\tHeader on Home Page:\tOK")

driver.quit()

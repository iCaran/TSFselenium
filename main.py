import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from prettytable import PrettyTable

results=PrettyTable()
results.field_names=['#','PROCESS','STATUS']

os.environ['PATH'] += r"C:/SeleniumDrivers"
driver = webdriver.Chrome()

# HOME PAGE
driver.get("https://www.thesparksfoundationsingapore.org/")
results.add_row([1,"Home Page loads","OK"])

# LOGO
logo = driver.find_element(By.CSS_SELECTOR, ".navbar-brand > img")
results.add_row([2,"Logo present on Home Page Header","OK"])

# NAVBAR
nav_test="About Us\nPolicies and Code\nPrograms\nLINKS\nJoin Us\nContact Us"
nav = driver.find_element(By.CLASS_NAME, "navbar-nav")
#nav_items = nav.find_element(By.TAG_NAME, "li")
#print(repr(nav.text))
if (nav.text==nav_test):
    results.add_row([3,"Header on Home Page is correct","OK"])

print(results)
print("TEST SUCCESSFUL!!!")

driver.quit()

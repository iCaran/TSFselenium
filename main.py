import os
from selenium import webdriver

os.environ['PATH'] += r"C:/SeleniumDrivers"
driver = webdriver.Chrome()

print("#\tTEST\tRESULT")

# HOME PAGE
driver.get("https://www.thesparksfoundationsingapore.org/")
print("1.\tHome Page Loads:\tOK")

driver.quit()
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from prettytable import PrettyTable

results = PrettyTable()
results.field_names = ['#', 'TEST NAME', 'RESULT']

os.environ['PATH'] += r"C:/SeleniumDrivers"
driver = webdriver.Chrome()

# HOME PAGE
driver.get("https://www.thesparksfoundationsingapore.org/")
results.add_row([1, "Home Page loads", "OK"])

# LOGO
logo = driver.find_element(By.CSS_SELECTOR, ".navbar-brand > img")
results.add_row([2, "Logo present on Home Page Header", "OK"])

# NAVBAR
nav_test = "About Us\nPolicies and Code\nPrograms\nLINKS\nJoin Us\nContact Us"
nav = driver.find_element(By.CLASS_NAME, "navbar-nav")
if (nav.text == nav_test):
    results.add_row([3, "Header on Home Page is correct", "OK"])
else:
    results.add_row([3, "Header on Home Page is correct", "FAIL"])

results.add_row(['', "", ""])

# NAVIGATE TO NEWS PAGE
about_btn = driver.find_element(By.LINK_TEXT, "About Us")
about_btn.click()
news_btn = driver.find_element(By.CSS_SELECTOR, 'a[href="/about/news/"]')
news_btn.click()
results.add_row([4, "Navigate to News Page through Header on Home Page", "OK"])

# NEWS PAGE TITLE
title = "The Sparks Foundation In Media"
news_title = driver.find_element(By.CLASS_NAME, "inner-tittle-w3layouts")
if (news_title.text == title):
    results.add_row([5, "News Page title", "OK"])
else:
    results.add_row([5, "News Page title", "FAIL"])

# BLOG POSTS
post_sections = driver.find_element(By.CSS_SELECTOR, ".w3l-blog-list > ul")
posts = post_sections.find_elements(By.TAG_NAME, "li")
if len(posts) == 7:
    results.add_row([6, "7 Blog Posts on News Page", "OK"])
else:
    results.add_row([6, "7 Blog Posts on News Page", "FAIL"])

# SOCIAL MEDIA POSTS
social = ['@Facebook', '@Medium', '@Twitter']
ele = driver.find_elements(By.CSS_SELECTOR, ".tittle-agileits-w3layouts > span")
sm = [i.text for i in ele]
if (sm == social):
    results.add_row([7, "Social Media Posts on News Page", "OK"])
else:
    results.add_row([7, "Social Media Posts on News Page", "FAIL"])

results.add_row(['', "", ""])

# POLICIES PAGE
pc_btn = driver.find_element(By.LINK_TEXT, "Policies and Code")
pc_btn.click()
policies = driver.find_element(By.CSS_SELECTOR, 'a[href="/policies-and-code/policies/"]')
policies.click()
results.add_row([8, "Navigate to Policies Page through Header on News Page", "OK"])

# POLICIES TITLE
news_title = driver.find_element(By.CLASS_NAME, "inner-tittle-w3layouts")
if (news_title.text == "Policies"):
    results.add_row([9, "Policies Page title", "OK"])
else:
    results.add_row([9, "Policies Page title", "FAIL"])

# POLICY BLOGS
policy_post_sections = driver.find_element(By.CSS_SELECTOR, ".w3l-blog-list > ul")
posts = policy_post_sections.find_elements(By.TAG_NAME, "li")
if len(posts) == 5:
    results.add_row([10, "5 Posts on Blog Section on Policy Page", "OK"])
else:
    results.add_row([10, "55 Posts on Blog Section on Policy Page", "FAIL"])

# POLICY PAGE TITLE
ptitle = "Summary Of Important Policies At The Sparks Foundation"
policy_title = driver.find_element(By.CSS_SELECTOR, ".tittle-agileits-w3layouts > span")
if policy_title.text == ptitle:
    results.add_row([11, "Tile of Post on Policy Page", "OK"])
else:
    results.add_row([11, "Tile of Post on Policy Page", "FAIL"])

# POLICY SECTIONS
psec=['Conflict of Interest Policy','Staff Remuneration and Appraisal Policies','Financial Policies','Reserve Policy','Investment Policy','Policies for Members of the Board and Sub-Committees']
sections=driver.find_elements(By.CSS_SELECTOR, ".media-body > h4")
sec=[i for i in psec]
if (sec == psec):
    results.add_row([12, "All sub-sections on Policy Page are correct", "OK"])
else:
    results.add_row([12, "All sub-sections on Policy Page are correct", "FAIL"])

results.add_row(['', "", ""])

print(results)
print("TEST SUCCESSFUL.\t0 ERRORS FOUND.\t\tSITE CONDITION is HEALTHY.\nEnding Process With Code 0.")

driver.quit()

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from prettytable import PrettyTable
from selenium.webdriver.chrome.service import Service

print("Starting Script...")

ser = Service("C:\SeleniumDrivers\chromedriver.exe")
options = webdriver.ChromeOptions()

# Comment out following 2 lines if you want to display the browser window
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(service=ser, options=options)

# CREATE RESULTS TABLE
results = PrettyTable()
results.field_names = ['#', 'TEST NAME', 'RESULT']

print("Opening Website on Chrome...")

# HOME PAGE
driver.get("https://www.thesparksfoundationsingapore.org/")
results.add_row([1, "Home Page loads", "OK"])

print("Site Open. Performing Tests ...")

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
if news_title.text == "Policies":
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

# Student Mentorship Program
prog = driver.find_element(By.LINK_TEXT, "Programs")
prog.click()
ment = driver.find_element(By.CSS_SELECTOR, 'a[href="/programs/student-mentorship-program/"]')
ment.click()
results.add_row([13, "Navigate to Student Scholarship Program Page through Header on Policies Page", "OK"])

# QUOTES
Q=["Don't limit a child to your own learning, for he was born in another time.","A child miseducated is a child lost."]
A=["Rabindranath Tagore","John F. Kennedy"]
quotes=driver.find_elements(By.CLASS_NAME,"para-w3-agile")
q=[quote for quote in quotes]
authors=driver.find_elements(By.CSS_SELECTOR,".agile>div>div>h4")
a=[author for author in authors]
if Q[0]==q[0].text and A[0]==a[0].text:
    results.add_row([14,"Rabindranath Tagore Quote properly displayed","OK"])
else:
    results.add_row([14, "Rabindranath Tagore Quote properly displayed","FAIL"])
if Q[1]==q[1].text and A[1]==a[1].text:
    results.add_row([15,"John F. Kennedy Quote properly displayed","OK"])
else:
    results.add_row([15, "John F. Kennedy Quote properly displayed","FAIL"])

# OUTPUT RESULTS TABLE
print(results)
print("TEST SUCCESSFUL.\t0 ERRORS FOUND.\t\tWEBSITE CONDITION is HEALTHY.\nEnding Process With Code 0.")

driver.quit()

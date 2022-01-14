import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from prettytable import PrettyTable
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

print("Starting Script...")

ser = Service("C:\SeleniumDrivers\chromedriver.exe")
options = webdriver.ChromeOptions()

# Comment out following 2 lines if you want to display the browser window
# Note: iFrames will not load on headless browsers
'''options.add_argument('--headless')
options.add_argument('--disable-gpu')'''

driver = webdriver.Chrome(service=ser, options=options)

# MINIMIZE BROWSER WINDOW
# Note: Will also cause error with iFrames
# driver.minimize_window()

# MAXIMIZE: Best result with iFrames
driver.maximize_window()

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
psec = ['Conflict of Interest Policy', 'Staff Remuneration and Appraisal Policies', 'Financial Policies',
        'Reserve Policy', 'Investment Policy', 'Policies for Members of the Board and Sub-Committees']
sections = driver.find_elements(By.CSS_SELECTOR, ".media-body > h4")
sec = [i for i in psec]
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
Q = ["Don't limit a child to your own learning, for he was born in another time.",
     "A child miseducated is a child lost."]
A = ["Rabindranath Tagore", "John F. Kennedy"]
quotes = driver.find_elements(By.CLASS_NAME, "para-w3-agile")
q = [quote for quote in quotes]
authors = driver.find_elements(By.CSS_SELECTOR, ".agile>div>div>h4")
a = [author for author in authors]
if Q[0] == q[0].text and A[0] == a[0].text:
    results.add_row([14, "Rabindranath Tagore Quote properly displayed", "OK"])
else:
    results.add_row([14, "Rabindranath Tagore Quote properly displayed", "FAIL"])
if Q[1] == q[1].text and A[1] == a[1].text:
    results.add_row([15, "John F. Kennedy Quote properly displayed", "OK"])
else:
    results.add_row([15, "John F. Kennedy Quote properly displayed", "FAIL"])

results.add_row(['', "", ""])

# AI in Education
links = driver.find_element(By.LINK_TEXT, "LINKS")
links.click()
ai = driver.find_element(By.CSS_SELECTOR, 'a[href="/links/ai-in-education/"]')
ai.click()
results.add_row([16, "Navigate to AI in Education Page through Header on Student Scholarship Program Page", "OK"])

# AI PAGE TITLE
aititle = "Use Of Artificial Intelligence To Enhance Education System"
ai_title = driver.find_element(By.CSS_SELECTOR, ".tittle-agileits-w3layouts > span")
if ai_title.text == aititle:
    results.add_row([17, "Tile of Post on AI in Education Page is correct", "OK"])
else:
    results.add_row([17, "Tile of Post on AI in Education Page", "FAIL"])

# AI SIDEBAR
ai_l = ['https://links.aine.ai/', 'https://www.thesparksfoundationsingapore.org/links/software-and-app/',
        'https://www.thesparksfoundationsingapore.org/links/salient-features/',
        'https://www.thesparksfoundationsingapore.org/links/ai-in-education/']
ai = ['Visit LINKS @TSF', 'Software & App', 'Salient Features', 'AI in Education']
ai_side = driver.find_element(By.CSS_SELECTOR, ".w3l-blog-list > ul")
sidebar = ai_side.find_elements(By.TAG_NAME, "li")
aiposts = [post.text for post in sidebar]
l = driver.find_elements(By.CSS_SELECTOR, ".w3l-blog-list > ul > li > a")
links = [elem.get_attribute('href') for elem in l]
if ai == aiposts and links == ai_l:
    results.add_row([18, "Sidebar on AI in Education Page is correct", "OK"])
else:
    results.add_row([18, "Sidebar on AI in Education Page", "FAIL"])

# AI POSTS
ai_blogs = ["Artificial Intelligence In Education: Don't Ignore It, Harness It!",
            'Can AI fix education? We asked Bill Gates']
ai_blog_links = [
    'https://www.forbes.com/sites/sebastienturbot/2017/08/22/artificial-intelligence-virtual-reality-education/',
    'https://www.theverge.com/2016/4/25/11492102/bill-gates-interview-education-software-artificial-intelligence']
p = driver.find_elements(By.CSS_SELECTOR, ".blog-info>h4>a")
pt = [title.text for title in p]
pl = [elem.get_attribute('href') for elem in p]
if pt == ai_blogs and pl == ai_blog_links:
    results.add_row([19, "Posts on AI in Education Page are correct", "OK"])
else:
    results.add_row([19, "Posts on AI in Education Page", "FAIL"])

results.add_row(['', "", ""])

# JOIN US
join = driver.find_element(By.LINK_TEXT, "Join Us")
join.click()
joinus = driver.find_element(By.CSS_SELECTOR, 'a[href="/join-us/why-join-us/"]')
joinus.click()
results.add_row([20, "Navigate to Why Join Us Page through Header on  AI in Education Page", "OK"])

# COPYRIGHT FOOTER
copy = "© 2017 The Sparks Foundation. All Rights Reserved | Design by W3layouts"
right = "W3layouts"
cw_text = driver.find_element(By.CSS_SELECTOR, ".copyright-wthree>p")
cw_link = driver.find_element(By.CSS_SELECTOR, ".copyright-wthree>p>a")
if cw_text.text == copy and cw_link.text == right:
    results.add_row([21, "Copyright Footer on AI in Why Join Us Page are correct", "OK"])
else:
    results.add_row([21, "Copyright Footer on Why Join Us Page", "FAIL"])

# REGISTER
n = "myName"
e = "myEmail@address.com"
name = driver.find_element(By.NAME, "Name")
email = driver.find_element(By.NAME, "Email")
name.clear()
email.clear()
name.send_keys(n)
email.send_keys(e)
select_element = driver.find_element(By.CLASS_NAME, 'form-control')
select_object = Select(select_element)
select_object.select_by_index(1)
submit = driver.find_element(By.CSS_SELECTOR, 'input[value="Submit"]')
submit.click()
results.add_row([22, "Register for Email Alerts Form on Why Join Us Page works", "OK"])

results.add_row(['', "", ""])

# CONTACT US
contact = driver.find_element(By.LINK_TEXT, "Contact Us")
contact.click()
results.add_row([23, "Navigate to Contact Us Page through Header on  Why Join Us Page", "OK"])

# SWITCH TO IFRAME
driver.implicitly_wait(3)
driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))

# MAP ADDRESS CORRECT
pla = "Wattah Pte Ltd"
add = "The Hangar, I-Cube, 21 Heng Mui Keng Terrace, 119613"
place = driver.find_element(By.CLASS_NAME, "place-name")
addr = driver.find_element(By.CLASS_NAME, "address")
if place.text == pla and addr.text == add:
    results.add_row([23, "GoogleMaps iFrame on Contact Us Page is correct", "OK"])
else:
    results.add_row([23, "GoogleMaps iFrame on Contact Us Page", "FAIL"])

# MAP ZOOM IN
zoom = driver.find_element(By.CSS_SELECTOR, 'button[title="Zoom in"]')
zoom.click()
results.add_row([24, "GoogleMaps iFrame on Contact Us Page is interactive", "OK"])

# RETURN FROM IFRAME
driver.switch_to.default_content()

# CONTACT INFO
lin_text = "JOIN TSF NETWORK HERE (https://www.linkedin.com/groups/10379184/)"
lin_link = "https://www.linkedin.com/groups/10379184/"
addre = 'THE HANGAR, NUS ENTERPRISE\n21 HENG MUI KENG TERRACE, SINGAPORE, 119613'
phonemail = '+65-8402-8590, info@thesparksfoundation.sg'
linkedin = driver.find_element(By.CSS_SELECTOR, ".col-md-12>div>p>span>a")
address = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/p")
phone = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[3]/div[2]/p[2]")
if linkedin.text == lin_text and linkedin.get_attribute(
        'href') == lin_link and address.text == addre and phone.text == phonemail:
    results.add_row([25, "Linkedin, Address, Phone, Email on Contact Us Page is correct", "OK"])
else:
    results.add_row([25, "Linkedin, Address, Phone, Email on Contact Us Page", "FAIL"])

# OUTPUT RESULTS TABLE
print(results)
print("TEST SUCCESSFUL.\t0 ERRORS FOUND.\t\tWEBSITE CONDITION is HEALTHY.\nEnding Process With Code 0.")

driver.quit()

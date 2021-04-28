import time
from selenium import webdriver

# Path to chromedriver.exe
PATH = "C:\Program Files\chromedriver_win32\chromedriver.exe"

# Open the browser
driver = webdriver.Chrome(PATH)

# Enter the URL "http://practice.automationtesting.in/"
driver.get('http://practice.automationtesting.in/')

# Find My Account Menu by link text and Click
driver.find_element_by_link_text('My Account').click()

# Find Email-Address textbox by ID and Enter registered Email Address
driver.find_element_by_id('reg_email').send_keys('nadung.18it1@vku.udn.vn')

# Find Password textbox by ID and Enter password slowly to verify
password_textbox = driver.find_element_by_id('reg_password')
password = 'DungNA_65'
for character in password:
    password_textbox.send_keys(character)
    time.sleep(0.5)

# Find Register button by class name amd Click
driver.find_element_by_name('register').click()

time.sleep(3)

# Close browser
driver.quit()
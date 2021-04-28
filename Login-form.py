import time
from selenium import webdriver

# Path to chromedriver.exe
PATH = "C:\Program Files\chromedriver_win32\chromedriver.exe"

# Open the browser
driver = webdriver.Chrome(PATH)

# Enter the URL "https://the-internet.herokuapp.com"
driver.get('https://the-internet.herokuapp.com')

# Find Form Authentication by link text and Click
driver.find_element_by_link_text('Form Authentication').click()

# Find Username textbox by ID and Enter 'tomsmith'
driver.find_element_by_id('username').send_keys('tomsmith')

# Find password textbox by ID and Enter 'SuperSecretPassword!'
driver.find_element_by_id('password').send_keys('SuperSecretPassword!')

# Find Login button by tag name amd Click
driver.find_element_by_tag_name('button').click()

# Print the title of page
print(driver.title)

time.sleep(3)

# Close browser
driver.quit()
import time
import datetime
from selenium import webdriver

# Path to chromedriver.exe
PATH = "C:\Program Files\chromedriver_win32\chromedriver.exe"

# Open the browser
driver = webdriver.Chrome(PATH)

# Enter the URL "https://itmscoaching.herokuapp.com/form"
driver.get('https://itmscoaching.herokuapp.com/form')

# Find First name textbox by ID and Enter 'Binh'
driver.find_element_by_id('first-name').send_keys('Binh')

# Find Last name textbox by ID and Enter 'Nguyen'
driver.find_element_by_id('last-name').send_keys('Nguyen')

# Find Job title textbox by ID and Enter 'Tester'
driver.find_element_by_id('job-title').send_keys('Tester')

# Find Grad School radio button by ID and Click
driver.find_element_by_id('radio-button-3').click()

# Find Female checkbox by ID and Click
driver.find_element_by_id('checkbox-2').click()

# Find 5-9 option in dropdown by xpath and Click
driver.find_element_by_xpath('//*[@id="select-menu"]/option[4]').click()

# Select Date 20/7/2011
# Find Date Picker by ID and Click
driver.find_element_by_id('datepicker').click()
# Select Date Picker Switch by class name and Click to select year and month
driver.find_element_by_class_name('datepicker-switch').click()
# Find Previous button by css selector
prev_button = driver.find_element_by_css_selector('.datepicker-months .prev')
# Find Next button by css selector
next_button = driver.find_element_by_css_selector('.datepicker-months .next')
# Select year 2011
current_year = int(datetime.datetime.now().year)
selected_year = 2011
if (current_year > selected_year):
    for i in range (0, current_year - selected_year):
        prev_button.click()
        time.sleep(0.2)
else:
    for i in range (0, selected_year - current_year):
        next_button.click()
        time.sleep(0.2)
# Find month 7 span by xpath and Click
driver.find_element_by_xpath('/html/body/div[2]/div[2]/table/tbody/tr/td/span[7]').click()
# Find day 20 span by xpath and Click
driver.find_element_by_xpath('/html/body/div[2]/div[1]/table/tbody/tr[4]/td[4]').click()

time.sleep(2)

# Find Submit button by link text amd Click
driver.find_element_by_link_text('Submit').click()

time.sleep(3)

# Close browser
driver.quit()
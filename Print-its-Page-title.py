import time
from selenium import webdriver

# Path to chromedriver.exe
PATH = "C:\Program Files\chromedriver_win32\chromedriver.exe"

# Open the browser
driver = webdriver.Chrome(PATH)

# Enter the URL "http://practice.automationtesting.in/"
driver.get('http://practice.automationtesting.in/')

# Maximize browser window
driver.maximize_window()

# Print the title of page
print(driver.title)

time.sleep(2)

# Close browser
driver.quit()
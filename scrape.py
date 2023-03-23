from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
import time



def browserSetup():
    driverPath = os.getcwd() + '\\drivers\\chromedriver.exe'    # Path to chromedriver.exe
    bravePath = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"   # Path to brave.exe
    options = webdriver.ChromeOptions()   # Create options object
    options.binary_location = bravePath  # Set binary location to brave.exe
    browser = webdriver.Chrome(service=Service(driverPath), options=options) # Create browser object
    return browser # Return browser object

limit = int(input("Enter limit: "))

driver = browserSetup() # Create browser object
url = "https://duckduckgo.com/?q=children+playing+in+the+park&t=h_&iar=images&iax=images&ia=images" # URL to scrape
driver.implicitly_wait(5) # Wait 5 seconds for page to load
driver.maximize_window() # Maximize window
driver.get(url)

count = 0
driver.find_element("class name", "js-lazyload").click()
for _ in range(limit):
    driver.find_element("class name", "js-detail-next").click()
    
    time.sleep(0.15)
    count += 1
print(f"Scraped {count} images")
print("program run successfullly")
time.sleep(5) # Wait 5 seconds for page to load

# https://duckduckgo.com/?q=gigi+hadid&t=h_&iar=images&iax=images&ia=images
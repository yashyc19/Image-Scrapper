from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import fileManager as fm
import os
import time


def driverSetup():
    driverPath = os.getcwd() + '\\drivers\\chromedriver.exe'    # Path to chromedriver.exe
    browserPath = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"   # Path to brave.exe
    options = webdriver.ChromeOptions()   # Create options object
    options.binary_location = browserPath  # Set binary location to brave.exe
    driver = webdriver.Chrome(service=Service(driverPath), options=options) # Create browser object
    return driver # Return browser object


def scrapeImages(searchLink, limit, outputFileName):    # url, limit, outputFileName
    print('Log: Scraping images...')
    driver = driverSetup() # Create browser object
    driver.implicitly_wait(5) # Wait 5 seconds for page to load
    driver.maximize_window() # Maximize window
    driver.get(searchLink)
    
    try:
        count = 0
        driver.find_element("class name", "js-lazyload").click()
        while count < limit:
            # extract image link and store in a text file
            link = driver.find_element("class name", "js-detail-img-high").get_attribute("src")
            fm.addToFile(outputFileName, link)            
            driver.find_element("class name", "js-detail-next").click()
            time.sleep(0.15)
            count += 1

    except Exception as err:
        print("An error occured: ", err)
        return

    finally:
        print(f"Log: Scraped {count} images")
        print(f"Log: Added links to {outputFileName}.txt")
        driver.close()
        driver.quit()
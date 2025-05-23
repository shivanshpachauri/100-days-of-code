# Advanced Web Scraping
# Web Automaton

# Selenium Web Driver
from selenium import webdriver
from selenium.webdriver.common.by import By

# install Chrome
# install and setup selenium
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

# Acts as a Bridge to work with Chrome
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.in/Linear-Programming-Game-Theory-2021/dp/9387162788/ref=sr_1_5?crid=ZLD9JV2V60P0&dib=eyJ2IjoiMSJ9.DZG4b73q_eg4eg8TSe-ApkTyS-3I6Ho8R3KVuFkXCcNlDiey6Te5kXvWPFH5rJB7UKd5mdusXyZn5KEWNoS_mN85haEGFByunEKQSuzt8-0IYK8GVKKtt6JPNSKoIhyxLbG_dw3hB4fk0G8O1vVTuMFaHVZpyCgCGZurTMqD2N0pjUO7iPryLnYtAaTyRxk4VKAWzks-Yr-lBi7rH8Pw3GvH1qiAXkah-DZkF3s67jg.m8cpjZNyFXKptDdA8djpEAUZkmcB-x6nEQAVnCC3Ml0&dib_tag=se&keywords=linear+programming+and+game+theory&qid=1747456085&sprefix=linear+programming+and+game+theory%2Caps%2C280&sr=8-5")

# Selenium Locator Strategy
whole=driver.find_element(By.CLASS_NAME,value='a-price-whole').text

# fraction=driver.find_element(By.CLASS_NAME,value='a-price-fraction').text or .tag_name
# fraction.get_attribute("placeholder")

# fraction=driver.find_element(By.ID,value='submit').text or .tag_name


# fraction=driver.find_element(By.CSS_SELECTOR,value='submit').text or .tag_name

# bug_link=driver.find_element(By.XPATH,value='').text

# multiplelements=driver.find_elements()

print(f"the price is {whole}")


# closes the tab
# driver.close()

# closes the browser
driver.quit()

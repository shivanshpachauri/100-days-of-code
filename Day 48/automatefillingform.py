# Selenium Web Driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# install Chrome
# install and setup selenium
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

# Acts as a Bridge to work with Chrome
driver=webdriver.Chrome(options=chrome_options)
wiki=driver.get("https://en.wikipedia.org/wiki/Main_Page")


article_count=driver.find_elements(By.CSS_SELECTOR,"div#articlecount ul li a")
article_count.click()

# find element by link text
all_portals=driver.find_element(By.LINK_TEXT,value='Content-links')

search=driver.find_element(By.NAME,value='search')
# 
# search.send_keys("Python")
search.send_keys("Python",Keys.enter)
driver.quit()
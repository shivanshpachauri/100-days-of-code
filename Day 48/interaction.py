# Selenium Web Driver
from selenium import webdriver
from selenium.webdriver.common.by import By

# install Chrome
# install and setup selenium
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

# Acts as a Bridge to work with Chrome
driver=webdriver.Chrome(options=chrome_options)
wiki=driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_number=driver.find_elements(By.CSS_SELECTOR,"div#articlecount ul li a")
print(article_number[1].text)
# for element in article_number:
#     print(element.text)
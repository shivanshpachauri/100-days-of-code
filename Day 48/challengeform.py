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
appbrewery=driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name=driver.find_element(By.NAME,'fName')
first_name.send_keys("Shivansh",Keys.TAB)


last_name=driver.find_element(By.NAME,'lName')

last_name.send_keys("pachauri",Keys.TAB)

email=driver.find_element(By.NAME,"email")

email.send_keys("shivanshpachauri00@gmail.com",Keys.TAB)

submit_button=driver.find_element(By.CSS_SELECTOR,"button")
submit_button.click()

# driver.quit()
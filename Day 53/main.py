from bs4 import BeautifulSoup
import requests
response=requests.get('https://appbrewery.github.io/Zillow-Clone/')
soup=BeautifulSoup(response.text,'html.parser')

all_price=[]
price=soup.find_all('span',class_='PropertyCardWrapper__StyledPriceLine')

links=soup.find_all('a',class_='StyledPropertyCardDataArea-anchor')

all_links=[]
addresses=[]
current=''
for i in price:
    current=i.text.replace('/mo','').replace("+",'').replace('bd','').replace(',','')
    all_price.append(current)


for j in links:
    addresses.append(j.text.replace('\n','').replace(' ','').replace('|',''))
    all_links.append(j.get('href'))


# selenium part starts here

# Advanced Web Scraping
# Web Automaton
import time
# Selenium Web Driver
from selenium import webdriver
from selenium.webdriver.common.by import By

# install Chrome
# install and setup selenium
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

# Acts as a Bridge to work with Chrome
driver=webdriver.Chrome(options=chrome_options)
website=driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdKRzUApC0oXITjjGtvM2wzMDHctfohYst10-B9F_2VhvjViA/viewform")

max_length=max(len(all_links),len(all_price),len(addresses))


for i in range(0,max_length):

    form_price=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea')
    form_link=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea')
    form_address=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea')

    button=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    # driver.navigate().refresh()
    form_link.send_keys(all_links[i])
    
    form_price.send_keys(all_price[i])
    form_address.send_keys(addresses[i])
    button.click()
    time.sleep(3)
    driver.refresh()
driver.quit()

# for i in all_links:
#     form_link.send_keys(i)
# for j in all_price:
#     form_price.send_keys(j)
# for k in addresses:
#     form_address.send_keys(k)
# button.click()

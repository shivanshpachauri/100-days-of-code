# Selenium Web Driver
from selenium import webdriver
from selenium.webdriver.common.by import By

# install Chrome
# install and setup selenium
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

# Acts as a Bridge to work with Chrome
driver=webdriver.Chrome(options=chrome_options)
events=driver.get("https://www.python.org/")

events=driver.find_elements(By.XPATH,'//*[@id="content"]/div/section/div[3]/div[2]/div/ul')
nametime=[]
dict={}
i=0
k=1
for item in events:
    nametime=item.text.split("\n")
    for j in nametime:
        
        if(i%2==0):
            dict[k]={
                "time":j
            }
        else:
            dict[k].update({
                "name":j
            })
            k=k+1
        i=i+1
    # dict[i].name=nametime[0]
    # dict[i].time=nametime[1]

print(dict)

driver.quit()

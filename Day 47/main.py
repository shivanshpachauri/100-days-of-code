from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
response=requests.get("https://appbrewery.github.io/instant_pot/")
soup=BeautifulSoup(response.text,'html.parser')
price_whole=soup.find("span",class_="a-price-whole")
price_fraction=soup.find("span",class_="a-price-fraction")
totalnumber=f"{price_whole.get_text()}{price_fraction.get_text()}"
print(totalnumber)
# MUSICAL TIME MACHINE PROJECT
from bs4 import BeautifulSoup
import requests

year=input(" Which year do you want to travel to? Type the data in this format YYY-MM-DD:")
headers={"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:138.0) Gecko/20100101 Firefox/138.0"}
url=f'https://www.billboard.com/charts/hot-100/{year}/'
response=requests.get(url,headers=headers)
soup=BeautifulSoup(response.text,'html.parser')
# titles=soup.find_all("h3",id='title-of-a-story')
# print(titles)
titles=soup.select("li ul li h3")
song_names=[song.getText().strip() for song in titles]
print(song_names)
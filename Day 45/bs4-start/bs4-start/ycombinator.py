from bs4 import BeautifulSoup
import requests

response=requests.get("https://news.ycombinator.com/")
yc_web_page=response.text
soup=BeautifulSoup(yc_web_page,'html.parser')

title1=soup.title

titleline=soup.find_all('span',class_='titleline')
article_rank=soup.find_all('span',class_='rank')

article_text=[]
article_link=[]
rank=[]
for title in titleline:
    article_text.append(title.get_text())
    article_link.append(title.a.get("href"))
for rank1 in article_rank:
    rank.append(int(rank1.get_text().split('.')[0]))
# article_text=titleline.get_text()
# article_link=titleline.a.get("href")
# article_upvote=soup.find('div',class_='votearrow')



print("title= ",title1)
# print("titleline= ",titleline)
print("article link = ",article_link)
print("article text = ",article_text)
# print("article upvote = ",article_upvote)
print("article rank = ",rank)
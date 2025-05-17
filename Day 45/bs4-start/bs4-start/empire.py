from bs4 import BeautifulSoup
import requests

response=requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
empire_movies=response.text
soup=BeautifulSoup(empire_movies,'html.parser')
movies=soup.find_all("h3",class_='title')
movie_list=[]
for movie in movies:
    movie_list.append(movie.get_text()+"\n")
movie_list=movie_list[::-1]
print(movie_list)
with open("movie.txt",mode="w") as file:
    for m in movie_list:
        file.write(m)
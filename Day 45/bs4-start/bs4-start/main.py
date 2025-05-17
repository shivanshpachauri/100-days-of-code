from bs4 import BeautifulSoup
with open("website.html") as file:
    contents=file.read()
    # print(contents)

soup=BeautifulSoup(contents,'html.parser')
# print(soup.title)
# print(soup.title.name)

# print(soup.title.string)
# print(soup.prettify())

# print(soup.a)

all_p_tag=soup.find_all(name="a")
for tag in all_p_tag:
    # print(tag.getText())
    # print(tag.get("href"))
    pass
heading=soup.find(name='h1',id='name')

section_heading=soup.find(name='h3',_class='heading')

company_url=soup.select_one(selector="p a")
print(company_url)

name=soup.select_one(selector="#name")
print(name)

heading=soup.select(".heading")
print(heading)
import requests
from bs4 import BeautifulSoup
url="https://www.n11.com/bilgisayar/dizustu-bilgisayar"
html=requests.get(url).content
soup=BeautifulSoup(html,"html.parser")
list=soup.find("div",{"class":"listView"}).find_all("li",{"class":"column"})
for i in list:
    title=i.find("div",{"class":"pro"}).find("a")
    fiyat=i.find("div",{"class":"proDetail"}).find("a",{"class":"newPrice"}).find("ins").text
    print(title.get("title"),"fiyat--",fiyat)



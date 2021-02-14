import requests
import json
class Movieapp:
    def __init__(self):
        self.url="https://api.themoviedb.org/3/"
    def popmovie(self):
        result=requests.get(self.url+"movie/popular?api_key=d66cd0c7f93a81d02bd35de4464be3d0&language=en-US&page=1")
        result=result.text
        result=json.loads(result)
        for i in result["results"]:
            print(i["original_title"])
    def nowplaying(self):
        result=requests.get(self.url+"movie/now_playing?api_key=d66cd0c7f93a81d02bd35de4464be3d0&language=en-US&page=1")
        result=result.text
        result=json.loads(result)
        for i in result["results"]:
            print(i["original_title"])
    def keyworld(self,keyworld):
        result=requests.get(f"{self.url}search/keyword?api_key=d66cd0c7f93a81d02bd35de4464be3d0&query={keyworld}&page=1")
        result = result.text
        result = json.loads(result)
        for i in result["results"]:
            print("*"+i["name"])


movieapp=Movieapp()
while True:
    secim=input("1-popüler filmler\n2-vizyondaki filmler\n3-anahtar kelimle ile arama\n4-exit\n")
    if secim=="1":
        movieapp.popmovie()
    if secim=="2":
        movieapp.nowplaying()
    if secim=="3":
        keyworld=input("anahtar kelimeyi giriniz")
        movieapp.keyworld(keyworld)
    if secim=="4":
        break
    else:
        print("yanlış seçim yaptınız")
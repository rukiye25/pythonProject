import requests
import json
#api alman lazım
result=requests.get("https://api.themoviedb.org/3/movie/popular?api_key=d66cd0c7f93a81d02bd35de4464be3d0&language=en-US&page=1")
result=result.text
result=json.loads(result)
for i in result["results"]:
    print(i["original_title"])

print(result)
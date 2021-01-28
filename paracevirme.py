import requests
import json
result=requests.get("https://api.exchangeratesapi.io/latest")
result=result.text
result=json.loads(result)
result["base"]="TRY"
print(result["base"])
bozulan=input("bozulan döviz türü")
alinan=input("alınan döviz türü")
nekadar=int(input("ne kadar {} bozdurmak istiyorsunuz".format(bozulan)))
bozulanin=result["rates"][bozulan]
cevrilen=result["rates"][alinan]
para=nekadar*cevrilen
print("1 {} = {}".format(bozulan,cevrilen))
print(para)


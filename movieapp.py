import requests
import json
#api alman lazım
result=requests.get("")
result=result.text
result=json.loads(result)
print(result)
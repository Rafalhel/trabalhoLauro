import json

import requests

token = 'NZBSBbbKgUwwQPdhVz6lHdBYtrnQIK3NzGqDBtyE'

link = f'https://api.nasa.gov/EPIC/api/natural/images?' \
       f'api_key={token}'

requisicao = requests.get(link)
# requests.request("GET", link)
# iRETORNO_REQ = json.loads(requisicao.text)
print(requisicao)
iRETORNO_REQ = json.loads(requisicao.text)

print(iRETORNO_REQ)
import requests
import hashlib
import time

token = 'a8b49507565e28dc09e010f67a41acf6'
privateToken = '4daee862a5ea4914a3ee839ffa53b9d0dbe27e22'
site = 'rml.marvel.com'
base = 'https://gateway.marvel.com'

m = hashlib.md5()
ts = str(time.time())

m.update(bytes(ts,'utf-8'))
m.update(bytes(privateToken,'utf-8'))
m.update(bytes(token,'utf-8'))
hasht = m.hexdigest()

personagem = 'hulk'
req = f'/v1/public/characters?name={personagem}'
hash = 'ffd275c5130566a2916217b101f26150'
url = base + req + '&apiKey=' + token + '&hash=' + hasht

dados = requests.get(url).json()
print(dados)

link = f'https://gateway.marvel.com/v1/public/characters?name=iron%20man&apikey={token}&hash={hasht}'
requisicao = requests.get(link).json()

print(requisicao)



import json
import traceback

import requests

class Tempo:
    def __init__(self, cidade):
        self._TOKEN = "a988719497196c6641b376754e65d835"
        self.cidade = cidade

    def tempoAtualCelsius(self):
        link = f"https://api.openweathermap.org/data/2.5/weather?q={self.cidade}&appid={self._TOKEN}"
        requisicao = requests.get(link)
        if requisicao.status_code == 404:
            self.cidade = 'São Paulo'
            link = f"https://api.openweathermap.org/data/2.5/weather?q={self.cidade}&appid={self._TOKEN}"
            requisicao = requests.get(link)
        iRETORNO_REQ = json.loads(requisicao.text)
        try:
            temperatura = iRETORNO_REQ["main"]["temp"]
            id = iRETORNO_REQ['weather'][0]['icon'].replace('n','').replace('d','')
            return [int(float(temperatura) - 273.15),int(id)]
        except:
            return None
    def tempoSemana(self):
        link = f"https://api.openweathermap.org/data/2.5/forecast?q={self.cidade}&appid={self._TOKEN}"
        requisicao = requests.get(link)
        if requisicao.status_code == 404:
            self.cidade = 'São Paulo'
            link = f"https://api.openweathermap.org/data/2.5/forecast?q={self.cidade}&appid={self._TOKEN}"
            requisicao = requests.get(link)
        iRETORNO_REQ = json.loads(requisicao.text)
        dados = {}
        dados2 = {}
        try:
            temperatura = iRETORNO_REQ["list"]
            for temp in temperatura:
                dia = temp['dt_txt'].split(' ')[0]
                tempMin = temp['main']['temp_min']
                tempMax = temp['main']['temp_max']
                icon = int(temp['weather'][0]['icon'].replace('n','').replace('d',''))
                tempMin = int(float(tempMin) - 273.15)
                tempMax = int(float(tempMax) - 273.15)

                if dados.get(dia) == None:
                    dados[dia] = []
                    dados[dia].append(tempMin)
                    dados[dia].append(tempMax)
                    # dados[dia].append(icon)
                else:
                    dados[dia].append(tempMin)
                    dados[dia].append(tempMax)
                    # dados[dia].append(icon)

                if dados2.get(dia) == None:
                    dados2[dia] = []
                    dados2[dia].append(icon)
                else:
                    dados2[dia].append(icon)

            for i in dados:
                minTemperatura = min(dados[i])
                maxTemperatura = max(dados[i])
                substituir = [minTemperatura, maxTemperatura]
                dados[i] = substituir

            for i in dados2:
                minId = int(min(dados2[i]))
                maxId = int(max(dados2[i]))
                medio = int(maxId/minId)
                dados2[i] = medio
            return [dados,dados2]
        except:
            print(traceback.format_exc())
            return None
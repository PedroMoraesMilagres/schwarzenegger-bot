import requests
import json

request = requests.get('https://economia.awesomeapi.com.br/json/all/USD-BRL,USDT-BRL,EUR-BRL,BTC-BRL')
cotacao = json.loads(request.text)

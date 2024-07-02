import requests


class CoinConversorService:

    def __init__(self):
        self.__base_url = 'https://economia.awesomeapi.com.br/last/'

    def converter(self, coin_origin, coin_target):
        resposta = requests.get(url = f'{self.__base_url}{coin_origin}-{coin_target}'
        )
        if resposta.status_code == 400:
            return resposta.json().get('message')
        return resposta.json().get(f'{coin_origin}{coin_target}').get('bid')
    

    # https://docs.awesomeapi.com.br/api-de-moedas
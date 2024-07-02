import requests

class CallMeBot():
    
    def __init__(self):
        self.__base_url = 'https://api.callmebot.com/whatsapp.php'
        self.__api_key = 'sua_api_key'

    def send_message(self, message):
        response = requests.get(
            url = f'{self.__base_url}?phone=+551199999999&text={message}&apikey={self.__api_key}'
        )
        return response.text
    

    # https://www.callmebot.com/blog/free-api-whatsapp-messages/
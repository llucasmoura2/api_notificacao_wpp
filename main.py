from clients.callmebot_services import CallMeBot
from clients.conversor_services import CoinConversorService

conversor_service = CoinConversorService()

conversion =conversor_service.converter('BTC', 'BRL')

wpp_service =CallMeBot()

wpp_service.send_message(
   message= f'cotação do bitcoin: {conversion} R$'
)

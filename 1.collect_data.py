import os
import requests
from dotenv import load_dotenv

load_dotenv()

def coletar_dados(campanha_id):
    api_key = os.getenv('MARKETING_API_KEY')
    url = f'https://api.hubapi.com/marketing/v3/campaigns/{campanha_id}?hapikey={api_key}'
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        return resposta.json()
    else:
        resposta.raise_for_status()
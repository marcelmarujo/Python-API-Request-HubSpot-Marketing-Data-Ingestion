import pandas as pd

def validar_dados(dados):
    required_fields = ['id', 'name', 'status', 'metrics']
    
    for field in required_fields:
        if field not in dados:
            raise ValueError(f"Campo obrigatório '{field}' não encontrado nos dados.")
    
    if 'impressions' not in dados['metrics'] or 'clicks' not in dados['metrics']:
        raise ValueError("Campos 'impressions' ou 'clicks' faltando em 'metrics'.")

def processar_dados(dados):
    validar_dados(dados)
    
    campanha_id = dados['id']
    nome = dados['name']
    status = dados['status']
    impressões = dados['metrics']['impressions']
    cliques = dados['metrics']['clicks']
    
    # Calcular a taxa de cliques (CTR)
    ctr = (cliques / impressões) * 100 if impressões > 0 else 0
    
    return {
        'Campanha ID': campanha_id,
        'Nome': nome,
        'Status': status,
        'Impressões': impressões,
        'Cliques': cliques,
        'CTR (%)': ctr
    }

def transformar_dados(dados):
    # Exemplo de transformação: converter status para maiúsculas
    dados['Status'] = dados['Status'].upper()
    return dados

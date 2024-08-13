from collect_data import coletar_dados
from process_data import processar_dados, transformar_dados
from database import salvar_dados

def main():
    campanha_id = '12345'  # Substitua pelo ID da campanha desejada
    
    dados = coletar_dados(campanha_id)
    dados_processados = processar_dados(dados)
    dados_transformados = transformar_dados(dados_processados)
    salvar_dados(dados_transformados)
    
    print(f'Dados para a campanha ID {campanha_id} foram coletados e armazenados com sucesso.')

if __name__ == "__main__":
    main()

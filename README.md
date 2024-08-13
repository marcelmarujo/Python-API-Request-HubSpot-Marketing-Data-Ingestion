# Projeto: Data Engineering w/ HubSpot Marketing API

O objetivo deste projeto é coletar, validar, processar e armazenar dados de marketing usando uma API pública. Este projeto inclui etapas de manipulação e tratamento de dados para criar um cenário mais robusto de engenharia de dados.

## Estrutura do Projeto

### 1. Coleta de Dados da API
- **Descrição**: Obter dados de marketing de uma API pública.
- **Detalhes**: Utiliza uma API para buscar informações relacionadas a campanhas de marketing.

### 2. Validação e Processamento
- **Descrição**: Validar a integridade dos dados, tratar dados ausentes e realizar transformações.
- **Detalhes**: Implementa rotinas para garantir que os dados estejam completos, consistentes e prontos para análise. Inclui limpeza e transformação dos dados conforme necessário.

### 3. Armazenamento em Banco de Dados
- **Descrição**: Salvar os dados em um banco de dados SQL.
- **Detalhes**: Utiliza SQLite para simplicidade, mas a estrutura permite fácil adaptação para outros bancos de dados SQL, como PostgreSQL ou MySQL.

### 4. Consulta e Análise
- **Descrição**: Consultar e analisar os dados armazenados.
- **Detalhes**: Executa consultas SQL para extrair informações úteis dos dados armazenados e realizar análises conforme os requisitos do projeto.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação para coleta, processamento e análise de dados.
- **API**: Interface para obtenção de dados de marketing.
- **SQLite**: Banco de dados SQL para armazenamento dos dados.
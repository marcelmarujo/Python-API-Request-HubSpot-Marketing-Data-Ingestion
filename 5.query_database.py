import sqlite3

def consultar_dados():
    conn = sqlite3.connect('dados_marketing.db')
    cursor = conn.cursor()

    # Executar uma consulta SQL
    cursor.execute('SELECT * FROM dados_marketing')

    # Obter e exibir os resultados
    resultados = cursor.fetchall()
    for row in resultados:
        print(f'ID: {row[0]}, Campanha ID: {row[1]}, Nome: {row[2]}, Status: {row[3]}, Impressões: {row[4]}, Cliques: {row[5]}, CTR: {row[6]}')

    # Fechar a conexão
    conn.close()

if __name__ == "__main__":
    consultar_dados()

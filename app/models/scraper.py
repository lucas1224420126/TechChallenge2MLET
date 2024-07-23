import requests

def download_csv(url):
    """Função para fazer o download de um arquivo CSV."""
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    # Verificar se o download foi bem-sucedido
    try:
        if response.status_code == 200:
            content = response.content
            return content
        else:
            print("Erro no download do arquivo")
    except Exception as e:
        print(f"Erro: {e}")


def scrape_viticulture_data(category):
    print(category)
    try:
        if category == "Produção": # Realizando o download do CSV de Produção
            response = download_csv('http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv') 
        
        elif category == "Processamento": # Realizando o download dos arquivos de Processamento
            ProcessaViniferas = download_csv('http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv') # Realizando o download dos arquivos CSV
            ProcessaAmericanas = download_csv('http://vitibrasil.cnpuv.embrapa.br/download/ProcessaAmericanas.csv') # Realizando o download dos arquivos CSV
            ProcessaMesa = download_csv('http://vitibrasil.cnpuv.embrapa.br/download/ProcessaMesa.csv') # Realizando o download dos arquivos CSV
            ProcessaSemclass = download_csv('http://vitibrasil.cnpuv.embrapa.br/download/ProcessaSemclass.csv') # Realizando o download dos arquivos CSV
            response = [ProcessaViniferas, ProcessaAmericanas, ProcessaMesa, ProcessaSemclass] #Juntando todos os arquivos em um único retorno

        elif category == "Comercialização": # Realizando o download do CSV de Comercio
            response = download_csv('http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv')

        elif category == "Importação": # Realizando o download dos arquivos de Importacao
            ImpVinhos = download_csv('http://vitibrasil.cnpuv.embrapa.br/download/ImpVinhos.csv') # Realizando o download dos arquivos CSV
            ImpEspumantes = download_csv('http://vitibrasil.cnpuv.embrapa.br/download/ImpEspumantes.csv') # Realizando o download dos arquivos CSV
            ImpFrescas = download_csv('http://vitibrasil.cnpuv.embrapa.br/download/ImpFrescas.csv') # Realizando o download dos arquivos CSV
            ImpPassas = download_csv('http://vitibrasil.cnpuv.embrapa.br/download/ImpPassas.csv') # Realizando o download dos arquivos CSV
            ImpSuco = download_csv('http://vitibrasil.cnpuv.embrapa.br/download/ImpSuco.csv') # Realizando o download dos arquivos CSV
            response = [ImpVinhos, ImpEspumantes, ImpFrescas, ImpPassas, ImpSuco] #Juntando todos os arquivos em um único retorno

        elif category == "Exportação": # Realizando o download dos arquivos de Exportacao
            ExpVinho = download_csv('http://vitibrasil.cnpuv.embrapa.br/download/ExpVinho.csv')# Realizando o download dos arquivos CSV
            ExpEspumantes = download_csv('http://vitibrasil.cnpuv.embrapa.br/download/ExpEspumantes.csv')# Realizando o download dos arquivos CSV
            ExpUva = download_csv('http://vitibrasil.cnpuv.embrapa.br/download/ExpUva.csv')# Realizando o download dos arquivos CSV
            ExpSuco = download_csv('http://vitibrasil.cnpuv.embrapa.br/download/ExpSuco.csv') # Realizando o download dos arquivos CSV
            response = [ExpVinho, ExpEspumantes, ExpUva, ExpSuco] #Juntando todos os arquivos em um único retorno
        #Processamento Comercialização Importação Exportação
    except Exception as e:
        print(f"Erro: {e}")
    
    return response

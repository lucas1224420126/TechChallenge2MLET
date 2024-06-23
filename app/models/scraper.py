import requests
from datetime import datetime
from bs4 import BeautifulSoup
import pandas as pd


def read_csv_file(filename: str):
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File not found")
    
    df = pd.read_csv(file_path)
    return df.to_csv(index=False)


def producao_vinicola():
    """Função para fazer o download do arquivo CSV com os dados de produção vinícola."""	
    url = 'http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv'
    response = requests.get(url)
    # Verificar se o download foi bem-sucedido
    if response.status_code == 200:
        # Salvar o conteúdo em um arquivo local
        name_file = fr'..\files\producao_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.csv'
        with open(name_file, 'wb') as arquivo:
            arquivo.write(response.content)
        final_content = read_csv_file(name_file)
    else:
        raise HTTPException(status_code=404, detail="Falha no download do arquivo.")
    
    return final_content


def scrape_viticulture_data(category):
    
    response = producao_vinicola()
    
    return response

# scraping/producao.py
import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_producao_data():
    url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'class': 'tb_base tb_dados'})
    rows = table.find_all('tr')
    data = [[cell.get_text(strip=True) for cell in row.find_all(['th', 'td'])] for row in rows]
    df = pd.DataFrame(data[1:], columns=data[0])
    return df


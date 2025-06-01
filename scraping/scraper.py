from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from api.config import ENDPOINTS

def fetch_table(table_name: str):
    """
    Raspagem de uma única tabela, identifcada pelo nome.
    Retorna uma lista de listas (linhas x Colunas).
    """
    url = ENDPOINTS.get(table_name)
    if not url:
        raise ValueError(f"Tabela desconhecida: {table_name}")
    
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        time.sleep(3)

        # Seleciona a tabela de dados pela classe
        tbl = driver.find_element(By.CSS_SELECTOR, "table.tb_base.tb_dados")
        linhas = tbl.find_elements(By.TAG_NAME, "tr")

        resultado = []
        for row in linhas:
            cols = row.find_elements(By.TAG_NAME, "td")
            if cols:
                resultado.append([c.text.strip() for c in cols])
        return resultado
    
    finally:
        driver.quit()
        
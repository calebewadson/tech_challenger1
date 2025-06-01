# services/scraper.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Aqui definimos as 5 URLs diretamente:
ENDPOINTS = {
    "Produção":        "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02",
    "Processamento":   "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_03",
    "Comercialização": "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04",
    "Importação":      "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_05",
    "Exportação":      "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_06",
}

def fetch_table(table_name: str):
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
        data_table = driver.find_element(By.CSS_SELECTOR, "table.tb_base.tb_dados")
        linhas = data_table.find_elements(By.TAG_NAME, "tr")
        resultado = []
        for row in linhas:
            cols = row.find_elements(By.TAG_NAME, "td")
            if cols:
                texto_cols = [c.text.strip() for c in cols]
                resultado.append(texto_cols)
        return resultado
    finally:
        driver.quit()
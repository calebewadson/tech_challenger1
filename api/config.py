import os

BASE_URL = "http://vitibrasil.cnpuv.embrapa.br/index.php"

# Mapeia o nome da tabela ao parâmetro opção
ENDPOINTS = {
    "Produção":         f"{BASE_URL}?opcao=opt_02",
    "Processamento":    f"{BASE_URL}?opcao=opt_03",
    "Comercialização":  f"{BASE_URL}?opcao=opt_04",
    "Importação":       f"{BASE_URL}?opcao=opt_05",
    "Exportação":       f"{BASE_URL}?opcao=opt_06",
}

SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")

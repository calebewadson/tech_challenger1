import json
from services.scraper import fetch_table
from pathlib import Path

if __name__ == "__main__":
    data = {}
    for tabela in ["Produção", "Processamento", "Comercialização", "Importação", "Exportação"]:
        try:
            data[tabela] = fetch_table(tabela)
        except Exception as e:
            print(f"Falha em raspar '{tabela}': {e}")
            data[tabela] = []

    dst = Path(__file__).parent.parent / "data" / "local_data.json"
    dst.parent.mkdir(parents=True, exist_ok=True)

    with open(dst, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Fallback salve em {dst}")
        
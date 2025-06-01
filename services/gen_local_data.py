import json
from scraping.scraper import fetch_all_data
from pathlib import Path

if __name__ == "__main__":
    data = fetch_all_data()
    dst = Path(__file__).parent.parent / "data" / "local_data.json"
    with open(dst, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Fallback salvo em {dst}")
    
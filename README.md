# Tech Challenger - Fase 1

Este projeto fornece uma API pública para consulta em tempo real de dados de vtivinicultura da Embrapa

## Funcionalidades

- Scraping em tempo real com Selenium
- Fallback para dados locais em JSON em caso de falha.
- Autenticação JWT.
- Endpoints documentados com Swagger UI.

## Instalação

```bash
git clone 
cd TECH_CHALLENGER
python3 -m venv venv
source ven/bin/activate
pip install -r requirements.txt
```

## Execução

### Local

```bash
uvicorn api.main:app --reload
```

## Testes

```bash
pytest
```

## Rotas

- `POST /token` - obtenção de JWT.
- `GET /data` - consulta de dados (JWT obrigatório).

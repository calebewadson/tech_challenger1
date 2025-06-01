from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from scraping.scraper import fetch_table
from scraping.cache import load_local_data
from auth.jwt import verify_token
from services.db import get_db, Producao, Processamento, Comercializacao, Importacao, Exportacao

router = APIRouter(
    prefix="/data",
    dependencies=[Depends(verify_token)],
    responses={404: {"descriptions": "Tabela não encontrada"}}
)

# ROTA: /routes/producao

@router.get("/producao", summary="Produção")
def get_producao(db: Session = Depends(get_db)):
    try:
        # Raspagem da taabela
        rows = fetch_table("Produção")
        if not rows or len(rows) < 2:
            raise Exception("Tabela vazia ou não encontrada")
        
        # Limpa registros antigos
        db.query(Producao).delete()
        db.commit()

        # Insere os novos registros
        for cols in rows[1:]:
            produto = cols[0].strip()
            qtd_str = cols[1].strip()

            # Normaliza a string: remove pontos de milhar e troca vírgula por ponto
            qtd_limpa = qtd_str.replace(".", "").replace(",", ".")
            try:
                qtd_numero = float(qtd_limpa)
            except ValueError:
                continue

            registro = Producao(produto=produto, quantidade=qtd_numero)
            db.add(registro)

        db.commit()
        return rows
    
    except ValueError:
        raise HTTPException(status_code=404, detail="Tabela não encontrada")
    except Exception:
        return load_local_data("Produção")
    
# ROTA: /routes/processamento

@router.get("/processamento", summary="Processamento")
def get_processamento(db: Session = Depends(get_db)):
    try:
        rows = fetch_table("Processamento")
        if not rows or len(rows) < 2:
            raise Exception("Tabela vazia ou não encontrada")
        
        db.query(Processamento).delete()
        db.commit

        for cols in rows[1:]:
            produto = cols[0].strip()
            qtd_str = cols[1].strip()

            qtd_limpa = qtd_str.replace(".", "").replace(",", ".")
            try:
                qtd_numero = float(qtd_limpa)
            except ValueError:
                continue
            
            registro = Processamento(produto=produto, quantidade=qtd_numero)
            db.add(registro)

        db.commit()
        return rows
    
    except ValueError:
        raise HTTPException(status_code=404, detail="Tabela não encontrada")
    except Exception:
        return load_local_data("Processamento")
    
# ROTA: /routes/comercializacao

@router.get("/comercializacao", summary="Comercialização")
def get_comercializacao(db: Session = Depends(get_db)):
    try:
        rows = fetch_table("Comercialização")
        if not rows or len(rows) < 2:
            raise Exception("Tabela vazia ou não encontrada")
        
        db.query(Comercializacao).delete()
        db.commit()

        for cols in rows[1:]:
            produto = cols[0].strip()
            qtd_str = cols[1].strip()

            qtd_limpa = qtd_str.replace(".", "").replace(",", ".")
            try:
                qtd_numero = float(qtd_limpa)
            except ValueError:
                continue

            registro = Comercializacao(produto=produto, quantidade=qtd_numero)
            db.add(registro)

        db.commit()
        return rows
    
    except ValueError:
        raise HTTPException(status_code=404, detail="Tabela não encontrada")
    except Exception:
        return load_local_data("Comercialização")
    
#ROTA: /routes/importacao

@router.get("/importacao", summary="Importação")
def get_importacao(db: Session = Depends(get_db)):
    try:
        rows = fetch_table("Importação")
        if not rows or len(rows) < 2:
            raise Exception("Tabela vazia ou não encontrada")
        
        db.query(Importacao).delete()
        db.commit()

        for cols in rows[1:]:
            pais = cols[0].strip()
            qtd_str = cols[1].strip()
            valor_str = cols[2].strip()

            qtd_limpa = qtd_str.replace(".", "").replace(",", ".")
            valor_limpo = valor_str.replace(".", "").replace(",", ".")
            try:
                qtd_numero = float(qtd_limpa)
                valor_numero  = float(valor_limpo)
            except ValueError:
                continue

            registro = Importacao(paises=pais, quantidade=qtd_numero, valor=valor_numero)
            db.add(registro)

        db.commit()
        return rows
    
    except ValueError:
        raise HTTPException(status_code=404, detail="Tabela não encontrada")
    except Exception:
        return load_local_data("Importação")
    

#ROTA: /routes/exportacao

@router.get("/exportacao", summary="Exportação")
def get_exportacao(db: Session = Depends(get_db)):
    try:
        rows = fetch_table("Exportação")
        if not rows or len(rows) < 2:
            raise Exception("Tabela vazia ou não encontrada")
        
        db.query(Exportacao).delete()
        db.commit()

        for cols in rows[1:]:
            pais = cols[0].strip()
            qtd_str = cols[1].strip()
            valor_str = cols[2].strip()

            qtd_limpa = qtd_str.replace(".", "").replace(",", ".")
            valor_limpo = valor_str.replace(".", "").replace(",", ".")
            try:
                qtd_numero = float(qtd_limpa)
                valor_numero = float(valor_limpo)
            except ValueError:
                continue

            registro = Exportacao(paises=pais, quantidade=qtd_numero, valor=valor_numero)

        db.commit()
        return rows
    
    except ValueError:
        raise HTTPException(status_code=404, detail="Tabela não encontrada")
    except Exception:
        return load_local_data("Exportação")
    
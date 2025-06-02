from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services.scraper import fetch_table
from services.cache   import load_local_data
from services.db      import get_db, Producao, Processamento, Comercializacao, Importacao, Exportacao
from typing import List

router = APIRouter()

@router.get("/", summary="Raiz de /data — apenas para testar")
def root_data():
    return {"message": "Você está autenticado no /data"}

@router.get("/producao", summary="Produção")
def get_producao(db: Session = Depends(get_db)) -> List[List[str]]:
    try:
        rows = fetch_table("Produção")
        if not rows or len(rows) < 2:
            raise Exception("Tabela vazia ou não encontrada")

        db.query(Producao).delete()
        db.commit()

        for ano, uf, qtd_str in rows[1:]:
            qtd_limpa = qtd_str.replace(".", "").replace(",", ".")
            try:
                qtd_numero = float(qtd_limpa)
            except ValueError:
                continue
            produto_texto = f"{ano} - {uf}"
            db.add(Producao(produto=produto_texto, quantidade=qtd_numero))
        db.commit()
        return rows
    except Exception:
        return load_local_data("Produção")


@router.get("/processamento", summary="Processamento")
def get_processamento(db: Session = Depends(get_db)) -> List[List[str]]:
    try:
        rows = fetch_table("Processamento")
        if not rows or len(rows) < 2:
            raise Exception("Tabela vazia ou não encontrada")
        db.query(Processamento).delete()
        db.commit()
        for ano, produto, qtd_str in rows[1:]:
            qtd_limpa = qtd_str.replace(".", "").replace(",", ".")
            try:
                qtd_numero = float(qtd_limpa)
            except ValueError:
                continue
            db.add(Processamento(produto=produto.strip(), quantidade=qtd_numero))
        db.commit()
        return rows
    except Exception:
        return load_local_data("Processamento")


@router.get("/comercializacao", summary="Comercialização")
def get_comercializacao(db: Session = Depends(get_db)) -> List[List[str]]:
    try:
        rows = fetch_table("Comercialização")
        if not rows or len(rows) < 2:
            raise Exception("Tabela vazia ou não encontrada")
        db.query(Comercializacao).delete()
        db.commit()
        for ano, uf, qtd_str in rows[1:]:
            qtd_limpa = qtd_str.replace(".", "").replace(",", ".")
            try:
                qtd_numero = float(qtd_limpa)
            except ValueError:
                continue
            produto_texto = f"{ano} - {uf}"
            db.add(Comercializacao(produto=produto_texto, quantidade=qtd_numero))
        db.commit()
        return rows
    except Exception:
        return load_local_data("Comercialização")


@router.get("/importacao", summary="Importação")
def get_importacao(db: Session = Depends(get_db)) -> List[List[str]]:
    try:
        rows = fetch_table("Importação")
        if not rows or len(rows) < 2:
            raise Exception("Tabela vazia ou não encontrada")
        db.query(Importacao).delete()
        db.commit()
        for pais, qtd_str, valor_str in rows[1:]:
            qtd_limpa   = qtd_str.replace(".", "").replace(",", ".")
            valor_limpo = valor_str.replace(".", "").replace(",", ".")
            try:
                qtd_numero   = float(qtd_limpa)
                valor_numero = float(valor_limpo)
            except ValueError:
                continue
            db.add(Importacao(paises=pais.strip(), quantidade=qtd_numero, valor=valor_numero))
        db.commit()
        return rows
    except Exception:
        return load_local_data("Importação")


@router.get("/exportacao", summary="Exportação")
def get_exportacao(db: Session = Depends(get_db)) -> List[List[str]]:
    try:
        rows = fetch_table("Exportação")
        if not rows or len(rows) < 2:
            raise Exception("Tabela vazia ou não encontrada")
        db.query(Exportacao).delete()
        db.commit()
        for pais, qtd_str, valor_str in rows[1:]:
            qtd_limpa   = qtd_str.replace(".", "").replace(",", ".")
            valor_limpo = valor_str.replace(".", "").replace(",", ".")
            try:
                qtd_numero   = float(qtd_limpa)
                valor_numero = float(valor_limpo)
            except ValueError:
                continue
            db.add(Exportacao(paises=pais.strip(), quantidade=qtd_numero, valor=valor_numero))
        db.commit()
        return rows
    except Exception:
        return load_local_data("Exportação")

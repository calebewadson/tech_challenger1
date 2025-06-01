import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from typing import Generator

# Configuração do banco

DB_URL = "sqlite:///embrapa.db"
engine = create_engine(
    DB_URL,
    echo=False,
    connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
Base = declarative_base()

#MODELS: Uma classe para cada tabela

class Producao(Base):
    __tablename__ = "producao"
    id = Column(Integer, primary_key=True, autoincrement=True)
    produto = Column(String(80), nullable=False)
    quantidade = Column(Float, nullable=False)
    criado_em = Column(DateTime, default=datetime.datetime.utcnow)

class Processamento(Base):
    __tablename__ = "processamento"
    id = Column(Integer, primary_key=True, autoincrement=True)
    produto = Column(String(80), nullable=False)
    quantidade = Column(Float, nullable=False)
    criado_em = Column(DateTime, default=datetime.datetime.utcnow)

class Comercializacao(Base):
    __tablename__ = "comercializacao"
    id = Column(Integer, primary_key=True, autoincrement=True)
    produto = Column(String(80), nullable=False)
    quantidade = Column(Float, nullable=False)
    criado_em = Column(DateTime, default=datetime.datetime.utcnow)

class Importacao(Base):
    __tablename__ = "importacao"
    id = Column(Integer, primary_key=True, autoincrement=True)
    paises = Column(String(80), nullable=False)
    quantidade = Column(Float, nullable=False)
    valor = Column(Float, nullable=False)
    criado_em = Column(DateTime, default=datetime.datetime.utcnow)

def Exportacao(Base):
    __tablename__ = "exportacao"
    id = Column(Integer, primary_key=True, autoincrement=True)
    paises = Column(String(80), nullable=False)
    quantidade = Column(Float, nullable=False)
    valor = Column(Float, nullable=False)
    criado_em = Column(DateTime, default=datetime.datetime.utcnow)

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.closse()

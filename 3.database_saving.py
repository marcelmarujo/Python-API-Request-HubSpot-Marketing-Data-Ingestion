from sqlalchemy import create_engine, Column, String, Float, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///dados_marketing.db"

Base = declarative_base()

class DadosMarketing(Base):
    __tablename__ = 'dados_marketing'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    campanha_id = Column(String, unique=True, nullable=False)
    nome = Column(String, nullable=False)
    status = Column(String, nullable=False)
    impressões = Column(Integer, nullable=False)
    cliques = Column(Integer, nullable=False)
    ctr = Column(Float, nullable=False)

def criar_banco_de_dados():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    return engine

def salvar_dados(dados):
    engine = criar_banco_de_dados()
    Session = sessionmaker(bind=engine)
    session = Session()
    
    novo_dado = DadosMarketing(
        campanha_id=dados['Campanha ID'],
        nome=dados['Nome'],
        status=dados['Status'],
        impressões=dados['Impressões'],
        cliques=dados['Cliques'],
        ctr=dados['CTR (%)']
    )
    
    session.add(novo_dado)
    session.commit()
    session.close()
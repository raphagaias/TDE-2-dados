from sqlalchemy_utils import create_database, database_exists
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from urllib.parse import quote
from models.__init__ import *

mysql_senha =  'C0x1nh4123'
instance: str = f"mysql+pymysql://root:{quote(mysql_senha)}@localhost:3306/youtube1"

if not database_exists(instance):
    create_database(instance)

engine = create_engine(instance, echo = True)
session = Session(bind=engine, autocommit=False, autoflush=True)

with Session(engine) as session:
        antonio = usuario(
            id= 1, birthday = "2000-01-02", name = "Antônio dos Santos", email = "santos@gmail.com",  registred = True
        )
        maria = usuario(
            id= 2, birthday = "2001-04-12", name = "Maria de Jesus", email = "jesus@outlook.com",  registred = True
        )
        jose = usuario(
             id =3,birthday ="2013-04-18", name ="José da Silva", email = "silva@gmail.com",registred =False
        )
        marcia = usuario(
            id =4, birthday ="1998-05-10", name ="Marcia Rocha", email ="rocha@yahoo.com", registred =True
        )
        

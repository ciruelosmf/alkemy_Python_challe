### crud.py ###
from config import DATABASE_URI, PASS
from models import Base
from sqlalchemy import create_engine

engine = create_engine(DATABASE_URI)

Base.metadata.create_all(engine)
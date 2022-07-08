### models.py ###

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date

Base = declarative_base()

class InfoNormalizada(Base):
    __tablename__ = 'InfoNormalizada'
 
    cod_localidad = Column(String, primary_key=True)
     
    #pages = Column(Integer)
    #published = Column(Date)
    
    def __repr__(self):
        return "< InfoNormalizada (cod_localidad='{}'}) > "\
                .format(self.cod_localidad)
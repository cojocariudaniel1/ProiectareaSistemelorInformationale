from sqlalchemy.orm import relationship

from base import Base
from sqlalchemy import Column, String, Integer, Table, ForeignKey


class Materiale(Base):
    __tablename__ = 'materiale'

    id = Column(Integer, primary_key=True)
    denumire_material = Column(String)
    cantitate_material = Column(Integer)
    unitate_de_masura = Column(String)

    def __init__(self, denumire_material, cantitate_material, unitate_de_masura):
        self.denumire_material = denumire_material
        self.cantitate_material = cantitate_material
        self.unitate_de_masura = unitate_de_masura

from sqlalchemy import Column, String, Integer, Date
from base import Base


class Operatii(Base):
    __tablename__ = 'operatii'

    id = Column(Integer, primary_key=True)
    denumire_operatie = Column(String)
    instructiuni = Column(String)
    alte_observatii = Column(String)

    def __init__(self, denumire_operatie, instructiuni, alte_observatii):
        self.denumire_operatie = denumire_operatie
        self.instructiuni = instructiuni
        self.alte_observatii = alte_observatii

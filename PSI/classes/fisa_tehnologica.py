from sqlalchemy.orm import relationship
from base import Base
from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey
from materiale import Materiale
from operatii import Operatii


class FisaTehnologica(Base):
    __tablename__ = 'fisa_tehnologica'
    materiale_fisa_relatie = Table('materiale_fisa', Base.metadata,
                                   Column('materiale_id', Integer, ForeignKey('materiale.id')),
                                   Column('fisa_id', Integer, ForeignKey('fisa_tehnologica.id')),

                                   )

    operatii_fisa_relatie = Table('opeatii_fisa', Base.metadata,
                                  Column('operatie_id', Integer, ForeignKey('operatii.id')),
                                  Column('fisa_id', Integer, ForeignKey('fisa_tehnologica.id')),

                                  )

    id = Column(Integer, primary_key=True)
    denumire_produs = Column(String)
    denumire_fisa = Column(String)
    date = Column(Date)
    materiale = relationship('Materiale', secondary=materiale_fisa_relatie)
    operatii = relationship('Operatii', secondary=operatii_fisa_relatie)

    def __init__(self, denumire_produs, denumire_fisa, date):
        self.denumire_produs = denumire_produs
        self.denumire_fisa = denumire_fisa
        self.date = date

from sqlalchemy.orm import sessionmaker

from base import Base, engine
from fisa_tehnologica import FisaTehnologica
from materiale import Materiale
from operatii import Operatii
Session = sessionmaker(bind=engine)
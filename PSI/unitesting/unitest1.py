from datetime import date

from sqlalchemy import create_engine, table
from sqlalchemy.orm import sessionmaker

from base import Session, Base, engine
from fisa_tehnologica import FisaTehnologica
from materiale import Materiale
from operatii import Operatii

# os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin/'

def create_all():
    session = Session()
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    # creare fisa tehnologica
    fisa1 = FisaTehnologica("Fisa inghetata cornet vanilie", "Inghetata vanilie cornet", date(2022, 3, 21))
    fisa2 = FisaTehnologica("Fisa inghetata menta", "Inghetata menta tort", date(2022, 3, 21))
    fisa3 = FisaTehnologica("Fisa inghetata fistic", "Inghetata fistic pe bat", date(2022, 3, 21))
    fisa4 = FisaTehnologica("Fisa inghetata ciocolata", "'Inghetata vafa", date(2022, 3, 21))

    # creare operatii
    operatii1 = Operatii('Racire', 'Materialele se răcesc la o temperatura de -20 grade C', 'Durata 30min')
    operatii2 = Operatii('Malaxor', 'Ingredientele se amestecă la malaxor', 'Durata 30min')
    operatii3 = Operatii('Malaxor', 'Ingredientele se amestecă la malaxor', 'Durata 15min')
    operatii4 = Operatii('Ingrosare', 'Se folosesc agenti de ingrosare', 'Durata 20min')
    operatii5 = Operatii('Racire', 'Materialele se răcesc la o temperatura de -25 grade C', 'Durata 30min')
    operatii6 = Operatii('Racire', 'Materialele se răcesc la o temperatura de -10 grade C', 'Durata 29min')
    operatii7 = Operatii('Ingrosare', 'Se folosesc agenti de ingrosare', 'Durata 14min')

    # Adaugrare operatii in fisa tehnologica
    fisa1.operatii = [operatii1, operatii4, operatii3]

    fisa2.operatii = [operatii1,operatii5,]

    fisa3.operatii = [operatii7,operatii3,operatii6]

    fisa4.operatii = [operatii6,operatii5]

    # creare materiale
    materiale1 = Materiale('Zahar', 190, 'g')
    materiale2 = Materiale('Lapte', 420, 'ml')
    materiale3 = Materiale('Menta', 210, 'g')
    materiale4 = Materiale('Stabilizatori', 4, 'g')
    materiale5 = Materiale('Lapte', 410, 'ml')
    materiale6 = Materiale('Zahar', 220, 'g')
    materiale7 = Materiale('Lapte', 459, 'ml')

    # Adaugare materiale in fisa tehnologica
    fisa1.materiale = [materiale1, materiale4, materiale3, materiale2]

    fisa2.materiale = [materiale1, materiale6, materiale3]

    fisa3.materiale = [materiale6, materiale2]

    fisa4.materiale = [materiale7, materiale5, materiale4]

    # adaugare date in sesiune
    session.add(materiale1)
    session.add(materiale2)
    session.add(materiale3)
    session.add(materiale4)
    session.add(materiale5)
    session.add(materiale6)
    session.add(materiale7)

    session.add(operatii1)
    session.add(operatii2)
    session.add(operatii3)
    session.add(operatii4)
    session.add(operatii5)
    session.add(operatii6)
    session.add(operatii7)

    session.add(fisa1)
    session.add(fisa2)
    session.add(fisa3)
    session.add(fisa4)
    session.commit()
    session.close()


create_all()
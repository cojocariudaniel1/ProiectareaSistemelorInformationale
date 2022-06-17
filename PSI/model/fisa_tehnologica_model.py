from base import Session
from materiale import Materiale
from operatii import Operatii
from fisa_tehnologica import FisaTehnologica


def load_data():
    session = Session()
    fise_tehnologice = session.query(FisaTehnologica)
    list_tuple = []
    for fisa_tehn in fise_tehnologice:
        date = (fisa_tehn.id, fisa_tehn.denumire_produs, fisa_tehn.denumire_fisa, fisa_tehn.date)
        list_tuple.append(date)

    return list_tuple


def filter_search(search_text):
    session = Session()
    query = session.query(FisaTehnologica).filter(FisaTehnologica.denumire_fisa.like(f"%{search_text}%")).all()
    list_tuple = []
    for fisa_tehn in query:
        date = (fisa_tehn.id, fisa_tehn.denumire_produs, fisa_tehn.denumire_fisa, fisa_tehn.date)
        list_tuple.append(date)
    session.close()
    return list_tuple

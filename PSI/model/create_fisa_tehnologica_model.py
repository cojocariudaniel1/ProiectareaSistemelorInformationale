from operatii import Operatii
from fisa_tehnologica import FisaTehnologica
from base import Session
from materiale import Materiale


class SaveEntryValues:
    def __init__(self, denumire_produs, denumire_fisa, fisa_data):
        self.denumire_produs = denumire_produs
        self.denumire_fisa = denumire_fisa
        self.fisa_data = fisa_data

        self.operatii_list = []
        self.operatii_list_set = []
        self.materiale_list = []
        self.materiale_list_set = []

    def SaveValues(self):
        session = Session()
        fisa_tehnologica_query = session.query(FisaTehnologica).filter(
            FisaTehnologica.denumire_produs == self.denumire_produs)

        if fisa_tehnologica_query.count() == 0:
            try:
                fisa_tehnologica_noua = FisaTehnologica(self.denumire_produs, self.denumire_fisa, self.fisa_data)
                fisa_tehnologica_noua.operatii = self.operatii_list_set
                fisa_tehnologica_noua.materiale = self.materiale_list_set
                session.add(fisa_tehnologica_noua)
                session.commit()

            except:
                session.close()
                return 2
            session.close()
            return 0

        else:
            session.close()
            return 1

    def get_operatii_list(self, *operatii):
        session = Session()
        for item in operatii:
            for j in item:
                if j[0] != 0:
                    operatii_get = session.query(Operatii).filter(Operatii.id == j[0])
                    for k in operatii_get:
                        self.operatii_list_set.append(k)
                else:
                    print(Operatii(j[1], j[2], j[3]))
                    print(j[1], j[2], j[3])
                    session.add(Operatii(j[1], j[2], j[3]))
                    self.operatii_list_set.append(Operatii(j[1], j[2], j[3]))
        session.commit()
        session.close()

    def get_materiale_list(self, *materiale):
        session = Session()
        for item in materiale:
            for k in item:
                if k[0] != 0:
                    materiale_get = session.query(Materiale).filter(Materiale.id == k[0])
                    for i in materiale_get:
                        self.materiale_list_set.append(i)
                else:
                    session.add(Materiale(k[1], k[2], k[3]))
                    self.materiale_list_set.append(Materiale(k[1], k[2], k[3]))
        session.commit()
        session.close()

def load_operatii():
    session = Session()
    operatii_list = []
    operatii_item = session.query(Operatii).all()
    for item in operatii_item:
        operatii_list.append(item.denumire_operatie)

    return tuple(operatii_list)


def load_materiale():
    session = Session()
    materiale_list = []
    materiale_obj = session.query(Materiale).all()
    for item in materiale_obj:
        materiale_list.append(item.denumire_material)

    return tuple(materiale_list)

def filter_materiale(id_material):
    session = Session()
    materiale_filter = session.query(Materiale).filter(Materiale.id == int(id_material))
    material_filter_list = ()
    for item in materiale_filter:
        material_filter_list = (item.id, item.denumire_material, item.cantitate_material, item.unitate_de_masura)

    return material_filter_list

def filter_operatii(id_operatie):
    session = Session()
    operatii_filter = session.query(Operatii).filter(Operatii.id == int(id_operatie))
    operatii_filter_list = ()
    for item in operatii_filter:
        operatii_filter_list = (item.id, item.denumire_operatie, item.instructiuni, item.alte_observatii)

    return operatii_filter_list

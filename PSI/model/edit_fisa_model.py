from operatii import Operatii
from fisa_tehnologica import FisaTehnologica
from base import Session
from materiale import Materiale


def load_data_from_database_model(fisa_id):
    list_operatii = []
    list_materiale = []
    list_of_materiale_and_operatii = []
    print('run load data')
    session = Session()
    data_session = session.query(FisaTehnologica).filter(FisaTehnologica.id == fisa_id)
    for item in data_session:
        for k in item.operatii:
            list_operatii.append((k.id, k.denumire_operatie, k.instructiuni, k.alte_observatii))

    for item in data_session:
        for k in item.materiale:
            list_materiale.append((k.id, k.denumire_material, k.cantitate_material, k.unitate_de_masura))
    list_of_materiale_and_operatii.append(list_operatii)
    list_of_materiale_and_operatii.append(list_materiale)
    return list_of_materiale_and_operatii


class SaveValues():
    def __init__(self, fisa_id, denumire_fisa, denumire_produs, date):
        self.fisa_id = fisa_id
        self.denumire_fisa = denumire_fisa
        self.denumire_produs = denumire_produs
        self.date = date
        self.operatii_list = []
        self.operatii_list_set = []
        self.materiale_list = []
        self.materiale_list_set = []

    def check_fisa_tehn(self):
        session = Session()
        query = session.query(FisaTehnologica).filter(FisaTehnologica.id == self.fisa_id)
        for i in query:
            if i.denumire_produs != self.denumire_produs:
                i.denumire_produs = self.denumire_produs
            if i.denumire_fisa != self.denumire_fisa:
                i.denumire_fisa = self.denumire_fisa
            if i.date != self.date:
                i.date = self.date
        try:
            session.commit()
        except:
            session.close()
            return 1

    def get_operatii_list(self, *operatii):
        session = Session()
        fisa = session.query(FisaTehnologica).filter(FisaTehnologica.id == self.fisa_id)
        print(self.fisa_id)
        for i in operatii:
            for item in i:
                if item[0] == 0:
                    self.operatii_list.append(Operatii(item[1], item[2], item[3]))
                    # session.add(Operatii(item[1], item[2], item[3]))
                else:
                    operatie = session.query(Operatii).filter(Operatii.id == item[0]).one()
                    self.operatii_list.append(operatie)

        print(self.operatii_list)
        for i in fisa:
            i.operatii = self.operatii_list
        session.commit()
        session.close()
        print('test')

    def get_materiale_list(self, *materiale):
        session = Session()
        fisa = session.query(FisaTehnologica).filter(FisaTehnologica.id == self.fisa_id)
        print(self.fisa_id)
        for i in materiale:
            for item in i:
                if item[0] == 0:
                    self.materiale_list.append(Materiale(item[1], item[2], item[3]))
                    # session.add(Materiale(item[1], item[2], item[3]))
                else:
                    material = session.query(Materiale).filter(Materiale.id == item[0]).one()
                    self.materiale_list.append(material)

        print(self.materiale_list)
        for i in fisa:
            i.materiale = self.materiale_list

        session.commit()
        session.close()


def delete_fisa_tehn(id_fisa):
    session = Session()

    query = session.query(FisaTehnologica).filter(FisaTehnologica.id == id_fisa)
    for i in query:
        i.operatii = []
        i.materiale = []
    query.delete()
    session.commit()
    session.close()

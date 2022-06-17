import tkinter as tk
from tkinter import ttk
from model.create_fisa_tehnologica_model import SaveEntryValues
from tkinter import messagebox
from . import fisa_tehnologica_view as FisaTehn
from model import create_fisa_tehnologica_model


class CreateForm:
    def __init__(self, master):
        self.master = master

        self.frame = ttk.Frame(self.master, height=750, width=915)

        self.anuleaza_buton = ttk.Button(self.frame, text="Anuleaza", command=self.anuleaza)
        self.anuleaza_buton.place(x=770, y=20)

        self.salveaza_button = ttk.Button(self.frame, text="Salveaza", command=self.salveaza_fisa_tehnologica)
        self.salveaza_button.place(x=40, y=20)

        #########
        self.list_frame_operatii = ttk.Frame(self.frame, width=800, height=350)
        self.list_frame_operatii.place(x=50, y=240)

        self.list_frame_materiale = ttk.Frame(self.frame, width=800, height=350)
        # self.list_frame_operatii.place(x=50, y=240)

        # self.buton_print = ttk.Button(self.frame, text='Print', command=self.print_data_from_tree_view)
        # self.buton_print.place(x=220, y=180)

        self.titlu_label = ttk.Label(self.frame, text="Creare Fisa Tehnologica Noua")
        self.titlu_label.place(x=330, y=20)
        self.titlu_label.config(font=64)

        self.denumire_produs_label = ttk.Label(self.frame, text="Denumire Produs")
        self.denumire_fisa_label = ttk.Label(self.frame, text="Denumire Fisa")
        self.date_label = ttk.Label(self.frame, text="Date")

        self.denumire_produs_label.place(x=50, y=105)
        self.denumire_fisa_label.place(x=420, y=105)
        self.date_label.place(x=760, y=105)

        self.entry_denumire_produs = ttk.Entry(self.frame)
        self.entry_denumire_fisa = ttk.Entry(self.frame)
        self.entry_data_label = ttk.Entry(self.frame)

        self.entry_denumire_produs.place(x=45, y=125, width=350)
        self.entry_denumire_fisa.place(x=415, y=125, width=320)
        self.entry_data_label.place(x=755, y=125, width=120)
        #########

        self.operatii_buton = ttk.Button(self.frame, text="Operatii", command=self.operatii_butin)
        self.operatii_buton.place(x=45, y=170)
        self.materiale_button = ttk.Button(self.frame, text="Materiale", command=self.materiale_buton)
        self.materiale_button.place(x=130, y=170)

        #########
        self.denumire_operatie_label = ttk.Label(self.frame, text="Denumire operatie")
        self.instructiuni_label = ttk.Label(self.frame, text="Instructiuni")
        self.alte_observartii_label = ttk.Label(self.frame, text="Alte observati")

        self.alte_observartii_label.place(x=725, y=630)
        self.instructiuni_label.place(x=360, y=630)
        self.denumire_operatie_label.place(x=50, y=630)

        self.entry_denumire_operatie = ttk.Entry(self.frame)
        self.entry_instructiuni_label = ttk.Entry(self.frame)
        self.entry_alte_observatii = ttk.Entry(self.frame)

        self.entry_alte_observatii.place(x=725, y=650)
        self.entry_instructiuni_label.place(x=360, y=650, width=355)
        self.entry_denumire_operatie.place(x=50, y=650, width=300)
        ############

        self.denumire_material_label = ttk.Label(self.frame, text="Denumire material")
        self.cantitate_material_label = ttk.Label(self.frame, text="Cantitate material")
        self.um_label = ttk.Label(self.frame, text="Cantitate de masura")
        self.entry_denumire_material = ttk.Entry(self.frame)
        self.entry_cantitate_material = ttk.Entry(self.frame)
        self.entry_um = ttk.Entry(self.frame)

        ########

        self.insert_operatie = ttk.Button(self.frame, text="Insert", command=self.insert_operatie_noua)
        self.insert_operatie.place(x=300, y=685)
        self.clear_operatii = ttk.Button(self.frame, text="Clear", command=self.clear_tree_operatii)
        self.clear_operatii.place(x=390, y=685)
        self.delete_operatii_row = ttk.Button(self.frame, text='Delete Row', command=self.delete_row_operatii_comanda)
        self.delete_operatii_row.place(x=480, y=685)

        self.insert_materiale = ttk.Button(self.frame, text="Insert", command=self.insert_materiale_noi)
        self.clear_materiale = ttk.Button(self.frame, text="Clear list", command=self.clear_tree_materiale)
        self.delete_row_materiale = ttk.Button(self.frame, text='Delete Row', command=self.delete_row_materiale_comanda)

        self.dropdown_operatii = ttk.Combobox(self.frame)
        self.dropdown_operatii.place(x=740, y=170)
        self.dropdown_materiale = ttk.Combobox(self.frame)
        self.label_select = ttk.Label(self.frame, text="Select existing")
        self.label_select.place(x=650, y=185)

        self.tree_header_operatii_var = ("id", "denumire_operatie", "instructiuni", "alte_observatii")
        self.tree_view_operatii = ttk.Treeview(self.list_frame_operatii, columns=self.tree_header_operatii_var,
                                               show='headings')
        self.tree_view_operatii.heading('id', text="ID")
        self.tree_view_operatii.heading('denumire_operatie', text="Denumire operatie")
        self.tree_view_operatii.heading('instructiuni', text='Instructiuni')
        self.tree_view_operatii.heading('alte_observatii', text="Alte observatii")
        self.tree_view_operatii.grid(row=0, column=0, sticky='nsew')
        self.scrollbar_operatii = ttk.Scrollbar(self.list_frame_operatii, orient=tk.VERTICAL,
                                                command=self.tree_view_operatii.yview)
        self.tree_view_operatii.configure(yscrollcommand=self.scrollbar_operatii.set)
        self.scrollbar_operatii.grid(row=0, column=1, sticky='ns')

        self.dropdown_operatii['values'] = create_fisa_tehnologica_model.load_operatii()
        self.dropdown_operatii.bind("<<ComboboxSelected>>", self.dropwdown_operatii_callback)
        self.dropdown_materiale.bind("<<ComboboxSelected>>", self.dropdown_materiale_callback)
        self.dropdown_materiale['values'] = create_fisa_tehnologica_model.load_materiale()

        ########

        self.tree_header_materiale_var = ("id", "denumire_material", "cantitate_material", "unitate_de_masura")
        self.tree_view_materiale = ttk.Treeview(self.list_frame_materiale, columns=self.tree_header_materiale_var,
                                                show='headings')
        self.tree_view_materiale.heading('id', text="ID")
        self.tree_view_materiale.heading('denumire_material', text="Denumire material")
        self.tree_view_materiale.heading('cantitate_material', text='Cantitate')
        self.tree_view_materiale.heading('unitate_de_masura', text="U.M")
        self.tree_view_materiale.grid(row=0, column=0, sticky='nsew')
        self.scrollbar_materiale = ttk.Scrollbar(self.list_frame_materiale, orient=tk.VERTICAL,
                                                 command=self.tree_view_materiale.yview)
        self.tree_view_operatii.configure(yscrollcommand=self.scrollbar_materiale.set)
        self.scrollbar_materiale.grid(row=0, column=1, sticky='ns')

        self.frame.pack()

    def load_operatii(self):
        self.dropdown_operatii['values'] = create_fisa_tehnologica_model.load_operatii()
        self.dropdown_operatii.bind('<<ComboboxSelected>>', self.dropwdown_operatii_callback)

    def dropwdown_operatii_callback(self, event):
        index = self.dropdown_operatii.current() + 1
        tree_row = create_fisa_tehnologica_model.filter_operatii(int(index))
        self.tree_view_operatii.insert('', tk.END, values=tree_row)

    def dropdown_materiale_callback(self,event):
        index = self.dropdown_materiale.current() + 1
        tree_row = create_fisa_tehnologica_model.filter_materiale(int(index))
        self.tree_view_materiale.insert('', tk.END, values=tree_row)

    def anuleaza(self):
        self.master.destroy()

    def print_data_from_tree_view_operatii(self):
        k = []
        for parent in self.tree_view_operatii.get_children():
            x = self.tree_view_operatii.item(parent)["values"]

            k.append(tuple(x))
        return k

    def print_data_from_tree_view_materiale(self):
        k = []
        for parent in self.tree_view_materiale.get_children():
            x = self.tree_view_materiale.item(parent)["values"]

            k.append(tuple(x))
        return k

    def salveaza_fisa_tehnologica(self):
        denumire_produs_val = self.entry_denumire_produs.get()
        denumire_fisa_val = self.entry_denumire_fisa.get()
        data_var = self.entry_data_label.get()
        save_data = SaveEntryValues(denumire_produs_val, denumire_fisa_val, data_var)
        save_data.get_operatii_list(self.print_data_from_tree_view_operatii())
        save_data.get_materiale_list(self.print_data_from_tree_view_materiale())
        x = save_data.SaveValues()

        if x == 0:
            print('test')
            FisaTehn.GUI.load_data_auto()
            self.master.destroy()
        elif x == 1:
            print('test2')
            messagebox.showerror('Error', 'Fisa exista deja in baza de date')
        elif x == 2:
            print('test3')
            messagebox.showerror('Error', 'Data introdusa nu este valida, ex(year-month-day)')

    def materiale_buton(self):
        self.denumire_operatie_label.place_forget()
        self.instructiuni_label.place_forget()
        self.alte_observartii_label.place_forget()
        self.entry_denumire_operatie.place_forget()
        self.entry_alte_observatii.place_forget()
        self.entry_instructiuni_label.place_forget()
        self.entry_um.place(x=385, y=650)
        self.entry_cantitate_material.place(x=250, y=650)
        self.entry_denumire_material.place(x=50, y=650, width=195)
        self.um_label.place(x=385, y=630)
        self.cantitate_material_label.place(x=250, y=630)
        self.denumire_material_label.place(x=50, y=630)
        self.instructiuni_label.place_forget()
        self.dropdown_operatii.place_forget()
        self.dropdown_materiale.place(x=740, y=170)

        self.insert_operatie.place_forget()
        self.clear_operatii.place_forget()
        self.delete_operatii_row.place_forget()

        self.insert_materiale.place(x=300,y=685)
        self.clear_materiale.place(x=390,y=685)
        self.delete_row_materiale.place(x=480,y=685)

        self.list_frame_operatii.place_forget()
        self.list_frame_materiale.place(x=50, y=240)

    def operatii_butin(self):
        self.denumire_material_label.place_forget()
        self.cantitate_material_label.place_forget()
        self.um_label.place_forget()
        self.entry_um.place_forget()
        self.entry_denumire_material.place_forget()
        self.entry_cantitate_material.place_forget()
        self.entry_denumire_operatie.place(x=50, y=650, width=300)
        self.entry_alte_observatii.place(x=725, y=650)
        self.entry_instructiuni_label.place(x=360, y=650, width=355)
        self.alte_observartii_label.place(x=725, y=630)
        self.denumire_operatie_label.place(x=50, y=630)
        self.instructiuni_label.place(x=360, y=630)
        self.dropdown_materiale.place_forget()
        self.dropdown_operatii.place(x=740, y=170)

        self.dropdown_operatii['values'] = create_fisa_tehnologica_model.load_operatii()
        self.dropdown_operatii.bind('<<ComboboxSelected>>', self.dropwdown_operatii_callback)

        try:
            self.list_frame_materiale.place_forget()
        except:
            pass
        self.list_frame_operatii.place(x=50, y=240)

    def insert_operatie_noua(self):
        denumire_operatie_get = self.entry_denumire_operatie.get()
        instructiuni_operatie_get = self.entry_instructiuni_label.get()
        alte_observatii_get = self.entry_alte_observatii.get()

        self.tree_view_operatii.insert('', tk.END, values=
        (0, denumire_operatie_get, instructiuni_operatie_get, alte_observatii_get)
                                       )


    def clear_tree_operatii(self):
        for i in self.tree_view_operatii.get_children():
            self.tree_view_operatii.delete(i)

    def delete_row_operatii_comanda(self):
        for i in self.tree_view_operatii.selection():
            self.tree_view_operatii.delete(i)


    def insert_materiale_noi(self):
        denumire_material_get = self.entry_denumire_material.get()
        cantitate_material_get = self.entry_cantitate_material.get()
        unitate_de_masura_get = self.entry_um.get()

        self.tree_view_materiale.insert('', tk.END, values=
        (0,denumire_material_get,cantitate_material_get,unitate_de_masura_get)
                                        )

    def clear_tree_materiale(self):
        for i in self.tree_view_materiale.get_children():
            self.tree_view_materiale.delete(i)

    def delete_row_materiale_comanda(self):
        for i in self.tree_view_materiale.selection():
            self.tree_view_materiale.delete(i)


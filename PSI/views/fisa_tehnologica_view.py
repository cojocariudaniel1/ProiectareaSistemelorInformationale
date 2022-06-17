import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from model import fisa_tehnologica_model as FisaModel
from model import create_fisa_tehnologica_model as CFisaModel
from model.create_fisa_tehnologica_model import SaveEntryValues
from tkinter import messagebox
from . import fisa_tehnologica_create_view as CForm
from . import fisa_tehnologica_edit_view as EForm
HEIGHT = 700
WIDTH = 1000

root = ThemedTk(theme="adapta")
root.title("Fișă tehnologică")


class Main:
    def __init__(self, master):
        super().__init__()
        self.master = master  # the variable that is assignet to main engine of the app.

        # fisa tehnologica frame
        self.frame = ttk.Frame(self.master, height=HEIGHT, width=WIDTH)  # the container
        self.create_form_frame = ttk.Frame(self.master, height=HEIGHT, width=WIDTH)

        self.list_frame = tk.Frame(self.master, height=500, width=700)
        self.list_frame.place(x=50, y=170)

        # Tree view
        self.tree_header_var = ("id", "denumire_produs", "denumire_fisa", "data_realizare")
        self.tree_view = ttk.Treeview(self.list_frame, columns=self.tree_header_var, show='headings')
        self.tree_view.heading('id', text="ID")
        self.tree_view.heading('denumire_produs', text="Denumire produs")
        self.tree_view.heading('denumire_fisa', text='Denumire fisa')
        self.tree_view.heading('data_realizare', text="Data realizare")
        self.tree_view.grid(row=0, column=0, sticky='nsew')
        self.scrollbar = ttk.Scrollbar(self.list_frame, orient=tk.VERTICAL, command=self.tree_view.yview)
        self.tree_view.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=1, sticky='ns')

        # MAIN FRAME labels
        self.fisa_tehnologica = ttk.Label(self.frame, text="Fișă tehnologică", font=20)  # crearea butonului
        self.fisa_tehnologica.place(x=10, y=10)  # implementarea si pozitionarea butonului

        self.filter_label = ttk.Label(self.frame, text="Filter")
        self.filter_label.place(x=720, y=65)

        # button1
        self.create_button = ttk.Button(self.frame, text="Create", command=self.create_fisa_tehnologica)
        self.create_button.place(x=50, y=65)

        # input fields
        self.filter_input = ttk.Entry(self.frame)
        self.filter_input.place(x=40 + 720, y=60)
        self.filter_input.bind("<Return>", self.filter_search)

        self.tree_view.bind('<<TreeviewSelect>>', self.tree_click_event)
        self.tree_view.bind('<Double-Button-1>', self.tree_double_click_event)

        self.tree_view_row = ()

        self.frame.pack()  # pack the frame

    def load_data(self):
        self.tree_view.destroy()
        self.tree_view_refresh()

        for item in FisaModel.load_data():
            self.tree_view.insert('', tk.END, values=item)

    def tree_view_refresh(self):
        self.tree_header_var = ("id", "denumire_produs", "denumire_fisa", "data_realizare")
        self.tree_view = ttk.Treeview(self.list_frame, columns=self.tree_header_var, show='headings')
        self.tree_view.heading('id', text="ID")
        self.tree_view.heading('denumire_produs', text="Denumire produs")
        self.tree_view.heading('denumire_fisa', text='Denumire fisa')
        self.tree_view.heading('data_realizare', text="Data realizare")
        self.tree_view.grid(row=0, column=0, sticky='nsew')
        self.scrollbar = ttk.Scrollbar(self.list_frame, orient=tk.VERTICAL, command=self.tree_view.yview)
        self.tree_view.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=1, sticky='ns')
        self.tree_view.bind('<<TreeviewSelect>>', self.tree_click_event)
        self.tree_view.bind('<Double-Button-1>', self.tree_double_click_event)

    def tree_click_event(self, event):
        real_coords = (self.tree_view.winfo_pointerx() - self.tree_view.winfo_rootx(),
                       self.tree_view.winfo_pointery() - self.tree_view.winfo_rooty())
        item = self.tree_view.identify('item', *real_coords)
        print('********** tree selection event **********')
        print('looks like this virtual event doesnt support event coordinates')
        print('event.x: %d, event.y: %d' % (event.x, event.y))
        print('real.x: %d, real.y: %d' % real_coords)
        print('clicked on', self.tree_view.item(item)['values'])
        print('******************************************\n')

    def tree_double_click_event(self, event):
        real_coords = (self.tree_view.winfo_pointerx() - self.tree_view.winfo_rootx(),
                       self.tree_view.winfo_pointery() - self.tree_view.winfo_rooty())
        item = self.tree_view.identify('item', *real_coords)
        self.tree_view_row = tuple(self.tree_view.item(item)['values'])
        run_edit_fisa()

    def filter_search(self, event):
        get_search_value = self.filter_input.get()
        k = FisaModel.filter_search(get_search_value)

        self.tree_view.destroy()
        self.tree_view_refresh()

        for item in k:
            self.tree_view.insert('', tk.END, values=item)



    def create_fisa_tehnologica(self):
        run_create_fisa()

def run_edit_fisa():
    edit_fisa = ThemedTk(theme="adapta")
    edit_fisa.title("Fisa Tehnologica Edit")
    x = GUI.tree_view_row
    k = EForm.EditFisa(edit_fisa, x[0],x[1], x[2],x[3])
    k.load_data_auto()
    k.load_data_from_database()
    edit_fisa.mainloop()

def run_create_fisa():
    create_fisa = ThemedTk(theme="adapta")
    create_fisa.title("Fișă tehnologică")
    k = CForm.CreateForm(create_fisa)
    k.load_operatii()

    create_fisa.mainloop()




def main_run():
    root.mainloop()


GUI = Main(root)
GUI.load_data()

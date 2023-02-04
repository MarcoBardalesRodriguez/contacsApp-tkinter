import tkinter as tk
from tkinter import ttk

from model.new_contact import Model as ModelNewContact
from view.new_contact import View as ViewNewContact
from controller.new_contact import Controller as ControllerNewContact

class App(tk.Tk):
  def __init__(self):
    super().__init__()

    self.title('Contactos')
    self.geometry('300x450')
    self.resizable(0,0)

    self.lbl_title = ttk.Label(self, text='Mis contactos')
    self.lbl_title.grid(row=0, column=0, padx=10, pady=20)

    #frame button new contact + frame window new contact
    view_new_contact = ViewNewContact(self)
    view_new_contact.grid(row=1, column=0)
    model_new_contact = ModelNewContact()
    controller_new_contact = ControllerNewContact(model_new_contact, view_new_contact)
    view_new_contact.set_controller(controller_new_contact)



if __name__ == '__main__':
  app = App()
  app.mainloop()

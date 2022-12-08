import tkinter as tk
from tkinter import ttk


class ContactFrame(tk.Toplevel):
  def __init__(self, container):
    super().__init__(container)
    self.container = container
    self.title('Agregar nuevo contacto')
    self.geometry('300x300')
    self.resizable(0,0)
    
    self.phone = tk.StringVar()
    self.lbl_phone = ttk.Label(self, text='Numero')
    self.lbl_phone.grid(row=1, column=0)
    self.box_phone = ttk.Entry(self, textvariable=self.phone)
    self.box_phone.grid(row=1, column=1)
    
    self.name = tk.StringVar()
    self.lbl_name = ttk.Label(self, text='Nombre')
    self.lbl_name.grid(row=2, column=0)
    self.box_name = ttk.Entry(self, textvariable=self.name)
    self.box_name.grid(row=2, column=1)
    
    self.last_name = tk.StringVar()
    self.lbl_last_name = ttk.Label(self, text='Apellido')
    self.lbl_last_name.grid(row=3, column=0)
    self.box_last_name = ttk.Entry(self, textvariable=self.last_name)
    self.box_last_name.grid(row=3, column=1)

    self.btn_cancel = ttk.Button(self, text='Cancelar', command=self.cancel)
    self.btn_cancel.grid(row=5, column=0)
  
    self.btn_accept= ttk.Button(self, text='Aceptar', command=self.accept)
    self.btn_accept.grid(row=5, column=2)

    self.controller = None

  
  def set_controller(self, controller):
    self.controller = controller
    
    
  def data_contact(self):
    self.data = {'phone' : self.phone.get(),
                        'name' : self.name.get(),
                        'last_name' : self.last_name.get()}
    return self.data
  
  def cancel(self):
    self.container.enabledButton()
    self.destroy()

  
  def accept(self):
    # self.container.enabledButton()
    data = self.data_contact()
    self.controller.save(data)


class View(ttk.Frame):
  def __init__(self, container):
    super().__init__(container)
    
    self.btn_add_contact = ttk.Button(self, text='Agregar', command=self.showContactFrame)
    self.btn_add_contact.grid(row=0, column=0)

    self.controller = None
  
  
  def set_controller(self, controller):
    self.controller = controller

  
  def disabledButton(self):
    self.btn_add_contact['state'] = tk.DISABLED
    

  def enabledButton(self):
    self.btn_add_contact['state'] = tk.NORMAL
    

  def showContactFrame(self):
    self.disabledButton()
    self.contact_frame = ContactFrame(self)
    self.contact_frame.set_controller(self.controller)
  
  def closeNewContactFrame(self):
    self.contact_frame.destroy()
    self.enabledButton()
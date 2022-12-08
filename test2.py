import re
import tkinter as tk
from tkinter import ttk



class Model:
  def __init__(self, data_contact = {'phone':'999999999', 'name':'name', 'last_name':'last_name'}):
    self.data_contact = data_contact
    
  
  # @property
  # def data_contact(self):
  #   if self.data_contact :
  #     return self._data_contact
  
  
  # @data_contact.setter
  # def data_contact(self, data_contact):
  #   pattern_phone = r'\b\9[0-9]{8}\b'
  #   pattern_name = r'.*'
  #   if data_contact:
  #   # if re.fullmatch(pattern_phone, data_contact['phone']) and re.fullmatch(pattern_name, data_contact['name']):
  #     self.data_contact = data_contact
  #   else:
  #     raise ValueError('Se produjo un error al guardar, ingrese datos correctos')
  
  
  def save(self):
    print(self.data_contact)
  #creacion de base de datos
  




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
    self.container.enabledButton()
    print(self.data_contact())
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





class Controller:
  def __init__(self, model, view):
    self.model = model
    self.view = view
    
  def save(self, data_contact):
    try:
      self.model.data_contact = data_contact
      self.model.save()
      print('se guardo correctamente')
      self.view.closeNewContactFrame()
    except ValueError as error:
      print(error)



class App(tk.Tk):
  def __init__(self):
    super().__init__()

    self.title('Contactos')
    self.geometry('300x450')
    self.resizable(0,0)
    
    self.lbl_title = ttk.Label(self, text='Mis contactos')
    self.lbl_title.grid(row=0, column=0, padx=10, pady=20)

    model_new_contact = Model()

    view_new_contact = View(self)
    #frame button new contact + frame window new contact
    view_new_contact.grid(row=1, column=0)
    
    controller_new_contact = Controller(model_new_contact, view_new_contact)

    view_new_contact.set_controller(controller_new_contact)

    
    
if __name__ == '__main__':
  app = App()
  app.mainloop()   
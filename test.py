import tkinter as tk


class View2(tk.Toplevel):
  def __init__(self, container):
    super().__init__(container)
    self.title('Agregar nuevo contacto')
    self.geometry('300x300')
    


class View(tk.Frame):
  def __init__(self, container):
    super().__init__(container)
    
    self.btn_add_contact = tk.Button(self, text='Agregar', command=self.openAddContactFrame)
    self.btn_add_contact.grid(row=0, column=0)

  
  def openAddContactFrame(self):
    contact_frame = View2(self)





class App(tk.Tk):
  def __init__(self):
    super().__init__()

    self.title('Contacts')
    self.geometry('300x450')
    self.resizable(0,0)
    
    self.lbl_title = tk.Label(self, text='Mis contactos')
    self.lbl_title.grid(row=0, column=0, padx=10, pady=20)

    btn_add_contact = View(self)
    btn_add_contact.grid(row=1, column=0)

    
    
if __name__ == '__main__':
  app = App()
  app.mainloop()
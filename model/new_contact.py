import re
import sqlite3

class DataBase:
  def __init__(self, name_db):
    self.conn = sqlite3.connect(name_db)
    self.cursor = self.conn.cursor()
  
    self.cursor.execute(""" CREATE TABLE IF NOT EXISTS contacts(
      phone CHAR(9) PRIMARY KEY,
      name VARCHAR(25) NOT NULL,
      last_name VARCHAR(50) ) """)

  def insert(self, data):
    self.cursor.execute(f" INSERT INTO contacts VALUES({data['phone']}, '{data['name']}', '{data['last_name']}') ")
    # self.query = f" INSERT INTO usuarios Values({self.id}, '{self.nombre}', '{self.apellido}')"
    self.conn.commit()

  
  def show(self):
    self.cursor.execute(" SELECT * FROM contacts ")
    print(self.cursor.fetchall())
    self.conn.close()
    

class Model:
  def __init__(self, data_contact = {}):
    self._data_contact = data_contact
    

  @property
  def data_contact(self):
    print('getter')
    return self._data_contact
  
  
  @data_contact.setter
  def data_contact(self, data_contact = {}):
    pattern = r'9\d{8}'
    if re.fullmatch(pattern, data_contact['phone']) and data_contact['name']:
      self._data_contact = data_contact
    else:
      raise ValueError('Se produjo un error al guardar, ingrese datos correctos')
      
  
  def save(self):
    print(self._data_contact)
    # conn = sqlite3.connect('contacts.db')
    DB = DataBase('contacts.db')
    DB.insert(self._data_contact)
    DB.show()

  
  
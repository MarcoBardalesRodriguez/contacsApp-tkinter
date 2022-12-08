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
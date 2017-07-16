class Item:

  def __init__(self, id, name, description, actions):
    """ Define an item """
    self.id = id
    self.name = name
    self.description = description
    self.actions = actions

  def set_status(self, action, status):
    """ set the status of the item """
    self.actions[action] = status  

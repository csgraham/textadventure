class Location:

  def __init__(self, id, name, description, items, characters, exits):
    """ Define a location """
    self.id = id
    self.name = name
    self.description = description
    self.items = items
    self.characters = characters
    self.exits = exits

  def add_item(self, item):
    """ Add an item to the location """
    self.items.append(item)

  def remove_item(self, item):
    """ Remove an item from the location """
    self.items.remove(item)

  def add_character(self, character):
    """ Add a character to the location """
    self.characters.append(character)

  def remove_character(self, character):
    """ Remove a character from the location """
    self.characters.remove(character)

class Character:

  def __init__(self, id, name, description, talks, items, combat, stats):
    """ defines a character """
    self.id = id
    self.name = name
    self.description = description
    self.talks = talks
    self.items = items
    self.combat = combat
    self.stats = stats

  def get_requests(self):
    """ returns what you can ask """
     return self.talks

  def add_item(self, item):
    """ Add an item to the character """
    self.items.append(item)

  def remove_item(self, item):
    """ Remove an item from the character """
    self.items.remove(item)

  def get_combat(self):
    """ returns how you can fight """
    return self.combat

  def get_stat(self, stat)
    """ returns a stat of the character """
    return self.stats[stat]

  def set_stat(self, stat, value):
    """ set a stat value """
    self.stats[stat] = value



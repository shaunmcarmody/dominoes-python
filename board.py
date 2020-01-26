from random import randrange

class Board:
  def __init__(self):
    self.stock = []
    self.chain = []
    self.front = None
    self.rear = None

  def add_to_stock(self, tile):
    self.stock.append(tile)

  def connect_to_front(self, tile):
    if self.front.ends[0] == tile.ends[0]:
      tile.rotate()
    self.chain.insert(0, tile)
    self.front = tile

  def connect_to_rear(self, tile):
    if self.rear.ends[1] == tile.ends[1]:
      tile.rotate()
    self.chain.append(tile)
    self.rear = tile

  def draw_tile(self):
    count = len(self.stock)
    if count > 0:
      i = randrange(count)
      tile = self.stock[i]
      self.stock = self.stock[:i] + self.stock[i+1:]
      return tile
    else:
      return False

  def get_ends(self):
    return self.front, self.rear

  def __str__(self):
    chain = ''
    for tile in self.chain:
      chain += f'{tile} '
    return f'Board is now: {chain}'
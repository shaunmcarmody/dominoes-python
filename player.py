class Player:
  def __init__(self, name, stock):
    self.name = name
    self.stock = stock
    self.total_stock = 0
    self.blocked = False

  def add_to_stock(self, tile):
    self.stock.append(tile)
    self.total_stock += 1

  def block(self):
    if self.blocked == False:
      self.blocked = True

  def check_board(self, front, rear):
    for i in range(self.total_stock):
      tile = self.stock[i]
      if front in tile.ends or rear in tile.ends:
        return self.remove_from_stock(i)
    return False

  def remove_from_stock(self, i):
    tile = self.stock[i]
    self.stock = self.stock[:i] + self.stock[i+1:]
    self.total_stock -= 1
    return tile

  def sum_remaining_tiles(self):
    total = 0
    for tile in self.stock:
      total = total + tile.ends[0] + tile.ends[1]
    return total

  def unblock(self):
    if self.blocked == True:
      self.blocked = False

  def __str__(self):
    return self.name
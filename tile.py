class Tile:
  def __init__(self, *args):
    self.ends = args

  def rotate(self):
    self.ends = self.ends[::-1]

  def __str__(self):
    return f'<{self.ends[0]}:{self.ends[1]}>'
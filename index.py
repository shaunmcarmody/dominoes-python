from board import Board
from player import Player
from tile import Tile

# Initialise Game
board = Board()

player_a = Player('Alice', [])
player_b = Player('Bob', [])

# Add 28 tiles to the board to form the stock
for i in range(7):
  for j in range(i + 1):
    tile = Tile(j, i)
    board.add_to_stock(tile)

# Each player draws seven tiles, then pick a random tile to start the line of play.
draw = 0
while draw < 7:
  player_a.add_to_stock(board.draw_tile())
  player_b.add_to_stock(board.draw_tile())
  draw += 1

initial_tile = board.draw_tile()
board.chain.append(initial_tile)
board.front = initial_tile
board.rear = initial_tile

# Start Game
active_player = player_a
blocked = False

print('Game starting with first tile:', initial_tile)
while active_player.total_stock > 0:
  def play(player):
    # Extend the line of play at one of its two ends
    front, rear = board.get_ends()
    front_value, rear_value = front.ends[0], rear.ends[1]
    tile = player.check_board(front_value, rear_value)
    # If a player is unable to place a valid tile, they must keep on pulling tiles from the stock until they can.
    if tile is False:
      player.block()
      drawn_tile = board.draw_tile()
      if drawn_tile is False:
        print(f"{player} can't play and is unable to draw a tile")
        return drawn_tile
      else:
        print(f"{player} can't play, drawing tile {drawn_tile}")
        player.add_to_stock(drawn_tile)
        play(player)
    # Respective values on the tile are identical to one of the ends, connect filenext to end tile.
    else:
      player.unblock()
      if front_value in tile.ends:
        print(f'{player} plays {tile} to connect to tile {front} on the board')
        board.connect_to_front(tile)
      elif rear_value in tile.ends:
        print(f'{player} plays {tile} to connect to tile {rear} on the board')
        board.connect_to_rear(tile)
      return tile

  active_tile = play(active_player)
  if active_tile == False:
    # If both players are blocked then break loop
    if player_a.blocked == True and player_b.blocked == True:
      blocked = True
      break
  else:
    print(board)
    # If one player has no tiles left then break loop
    if active_player.total_stock == 0:
      break
  # Or players alternate
  active_player = player_b if active_player.name == player_a.name else player_a

# If both players have avoided being blocked then we can declare the winner
if blocked is False:
  print(f'Player {active_player} has won!')
# else we are going to sum the combined value of each players ends in there stock and whoever has the lowest value is the winner
else:
  player_a_sum = player_a.sum_remaining_tiles()
  print(f'{player_a} has remaining tiles with a combined value of {player_a_sum} left on the board')
  player_b_sum = player_b.sum_remaining_tiles()
  print(f'{player_b} has remaining tiles with a combined value of {player_b_sum} left on the board')

  winner = None
  if player_a_sum == player_b_sum:
    winner = 'Draw'
  elif player_a_sum < player_b_sum:
    winner = player_a
  else:
    winner = player_b

  if winner == 'Draw':
    print(f'Match ends draw!')
  else:
    print(f'Player {winner} has won!')
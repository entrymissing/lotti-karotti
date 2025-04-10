import random


class CardStack(object):
  def __init__(self):
    self.all_cards = ['3'] * 3 + ['2'] * 4 + ['1'] * 5 + ['K'] * 5
    self.shuffle()

  def shuffle(self):
    self.cards = self.all_cards.copy()
    random.shuffle(self.cards)

  def draw(self):
    if len(self.cards) == 0:
      self.shuffle()
    return self.cards.pop()


class GameState(object):
  _GOAL_FIELD = 26

  def __init__(self, number_of_players=2):
    assert number_of_players >= 2, 'There must be at least 2 players'
    assert number_of_players <= 4, 'There can be at most 4 players'

    self.players = []
    for i in range(number_of_players):
      self.players.append(['S', 'S', 'S', 'S'])
    self.current_player = 0
    self.card_stack = CardStack()

  def is_spot_free(self, spot: int) -> bool:
    for player in self.players:
      if spot in player:
        return False
    return True

  # Figure out where a figure starting at start would end up after moving
  # steps times.
  # Returns None if the figure cannot be moved.
  def can_move_figure(self, start: int, steps: int) -> int:
    offset = 1
    while not self.is_spot_free(start + offset):
      offset += 1
    if start + offset > self._GOAL_FIELD:
      return None
    if steps == 1:
      return start + offset
    return self.can_move_figure(start + offset, steps - 1)

  def get_moves(self, player, steps) -> list:
    assert player >= 0, 'Player index must be >= 0'
    assert player < len(self.players), 'Player index out of range'
    assert isinstance(steps, int), 'Steps must be an integer'
    assert steps is not None, 'Steps must not be None'
    assert steps >= 0, 'Steps must be >= 0'
    assert steps <= 4, 'Steps must be <= 4'

    moves = set()
    for i in range(4):
      if self.players[player][i] == 'S':
        moves.append(i)
    return moves


deck = CardStack()
print(deck.draw())

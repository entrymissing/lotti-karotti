from lotti import GameState


def test_GameState_init():
  game = GameState(3)
  assert len(game.players) == 3, 'Number of players is incorrect'
  for player in game.players:
    assert player == ['S', 'S', 'S', 'S'], 'Start positions are incorrect'


def test_GameState_is_spot_free():
  game = GameState(2)

  game.players[0] = [0, 1, 'S', 3]
  game.players[1] = ['S', 5, 6, 7]
  for spots in (0, 1, 5, 6, 7):
    assert not game.is_spot_free(spots), f'Spot {spots} should be occupied'
  for spots in (2, 4, 8):
    assert game.is_spot_free(spots), f'Spot {spots} should be free'


def test_GameState_can_move_figure():
  game = GameState(2)

  game.players[0] = [0, 1, 'S', 3]
  game.players[1] = ['S', 5, 6, 7]
  assert game.can_move_figure(0, 1) == 2, 'Incorrect move'
  assert game.can_move_figure(1, 1) == 2, 'Incorrect move'
  assert game.can_move_figure(0, 2) == 4, 'Incorrect move'
  assert game.can_move_figure(0, 3) == 8, 'Incorrect move'
  assert game.can_move_figure(25, 1) == 26, 'Incorrect move'
  assert not game.can_move_figure(26, 1), 'Move should be impossible'
  assert not game.can_move_figure(25, 2), 'Move should be impossible'
  assert not game.can_move_figure(26, 1), 'Move should be impossible'
  assert not game.can_move_figure(27, 2), 'Move should be impossible'

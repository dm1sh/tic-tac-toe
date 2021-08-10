from src.ttt_game import Game, Tr


def test_init():
  g = Game()

  assert len(g._board) == 9

  for i in range(9):
    assert g._board[i] == Tr.E


def setup_insert_1X() -> Game:
  g = Game()
  g.insert(1, Tr.X)

  return g


def setup_insert_13X5O() -> Game:
  g = Game()
  g.insert(1, Tr.X)
  g.insert(5, Tr.O)
  g.insert(3, Tr.X)

  return g


def test_insert_1X():
  g = setup_insert_1X()

  b = g._board
  assert b.count(Tr.X) == 1
  assert b.count(Tr.O) == 0
  assert b.count(Tr.E) == 8


def test_insert_1X5O():
  g = setup_insert_13X5O()

  b = g._board
  assert b.count(Tr.X) == 2
  assert b.count(Tr.O) == 1
  assert b.count(Tr.E) == 6

  assert b[1] == Tr.X
  assert b[3] == Tr.X
  assert b[5] == Tr.O


def test_get_board():
  g1 = setup_insert_1X()
  g2 = setup_insert_13X5O()

  for g in (g1, g2):
    b = g._board
    test_b = g.get_board()

    for el in Tr:
      assert b.count(el) == test_b.count(el)


def test_move():
  g = Game()

  res = g.move(0, Tr.X)
  assert res == False
  res_board = g.get_board()
  assert res_board[0] == Tr.X
  assert res_board.count(Tr.X) == 1
  assert res_board.count(Tr.O) == 0
  assert res_board.count(Tr.E) == 8

  res = g.move(3, Tr.O)
  assert res == False
  res_board = g.get_board()
  assert res_board[3] == Tr.O
  assert res_board.count(Tr.X) == 1
  assert res_board.count(Tr.O) == 1
  assert res_board.count(Tr.E) == 7

  res = g.move(1, Tr.X)
  assert res == False
  res_board = g.get_board()
  assert res_board[1] == Tr.X
  assert res_board.count(Tr.X) == 2
  assert res_board.count(Tr.O) == 1
  assert res_board.count(Tr.E) == 6

  res = g.move(2, Tr.X)
  assert res == True
  res_board = g.get_board()
  assert res_board[2] == Tr.X
  assert res_board.count(Tr.X) == 3
  assert res_board.count(Tr.O) == 1
  assert res_board.count(Tr.E) == 5

  res = g.move(2, Tr.X)
  assert res == False


def test_get_free():
  g1 = setup_insert_1X()
  g2 = setup_insert_13X5O()

  for g in (g1, g2):
    b = g._board
    free = g.get_free()

    assert len(free) == b.count(Tr.E)

    for i in free:
      assert b[i] == Tr.E


def test_check_move():
  g = setup_insert_13X5O()

  assert g.check_move(3) == False
  assert g.check_move(0) == True


def test_check_filled():
  g = Game()

  assert g.check_filled() == False

  for i in range(8):
    g.insert(i, (Tr.X, Tr.O)[i % 2])
    assert g.check_filled() == False

  g.insert(8, Tr.X)
  assert g.check_filled() == True


def test_check_win():
  for steps in ((0, 1, 2), (0, 3, 6), (0, 4, 8), (2, 4, 6)):
    g = Game()

    for i in range(9):
      assert g.check_win(i) == False

    g.insert(5, Tr.O)

    for i in range(9):
      assert g.check_win(i) == False

    for i in steps:
      g.insert(i, Tr.X)

    assert g.check_win(i) == True

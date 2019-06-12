from solution import flip_inside_O_by_UF


def test_empty_board():
    board = []
    flip_inside_O_by_UF(board)
    assert [] == board


def test_given_sample():
    board = [['X', 'X', 'X', 'X'],
             ['X', 'O', 'O', 'X'],
             ['X', 'X', 'O', 'X'],
             ['X', 'O', 'X', 'X']]  # yapf: disable
    expected = [['X', 'X', 'X', 'X'],
                ['X', 'X', 'X', 'X'],
                ['X', 'X', 'X', 'X'],
                ['X', 'O', 'X', 'X']]  # yapf: disable

    flip_inside_O_by_UF(board)
    assert expected == board


def test_no_flip_sample():
    board = [["O", "O", "O", "O", "X", "X"],
             ["O", "O", "O", "O", "O", "O"],
             ["O", "X", "O", "X", "O", "O"],
             ["O", "X", "O", "O", "X", "O"],
             ["O", "X", "O", "X", "O", "O"],
             ["O", "X", "O", "O", "O", "O"]]  # yapf: disable

    expected = [r[:] for r in board]
    flip_inside_O_by_UF(board)

    assert expected == board


def test_boundary_node1_node12_noflip_sample():
    # yapf: disable
    board = [["X", "O", "O", "X", "X", "X", "O", "X", "O", "O"],
             ["X", "O", "X", "X", "X", "X", "X", "X", "X", "X"],
             ["X", "X", "X", "X", "O", "X", "X", "X", "X", "X"],
             ["X", "O", "X", "X", "X", "O", "X", "X", "X", "O"],
             ["O", "X", "X", "X", "O", "X", "O", "X", "O", "X"],
             ["X", "X", "O", "X", "X", "O", "O", "X", "X", "X"],
             ["O", "X", "X", "O", "O", "X", "O", "X", "X", "O"],
             ["O", "X", "X", "X", "X", "X", "O", "X", "X", "X"],
             ["X", "O", "O", "X", "X", "O", "X", "X", "O", "O"],
             ["X", "X", "X", "O", "O", "X", "O", "X", "X", "O"]]
    expected = [["X", "O", "O", "X", "X", "X", "O", "X", "O", "O"],
                ["X", "O", "X", "X", "X", "X", "X", "X", "X", "X"],
                ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
                ["X", "X", "X", "X", "X", "X", "X", "X", "X", "O"],
                ["O", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
                ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
                ["O", "X", "X", "X", "X", "X", "X", "X", "X", "O"],
                ["O", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
                ["X", "X", "X", "X", "X", "X", "X", "X", "O", "O"],
                ["X", "X", "X", "O", "O", "X", "O", "X", "X", "O"]]

    flip_inside_O_by_UF(board)
    assert expected == board

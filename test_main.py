from main import *

def test_horizontal_winner():
    assert horizontal_winner([["X", "O", "X"],["O", "O", "O"],["X", "X", "O"]],"O") == True
    assert horizontal_winner([["X", "O", "X"],["O", "X", "O"],["X", "X", "O"]],"O") == False

def test_vertical_winner():
    assert vertical_winner([["X", "O", "X"],["O", "O", "X"],["X", "O", "O"]], "O") == True
    assert vertical_winner([["X", "O", "X"],["O", "X", "X"],["X", "O", "O"]], "O") == False

def test_diagonal_winner():
    assert diagonal_winner([["X", "O", "X"],["O", "X", "O"],["X", "X", "X"]], "X") == True
    assert diagonal_winner([["X", "O", "X"],["O", "O", "X"],["X", "X", "O"]], "X") == False

def test_anywhere_winner():
    assert anywhere_winner([["X", "O", "X"],["O", "O", "O"],["X", "X", "O"]], "O") == True
    assert anywhere_winner([["X", "O", "X"],["O", "X", "O"],["X", "X", "O"]], "X") == True
    assert anywhere_winner([["X", "O", "X"],["O", "X", "O"],["O", "X", "O"]], "O") == False
    assert anywhere_winner([["X", "O", "X"],["O", "O", "X"],["X", "X", "O"]], "O") == False

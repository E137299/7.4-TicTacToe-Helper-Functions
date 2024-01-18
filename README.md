# Tic-Tac-Toe Helper Functions


### `horizontal_winner(board, player)`

#### Description:
This function checks if the player has three consecutive horizontal marks on the Tic-Tac-Toe board.

#### Parameters:
- `board`: a 2D list representing the Tic-Tac-Toe board.
- `player`: either an "X" or an "O"

#### Return:
- `True` if there is a horizontal winner.
- `False` otherwise.

#### Instructions:
1. Iterate through each row in the `board`.
2. Check if all elements in any row are the same and not equal to an empty space (e.g., "X" or "O").
3. If found, return `True`.
4. If no horizontal winner is found, return `False`.

### `vertical_winner(board, player)`

#### Description:
This function checks if the player has three consecutive, vertical marks on the Tic-Tac-Toe board.

#### Parameters:
- `board`: a 2D list representing the Tic-Tac-Toe board.
- `player`: either an "X" or an "O"

#### Return:
- `True` if there is a vertical winner.
- `False` otherwise.

#### Instructions:
1. Iterate through each column in the `board`.
2. Check if all elements in any column are the same and not equal to an empty space.
3. If found, return `True`.
4. If no vertical winner is found, return `False`.

### `diagonal_winner(board, player)`

#### Description:
This function checks if the player has three consecutive, diagonal marks on the Tic-Tac-Toe board.

#### Parameters:
- `board`: a 2D list representing the Tic-Tac-Toe board.
- `player`: either an "X" or an "O"

#### Return:
- `True` if there is a diagonal winner.
- `False` otherwise.

#### Instructions:
1. Check both main diagonals of the `board`.
2. Ensure that all elements in any diagonal are the same and not equal to an empty space.
3. If found, return `True`.
4. If no diagonal winner is found, return `False`.


### 4. `anywhere_winner(board, player)`

#### Description:
This function checks if the player wins either horizontally, vertically, or diagonally on the Tic-Tac-Toe board.

#### Parameters:
- `board`: a 2D list representing the Tic-Tac-Toe board.
- `player`: either an "X" or an "O"

#### Return:
- `True` if there is a winner anywhere on the board.
- `False` otherwise.

#### Instructions:
1. Call the `horizontal_winner(board)`, `vertical_winner(board)`, and `diagonal_winner(board)` functions to check for a winner in each direction.
2. If any of the three functions returns `True`, indicating a winner in that direction, return `True`.
3. If none of the functions finds a winner, return `False`.


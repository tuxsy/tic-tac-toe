class Game:

    def __init__(self):
        self.turns = 0
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

    # Public methods
    def start(self):
        self._display_board()
        while True:
            if self.turns >= 8:
                print("Game over! It's a draw.")
                break
            if self._ask_for_move(1, "X"):
                print("Game over! Player X wins!")
                break
            if self._ask_for_move(-1, "O"):
                print("Game over! Player O wins!")
                break

    # Private methods
    def _print_sprite(self, value):
        if value == 0:
            return " "
        elif value == 1:
            return "X"
        elif value == -1:
            return "O"

    def _display_board(self):
        print("     1   2   3")
        print("  ", "-" * 14)
        for i, row in enumerate(self.board):
            print(f"{i+1} | {self._print_sprite(row[0])} | {self._print_sprite(row[1])} | {self._print_sprite(row[2])} |")
            print("  ", "-" * 14)

    def _ask_for_move(self, value, player):
        while True:
            move = input(f"Player {player}, enter your move (row, column): ")
            try:
                move = tuple(map(int, move.split(",")))
                if len(move) != 2:
                    raise ValueError
                row, col = move
                if not (1 <= row <= 3 and 1 <= col <= 3):
                    raise ValueError
                if self.board[row - 1][col - 1] != 0:
                    print("That cell is already occupied. Please choose another one.")
                    continue
                self.board[row - 1][col - 1] = value
                self.turns += 1
                self._display_board()
                return self._check_winner()
            except ValueError:
                print("Invalid input. Please enter your move in the format 'row,column'.")

    def _check_winner(self):
        rows = [r for r in self.board]
        rows_sum = self._sum_values(rows)
        if rows_sum != 0:
            return rows_sum
        cols = [[self.board[i][j] for i in range(3)] for j in range(3)]
        cols_sum = self._sum_values(cols)
        if cols_sum != 0:
            return cols_sum
        diagonals = [[self.board[i][i] for i in range(3)], [self.board[i][2 - i] for i in range(3)]]
        diagonals_sum = self._sum_values(diagonals)
        if diagonals_sum != 0:
            return diagonals_sum
        return 0

    def _sum_values(self, matrix):
        matrix_sum = [sum(e) for e in matrix]
        if 3 in matrix_sum:
            return 1
        elif -3 in matrix_sum:
            return -1
        return 0
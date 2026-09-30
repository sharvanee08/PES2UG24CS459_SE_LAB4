import random


class Puzzle:
    def __init__(self, size=4):
        self.size = size
        self.board = self.make_board()

    def make_board(self):
        # Start from the solved board
        tiles = list(range(1, self.size * self.size)) + [0]
        board = [
            tiles[r * self.size:(r + 1) * self.size]
            for r in range(self.size)
        ]

        # Scramble only through legal blank moves
        self.board = board
        scramble_moves = self.size * self.size * 20

        previous_move = None
        opposite = {
            "w": "s",
            "s": "w",
            "a": "d",
            "d": "a"
        }

        for _ in range(scramble_moves):
            valid_moves = []

            r, c = self.blank_pos()

            if r > 0:
                valid_moves.append("w")
            if r < self.size - 1:
                valid_moves.append("s")
            if c > 0:
                valid_moves.append("a")
            if c < self.size - 1:
                valid_moves.append("d")

            # Avoid immediately undoing the previous move
            if previous_move and len(valid_moves) > 1:
                valid_moves.remove(opposite[previous_move])

            direction = random.choice(valid_moves)
            self.move(direction)
            previous_move = direction

        return self.board

    def blank_pos(self):
        for r in range(self.size):
            for c in range(self.size):
                if self.board[r][c] == 0:
                    return r, c

    def move(self, direction):
        r, c = self.blank_pos()

        dr, dc = {
            "w": (-1, 0),
            "s": (1, 0),
            "a": (0, -1),
            "d": (0, 1)
        }[direction]

        nr, nc = r + dr, c + dc

        if not (0 <= nr < self.size and 0 <= nc < self.size):
            return False

        self.board[r][c], self.board[nr][nc] = (
            self.board[nr][nc],
            self.board[r][c]
        )

        return True

    def solved(self):
        return (
            sum(self.board, [])
            == list(range(1, self.size * self.size)) + [0]
        )

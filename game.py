import time
from puzzle import Puzzle


class SlidingPuzzle:
    def __init__(self, size=4):
        self.size = size
        self.puzzle = Puzzle(self.size)
        self.moves = 0
        self.started = time.monotonic()
        self.game_over = False

    def display(self):
        print()
        for row in self.puzzle.board:
            print(" ".join(f"{x or ' ':>2}" for x in row))

        print(
            "Moves:", self.moves,
            " Time:", int(time.monotonic() - self.started), "s"
        )

    def run(self):
        print(
            f"Sliding Puzzle {self.size}x{self.size} — "
            "W/A/S/D moves the tile into the blank. Q quits."
        )

        while not self.game_over:
            self.display()

            if self.puzzle.solved():
                self.game_over = True
                print("🎉 Puzzle solved!")
                print("Final moves:", self.moves)
                print(
                    "Final time:",
                    int(time.monotonic() - self.started),
                    "s"
                )
                break

            key = input("> ").strip().lower()

            if key == "q":
                print("Game exited.")
                return

            if key not in "wasd":
                print("Invalid command. Use W/A/S/D or Q.")
                continue

            # Only count and report a move if the tile actually moved.
            if self.puzzle.move(key):
                self.moves += 1
                print("Tile moved.")

                if self.puzzle.solved():
                    self.game_over = True
                    self.display()
                    print("🎉 Puzzle solved!")
                    print("Final moves:", self.moves)
                    print(
                        "Final time:",
                        int(time.monotonic() - self.started),
                        "s"
                    )
                    break
            else:
                print("That move is not possible.")

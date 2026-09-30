from game import SlidingPuzzle


def choose_size():
    while True:
        print()
        print("Choose puzzle size:")
        print("1. 3x3")
        print("2. 4x4")
        print("3. 5x5")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            return 3
        elif choice == "2":
            return 4
        elif choice == "3":
            return 5
        else:
            print("Please enter 1, 2, or 3.")


def main():
    size = choose_size()
    game = SlidingPuzzle(size)
    game.run()


if __name__ == "__main__":
    main()

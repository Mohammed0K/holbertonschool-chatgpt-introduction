#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        # Randomly place mines as a set of flattened indices
        self.mines = set(random.sample(range(width * height), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def print_board(self, reveal=False):
        clear_screen()
        # Print column headers
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            # Print row header
            print(y, end=' ')
            for x in range(self.width):
                idx = y * self.width + x
                if reveal or self.revealed[y][x]:
                    # Show mine or adjacent mine count
                    if idx in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    # Hidden cell
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        idx = y * self.width + x
        # Return False if a mine is revealed
        if idx in self.mines:
            return False

        # Mark this cell as revealed
        self.revealed[y][x] = True

        # If no adjacent mines, reveal neighbors recursively
        if self.count_mines_nearby(x, y) == 0:
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < self.width and
                        0 <= ny < self.height and
                        not self.revealed[ny][nx]):
                        self.reveal(nx, ny)
        return True

    def is_won(self):
        # Count how many cells have been revealed
        revealed_count = sum(
            self.revealed[y][x]
            for y in range(self.height)
            for x in range(self.width)
        )
        # Win when all non-mine cells are revealed
        return revealed_count == (self.width * self.height - len(self.mines))

    def play(self):
        while True:
            self.print_board()
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))

                # If stepping on a mine, game over
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break

                # Check for victory
                if self.is_won():
                    self.print_board(reveal=True)
                    print("Congratulations! You've won the game.")
                    break

            except ValueError:
                print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()


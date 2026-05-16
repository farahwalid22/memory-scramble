from game import GameBoard

# quick test to make sure game logic works
if __name__ == "__main__":
    b = GameBoard(4, 4)
    print(f"Board created: {b.rows}x{b.cols}, {b.total_pairs} pairs")
    print("game.py is working - ui coming next")

import random

SYMBOLS = [
    "🐶", "🐱", "🐭", "🐹", "🐰", "🦊", "🐻", "🐼",
    "🐨", "🐯", "🦁", "🐮", "🐷", "🐸", "🐙", "🦋",
    "🌸", "🌟", "🎯", "🎮", "🏆", "🎸", "🚀", "🌈"
]


class Card:
    def __init__(self, symbol, position):
        self.symbol = symbol
        self.position = position  # (row, col)
        self.is_face_up = False
        self.is_matched = False

    def flip(self):
        if not self.is_matched:
            self.is_face_up = not self.is_face_up


class GameBoard:
    def __init__(self, rows, cols):
        if (rows * cols) % 2 != 0:
            raise ValueError("Board size must be even.")
        if rows < 2 or cols < 2:
            raise ValueError("Minimum board size is 2x2.")

        self.rows = rows
        self.cols = cols
        self.board = []
        self.selected = []
        self.matched_pairs = 0
        self.total_pairs = (rows * cols) // 2
        self._build()

    def _build(self):
        n = self.total_pairs
        if n > len(SYMBOLS):
            raise ValueError("Board too large, not enough symbols.")

        picked = random.sample(SYMBOLS, n)
        all_symbols = picked * 2
        random.shuffle(all_symbols)

        idx = 0
        for r in range(self.rows):
            row = []
            for c in range(self.cols):
                row.append(Card(all_symbols[idx], (r, c)))
                idx += 1
            self.board.append(row)

    def get_card(self, r, c):
        return self.board[r][c]

    def select_card(self, r, c):
        card = self.get_card(r, c)

        if card.is_matched or card.is_face_up:
            return "already_open"

        if len(self.selected) == 2:
            return "wait"

        card.flip()
        self.selected.append(card)

        if len(self.selected) == 1:
            return "flipped"

        c1, c2 = self.selected
        if c1.symbol == c2.symbol:
            c1.is_matched = True
            c2.is_matched = True
            self.matched_pairs += 1
            self.selected = []
            return "match"

        return "no_match"

    def reset_unmatched(self):
        for card in self.selected:
            card.is_face_up = False
        self.selected = []

    def is_complete(self):
        return self.matched_pairs == self.total_pairs

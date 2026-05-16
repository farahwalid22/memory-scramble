import tkinter as tk
from tkinter import messagebox
from game import GameBoard
import config


class MemoryGameApp:
    def __init__(self, root):
        self.root = root
        self.root.configure(bg=config.BG_COLOR)
        self.board = None
        self.buttons = []
        self.timer_id = None
        self.time_left = 0
        self.waiting = False
        self._setup_screen()

    def _setup_screen(self):
        self._clear()
        self.root.title("Memory Scramble")

        frame = tk.Frame(self.root, bg=config.BG_COLOR, padx=40, pady=30)
        frame.pack()

        tk.Label(frame, text="Memory Scramble", font=("Arial", 20, "bold"),
                 bg=config.BG_COLOR, fg=config.TEXT_COLOR).grid(row=0, column=0, columnspan=2, pady=(0, 18))

        tk.Label(frame, text="Rows:", font=("Arial", 12),
                 bg=config.BG_COLOR, fg=config.TEXT_COLOR).grid(row=1, column=0, sticky="e", pady=5)
        self.rows_var = tk.IntVar(value=config.DEFAULT_ROWS)
        tk.Spinbox(frame, from_=2, to=8, textvariable=self.rows_var,
                   width=5, font=("Arial", 12)).grid(row=1, column=1, sticky="w", padx=8)

        tk.Label(frame, text="Columns:", font=("Arial", 12),
                 bg=config.BG_COLOR, fg=config.TEXT_COLOR).grid(row=2, column=0, sticky="e", pady=5)
        self.cols_var = tk.IntVar(value=config.DEFAULT_COLS)
        tk.Spinbox(frame, from_=2, to=8, textvariable=self.cols_var,
                   width=5, font=("Arial", 12)).grid(row=2, column=1, sticky="w", padx=8)

        tk.Label(frame, text="Time (sec):", font=("Arial", 12),
                 bg=config.BG_COLOR, fg=config.TEXT_COLOR).grid(row=3, column=0, sticky="e", pady=5)
        self.timeout_var = tk.IntVar(value=config.DEFAULT_TIMEOUT)
        tk.Spinbox(frame, from_=10, to=300, increment=10, textvariable=self.timeout_var,
                   width=5, font=("Arial", 12)).grid(row=3, column=1, sticky="w", padx=8)

        tk.Button(frame, text="Start Game", font=("Arial", 13, "bold"),
                  bg=config.BUTTON_COLOR, fg="white", relief="flat",
                  padx=18, pady=7, cursor="hand2",
                  command=self._start).grid(row=4, column=0, columnspan=2, pady=18)

    def _start(self):
        rows = self.rows_var.get()
        cols = self.cols_var.get()
        timeout = self.timeout_var.get()

        if (rows * cols) % 2 != 0:
            messagebox.showerror(
                "Invalid Size", "rows x columns must be even.")
            return

        try:
            self.board = GameBoard(rows, cols)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return

        self.time_left = timeout
        # game screen coming in next commit
        messagebox.showinfo(
            "OK", f"Board {rows}x{cols} ready, timer={timeout}s")

    def _clear(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None
        for w in self.root.winfo_children():
            w.destroy()


class MemoryGameApp:
    def __init__(self, root):
        self.root = root
        self.root.configure(bg=config.BG_COLOR)
        self.board = None
        self.buttons = []
        self.timer_id = None
        self.time_left = 0
        self.waiting = False
        self._setup_screen()

    def _setup_screen(self):
        self._clear()
        self.root.title("Memory Scramble")

        frame = tk.Frame(self.root, bg=config.BG_COLOR, padx=40, pady=30)
        frame.pack()

        tk.Label(frame, text="Memory Scramble", font=("Arial", 20, "bold"),
                 bg=config.BG_COLOR, fg=config.TEXT_COLOR).grid(row=0, column=0, columnspan=2, pady=(0, 18))

        tk.Label(frame, text="Rows:", font=("Arial", 12),
                 bg=config.BG_COLOR, fg=config.TEXT_COLOR).grid(row=1, column=0, sticky="e", pady=5)
        self.rows_var = tk.IntVar(value=config.DEFAULT_ROWS)
        tk.Spinbox(frame, from_=2, to=8, textvariable=self.rows_var,
                   width=5, font=("Arial", 12)).grid(row=1, column=1, sticky="w", padx=8)

        tk.Label(frame, text="Columns:", font=("Arial", 12),
                 bg=config.BG_COLOR, fg=config.TEXT_COLOR).grid(row=2, column=0, sticky="e", pady=5)
        self.cols_var = tk.IntVar(value=config.DEFAULT_COLS)
        tk.Spinbox(frame, from_=2, to=8, textvariable=self.cols_var,
                   width=5, font=("Arial", 12)).grid(row=2, column=1, sticky="w", padx=8)

        tk.Label(frame, text="Time (sec):", font=("Arial", 12),
                 bg=config.BG_COLOR, fg=config.TEXT_COLOR).grid(row=3, column=0, sticky="e", pady=5)
        self.timeout_var = tk.IntVar(value=config.DEFAULT_TIMEOUT)
        tk.Spinbox(frame, from_=10, to=300, increment=10, textvariable=self.timeout_var,
                   width=5, font=("Arial", 12)).grid(row=3, column=1, sticky="w", padx=8)

        tk.Button(frame, text="Start Game", font=("Arial", 13, "bold"),
                  bg=config.BUTTON_COLOR, fg="white", relief="flat",
                  padx=18, pady=7, cursor="hand2",
                  command=self._start).grid(row=4, column=0, columnspan=2, pady=18)

    def _start(self):
        rows = self.rows_var.get()
        cols = self.cols_var.get()
        timeout = self.timeout_var.get()

        if (rows * cols) % 2 != 0:
            messagebox.showerror(
                "Invalid Size", "rows x columns must be even.")
            return

        try:
            self.board = GameBoard(rows, cols)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return

        self.time_left = timeout
        self._game_screen()

    def _game_screen(self):
        self._clear()

        top = tk.Frame(self.root, bg=config.BG_COLOR, pady=6)
        top.pack(fill="x")

        tk.Label(top, text="Time Left:", font=("Arial", 12),
                 bg=config.BG_COLOR, fg=config.TEXT_COLOR).pack(side="left", padx=(16, 4))

        self.timer_lbl = tk.Label(top, text=str(self.time_left),
                                  font=("Arial", 14, "bold"),
                                  bg=config.BG_COLOR, fg=config.TIMER_NORMAL_COLOR)
        self.timer_lbl.pack(side="left")

        self.score_lbl = tk.Label(top, text=f"Pairs: 0 / {self.board.total_pairs}",
                                  font=("Arial", 12),
                                  bg=config.BG_COLOR, fg=config.TEXT_COLOR)
        self.score_lbl.pack(side="right", padx=16)

        grid = tk.Frame(self.root, bg=config.BG_COLOR, padx=10, pady=8)
        grid.pack()

        self.buttons = []
        for r in range(self.board.rows):
            row_btns = []
            for c in range(self.board.cols):
                btn = tk.Button(
                    grid,
                    text="", width=4, height=2,
                    font=("Arial", config.CARD_FONT_SIZE),
                    bg=config.CARD_BACK_COLOR,
                    fg=config.CARD_BACK_COLOR,
                    relief="raised", bd=3,
                    cursor="hand2",
                    command=lambda row=r, col=c: self._click(row, col)
                )
                btn.grid(row=r, column=c, padx=4, pady=4)
                row_btns.append(btn)
            self.buttons.append(row_btns)

    def _click(self, r, c):
        if self.waiting:
            return

        result = self.board.select_card(r, c)

        if result in ("already_open", "wait"):
            return

        self._refresh_card(r, c)

        if result == "match":
            for row in self.board.board:
                for card in row:
                    if card.is_matched:
                        self.buttons[card.position[0]][card.position[1]].config(
                            bg=config.CARD_MATCHED_COLOR)

            self.score_lbl.config(
                text=f"Pairs: {self.board.matched_pairs} / {self.board.total_pairs}")

        elif result == "no_match":
            self.waiting = True
            self.root.after(850, self._flip_back)

    def _refresh_card(self, r, c):
        card = self.board.get_card(r, c)
        btn = self.buttons[r][c]
        if card.is_face_up or card.is_matched:
            btn.config(text=card.symbol, fg=config.CARD_FRONT_COLOR,
                       bg=config.CARD_FRONT_COLOR)
        else:
            btn.config(text="", fg=config.CARD_BACK_COLOR,
                       bg=config.CARD_BACK_COLOR)

    def _flip_back(self):
        self.board.reset_unmatched()
        for r in range(self.board.rows):
            for c in range(self.board.cols):
                card = self.board.get_card(r, c)
                if not card.is_face_up and not card.is_matched:
                    self.buttons[r][c].config(text="",
                                              fg=config.CARD_BACK_COLOR,
                                              bg=config.CARD_BACK_COLOR)
        self.waiting = False

    def _clear(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None
        for w in self.root.winfo_children():
            w.destroy()

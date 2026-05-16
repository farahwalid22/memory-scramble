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
            messagebox.showerror("Invalid Size", "rows x columns must be even.")
            return

        try:
            self.board = GameBoard(rows, cols)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return

        self.time_left = timeout
        # game screen coming in next commit
        messagebox.showinfo("OK", f"Board {rows}x{cols} ready, timer={timeout}s")

    def _clear(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None
        for w in self.root.winfo_children():
            w.destroy()

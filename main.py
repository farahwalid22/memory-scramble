import tkinter as tk
from ui import MemoryGameApp

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Memory Scramble")
    root.resizable(False, False)
    app = MemoryGameApp(root)
    root.mainloop()

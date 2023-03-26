import tkinter as tk
from detect_language import setup_language_processing

def window():
    label = tk.Label(text="this is the language")
    label.pack()
    window.mainloop()

window()
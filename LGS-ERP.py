# LGS ERP
# Marko, Marcel, Willem

import tkinter as tk
import ttkthemes as ttkt
from tkinter import ttk

root = ttkt.ThemedTk(theme="adapta")
root.geometry("300x200")
root.iconbitmap("lgslogo.ico")
root.title("LGS ERP")

button = ttk.Button(root, text="Click Me!")
button.pack(pady=50)

root.mainloop()
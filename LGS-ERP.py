# LGS ERP
# Marko, Marcel, Willem

import tkinter as tk
import ttkthemes as ttkt
from tkinter import ttk

root = ttkt.ThemedTk(theme="adapta")
root.iconbitmap("lgslogo.ico")
root.title("LGS ERP")

topbar_title = ttk.Label(root, text="LGS ERP", borderwidth="2")
topbar_title.pack(pady=10, padx=10, anchor="nw")

root.mainloop()
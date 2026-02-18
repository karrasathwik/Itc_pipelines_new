import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("CKD Diet Guidance Tool")
root.geometry("400x400")

title = tk.Label(root, text="CKD Dietary Guidance",font=("Arial", 16, "bold"))
title.pack(pady=10)

#Label for the egfr
egfr_label = tk.Label(root, text="Enter eGFR:")
egfr_label.pack()
egfr_entry = tk.Entry(root)
egfr_entry.pack(pady=5)
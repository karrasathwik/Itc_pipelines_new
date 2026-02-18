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


#Label for the egfr
egfr_label = tk.Label(root, text="Enter eGFR:")
egfr_label.pack()
egfr_entry = tk.Entry(root)
egfr_entry.pack(pady=5)

#Label for potassium
potassium_label = tk.Label(root, text="Enter Potassium (mmol/L):")
potassium_label.pack()
potassium_entry = tk.Entry(root) pot_entry.pack(pady=5)

#Label for phosphate
phosphate_label = tk.Label(root, text="Enter Phosphate (mmol/L):")
phosphate_label.pack()
phosphate_entry = tk.Entry(root)
phosphate_entry.pack(pady=5)

#function to say received data and messagebox
def data_recieved_message():
    try:
        egfr = float(egfr_entry.get())
        potassium = float(potassium_entry.get())
        phosphate = float(phosphate_entry.get())
        message = (f"Inputs received:\n\n" f"eGFR: {egfr}\n" f"Potassium: {potassium}\n" f"Phosphate: {phosphate}")
        messagebox.showinfo("Success", message)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.") 

submit_btn = tk.Button(root, text="Submit", command=data_recieved_message) submit_btn.pack(pady=20)

root.mainloop()
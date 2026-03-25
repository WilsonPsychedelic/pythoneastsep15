import tkinter as tk
from tkinter import messagebox

def fibonacci_sequence(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    sequence = []
    a, b = 0, 1
    
    for _ in range(n + 1):
        sequence.append(a)
        a, b = b, a + b

    return sequence

def on_calculate():
    try:
        n_text = entry_n.get().strip()

        if not n_text:
            messagebox.showerror("Input Error", "Please enter a number.")
            return
        
        n = int(n_text)
        seq = fibonacci_sequence(n)
        result_str = ", ".join(str(num) for num in seq)

        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, f"Sequence up to {n}:\n{result_str}")

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

def on_clear():
    entry_n.delete(0, tk.END)
    result_text.delete("1.0", tk.END)

# Main window
root = tk.Tk()
root.title("Fibonacci Calculator")
root.geometry("420x300")
root.resizable(False, False)

# Title
title_label = tk.Label(root, text="Fibonacci Sequence Calculator", font =("Arial", 14, "bold"))
title_label.pack(pady=10)

# Input label
input_label = tk.Label(root, text="Enter n (0 or greater):")
input_label.pack()

# Input box
entry_n = tk.Entry(root, width=20)
entry_n.pack(pady=5)

# Buttons
calculate_button = tk.Button(root, text="Show Sequence", command=on_calculate)
calculate_button.pack(pady=8)

clear_button = tk.Button(root, text="Clear", command=on_clear)
clear_button.pack()

# Result
result_text = tk.Text(root, height=8, width=45, wrap="word")
result_text.pack(pady=10)

# Run app
root.mainloop()

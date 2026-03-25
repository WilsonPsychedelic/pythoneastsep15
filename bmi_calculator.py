import tkinter as tk
from tkinter import messagebox

def calculate_bmi(weight_kg, height_m):
    """
    Calculates BMI and returns both height and weight.
    """
    if height_m <= 0:
        raise ValueError("Height must be greater than zero.")
    if weight_kg < 0:
        raise ValueError("Weight cannot be negative.")
    
    return weight_kg / (height_m ** 2)

def bmi_category(bmi):
    """
    Determines BMI category.
    """
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def bmi_report(weight_kg, height_m):
    """
    Returns BMI value and category as a tuple.
    """
    bmi = calculate_bmi(weight_kg, height_m)
    category = bmi_category(bmi)
    return bmi, category

def on_calculate():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        bmi, category = bmi_report(weight, height)
        result_label.config(text=f"Your BMI is {bmi:.2f}\nCategory: {category}")

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

# Create main window
root =  tk.Tk()
root.title("BMI Calculator")
root.geometry("300x250")

#Weight input
weight_label = tk.Label(root, text="Weight (kg):")
weight_label.pack(pady=(15, 5))

weight_entry = tk.Entry(root)
weight_entry.pack()

# Height input
height_label = tk.Label(root, text="Height (m):")
height_label.pack(pady=(10, 5))

height_entry = tk.Entry(root)
height_entry.pack()

# Calculate button
calculate_button = tk.Button(root, text="Calculate BMI", command=on_calculate)
calculate_button.pack(pady=15)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Start app
root.mainloop()

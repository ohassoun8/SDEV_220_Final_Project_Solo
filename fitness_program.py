import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

# Calculate BMI
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100  # Convert cm to meters
        bmi = weight / (height ** 2)
        bmi_result.config(text=f"BMI: {bmi:.2f}", fg="#4CAF50")  
    except ValueError:
        messagebox.showerror("Error", "Please enter valid weight and height.")

# Function for workout log
def save_workout():
    workout = workout_entry.get()
    if workout:
        with open("workout_log.txt", "a") as file:
            file.write(f"{workout}\n")
        messagebox.showinfo("Success", "Workout saved successfully!")
    else:
        messagebox.showerror("Error", "Please enter a workout.")

# The main window
root = tk.Tk()
root.title("Fitness Program")
root.geometry("500x500")
root.configure(bg="#F0F0F0")  # Light gray background

# Load and display logo
logo_image = Image.open("logo.png")  
logo_image = logo_image.resize((100, 100), Image.Resampling.LANCZOS)  
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = tk.Label(root, image=logo_photo, bg="#F0F0F0")
logo_label.grid(row=0, column=0, columnspan=2, pady=10)

# Title label
title_label = tk.Label(root, text="Fitness Tracker", font=("Arial", 20, "bold"), bg="#F0F0F0", fg="#333333")
title_label.grid(row=1, column=0, columnspan=2, pady=10)

# Labels and entries for user details
tk.Label(root, text="Weight (kg):", font=("Arial", 12), bg="#F0F0F0", fg="#333333").grid(row=2, column=0, padx=10, pady=10)
weight_entry = tk.Entry(root, font=("Arial", 12), bg="#FFFFFF", fg="#333333", relief="flat")
weight_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Height (cm):", font=("Arial", 12), bg="#F0F0F0", fg="#333333").grid(row=3, column=0, padx=10, pady=10)
height_entry = tk.Entry(root, font=("Arial", 12), bg="#FFFFFF", fg="#333333", relief="flat")
height_entry.grid(row=3, column=1, padx=10, pady=10)

# Button to calculate BMI
bmi_button = ttk.Button(
    root,
    text="Calculate BMI",
    style="Fancy.TButton",
    command=calculate_bmi
)
bmi_button.grid(row=4, column=0, columnspan=2, pady=10)

# Label to display BMI result
bmi_result = tk.Label(root, text="BMI: ", font=("Arial", 12), bg="#F0F0F0", fg="#333333")
bmi_result.grid(row=5, column=0, columnspan=2, pady=10)

# Workout log section
tk.Label(root, text="Enter your workout:", font=("Arial", 12), bg="#F0F0F0", fg="#333333").grid(row=6, column=0, padx=10, pady=10)
workout_entry = tk.Entry(root, font=("Arial", 12), bg="#FFFFFF", fg="#333333", relief="flat", width=30)
workout_entry.grid(row=6, column=1, padx=10, pady=10)

# Button to save workout
save_button = ttk.Button(
    root,
    text="Save Workout",
    style="Fancy.TButton",
    command=save_workout
)
save_button.grid(row=7, column=0, columnspan=2, pady=10)

# Display image
fitness_image = Image.open("fitness.jpg")  
fitness_image = fitness_image.resize((200, 150), Image.Resampling.LANCZOS) 
fitness_photo = ImageTk.PhotoImage(fitness_image)
fitness_label = tk.Label(root, image=fitness_photo, bg="#F0F0F0")
fitness_label.grid(row=8, column=0, columnspan=2, pady=10)

# Style for buttons
style = ttk.Style()
style.configure(
    "Fancy.TButton",
    font=("Arial", 12, "bold"),
    background="#8BC34A",  
    foreground="#FFFFFF",  
    borderwidth=0,
    focusthickness=3,
    focuscolor="#8BC34A",
    padding=10,
    relief="raised",
)
style.map(
    "Fancy.TButton",
    background=[("active", "#7CB342")],  
    relief=[("pressed", "sunken"), ("!pressed", "raised")],
)

# Run the program and have fun
root.mainloop()
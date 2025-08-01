import tkinter as tk
from tkinter import messagebox

def create_name_entries():
    try:
        for widget in name_frame.winfo_children():
            widget.destroy()

        global name_entries
        name_entries = []

        num_people = int(entry_people.get())
        if num_people <= 0:
            raise ValueError("Number of people must be greater than 0")

        for i in range(num_people):
            tk.Label(name_frame, text=f"Name {i+1}:", bg="#d6eaf8", fg="#154360").grid(row=i, column=0, padx=5, pady=3)
            entry = tk.Entry(name_frame)
            entry.grid(row=i, column=1, padx=5, pady=3)
            name_entries.append(entry)

    except ValueError as ve:
        messagebox.showerror("Invalid Input", f"Error: {ve}")
    except Exception:
        messagebox.showerror("Error", "Enter a valid number of people.")

def calculate_rent():
    try:
        total_rent = float(entry_rent.get())
        num_people = int(entry_people.get())
        utilities = float(entry_util.get() or 0)

        if num_people <= 0:
            raise ValueError("Number of people must be greater than 0")

        names = [entry.get().strip() for entry in name_entries]
        if any(name == "" for name in names):
            raise ValueError("All names must be filled.")

        total = total_rent + utilities
        per_person = total / num_people

        result = ""
        for name in names:
            result += f"{name}: ₹{per_person:.2f}\n"

        result_label.config(text=result, fg="#006400")

    except ValueError as ve:
        messagebox.showerror("Invalid Input", f"Error: {ve}")
    except Exception:
        messagebox.showerror("Error", "Please check your inputs.")

# GUI setup
root = tk.Tk()
root.title("Rent Calculator")
root.geometry("400x500")
root.config(bg="#d6eaf8")

label_style = {"bg": "#d6eaf8", "fg": "#154360", "font": ("Segoe UI", 10, "bold")}

tk.Label(root, text="Total Rent (₹):", **label_style).pack(pady=4)
entry_rent = tk.Entry(root)
entry_rent.pack()

tk.Label(root, text="Utility Charges (₹):", **label_style).pack(pady=4)
entry_util = tk.Entry(root)
entry_util.pack()

tk.Label(root, text="Number of People:", **label_style).pack(pady=4)
entry_people = tk.Entry(root)
entry_people.pack()

tk.Button(root, text="Enter Names", command=create_name_entries,
          bg="#5dade2", fg="white", font=("Segoe UI", 10, "bold")).pack(pady=8)


name_frame = tk.Frame(root, bg="#d6eaf8")
name_frame.pack(pady=5)

tk.Button(root, text="Calculate Rent", command=calculate_rent,
          bg="#1abc9c", fg="white", font=("Segoe UI", 10, "bold")).pack(pady=12)


result_label = tk.Label(root, text="", font=("Segoe UI", 11),
                        bg="#d6eaf8", justify="left")
result_label.pack(pady=10)

root.mainloop()

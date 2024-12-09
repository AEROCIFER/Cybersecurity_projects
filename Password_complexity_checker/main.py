import tkinter as tk
from tkinter import messagebox
import re

def check_password_complexity(password):
    criteria = {
        "length": len(password) >= 8,
        "uppercase": any(char.isupper() for char in password),
        "lowercase": any(char.islower() for char in password),
        "digit": any(char.isdigit() for char in password),
        "special": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)),
        "no_repeated_characters": len(password) == len(set(password)),
        "no_common_passwords": password not in ["password", "123456", "qwerty"],
        "no_consecutive_characters": not any(ord(password[i]) + 1 == ord(password[i + 1]) for i in range(len(password) - 1)),
    }
    
    # Calculate score
    score = sum(criteria.values())
    strength = "Strong" if score == 5 else "Weak"
    
    # Generate feedback
    feedback = []
    if not criteria["length"]:
        feedback.append("Password must be at least 8 characters long.")
    if not criteria["uppercase"]:
        feedback.append("Password must include at least one uppercase letter.")
    if not criteria["lowercase"]:
        feedback.append("Password must include at least one lowercase letter.")
    if not criteria["digit"]:
        feedback.append("Password must include at least one digit.")
    if not criteria["special"]:
        feedback.append("Password must include at least one special character.")
    if not criteria["no_common_passwords"]:
        feedback.append("The password contains repeated characters.")
    if not criteria["no_consecutive_characters"]:
        feedback.append("The password contains common passowrds.")
    if not criteria["no_repeated_characters"]:
        feedback.append("The password contains repeated characters.")

    return strength, feedback

def on_check_password(event=None):  # Accepts an optional event argument
    password = password_entry.get()
    if not password.strip():
        messagebox.showerror("Error", "Password field cannot be empty.")
        return

    strength, feedback = check_password_complexity(password)
    result_label.config(text=f"Password Strength: {strength}")
    feedback_text.delete("1.0", tk.END)
    if feedback:
        feedback_text.insert(tk.END, "\n".join(feedback))
    else:
        feedback_text.insert(tk.END, "Your password meets all criteria!")

# Create main window
root = tk.Tk()
root.title("Password Complexity Checker")
root.geometry("400x300")
root.resizable(False, False)

# GUI components
tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack(pady=10)
password_entry = tk.Entry(root, show="*", font=("Arial", 12), width=30)
password_entry.pack()

# Bind the Enter key to the on_check_password function
password_entry.bind("<Return>", on_check_password)

tk.Button(root, text="Check Password", command=on_check_password, font=("Arial", 12)).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), fg="blue")
result_label.pack(pady=5)

tk.Label(root, text="Feedback:", font=("Arial", 12)).pack(pady=5)
feedback_text = tk.Text(root, height=8, width=40, font=("Arial", 10), wrap="word")
feedback_text.pack()

# Run the application
root.mainloop()

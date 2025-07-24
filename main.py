# # import string
# # import random
# # if __name__ == "__main__":
# #     S1 = string.ascii_lowercase
# #     # print(S1)

# #     S2 = string.ascii_uppercase
# #     # print(S2)

# #     S3 = string.digits
# #     # print(S3)

# #     S4 = string.punctuation
# #     # print(S4)

# #     plen = int(input("Enter the length of password:\n"))
    

# #     S = []
# #     S.extend(list(S1))
# #     S.extend(list(S2))
# #     S.extend(list(S3))
# #     S.extend(list(S4))

# #     # print(S)
# #     random.shuffle(S)
# #     # print(S)
# # <<<<<<< HEAD
# #     print("Your Password Are:")
# # =======
# #     print("Your Password is:")
# # >>>>>>> 141684ef065607d23c37324540d8cfaf80c3d3b2
# #     print("".join(S[0:plen]))




# import string
# import random

# if __name__ == "__main__":
#     S1 = string.ascii_lowercase
#     S2 = string.ascii_uppercase
#     S3 = string.digits
#     S4 = string.punctuation

#     plen = int(input("Enter the length of password:\n"))

#     S = []
#     S.extend(list(S1))
#     S.extend(list(S2))
#     S.extend(list(S3))
#     S.extend(list(S4))

#     random.shuffle(S)

#     print("Your Password is given :")
#     print("".join(S[:plen]))


import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import string
import random
import pyperclip

# Global password history list
history = []

# Check password strength
def check_strength(pw):
    score = 0
    if any(c.islower() for c in pw): score += 1
    if any(c.isupper() for c in pw): score += 1
    if any(c.isdigit() for c in pw): score += 1
    if any(c in string.punctuation for c in pw): score += 1

    if len(pw) >= 12 and score == 4:
        return "💪 Strong"
    elif len(pw) >= 8 and score >= 3:
        return "👍 Moderate"
    else:
        return "⚠️ Weak"

# Estimate time to crack the password
def estimate_crack_time(password):
    charset = 0
    if any(c.islower() for c in password): charset += 26
    if any(c.isupper() for c in password): charset += 26
    if any(c.isdigit() for c in password): charset += 10
    if any(c in string.punctuation for c in password): charset += len(string.punctuation)

    combinations = charset ** len(password)
    guesses_per_second = 1e9  # 1 billion guesses/second
    seconds = combinations / guesses_per_second
    return human_readable_time(seconds)

def human_readable_time(seconds):
    if seconds < 60:
        return f"{seconds:.2f} seconds"
    elif seconds < 3600:
        return f"{seconds/60:.2f} minutes"
    elif seconds < 86400:
        return f"{seconds/3600:.2f} hours"
    elif seconds < 31536000:
        return f"{seconds/86400:.2f} days"
    else:
        return f"{seconds/31536000:.2f} years"

# Generate Password
def generate_password():
    length = length_slider.get()
    S = []

    if var_lower.get():
        S.extend(string.ascii_lowercase)
    if var_upper.get():
        S.extend(string.ascii_uppercase)
    if var_digits.get():
        S.extend(string.digits)
    if var_symbols.get():
        S.extend(string.punctuation)

    if not S:
        messagebox.showwarning("Warning", "Please select at least one character type.")
        return

    password = ''.join(random.choices(S, k=length))
    password_entry.config(show="" if show_password_var.get() else "*")
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

    # Update strength and crack time
    strength = check_strength(password)
    strength_label.config(text=f"Password Strength: {strength}")

    crack_time = estimate_crack_time(password)
    crack_time_label.config(text=f"⏱️ Time to Crack: {crack_time}")

    # Copy to clipboard
    pyperclip.copy(password)
    copied_label.config(text="📋 Copied to clipboard!")

    # Update history
    history.insert(0, password)
    if len(history) > 5:
        history.pop()
    update_history_box()

# Show/Hide Password
def toggle_password():
    if show_password_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

# Save to file
def save_password():
    pw = password_entry.get()
    if not pw:
        messagebox.showerror("Error", "No password to save.")
        return

    with open("saved_passwords.txt", "a") as f:
        f.write(pw + "\n")
    messagebox.showinfo("Saved", "Password saved to saved_passwords.txt")

# Update history display
def update_history_box():
    history_text.config(state="normal")
    history_text.delete("1.0", tk.END)
    for pw in history:
        history_text.insert(tk.END, pw + "\n")
    history_text.config(state="disabled")

# Setup window
win = tk.Tk()
win.title("🔐 Password Generator")
win.geometry("450x600")
win.resizable(False, False)

# Title
tk.Label(win, text="🛡️ Secure Password Generator", font=("Arial", 14, "bold")).pack(pady=10)

# Options
frame = tk.Frame(win)
frame.pack()

var_lower = tk.BooleanVar(value=True)
var_upper = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=False)

tk.Checkbutton(frame, text="Lowercase (a-z)", variable=var_lower).grid(row=0, column=0, sticky="w")
tk.Checkbutton(frame, text="Uppercase (A-Z)", variable=var_upper).grid(row=1, column=0, sticky="w")
tk.Checkbutton(frame, text="Digits (0-9)", variable=var_digits).grid(row=2, column=0, sticky="w")
tk.Checkbutton(frame, text="Symbols (!@#)", variable=var_symbols).grid(row=3, column=0, sticky="w")

# Password Length
tk.Label(win, text="🔢 Select Password Length:").pack(pady=(10, 0))
length_slider = tk.Scale(win, from_=4, to=32, orient="horizontal", length=300)
length_slider.set(12)
length_slider.pack()

# Password Display
tk.Label(win, text="🔑 Generated Password:").pack(pady=(10, 0))
password_entry = tk.Entry(win, font=("Courier", 12), justify="center", width=30, show="*")
password_entry.pack(pady=5)

# Show/Hide toggle
show_password_var = tk.BooleanVar()
tk.Checkbutton(win, text="👁️ Show Password", variable=show_password_var, command=toggle_password).pack()

# Strength and copied message
strength_label = tk.Label(win, text="", font=("Arial", 10))
strength_label.pack()
crack_time_label = tk.Label(win, text="", font=("Arial", 10), fg="blue")
crack_time_label.pack()
copied_label = tk.Label(win, text="", font=("Arial", 10), fg="green")
copied_label.pack()

# Buttons
tk.Button(win, text="Generate Password", command=generate_password, bg="green", fg="white").pack(pady=10)
tk.Button(win, text="💾 Save Password", command=save_password, bg="blue", fg="white").pack(pady=5)

# Password History
tk.Label(win, text="🕓 Password History (Last 5):").pack(pady=(15, 0))
history_text = tk.Text(win, height=5, width=40, state="disabled")
history_text.pack(pady=(0, 10))

# Run the GUI
win.mainloop()

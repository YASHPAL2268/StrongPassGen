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
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

    strength = check_strength(password)
    strength_label.config(text=f"Password Strength: {strength}")

    pyperclip.copy(password)
    copied_label.config(text="📋 Copied to clipboard!")

# Setup window
win = tk.Tk()
win.title("🔐 Password Generator")
win.geometry("400x400")
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
length_slider = tk.Scale(win, from_=4, to=32, orient="horizontal", length=250)
length_slider.set(12)
length_slider.pack()

# Password Display
tk.Label(win, text="🔑 Generated Password:").pack(pady=(10, 0))
password_entry = tk.Entry(win, font=("Courier", 12), justify="center", width=30)
password_entry.pack(pady=5)

# Strength and copy feedback
strength_label = tk.Label(win, text="", font=("Arial", 10))
strength_label.pack()
copied_label = tk.Label(win, text="", font=("Arial", 10), fg="green")
copied_label.pack()

# Buttons
tk.Button(win, text="Generate Password", command=generate_password, bg="green", fg="white").pack(pady=15)

# Run the GUI
win.mainloop()

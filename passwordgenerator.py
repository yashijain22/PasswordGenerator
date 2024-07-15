import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
import random
import string
import pyperclip


# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for password length.")
        return

    if length <= 0:
        messagebox.showerror("Error", "Password length should be greater than zero.")
        return

    include_letters = include_letters_var.get()
    include_numbers = include_numbers_var.get()
    include_symbols = include_symbols_var.get()

    characters = ''

    if include_letters:
        characters += string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "Please select at least one character type.")
        return

    generated_password = ''.join(random.choice(characters) for _ in range(length))

    password_text.delete(1.0, tk.END)  # Clear previous content
    password_text.insert(tk.END, generated_password)

    # Copy to clipboard
    pyperclip.copy(generated_password)
    messagebox.showinfo("Success", "Password generated and copied to clipboard!")


# Create the main window
window = tk.Tk()
window.title("Advanced Password Generator")

# Password Length
length_label = tk.Label(window, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(window)
length_entry.pack()

# Character type checkboxes
include_letters_var = tk.BooleanVar()
include_numbers_var = tk.BooleanVar()
include_symbols_var = tk.BooleanVar()

include_letters_checkbox = tk.Checkbutton(window, text="Include letters", variable=include_letters_var)
include_letters_checkbox.pack()

include_numbers_checkbox = tk.Checkbutton(window, text="Include numbers", variable=include_numbers_var)
include_numbers_checkbox.pack()

include_symbols_checkbox = tk.Checkbutton(window, text="Include symbols", variable=include_symbols_var)
include_symbols_checkbox.pack()

# Generate button
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack()

# Display generated password
password_label = tk.Label(window, text="Generated Password:")
password_label.pack()

password_text = scrolledtext.ScrolledText(window, height=5)
password_text.pack()

# Run the main loop
window.mainloop()

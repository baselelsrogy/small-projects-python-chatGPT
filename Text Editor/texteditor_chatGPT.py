import tkinter as tk
from tkinter import filedialog, messagebox

# -----------------------------
# Simple Text Editor App
# -----------------------------

root = tk.Tk()
root.title("Simple Text Editor")
root.geometry("600x400")

# -----------------------------
# Functions for Open and Save
# -----------------------------

def open_file():
    """Open a text file and display its content in the textbox."""
    try:
        file_path = filedialog.askopenfilename(
            title="Open File",
            filetypes=(("Text Files", "*.txt"), ("All Files", "*.*"))
        )
        if file_path:
            with open(file_path, "r", encoding="utf-8") as file:
                text_box.delete("1.0", tk.END)
                text_box.insert(tk.END, file.read())
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open file:\n{e}")

def save_file():
    """Save the current text from the textbox into a file."""
    try:
        file_path = filedialog.asksaveasfilename(
            title="Save File",
            defaultextension=".txt",
            filetypes=(("Text Files", "*.txt"), ("All Files", "*.*"))
        )
        if file_path:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(text_box.get("1.0", tk.END))
            messagebox.showinfo("Success", "File saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save file:\n{e}")

# -----------------------------
# Create UI Components
# -----------------------------

# Frame for buttons (bottom of window)
frame_buttons = tk.Frame(root)
frame_buttons.pack(side=tk.BOTTOM, fill=tk.X, pady=10, padx=10)

# Buttons (left and right)
btn_open = tk.Button(frame_buttons, text="Open File", command=open_file, width=15)
btn_open.pack(side=tk.LEFT)

btn_save = tk.Button(frame_buttons, text="Save File", command=save_file, width=15)
btn_save.pack(side=tk.RIGHT)

# Frame for text area (center)
frame_text = tk.Frame(root)
frame_text.pack(expand=True, fill=tk.BOTH, padx=10, pady=(10, 0))  # top padding only

# Text box in the center
text_box = tk.Text(frame_text, wrap=tk.WORD, font=("Arial", 12))
text_box.pack(expand=True, fill=tk.BOTH)

# -----------------------------
# Run the App
# -----------------------------
root.mainloop()

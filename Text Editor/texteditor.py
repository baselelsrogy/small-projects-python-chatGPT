from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    filepath = askopenfilename(title="Select a Text File",filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if filepath:
        with open(filepath, 'r') as file:
            read_file = file.read()
            textbox.delete(1.0, END)
            textbox.insert(END, read_file)
    
    window.title(f'BaselTextEditor {filepath}')
    
def save_file():
    files = [("All Files", "*.*"), ("Python Files", "*.py"), ("Text Files", "*.txt")]
    filepath = asksaveasfilename(defaultextension=files, filetypes=files)
    if filepath:
        with open(filepath, 'w') as file:
            content = textbox.get(1.0, END)
            file.write(content)
    
    window.title(f'BaselTextEditor {filepath}')
    
window = Tk()
window.title("Basel Text Editor")
window.rowconfigure(0, minsize=600)
window.columnconfigure(1, minsize=800)

textbox = Text(window)
frame_btn = Frame(window, relief=RAISED)
open_btn = Button(frame_btn, text="Open File", command=open_file)
save_btn = Button(frame_btn, text="Save File", command=save_file)

open_btn.grid(column=0, row=0, padx=10, pady=5, sticky="ew")
save_btn.grid(column=0, row=1, padx=10, pady=5, sticky="ew")

frame_btn.grid(column=0, row=0, sticky="ns")
textbox.grid(column=1, row=0, sticky="nsew")



mainloop()
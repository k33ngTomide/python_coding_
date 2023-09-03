import tkinter as tk
from tkinter import simpledialog


def custom_multiline_input(title, prompt):
    top = tk.Toplevel(root)
    top.title(title)

    text_widget = tk.Text(top, wrap=tk.WORD, width=40, height=10)
    text_widget.pack()

    def get_input():
        result = text_widget.get("1.0", tk.END)

        return result

    ok_button = tk.Button(top, text="OK", command=get_input)
    ok_button.pack()

    top.wait_window()


root = tk.Tk()
root.title("Custom Multiline Input Example")
root.mainloop()

result = custom_multiline_input("Custom Multiline Input", "Enter multiline text:")

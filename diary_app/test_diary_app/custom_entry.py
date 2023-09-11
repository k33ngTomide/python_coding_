# CUSTOM ENTRY WIDGET
# import tkinter as tk
# from tkinter import simpledialog
#
#
# def custom_multiline_input(title, prompt):
#     top = tk.Toplevel(root)
#     top.title(title)
#
#     text_widget = tk.Text(top, wrap=tk.WORD, width=40, height=10)
#     text_widget.pack()
#
#     def get_input():
#         result = text_widget.get("1.0", tk.END)
#
#         return result
#
#     ok_button = tk.Button(top, text="OK", command=get_input)
#     ok_button.pack()
#
#     top.wait_window()
#
#
# root = tk.Tk()
# root.title("Custom Multiline Input Example")
# root.mainloop()
#
# another_result = custom_multiline_input("Custom Multiline Input", "Enter multiline text:")

# ENTRY WIDGET SAMPLE CODE
# import tkinter as tk
#
#
# def on_button_click():
#     entered_text = entry.get()
#     label.config(text=f"You entered: {entered_text}")
#
#
# window = tk.Tk()
# window.title("Entry Widget Example")
#
# entry = tk.Entry(window, width= 100, )
# entry.pack()
#
# button = tk.Button(window, text="Submit", command=on_button_click)
# button.pack()
#
# label = tk.Label(window, text="")
# label.pack()
#
# window.mainloop()

import tkinter as tk

window = tk.Tk()
window.title("Text Widget Example")

text_widget = tk.Text(window, width=60, height=15, borderwidth=6)
text_widget.pack()


def on_button_click():
    text_content = text_widget.get("1.0", "end-1c")
    result_label.config(text=f"You entered:\n{text_content}")


submit_button = tk.Button(window, text="Submit", command=on_button_click)
submit_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()

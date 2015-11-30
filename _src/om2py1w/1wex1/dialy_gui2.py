# coding=utf-8
#exercise for Tkinter

import Tkinter as tk
from dialy import *

root = tk.Tk()
tk.Label(root, text="Hello world").pack()

var = tk.StringVar(value="Hi, please enter here:")

text_input = tk.Entry(root, textvar=var)
text_input.pack()

def update_text():
	append_text(var.get())
	text_output.config(text=get_text())
	var.set('')

tk.Button(root, text="print", command=update_text).pack()
root.bind('<Return>', lambda event:update_text())

text_output = tk.Message(root,text='')
text_output.pack()

root.mainloop()

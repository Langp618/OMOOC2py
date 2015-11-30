# coding=utf-8
#exercise for Tkinter
#adjust GUI base on gui2

import Tkinter as tk
from dialy import *

root = tk.Tk()
root.title("Lang's diary")
root.geometry('400x400')
tk.Label(root, text="Welcome!!", pady=20).pack()

var = tk.StringVar(value="Hi, please enter here:")

text_input = tk.Entry(root, textvar=var, width=36)
text_input.pack()

def update_text():
	append_text(var.get())
	text_output.config(text=get_text())
	var.set('')

tk.Button(root, text="print", command=update_text).pack()
root.bind('<Return>', lambda event:update_text())

text_output = tk.Message(root,text='', width=360, pady=20)
#text_output.pack(side=left)
text_output.pack()

root.mainloop()

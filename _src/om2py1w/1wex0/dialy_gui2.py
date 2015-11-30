#exercise for Tkinter

import Tkinter as tk

root = tk.Tk()
tk.Label(root, text="Hello world").pack()

var = tk.StringVar(value="Hi, please enter here:")

text_input = tk.Entry(root, textvar=var)
text_input.pack()

def print_content():
#	text_output.config(text=var.get())
	text_output['text'] = var.get()
	var.set('')

tk.Button(root, text="print", command=print_content).pack()
root.bind('<Return>', lambda event:print_content())

text_output = tk.Message(root,text='')
text_output.pack()

root.mainloop()

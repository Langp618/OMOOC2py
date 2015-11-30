import Tkinter as tk

root = tk.Tk()
tk.Label(root, text="Hello world").pack()
#tk.label(root, text="Hello World!").pack(side="left")
# error in upper code
#message = tk.Entry(root)
#message.insert(0, "Hi, Please enter here:")

var = tk.StringVar(value="Hi, please enter here:")

#message = tk.Entry(root,textvariable=var)
#message.pack()

text_input = tk.Entry(root, textvar=var)
text_input.pack()

def print_content():
	print var.get()
	var.set('')
	#message.delete(0,'end') #delete orgin input

#tk.Button(root, text="print", command=print_content).pack()
tk.Button()
root.bind('<Return>', lambda event:print_content())

text_output = tk.Message(root,textvar=var)
text_output.pack()

root.mainloop()

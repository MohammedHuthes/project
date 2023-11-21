from tkinter import *
from tkinter import ttk
#from tkinter import messagebox
import tkinter as tk
import os

root = Tk()
root.geometry("700x500")
root.title("Student Record")


tab_item = ttk.Notebook (root)

tab1 = ttk.Frame(tab_item)
tab_item.add(tab1, text="Add marks")
tab_item.pack(expand = 1, fill= "both")

tab2 = ttk.Frame(tab_item)
tab_item.add(tab2, text="Show Marks")
tab_item.pack(expand = 1, fill= "both")

tab3 = ttk.Frame(tab_item)
tab_item.add(tab3, text="About")
tab_item.pack(expand= 1, fill= "both")



text_widget = tk.Text(tab2)

def open_file():
	file_path = os.path.abspath(os.getcwd()) + "user.txt"
	with open("user.txt", "r") as f:
		text_widget.delete("1.0", tk.END)
		text_widget.insert("1.0",f.read())


heading = Label(tab2, text = "Records",font = ("calibri", 13))
heading.pack()


open_file_button = tk.Button(tab2, text="Show", command=open_file)
text_widget.pack()
open_file_button.pack()

def my_reset():
	for widget in tab1.winfo_children(): 
		if isinstance(widget,Entry): 
			widget.delete(0, 'end')
user = []
def save_info():
	name_info = name.get() 
	sid_info = sid.get()
	sid_info = str(sid_info)

	module_name_info = module_name.get()
	module_grade_info = module_grade.get()
	print(name_info, sid_info, module_name_info, module_grade_info)

	file = open("user.txt", "a")
	file.write(f"Name: {name_info} ID: {sid_info} Module Name: {module_name_info} Module Grade: {module_grade_info}\n")
	print(" Dear", name_info," You're Successfully Submitted...............")


name = StringVar()
sid = IntVar()
module_name = StringVar()
module_grade = StringVar()

name_text = Label(tab1,text = "Student Name :",)
name_text.pack()

name_entry = Entry(tab1,textvariable = name)
name_entry.pack()
sid_text = Label(tab1,text = "Student ID: ",)
sid_text.pack()

sid_entry = Entry(tab1,textvariable = sid) 
sid_entry.pack()
module_name_text = Label(tab1,text = "Module Name: ",)
module_name_text.pack() 

module_name_entry = Entry (tab1,textvariable = module_name)
module_name_entry.pack()

module_grade_text = Label(tab1,text = "Module Grade: ",)
module_grade_text.pack()

module_grade_entry = Entry(tab1,textvariable = module_grade) 
module_grade_entry.pack()

enter = Button(tab1, text = "Submitt", command = save_info)
enter.pack()
reset = Button(tab1, text = "Reset", command = lambda: my_reset())
reset.pack()


about = Label(tab3,
	text="\n huthes@gmail.com \n Developer:Huthes. Batch: CSD-18",
	font="arial 20 bold", justify="center")
about.pack()



root.mainloop()
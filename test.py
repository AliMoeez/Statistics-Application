from tkinter import *
task_list=["Call","Work","Help"]
root=Tk()
Label(root,text="My Tasks").grid(row=0,column=0)
placement=3
for tasks in task_list:
    Checkbutton(root,text=str(tasks)).grid(row=placement,column=0,sticky="w")
    placement+=3
root.mainloop()
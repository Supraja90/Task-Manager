from tkinter import *
from tkinter import messagebox
from tkinter import ttk
root=Tk()
root.geometry("600x500")
root.configure(background="light blue")
root.title("Task manager")
l1=Label(root,text='Welcome to Task manager!!')
l1.configure(foreground="black",font=('Helvetica bold',25))

list1=[]
#error
def inputerror() :
    if e1.get() == "" :
         messagebox.showwarning("warning", "Please enter some task.")
         return 0
    return 1
#logo
bg = PhotoImage(file = "tick2.png")
l=Label(image=bg)
l.grid(row=0,column=0)

#exit
menu_bar=Menu(root)
fileMenu=Menu(menu_bar,tearoff=0)
fileMenu.add_command(label="EXIT", command=root.destroy)
menu_bar.add_cascade(label="File",menu=fileMenu)
root.config(menu=menu_bar)
counter=1

#enter the text
e1=Entry(root)
def enter_msg():
    global counter
    value = inputerror()
    if value == 0:
        return
    c=e1.get()+'\n'
    list1.append(c)
    tarea.insert('end -1 chars',"["+str(counter)+"]"+c)
    counter+=1
    clear_taskField() 
#delete the text
def clear_taskNumberField() :
    taskNumberField.delete(0.0, END)
def clear_taskField() :
    e1.delete(0, END)
def delete_msg():
    global counter
    if len(list1) == 0 :
        messagebox.showwarning("warning","No task")
        return
    number = taskNumberField.get(1.0, END)
    if number == "\n" :
        messagebox.showwarning("warning","input error")
        return
    else:
        task_no = int(number)
    clear_taskNumberField()
    list1.pop(task_no - 1)
    counter -= 1
    tarea.delete(1.0, END)
    for i in range(len(list1)) :
        tarea.insert('end -1 chars', "[ " + str(i + 1) + " ] " + list1[i])
    
b1=Button(root,text='Enter',command=enter_msg,font=('times 10'),pady=5)
b1.configure(background="yellow",foreground="black")
taskNumber = Label(root, text = "Delete Task Number", bg = "lightblue",font=('Helvetica bold',15))
taskNumberField = Text(root, height = 1, width = 2, font = "lucida 13")

tarea=Text(root,height=10,width=50,font="lucida 13")
scrollbar = ttk.Scrollbar(root, orient='vertical', command=tarea.yview)
scrollbar.grid(row=3, column=3, sticky='ns',ipadx=0,pady=0)
tarea['yscrollcommand'] = scrollbar.set

delete_msg=Button(root,text="Delete",command=delete_msg)
delete_msg.configure(background="red",foreground="black")
l1.grid(row = 0, column = 2)			
e1.grid(row = 1, column = 2, ipadx = 75,ipady=8,pady=10)
b1.grid(row = 2, column = 2)
tarea.grid(row = 3, column = 2, padx = 10, sticky = W,pady=10)
						
taskNumber.grid(row = 4, column = 2, pady = 5)
						
taskNumberField.grid(row = 5, column = 2)

delete_msg.grid(row = 10, column = 2, pady = 5)
						

root.mainloop()
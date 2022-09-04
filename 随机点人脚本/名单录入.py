import tkinter as tk
import os

# 写入名单


def writein():
    path = os.getcwd()
    name = enter1.get()
    sex = enter2.get()
    id = enter3.get() + os.linesep
    with open(path + "\\名单.txt", 'a') as f:
        f.write(name + ',' + sex + ',' + id)
    enter1.delete(0, tk.END)
    enter2.delete(0, tk.END)
    enter3.delete(0, tk.END)


root = tk.Tk()
root.title('名单录入')

label1 = tk.Label(root, text="姓名:")
label2 = tk.Label(root, text="性别:")
label3 = tk.Label(root, text="学号:")
label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
label3.grid(row=2, column=0)

enter1 = tk.Entry(root)
enter2 = tk.Entry(root)
enter3 = tk.Entry(root)
enter1.grid(row=0, column=1)
enter2.grid(row=1, column=1)
enter3.grid(row=2, column=1)

button = tk.Button(root, text="录入", command=writein)
button.grid(row=3, column=0)

root.mainloop()

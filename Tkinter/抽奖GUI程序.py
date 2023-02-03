import random
import tkinter as tk


def solve():
    # 初始化
    IDs = []
    # 数据处理
    IDs = list(List1.get(0, tk.END))
    random.shuffle(IDs)  # 随机打乱列表
    # 结果输出
    List2.insert(tk.END, IDs[0])


def submit():
    List1.insert(tk.END, Enter.get())
    Enter.delete(0, tk.END)


# GUI界面编写
root = tk.Tk()
root.title("抽奖程序")

tk.Label(root, text="输入id:").grid(row=0, column=0, padx=10, pady=10)

Enter = tk.Entry(root)
Enter.grid(row=0, column=1, padx=10, pady=10)

List1 = tk.Listbox(root, setgrid=True, height=15)
List1.grid(row=1, column=0)
List2 = tk.Listbox(root, setgrid=True, height=1)
List2.grid(row=1, column=3)

tk.Button(root, text="提交", width=10, command=submit).grid(
    row=0, column=2, padx=10, pady=5)
tk.Button(root, text="抽取", width=10, command=solve).grid(
    row=0, column=3, padx=10, pady=5)
tk.Button(root, text="删除", width=10, command=lambda x=List1: x.delete(
    tk.ACTIVE)).grid(row=1, column=1, sticky=tk.NW, padx=10, pady=5)

# 主事件循环
root.mainloop()

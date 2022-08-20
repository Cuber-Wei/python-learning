import tkinter as tk
import random


def solve():
    # 初始化初始存储
    PlayerName = []
    PlayerID = []
    # 初始化结果存储
    Playername = []
    Playerid = []
    # 处理每一项，存入相应列表中
    for each in Label2.get(0, tk.END):
        PlayerID.append(each.split(",")[1])
        PlayerName.append(each.split(",")[0])
    # 中间处理过程：生成随机数，从相应数组中弹出相应的项，同时存储至结果列表
    k = len(PlayerID)
    while k > 0:
        ran = random.randint(0, k - 1)  # 随机数生成
        Playername.append(PlayerName[ran])
        PlayerName.pop(ran)
        Playerid.append(PlayerID[ran])
        PlayerID.pop(ran)
        k -= 1
    # 输出
    i = 0
    while i < len(Playerid) - 1:
        k = (i // 2) + 1  # 组数
        Label3.insert(tk.END, "第{}组:".format(
            k) + Playerid[i] + "," + Playername[i] + "   " + Playerid[i + 1] + "," + Playername[i + 1])
        i += 2
    if len(Playerid) % 2 != 0:
        Label3.insert(tk.END, Playerid[len(
            Playerid) - 1] + "," + Playername[len(Playername) - 1] + "轮空了")  # 剩余项处理（轮空）


def submit():
    Label2.insert(tk.END, Enter.get())
    Enter.delete(0, tk.END)


# GUI界面编写
root = tk.Tk()
root.title("比赛组队程序")

tk.Label(root, text="输入玩家昵称和id,其间用逗号(英文)分隔:").grid(row=0, column=0)

tk.Button(root, text="提交", width=10, command=submit).grid(
    row=0, column=2, padx=10, pady=5)
tk.Button(root, text="组队", width=10, command=solve).grid(
    row=0, column=3, padx=10, pady=5)

Label2 = tk.Listbox(root, setgrid=True)
Label2.grid(row=1, column=0, padx=10, pady=10)

tk.Button(root, text="删除", width=10, command=lambda x=Label2: x.delete(
    tk.ACTIVE)).grid(row=1, column=1, sticky=tk.NW, padx=10, pady=5)

Label3 = tk.Listbox(root, setgrid=True, width=50)
Label3.grid(row=1, column=3, padx=10, pady=10)

Enter = tk.Entry(root)
Enter.grid(row=0, column=1)
# 主事件循环
root.mainloop()

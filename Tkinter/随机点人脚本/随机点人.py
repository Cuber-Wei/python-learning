import random
import os
import tkinter as tk
import re

# 男女生分组


def list_sort(para):
    name, sex, id = para
    for j in range(0, len(name) - 1):
        i = 0
        while i < len(name) - 1:
            if sex[i] == '男' and sex[i + 1] == '女':
                name[i], name[i + 1] = name[i + 1], name[i]
                sex[i], sex[i + 1] = sex[i + 1], sex[i]
                id[i], id[i + 1] = id[i + 1], id[i]
            i += 1
    return (name, sex, id)
# 读取白名单


def white_list_read():
    path = os.getcwd()
    p = re.compile('[0-9]{1,9}')
    white_name = []
    white_id = []
    white_sex = []
    s = ''
    with open(path + "\\白名单.txt", "r") as f:
        for eachline in f:
            if eachline != '\n':
                white_name.append(eachline.split(',')[0])
                white_sex.append(eachline.split(',')[1])
                white_id.append(p.findall(eachline.split(',')[2])[0])
    return (white_name, white_sex, white_id)

# 读取名单


def list_read():
    path = os.getcwd()
    p = re.compile('[0-9]{1,9}')
    name = []
    id = []
    sex = []
    with open(path + "\\名单.txt", "r") as f:
        for eachline in f:
            if eachline != '\n':
                name.append(eachline.split(',')[0])
                sex.append(eachline.split(',')[1])
                id.append(p.findall(eachline.split(',')[2])[0])
    return (name, sex, id)

# 写入白名单


def white_writein(para):
    path = os.getcwd()
    name, sex, id = para
    with open(path + '\\白名单.txt', 'a') as f:
        f.write(name + ',' + sex + ',' + id + os.linesep)

# 主函数(bushi)


def solve():
    # 获取人数,计算男女生人数
    num = int(enter1.get())
    if num * 2 / 7 == num * 2 // 7:
        female_num = int(num * 2 / 7)
    else:
        female_num = int(num * 2 / 7) + 1
    male_num = num - female_num

    # 读取白名单和名单,生成抽取范围
    whitename, whitesex, whiteid = white_list_read()
    name, sex, id = list_read()
    if num > len(name):
        listbox.insert(tk.END, '全部抽取完成,请清空白名单!')
    l = whitename[:]
    i = 0
    if l != []:
        while i < len(l):
            name.remove(whitename[i])
            sex.remove(whitesex[i])
            id.remove(whiteid[i])
            i += 1
    # 列表整理
    name, sex, id = list_sort((name, sex, id))
    pos = 0  # 男女分割线,最终指向第一个男生
    for each in sex:
        if each == '女':
            pos += 1
    # 随机抽取
    i = 0
    ran = 0
    while i < female_num:
        try:
            if pos > 1:
                ran = random.randint(0, pos - 1)
            else:
                ran = 0
            print(ran)
            ran = random.randint(0, pos - i - 1)
            result_name = name[ran]
            result_sex = sex[ran]
            result_id = id[ran]
            white_writein((result_name, result_sex, result_id))
            listbox.insert(tk.END, result_name + ',' +
                           result_sex + ',' + result_id)
            m = 0
            p = 0
            while m < len(name):
                if name[m] == result_name:
                    p = m
                m += 1
            name.remove(result_name)
            sex.pop(p)
            id.remove(result_id)
        except:
            print(name)
            listbox.insert(tk.END, '全部抽取完成,请清空白名单!')
        i += 1
    i = 0
    ran = 0
    start = pos - female_num
    while i < male_num:
        try:
            if len(name) > 1:
                ran = random.randint(start, len(name) - 1)
            else:
                ran = 0
            print(ran)
            result_name = name[ran]
            result_sex = sex[ran]
            result_id = id[ran]
            white_writein((result_name, result_sex, result_id))
            listbox.insert(tk.END, result_name + ',' +
                           result_sex + ',' + result_id)
            m = 0
            p = 0
            while m < len(name):
                if name[m] == result_name:
                    p = m
                m += 1
            name.remove(result_name)
            sex.pop(p)
            id.remove(result_id)
        except:
            print(name)
            listbox.insert(tk.END, '全部抽取完成,请清空白名单!')
        i += 1


root = tk.Tk()
root.title("随机点人")

label1 = tk.Label(root, text="抽取人数:")
label1.grid(row=0, column=0)
label2 = tk.Label(root, text='抽取结果')
label2.grid(row=0, column=2)

enter1 = tk.Entry(root)
enter1.grid(row=0, column=1)

listbox = tk.Listbox(root, height=10, width=30)
listbox.grid(row=1, column=2)

button = tk.Button(root, text="抽取", command=solve, width=6, height=3)
button.grid(row=1, column=0)

root.mainloop()

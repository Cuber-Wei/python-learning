import re
from math import *
import tkinter as tk


def fact(num):  # 重写阶乘函数
    i = 1
    result = 1
    while i <= num:
        result = result * i
        i += 1
    return result


def Multi(a, b):  # 幂次函数翻译
    try:
        result = a ** b
    except:
        print('求幂函数出错了!')
    return result
# 函数参数格式转换


def turn_to_float(par: list):
    result = []
    for each in par:
        result.append(float(each))
    return result

# paren_pos函数
# 先搜索后括号，再搜索对应的前括号
# 记录前后括号的位置，形成区间，此区间内的表达式先行计算


def paren_pos(group: list):
    pos = []  # 括号位置组列表
    Llist = []  # 历史前括号位置
    R, L, i, j = [0] * 4
    for each in group:
        if each == ')':  # 检测到后括号
            R = i  # 记录后括号位置
            while j < i:  # 扫描前区间
                if group[j] == '(' and j not in Llist:  # 检测到与当前后括号对应的前括号
                    L = j  # 记录前括号位置
                j += 1  # 后推指针
            Llist.append(L)  # 记录历史前括号位置，避免重复匹配
            pos.append((L, R))  # 打包：一组对应的前后括号
        i += 1  # 后推指针
        j = 0  # 重置扫描初始点
    if pos == []:
        return (0, 0)
    else:
        return pos[0]
# 获取括号内的参数集


def getpar(pos: tuple, para: list, cutlist: list):
    posL = 0
    posR = len(para)
    beforeL = cutlist[:pos[0]]
    behindR = cutlist[pos[1]:]

    for each in beforeL:
        if each not in ['(', ')', '+', '-', '*', '/']:
            posL += 1
    for each in behindR:
        if each not in ['(', ')', '+', '-', '*', '/']:
            posR -= 1
    return para[posL:posR]
# 四则运算符号位置获取


def getpos(group: list):
    pos = []
    i = 0
    for each in group:
        if each in ['+', '-', '*', '/']:
            pos.append((i, each))
        i += 1
    return pos
# 获取区间内四则运算符的相对位置


def get_calc(pos: tuple, cutlist: list):
    interval = cutlist[pos[0] + 1: pos[1]]
    p = []
    i = 0
    for each in interval:
        if each in ['+', '-', '*', '/']:
            p.append((i, each))
        i += 1
    return p


# calc函数
# 计算各区间的函数值


def calc(par):
    result = []
    for each in par:
        if each[1][0] == "NONE":
            result.append("NONE")
        elif each[0] == 'NUM':
            result.append(each[1][0])
        else:
            result.append(each[0](*each[1]))
    return result
# 更新数据集


def update_cutlist(pos: tuple, cutlist: list, result):
    left = pos[0]
    right = pos[1]
    cutlist = cutlist[:left] + [str(result)] + cutlist[right + 1:]
    return cutlist
# 更新参数集


def update_para(cutlist: list):
    cutstring = ''
    for each in cutlist:
        cutstring = cutstring + each
    return exact_par(cutstring)
# single_calc()函数：从右往左扫描两次，第一次计算乘除，第二次加减


def single_calc(data: list, symbol: list):
    i = 0
    symbol.append((0, 0))
    sestence = []
    while i < len(data):
        if symbol != []:
            sestence.append(data[i])
            sestence.append(symbol[i][1])
        i += 1
    sestence = sestence[:len(sestence) - 1]
    i = 0
    while i < len(sestence):
        if sestence[i] == '*':
            sestence = sestence[:i - 1] + [sestence[i - 1]
                                           * sestence[i + 1]] + sestence[i + 2:]
            i -= 1
        elif sestence[i] == '/':
            try:
                sestence = sestence[:i - 1] + [sestence[i -
                                                        1] / sestence[i + 1]] + sestence[i + 2:]
                i -= 1
            except:
                print('除数为零!')
                i += 1
        i += 1
    i = 0
    while i < len(sestence):
        if sestence[i] == '+':
            sestence = sestence[:i - 1] + [sestence[i -
                                                    1] + sestence[i + 1]] + sestence[i + 2:]
            i -= 1
        elif sestence[i] == '-':
            sestence = sestence[:i - 1] + [sestence[i -
                                                    1] - sestence[i + 1]] + sestence[i + 2:]
            i -= 1
        i += 1
    if len(data) == 1:
        sestence = [data[0]]
    return sestence[0]
# cut函数
# 分割原字符串


def cut(String: str):
    # 字符串空格处理
    i = 0
    for each in String:
        if each in ['(', ')', '+', '-', '*', '/']:  # 遇上分割符号
            if String[i - 1:i] != ' ' and String[i + 1:i + 2] != ' ':  # 前后均无空格
                String = String[:i] + ' ' + each + ' ' + String[i + 1:]
                i += 2
            elif String[i + 1:i + 2] != ' ':  # 后无空格
                String = String[:i] + each + ' ' + String[i + 1:]
                i += 1
            else:
                String = String[:i] + ' ' + each + ' ' + String[i + 1:]  # 前无空格
                i += 2
        i += 1
    return list(filter(None, String.split(' ')))
# 提取函数及其参数并打包


def exact_par(String: str):
    par = []  # par 存储各分解需计算的结构
    par_num = []  # par_num 函数参数打包
    func = []  # func 函数提取暂存
    par_package = []  # par_package 函数及其参数打包

    func_re = re.compile(r"[a-z]{1,10}")  # 匹配纯英文函数名
    num_re = re.compile(r'[0-9]+[.]?[0-9]*')  # 匹配数字
    par = list(filter(lambda x: x not in [
        '(', ')', '+', '-', '*', '/'], cut(String)))
    for each in par:  # 参数打包
        if each.isalpha():
            par_num.append(tuple(["NONE"]))   # 只有函数名，意为后面为其参数且参数有小括号隔离运算
        else:
            par_num.append(tuple(turn_to_float(num_re.findall(each))))
    for each in par:
        if '!' in each:  # 阶乘
            func.append(fact)
        elif '^' in each:  # 幂次
            func.append(Multi)
        else:
            # 纯数字或纯函数名或含数字参数的函数表达式
            if num_re.findall(each) != [] or func_re.findall(each) != []:
                if func_re.findall(each) != [] and func_re.findall(each)[0] == each:  # 纯函数名
                    func.append(eval(each))
                elif num_re.findall(each) != [] and num_re.findall(each)[0] == each:  # 纯数字
                    func.append("NUM")  # 占位符，表示纯数字参数
                else:  # 带参数的函数名
                    func.append(eval(func_re.findall(each)[0]))
    i = 0
    while i < len(func):  # 函数名打包
        par_package.append((func[i], par_num[i]))
        i += 1
#    print(par_package)
    return par_package  # 返回打包数据集


# 主计算函数
def solve():
    test = Enter.get()
#test = "(sin(3.9865)) +(4!-4^(3*7))*90.6"
    para = exact_par(test)  # 提取函数及参数
    cut_list = cut(test)  # 分割
    pare_pos = paren_pos(cut_list)  # 括号位置获取
    par = getpar(pare_pos, para, cut_list)  # 括号内的参数获取
    data = calc(par)  # 括号内各部分计算结果数据集
    pos = get_calc(pare_pos, cut_list)  # 获取括号内四则运算符的位置
    while pare_pos != (0, 0):
        cut_list = update_cutlist(pare_pos, cut_list, single_calc(data, pos))
        para = update_para(cut_list)
        pare_pos = paren_pos(cut_list)  # 括号位置获取
        par = getpar(pare_pos, para, cut_list)  # 括号内的参数获取
        data = calc(par)  # 括号内各部分计算结果数据集
        pos = get_calc(pare_pos, cut_list)  # 获取括号内四则运算符的位置
    i = 0
    for each in cut_list:
        if each not in ['+', '-', '*', '/']:
            data.append(float(each))
        else:
            pos.append((i, each))
        i += 1
#print(single_calc(data, pos))
    Label.insert(tk.END, str(single_calc(data, pos)))


# GUI编写
root = tk.Tk()
root.title("字符串数学表达式计算")

tk.Label(root, text='输入表达式:').grid(row=0, column=0)
tk.Button(root, text='计算', width=10, command=solve).grid(
    row=0, column=2, padx=10, pady=10)
Enter = tk.Entry(root, width=100)
Enter.grid(row=0, column=1)
Label = tk.Listbox(root, setgrid=True, width=100)
Label.grid(row=1, column=1, padx=10, pady=10)

root.mainloop()

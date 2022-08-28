import tkinter
import tkinter.messagebox
import random

# 暂停线程


def stop():
    global root
    score = 0
    for each in body:
        if each != -1:
            score += 1
    tkinter.messagebox.showinfo("提示",  "游戏结束,您的得分是" + str(score))
    root.wait_variable(pause_var)
    root.quit()


"""随机生成食物"""


def getfood():
    notfoodindex = []
    foodindex = []
    for i in range(100):
        if body[i] != -1:
            notfoodindex = notfoodindex + [body[i]]
    for i in range(100):
        if i not in notfoodindex:
            foodindex = foodindex + [i]
    return foodindex[random.randrange(0, len(foodindex))]


"""蛇移动的函数代码"""


def move():
    global head, oldhead, last, direction, food
    last = -1

    """方向，寻找下一个头的位置"""
    if direction == "right":
        head += 1
        if head // 10 == head / 10:
            head -= 10
    elif direction == "left":
        head -= 1
        if head == -1 or head % 10 == 9:
            head += 10
    elif direction == "up":
        head -= 10
        if head < 0:
            head += 100
    elif direction == "down":
        head += 10
        if head > 99:
            head -= 100

    """身体移动"""
    if head != food:  # 没吃到食物
        if head in [x for x in body]:
            stop()
        for i in range(99, 0, -1):  # 后面的身体向前移
            if body[i] != -1 and last == -1:
                last = body[i]
                body[i] = body[i - 1]
            elif last != -1:
                body[i] = body[i - 1]
        lattice[last]["bg"] = "black"
    else:  # 吃到食物
        for i in range(99, 0, -1):
            body[i] = body[i - 1]
        food = getfood()

    body[0] = head

    lattice[food]["bg"] = "yellow"
    lattice[head]["bg"] = "red"
    lattice[oldhead]["bg"] = "green"
    oldhead = head

    root.after(100, move)


"""窗体"""
root = tkinter.Tk()
root.title("贪吃蛇")

pause_var = tkinter.StringVar()

"""方向 上下左右,用direction变量记录"""
direction = "right"
"""改变方向的函数,其实可以一起写,用keycode,不过4个按键也不多,也可以用class封装一下"""


def left(event):
    global direction
    direction = "left"


def right(event):
    global direction
    direction = "right"


def up(event):
    global direction
    direction = "up"


def down(event):
    global direction
    direction = "down"


"""键盘输入事件添加"""
root.bind("<KeyPress-a>", left)  # 左
root.bind("<KeyPress-d>", right)  # 右
root.bind("<KeyPress-w>", up)  # 上
root.bind("<KeyPress-s>", down)  # 下
root.bind("<Enter>", lambda x: pause_var.set(1))  # 回车键解除暂停状态

"""网格生成"""
lattice = [tkinter.Label(width=5, height=2, bg="black",
                         relief="solid", borderwidth=2) for i in range(100)]
for i in range(0, 100):
    lattice[i].grid(row=i // 10, column=i % 10)
"""初始生成一条大蟒蛇python"""
last = -1
lattice[40]["bg"] = "green"
lattice[41]["bg"] = "green"
lattice[42]["bg"] = "green"
lattice[43]["bg"] = "red"
"""蛇的身体位置存入body中"""
body = [-1]*100
head = 43
oldhead = 43
body[0] = 43
body[1] = 42
body[2] = 41
body[3] = 40
food = getfood()  # 第一个食物的位置
root.after(500, move)


root.mainloop()

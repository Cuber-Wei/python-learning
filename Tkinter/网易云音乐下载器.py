import re
import os
import time
import tkinter as tk
import requests

PATH = os.getcwd()


def getMessage():
    pass


def getMusic(path, music_id, music_name):
    url = f"http://music.163.com/song/media/outer/url?id={music_id}.mp3"
    mp3 = requests.get(url).content
    path += '\\' + music_name + ".mp3"
    with open(path, "wb") as file:
        file.write(mp3)


def handleMsg():
    # 创建文件夹
    path = PATH + r"\download"
    try:
        os.mkdir(path)
    except:
        pass
    # 获取相关信息
    msg = Enter1.get()
    nAme = Enter2.get()

    Enter1.delete(0, tk.END)
    Enter2.delete(0, tk.END)
    id_match = re.compile(r"id=[0-9]{3,15}")
    id = id_match.findall(msg)[0][3:]
    name = re.findall('《(.*)》', msg)
    name = nAme if nAme != '' else name[0] if name != [] else id

    # 爬取
    getMusic(path, int(id), name)
    # 日志
    t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    logMsg = f"[{t}] id={id}, name={name}\n"
    with open(PATH + r"\log.txt", "a") as f:
        f.write(logMsg)
    print(logMsg)
    time.sleep(2)


# GUI界面编写
root = tk.Tk()
root.title("网易云音乐下载器(试听歌曲无法下载)")

tk.Label(root, text="输入分享链接:").grid(row=0, column=0, padx=10, pady=10)
tk.Label(root, text="输入保存文件名\n(可以为空,通过链接解析):").grid(
    row=1, column=0, padx=10, pady=10)

Enter1 = tk.Entry(root, width=50)
Enter1.grid(row=0, column=1, padx=10, pady=10)

Enter2 = tk.Entry(root, width=50)
Enter2.grid(row=1, column=1, padx=10, pady=10)

tk.Button(root, text="提交", width=10, command=handleMsg).grid(
    row=0, column=2, padx=10, pady=5)

# 主事件循环
root.mainloop()

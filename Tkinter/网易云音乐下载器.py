import re
import os
import time
import requests
import tkinter as tk

PATH = os.getcwd()


def getMusic(path, music_id, music_name):
    """
    爬取网易云音乐的函数
    param path: 文件保存的路径
    param music_id: 音乐id
    param music_name: 音乐名称
    return: None
    """
    url = f"http://music.163.com/song/media/outer/url?id={music_id}.mp3"
    res = requests.get(url)
    if res.status_code == 200:
        mp3 = res.content
        path += f'/{music_name}.mp3'
        with open(path, "wb") as file:
            file.write(mp3)
    else:
        List1.insert(tk.END, f"访问出错,错误码:{res.status_code}")
        print(f"访问出错,错误码:{res.status_code}\n")


def handleMsg():
    """
    处理数据的函数
    param: None
    return: None
    """
    # 创建文件夹
    path = PATH + r"\download"
    try:
        os.mkdir(path)
    except:
        pass
    # 获取相关信息及输入窗口的恢复
    msg = Enter1.get()
    nAme = Enter2.get()

    Enter1.delete(0, tk.END)
    Enter2.delete(0, tk.END)
    List1.delete(tk.END)

    id = re.findall(r"id=[0-9]{3,15}", msg)
    name = re.findall('《(.*)》', msg)
    # 错误处理
    if id == []:
        List1.insert(tk.END, "链接id解析出错,请检查格式!")
        print("链接id解析出错,请检查格式!\n")
    else:
        id = id[0][3:]
        name = nAme if nAme != '' else name[0] if name != [] else id
        # 爬取
        getMusic(path, int(id), name)
        # 日志
        t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        logMsg = f"[{t}] id={id}, name={name}\n"
        with open(PATH + r"\log.txt", "a") as f:
            f.write(logMsg)
        List1.insert(tk.END, logMsg[:-1])
        print(logMsg)


# GUI界面编写
root = tk.Tk()
root.title("网易云音乐下载器(试听歌曲无法下载)")

tk.Label(root, text="输入分享链接:").grid(row=0, column=0, padx=10, pady=10)
tk.Label(root, text="输入保存文件名\n(可以为空,通过链接解析):").grid(
    row=1, column=0, padx=10, pady=10)
tk.Label(root, text="状态:").grid(row=2, column=0, padx=10, pady=10)

Enter1 = tk.Entry(root, width=50)
Enter1.grid(row=0, column=1, padx=10, pady=10)

Enter2 = tk.Entry(root, width=50)
Enter2.grid(row=1, column=1, padx=10, pady=10)

tk.Button(root, text="下载", width=10, command=handleMsg).grid(
    row=0, column=2, padx=10, pady=5)

List1 = tk.Listbox(root, setgrid=True, height=1, width=50)
List1.grid(row=2, column=1)

root.mainloop()

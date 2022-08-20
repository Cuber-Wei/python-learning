import random

#初始化初始存储
PlayerName = []
PlayerID = []
#初始化结果存储
Playername = []
Playerid = []
#输入
OrignString = input("输入各玩家昵称和ID(名称与ID,不同玩家间用逗号隔开[均为英文半角]):\n")
'''char = ""    #初始化

for each in OrignString:
    if each == ",":
        PlayerName.append(char)
        char = ""
    elif each == ";":
        PlayerID.append(char)
        char = ""
    else:
        char = char + each
    #补全最末的内容，防止内容残缺
if len(PlayerID) < len(PlayerName):
    PlayerID.append(char)
elif len(PlayerID) > len(PlayerName):
    PlayerName.append(char)'''
#分割原字符串，存储至相应列表
i = 0

for each in OrignString.split(","):
    i += 1
    if i % 2 == 0:
        PlayerID.append(each)
    else:
        PlayerName.append(each)

#中间处理过程：生成随机数，从相应数组中弹出相应的项，同时存储至结果列表
'random.shuffle(PlayerID)'
k = len(PlayerID)

while k > 0:
    ran = random.randint(0,k - 1)       #随机数生成
    Playername.append(PlayerName[ran])
    PlayerName.pop(ran)
    Playerid.append(PlayerID[ran])
    PlayerID.pop(ran)
    k -= 1

#输出
i = 0
while i < len(Playerid) - 1:
    k = (i // 2) + 1
    print("第{}组:".format(k) + Playerid[i] + "," + Playername[i],end = "\t")
    print(Playerid[i + 1] + "," + Playername[i + 1])
    i += 2
if (Playerid) % 2 != 0:
    print(Playerid[len(Playerid) - 1] + "," + Playername[len(Playername) - 1] + "轮空了")     #剩余项处理（轮空）
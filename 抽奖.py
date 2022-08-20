import random

IDs = []
num = 0

OrigonString = input("输入id:" + "\n")
num = int(input("输入一个数字:"))

for each in OrigonString.split(","):
    IDs.append(each)

#print(IDs)
random.shuffle(IDs)
#print(IDs)
print(IDs[num % len(IDs) - 1 ])
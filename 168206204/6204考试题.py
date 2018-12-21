print('''A：我没有偷钻石。
B：D就是罪犯。
C：B是盗窃这块钻石的罪犯。
D：B有意诬陷我。''')

list=['A','B','C','D']
for i in list:
    if (i!='A')+(i=='D')+(i=='B')+(i!='D')==1:
        print("偷走钻石的犯罪嫌疑人是："+i)

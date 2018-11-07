# 打开文件读取信息并整理 制作个性化信息  找到发信人并匹配人数  发送信息
# 这个py文件的思路是 通过遍历csv文件包含的人来获取发送人的信息同时分析是不是少人 然后发送信息 而给定的发送人信息只是一个参考
#换一个思路   通过遍历给定的发送人信息来 到csv文件中去获取发送的信息并发送 获取不到信息时表示缺少一个需要发送的人的信息 这个思路需要重新设计一个get_msg()函数
 
import os
from wxpy import *
import csv
import time

# 读取文件 注意读取格式
def read_csv(path) :
    file=open(path,'r',encoding='utf-8')  #尽量以只读的形式打开源文件 指定文件的编码格式 一般来说就是gbk 和 utf-8
    reader=csv.DictReader(file)
    return [info for info in reader]



def make_msg(raw_msg) :  #生成要发送的文本
    return ['{微信昵称}，提醒下，{时间}记得来{地址}参加我们的{事件}，{备注}'.format(**msg) for msg in raw_msg ] # {}表示占位符 在format中指定每个占位符所对应的变量

# 找到要发送的和漏发送的人
def find_person(raw_msg,row_names) :
    bot=Bot() # 登陆微信机器人
    friends=[]
    names=[]
    for msg in raw_msg :
        name=msg['微信昵称']
        names.append(name)
        person=bot.search(name)
        if len(person)==1 : # 保证不会给重名的人发送信息
            friends.append(person[0])
        else :
            print('多人符合请重新检索')
    for n in row_names :  # 检测是不是有人漏发了
        if n not in names :
            print('没有%s的发送信息'%(n))
    return friends


# 发送信息
def send_msg(friends,msgs) :
    for i in range(len(msgs)) :
        friends[i].send_msg(msgs[i])
        time.sleep(3)  # 防止发送太频繁被封号


path='./MeetingMsg.csv'
obj=['麻瓜编程君','麻瓜编程OK姐','王总']
raw_msg=read_csv(path)
#for m in raw_msg :
#    print(raw_msg)
msgs=make_msg(raw_msg)
friends=find_person(raw_msg,obj)
send_msg(friends,msgs)
# 思路还是过于接近面向过程的编程,可以考虑增加函数之间的相互调用,似的主函数内代码更加简洁
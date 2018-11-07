#查找第三方库 构造显示器

import os
from tkinter import *
#官方不建议直接使用import pip 而建议调用一个子进程来使用命令行来调用pip的命令
import sys
import subprocess

#获取第三方库list
reqs=subprocess.check_output([sys.executable,'-m','pip','list'])
installed=reqs.decode("utf-8").split("\r\n")

#创建窗口实例
app=Tk() #创建窗口对象

label=Label(text='已安装包')
label.pack()  # 将小部件放置到窗口中
listbox=Listbox()
listbox.pack(fill=BOTH,expand=True)
for l in installed :
    listbox.insert(END,l)

app.mainloop()  # 进入消息循环


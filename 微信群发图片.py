# 找到要发送的人  制作要发送的信息  发送     加上一部分异常处理

import os
import wxpy
import time
#from wxpy import *   #导入wxpy中的所有方法  注意这种写法 与上面写法的区别

#找到要发送的目标
#注意非常重要的一点是 使用 ensure_one()方法 保证我们找到的名字只有一个人 不然肯定会错发信息，一定要注意保证只有一个搜索结果匹配，若有重名则要在search中添加多的筛选条件来确保结果的唯一性
def find_person(names) : 
    bot=wxpy.Bot() #若是采用from import 则这里可以写成 bot=Bot() 此时Bot()方法已经引入 不用通过模块名来调用
    friends=[]
    # 使用异常处理
    for name in names :
        try :
            friend=bot.search(name)
            wxpy.ensure_one(friend)
            friends.append(friend)
        except ValueError :
            print('检索名重复,请重新输入')
        except wxpy.ResponseError as e :
            print(e.err_code,e.err_msg)     
    return friends 

# 找到要发送的文件的位置
def make_msg(path) :
    files=os.listdir(path)
    return [os.path.join(path,file_name) for file_name in files ]

#发送文件
def send(friends,paths) :
    for friend in friends :
        for path in paths :
            # 由于网络不稳定 或者 封号 之类不可预见的外部因素会导致信息无法全部发送完,此时可以通过异常处理的except来记录发送进度,
            try :
                friend[0].send('@img@%s'%(path)) # 注意这里使用search方法返回的是一个Chars对象它是一个列表 不是Char对象无法使用send方法  所以要添加[0]
            except :
                print('发送到')
                print(friend[0].name)
            time.sleep(3)
        
path='./image'
names=['王总','麻瓜编程OK姐']
friends=find_person(names)
msg=make_msg(path)
send(friends,msg)


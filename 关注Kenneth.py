
import requests
import webbrowser
import time

api='https://api.github.com/users/kennethreitz/starred' #一页列出30个最近关注的 网页搜素 github api 找到开发者文档

# 先获得一次starred信息
info=requests.get(api).json() # 将json文档解析成python识别的类型存储
starred=[]
for i in info :
    starred.append(i['id'])

while True :

    info=requests.get(api).json()
    for i in info :
        #如果获取到的有不在项目中的我们就把它添加进入项目然后打开这个项目的网页
       if i['id'] not in starred :
           starred.append(i['id'])
           #获取项目名字
           repo_name=i['name']
           #获取作者名字
           owner=i['owner']['login']
           #打开网页
           web_page='https://github.com/%s/%s'%(owner,repo_name)
           webbrowser.open(web_page)
    time.sleep(60*60)



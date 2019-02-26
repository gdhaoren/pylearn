import urllib.request
import re

# 响应地址
url = 'http://news.baidu.com/'
# 伪装浏览器用户
header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'}
req = urllib.request.Request(url,headers=header)

# 执行请求获取响应对象
res = urllib.request.urlopen(req)

# 从响应对象中读取信息并解码
html= res.read().decode('utf-8')

# 使用正则解析出新闻标题信息
patten = '<a href="(.*?)".*?target="_blank">(.*?)</a>'
dlist = re.findall(patten,html)

# 遍历输出结果
for v in dlist:
    print(v[1]+':'+v[0])

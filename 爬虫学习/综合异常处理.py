from urllib import request,error

url = 'https://edu.csdn.net/sddf'

req = request.Request(url)

try:
    res = request.urlopen(req)
    html = res.read().decode('utf-8')
    print(len(html))

'''
# 多重异常处理
except error.HTTPError as e :# HTTPError是URLError的子类，先于父类处理
    print('HTTPError')
    print(e.reason)# 输出错误原因
    print(e.code)# HTTP状态码
except error.URLError as e :
    print('URLError')
    print(e.reason)# 输出原因
'''

# 通用异常处理
# 不清楚会出什么异常时使用
except Exception as e:
    if hasattr(e,'code'):
        print('HTTPError')
        print(e.reason)# 输出错误原因
        print(e.code)# HTTP状态码
    elif hasattr(e,'reason'):
        print('URLError')
        print(e.reason)# 输出错误原因

print('OK')


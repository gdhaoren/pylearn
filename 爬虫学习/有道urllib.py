# post请求

# 导入使用包
# 分别导入处理请求，错误和格式转换的模块
from urllib import request,error,parse

# 导入json数据处理包
import json


def youdao(keyword):
    # 请求地址
    # url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule' # 这个地址是加密的，有验证字段
    # 有道的加密是在请求参数中添加了两个字段：
    # 'salt': '15512649728343', # 代表时间戳
    # 'sign': 'd265efef59d39460c476c7bc204894d6', # 根据一系列数据进行MD5加密生成
    # 这两个字段是使用js语言自动生成的

    # 使用新的地址
    url = 'https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    # 定义请求参数（post提交的表单参数）
    data = {'i': keyword,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'ts': '1551264972834',
    'bv': '6dfac01e4ee085fbf06475a5a3c2a9c2',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTIME',
    'typoResult': 'false'}

    # 编码转换
    data = parse.urlencode(data)

    # 封装headers, 会带有浏览器访问的信息，用来模拟浏览器访问
    headers = {
    'Content-Length': len(data),
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
    }

    # 封装请求
    # urllib的请求参数要转换为字节
    req = request.Request(url,data=bytes(data,encoding='utf-8'),headers=headers)

    # 发送请求,并保存响应信息
    res = request.urlopen(req)

    # 响应信息解码
    # 回应信息根据浏览器给出的信息，是一个json数据,需要转换成字典格式
    str_js_data = res.read().decode('utf-8')

    # 把json转换成字典格式
    mydata = json.loads(str_js_data)
    # 根据浏览器的reponse响应信息，提取我们需要的数据
    trans = mydata['translateResult'][0][0]['tgt']

    return trans

if __name__ == '__main__':
    while True:
        keyword = input('请输入要翻译的单词: ')
        if keyword == 'q':
            break
        result = youdao(keyword)
        print(f'翻译结果为： {result}\n')


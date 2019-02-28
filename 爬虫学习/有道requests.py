# post 请求
import requests
import json

def youdao(keyword):
	'''使用有道翻译链接翻译字词'''
	url = 'https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

	# post提交的表单参数
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

	# 打包header，用来模拟浏览器访问

	# 封装请求并发送，将响应信息存入res
	res = requests.post(url,data=data)

	# 解析响应数据
	js_data = res.content.decode('utf-8') # 获取响应的json字符串
	# 解析json数据转换为字典格式
	mydata = json.loads(js_data)
	# 提取我们需要的数据
	trans = mydata['translateResult'][0][0]['tgt']

	return trans

if __name__ == '__main__':
	while True:
		keyword = input('请输入要翻译的单词: ')
		if keyword == 'q':
		    break
		result = youdao(keyword)
		print(f'翻译结果为： {result}\n')
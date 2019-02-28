# get方式

# 导入爬取使用的包
import requests
import re

def tc58_qd_huangdao(pIndex):
	# 请求地址
	url = f'https://qd.58.com/huangdao/chuzu/pn{pIndex}'

	# 请求参数
	params = {'ClickID':2}
	
	# 封装请求并发送获取响应
	res = requests.get(url,params=params)

	# 获取解析数据
	html = res.content.decode('utf-8')
	#print(len(html))
	#print(html)

	# 提取目标信息
	# 提取目标链接
	pat = '"(//qd.58.com/.*?/.*?.shtml)" tongji_label'
	urllist = re.findall(pat,html)

	urllist = ['https:'+url for url in urllist]

	return urllist

def url_info_extract(urllist):
	house = []
	# 请求地址
	for url in urllist:
		info = {}
		# 请求信息
		res = requests.get(url)
		# 处理响应
		html = res.content.decode('utf-8')
		# 标题正则
		pat_tit = '<title>\s+(.*?)\s+</title>'
		title = re.findall(pat_tit,html)
		info['title'] = title[0]
		# 提取房源描述
		pat_cont = '<meta name="description" content="(.*?)"/>'
		content = re.findall(pat_cont,html)
		# 提取价格
		pat_p = '(\d+)元'
		price = re.findall(pat_p,content[0])
		info['price'] = float(price[0])
		# 提取户型
		pat_d = '^(.*?)价格'
		des = re.findall(pat_d,content[0])
		info['describe'] = des[0]
		# 提取图片信息
		pat_pic = '<img id="smainPic"\s+src="(.*?)">'
		pic = re.findall(pat_pic,html)
		info['picture'] = 'https:'+pic[0]
		# 存储房屋信息
		house.append(info)
	return house

def main():
	p = input('请输入要获取的页码: ')
	urllist = tc58_qd_huangdao(p)
	house_info = url_info_extract(urllist)
	print(house_info)


if __name__ == '__main__':
	main()

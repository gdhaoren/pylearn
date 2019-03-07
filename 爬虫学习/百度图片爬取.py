# 导包
import requests
from urllib.request import urlretrieve
import time
import os

def getPage(pn):
	'''爬取图片信息'''
	url = f'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E8%A1%97%E6%8B%8D&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word=%E8%A1%97%E6%8B%8D&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn={pn}&rn=30&gsm=1e&1551939593402='
	headers = {
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
		'Referer':'https://image.baidu.com'
	}
	try:
		res = requests.get(url,headers=headers)
		#print(res.url)
		#print(res)
		if res.status_code ==200:
			# 返回json数据
			#print(res.json())
			return res.json(encoding='utf-8')
		else :
			#print(res)
			return None
	except Exception as err:
		print(err)
		return None

def parsePage(json):
	'''解析js数据'''
	data = json['data']
	if data:
		for item in data:
			if item:
				yield{
					'imurl': item['middleURL']
				}
	

def saveImage(item):
	rpath = './baidu_image'
	if not os.path.exists(rpath):
		os.mkdir(rpath)
	# 函数内部仅仅使用全局变量而不做修改则可以不用做声明
	fname = f'{rpath}/{count}.jpg'
	# 存储方案1
	#urlretrieve(item['imurl'],fname)
	# 存储方案2
	# 打开网址的图片字节流
	with requests.get(item['imurl'],stream=True) as ir:
		# 打开文件流
		with open(fname,'wb') as f:
			# 从ir中取数据写入文件中
			for chunk in ir:
				f.write(chunk)

	


def main(pn):
	json = getPage(pn)
	for item in parsePage(json):
		#print(item)
		saveImage(item)
		# 函数内部涉及到对全局变量的修改，要先声明使用的是全局变量避免歧义
		global count
		count+=1

if __name__ == '__main__':
	# 抓取多少页的图片
	npage = 2
	# 先声明全局变量count
	global count
	# 再初始化全局变量
	count = 1
	for i in range(npage):
		pn = i*30
		main(pn)
		time.sleep(1)
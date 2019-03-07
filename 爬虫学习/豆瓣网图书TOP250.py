# 导入包
import requests
import time
from lxml import etree
import json
from bs4 import BeautifulSoup
from pyquery import PyQuery

def getPage(url):
	'''请求网页数据'''
	try:
		# 伪装浏览器
		headers = {
			'User-Agent':'User-Agent:Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
			'Referer':'https://www.baidu.com'
		}
		res = requests.get(url,headers=headers)
		if res.status_code == 200:
			return res.text
		else:
			return None
	except Exception as err:
		print(err)
		return None

def parsePage(content):
	'''解析网页数据'''
	
	# 使用PyQuery解析数据
	doc = PyQuery(content)
	items = doc('table[width="100%"]')
	# 由于返回的并不是直接的列表需要进行转换
	for item in items.items():
		yield{
			'title-cn':item.find('div.pl2 a').text(),
			'title-o':item.find('div.pl2 span').text(),
			'writer':item.find('p.pl').text(),
			'score':item.find('span.rating_nums').text(),
			'comment':item.find('span.inq').text()
		}
	
	'''
	# 使用BeautifulSoup解析数据
	# 使用lxml的方式初始化解析器
	soup = BeautifulSoup(content,'lxml')
	items = soup.find_all(name='table',attrs={'width':'100%'})
	for item in items:
		yield{
			#关于选择出来的数据怎么提取内容有待进一步学习，下面的写法有问题
			'title-cn':item.select('div.pl2 a')[0].get_text(),
			'title-o':item.select('div.pl2 span')[0].string,
			'writer':item.select('p.pl')[0].string,
			'score':item.select('span.rating_nums')[0].string,
			'comment':item.select('span.inq')[0].string
		}
	'''

	'''
	# 使用xml解析数据
	# 初步解析数据
	html = etree.HTML(content)
	# 找到所有width属性为100%的table标签
	items = html.xpath('//table[@width="100%"]')
	# 遍历
	for item in items:
		yield{
			'title-cn':item.xpath('.//div[@class="pl2"]/a/text()')[0],
			# span标签的解析结果不是一个list不需要使用[0]来提取数据
			'title-o':item.xpath('.//div[@class="pl2"]/span/text()'),
			'writer':item.xpath('.//p[@class="pl"]/text()')[0],
			'score':item.xpath('.//span[@class="rating_nums"]/text()'),
			'comment':item.xpath('.//span[@class="inq"]/text()')
		}
	'''

def writeFile(content):
	'''存入文件,追加写'''
	with open('./result.txt','a',encoding='utf-8') as f:
		# 将字典格式（json格式）转换为字符串，又称为序列化，并指定ensrue_ascii=False以保证汉字输出
		#json.dumps 序列化时对中文默认使用的ascii编码.想输出真正的中文需要指定ensure_ascii=False
		f.write(json.dumps(content,ensure_ascii=False)+'\n')

def main(start):
	'''控制爬取过程'''
	url = f'https://book.douban.com/top250?start={start}'
	html = getPage(url)
	for content in parsePage(html):
		#print(content)
		writeFile(content)

if __name__ == '__main__':
	#main(0)
	for i in range(10):
		start = i*25
		main(start)
		time.sleep(1)


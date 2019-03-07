# 导入包
import requests
from pyquery import PyQuery
import json
# str转bytes叫encode，bytes转str叫decode
# 这段代码由于修改标准输出的默认编码，由于python默认字符集缺陷 因此他在输出的时候认不全所有的unicode字符，从而导致编码错误
import sys,io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

def getPage(url):
	'''伪装成添加了购物车信息的浏览器'''
	try:
		# cookie用来维持状态
		headers = {
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'zh-CN,zh;q=0.9',
			'cache-control': 'max-age=0',
			'cookie':'__jdc=122270672; __jdu=1474803109; PCSYCityID=1007; shshshfpa=90c7c4e5-7ec9-4a06-a0e9-022f5a7af825-1551868277; shshshfpb=jDy%20ehJ6xO6S1lUQNUk%2FMVw%3D%3D; unpl=V2_ZzNtbRECSkJxWBJTLxFbDWIGRQ9KUEIUIVpHVHNOCAQzBkZVclRCFX0UR1ZnGFsUZAAZX0NcRxVFCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZHscWgBuAhBdQ19zJXI4dmRzEVsAZAoiXHJWc1chVEZSehBeBSoDF1tHXkIXdQlOZHopXw%3d%3d; __jda=122270672.1474803109.1551868275.1551868276.1551882660.2; __jdv=122270672|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_bd8f5ae6e96944fc9600ec019fe0e4e9|1551882660232; _gcl_au=1.1.2065117534.1551882667; 3AB9D23F7A4B3C9B=TJ5EVEDOX5T27WJVZGXJ4BFUXP5AR3SXJWLMH2BYT6OODUQHK2JK3JEU7UNDURTDIJB4WGK2X3GE2PRGSXGM3GIQHU; user-key=302758ac-1813-47c1-837c-bff1d433bb36; cart-main=xx; cn=5; cd=0; shshshfp=045a03f035c5c2c424a27f27a5fcb9cc; ipLoc-djd=1-72-2819; shshshsID=06869ef730e1b073fae55f2176ba508d_10_1551882772809; __jdb=122270672.16.1474803109|2.1551882660',
			'referer': 'https://cart.jd.com/addToCart.html?rcd=1&pid=30594070216&pc=1&eb=1&rid=1551882679467&em=',
			'upgrade-insecure-requests': '1',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
		}
		# 请求数据
		res = requests.get(url,headers=headers)
		if res.status_code == 200:
			return res.text
		else:
			return None
	except Exception as err:
		print(err)
		return None

def parsePage(content):
	'''对数据进行解析'''
	if content:
		# 使用pyquery进行数据解析
		doc = PyQuery(content)
		items = doc('div.cart-item-list')
		for item in items.items():
			detial1 = f"https:{item.find('div.p-name a').attr('href')}"
			detial2 = item.find('a.gift-info').attr('href')
			if detial2:
				detial2 = f"https:{item.find('a.gift-info').attr('href')}"
			else:
				detial2 = ''
			yield{
				'商家信息':item.find('span.shop-txt').text(),
				'商品名称':item.find('div.p-name a').text(),
				'商品详情地址':detial1,
				'商品属性':item.find('div.props-txt').text(),
				'商品价格':item.find('p.plus-switch strong').text(),
				'赠品信息':item.find('a.gift-info').text(),
				'赠品详细地址':detial2
			}
	else:
		print('无数据')

def writeFile(content):
	'''写入文件'''
	# 一定要注意windows下文件的编码问题
	# 在windows下面，新文件的默认编码是gbk，这样的话，python解释器会用gbk编码去解析我们的网络数据流txt，
	# 然而txt此时已经是decode过的unicode编码，这样的话就会导致解析不了，
	# 出现编码错误问题，解决的办法就是，改变目标文件的编码，加上encoding='utf-8'
	with open('./cart.txt','a',encoding='utf-8') as f:
		# 在这里使用dumps的时候如果 ensure_ascii=False 则会导致编码错误，具体原因不明
		f.write(json.dumps(content,ensure_ascii=False)+'\n')

def main():
	url = 'https://cart.jd.com/cart.action'
	html = getPage(url)
	for content in parsePage(html):
		writeFile(content)

if __name__ == '__main__':
	main()

# 爬取豆瓣图书分类的所有标签并保存
import requests
from pyquery import PyQuery as pq
import redis


def main():
	# 获取豆瓣标签网页
	res = requests.get('https://book.douban.com/tag/?view=type&icn=index-sorttags-all')
	res.encoding = 'utf-8'
	# print(res.status_code)
	# 解析标签数据
	# .content方法是获取实际的二进制信息，当存在图片，声音等信息的时候使用，想要获取文本使用text就可以了
	doc = pq(res.text)
	# 提取所有table标签下的a标签
	alist = doc('table.tagCol a')
	# 提取a标签中的href属性保存为一个列表（可以不用这么复杂）
	#taglist = [item.attr('href') for item in tablelist.items()]

	# 连接redis数据库保存标签的url地址
	r = redis.client.Redis(host='localhost',port='6379')
	for a in alist.items():
		tag = a.attr.href
		r.lpush('book:tag_urls',tag)
	print('添加完成')

if __name__ == '__main__':
	main()



# 导入模块
from pyquery import PyQuery as pq
import requests
'''
# 简单使用
# 打开url封装为一个对象,将请求网络信息和解析一体化
doc = pq(url='http://www.baidu.com',encoding='utf-8')
print(doc('title').text())

# 推荐使用方式：自行爬取信息(urllib或者requests) 然后使用pyquery来进行解析
res = requests.get('http://www.baidu.com')
res.encoding ='utf-8'
doc = pq(res.text)
print(doc('title'))
'''

# 读取my.html
with open('./my.html','r',encoding='utf-8') as f:
	content = f.read()

# 使用puquery来解析网络内容

# 初始化解析器
doc = pq(content)
# 使用选择器
print(doc('h3'))# 获取h3节点
print(doc('#hid'))# 获取id为hid的节点
print(doc('.aa'))# 获取class属性值为aa的标签节点
print(doc('.shop'))# 获取class属性值为shop的节点
print(doc('li a'))# 获取li标签内的a标签
print(doc('li'))# 获取网页中所有的li标签
print(doc('li.shop'))# 获取网页中li中class为shop的节点
print(doc('li:first'))# 获取网页中第一个li
print(doc('li:last'))# 获取网页中最后一个li
print(doc('li:eq(2)'))# 获取网页中第三个li（eq的索引是从0开始的）

# 二次查找
print(doc('li').find('a.bb'))# 查找页面中的所有li，然后再在查找结果上搜索其中的所有a节点class属性为bb的节点

# 节点遍历

alist = doc('a')
# 由于直接解析返回的不是一个list,而是一个网页类型的东西，需要进行类型转换为list
for a in alist.items():
	print(a)
	print(a.text())# 获取标签文本内容
	print(a.html())
	print(a.attr('href'))# 获取属性
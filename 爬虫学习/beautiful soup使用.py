# 导入模块
from bs4 import BeautifulSoup

# 读取my.html
with open('./my.html','r',encoding='utf-8') as f:
	content = f.read()

# 初始化html文档的解析对象
soup = BeautifulSoup(content,'lxml')
# 在初始化的时候它会对未经排版的文档来进行格式化，方便解析

# 三种选择器

# 节点选择器解析
print(soup.li)# 获取网页中第一个li节点
print(soup.a)# 获取网页中的第一个a节点
print(soup.a.attrs)# 获取网页中第一个a节点的所有属性 返回一个字典
print(soup.a.attrs['href'])# 获取网页中第一个a节点的具体属性
print('='*50)

print(soup.li.a.string)# 获取第一个li标签中a标签的文本内容

# 方法选择器
print(soup.find(name='li'))# 获取节点名字等于li的第一个节点
print(soup.find(name='a'))# 获取网页中第一个a节点
print(soup.find(attrs={'class':'aa'}))# 获取第一个class属性为aa的节点
print(soup.find_all(attrs={'class':'aa'}))# 获取所有的class属性为aa的节点
print(soup.find_all(name='a',attrs={'class':'aa'}))# 获取所有的class属性为aa的节点的a节点
print(soup.find_all(text='百度'))# 获取文本内容为百度的节点的内容

# css选择器
# 按照css的写法格式
print(soup.select('li'))# 获取所有的li节点
print(soup.select('#hid'))# 获取id属性值为hid的节点
print(soup.select('.shop'))# 获取所有class属性为shop的节点

list = soup.select('ul li a')
for v in list:
	#print(v.string+':'+v['href'])
	# 或者使用下面这种方式
	print(v.get_text()+':'+v.attrs['href'])
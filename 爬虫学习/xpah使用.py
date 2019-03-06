# 导入模块
from lxml import etree

# 读取my.html
f = open('./my.html','r',encoding='utf-8')
content = f.read()
f.close()

# 初始化解析html文档并返回根节点对象
# 使用html内容来生成一个树状的信息
html = etree.HTML(content)

# 根据html的结果通过文件path的方式获取节点
result = html.xpath('/html/head/title/text()')# 获取title节点对象的内容
result = html.xpath('/html/body/h3/text()')# 获取h3标签的对象内容
result = html.xpath('/html/body/h3/@id')# 获取h3标签的id属性
result = html.xpath('/html/body/ul/li')# 获取/html/body/ul下的所有li节点
result = html.xpath('//li')# 获取网页的所有li元素节点

# 批量获取
# 获取节点的内容
result = html.xpath('//li/a/text()')
# 获取属性信息
result = html.xpath('//li/a/@href')
print(result)

# 按顺序选择
result = html.xpath('//ul/li[1]/a/text()')# 第一个li中的a的内容
result = html.xpath('//ul/li[last()]/a/text()')# 最后一个li中的a的内容
result = html.xpath('//ul/li[position()<3]/a/text()')# 前两个li的a的内容
result = html.xpath('//ul/li[last()-2]/a/text()')# 从最后一个向前数第三个li中的a的内容
print(result)

# 节点轴选择
result = html.xpath('//li[1]/a/ancestor::*')# 获取第一个li节点中a节点的所有祖先节点
result = html.xpath('//li[1]/a/ancestor::ul')# 获取第一个li中a节点的ul祖先节点
result = html.xpath('//li[3]/a/attribute::*')# 获取第三个li节点的a节点的所有属性值
result = html.xpath('//li//a[@class="aa"]/text()')# 获取属性class的属性值为aa的所有a节点的内容
result = html.xpath('//table/tbody/child::*')# 获取table节点下的tbody节点的所有子节点
#result = html.xpath('//table/tbody/child::[@class="tt"]')# 获取table节点下的tbody节点的所有子节点中class属性为tt的子节点
print(result)

print('='*40)

# 节点遍历(多层解析)
result = html.xpath('//li/a')
for v in result:
	# 子解析
	#print(v.xpath("text()")[0]+':'+v.xpath('@href')[0])
	# 如果你能确定你已经来到了某个具体的节点内部，则可以使用下面的这种写法
	print(v.text+':'+v.get('href'))
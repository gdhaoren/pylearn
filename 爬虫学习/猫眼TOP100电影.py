# get请求

# 导包
import requests
import re
import pandas as pd

def maoyan_top100(path):
	# 保存数据
	movie_list = []
	for i in range(0,100,10):
		# 请求地址
		url = f'https://maoyan.com/board/4?offset={i}'

		# 请求数据
		res = requests.get(url)

		# 解码数据
		html = res.content.decode('utf-8')

		# 解析数据
		info_pat = '<dd>.*?board-index-.*?">(\d+)</i>.*?title="(.*?)" class="image-link".*?<img data-src="(.*?)" alt=.*?<p class="star">\s+主演：(.*?)\s+</p>.*?上映时间：(.*?)</p>.*?class="integer">(.*?)</i><i class="fraction">(.*?)</i></p>.*?</dd>'
		infos = re.findall(info_pat,html,re.S)

		movie_list.extend(infos)

	# 生成dataframe
	columns = ['排序','电影名称','图片','主演','上映日期','评分1','评分2']
	movie_df = pd.DataFrame(movie_list,columns=columns)
	# 处理评分列
	movie_df['评分'] = movie_df['评分1']+movie_df['评分2']
	movie_df.drop(movie_df[['评分1','评分2']],axis=1,inplace=True)
	# 保存为csv文件
	movie_df.to_csv(path,index=0,encoding='utf-8')

def main():
	path = input('请输入要保存的文件位置： ')
	maoyan_top100(path)
	print('保存成功')

if __name__ == '__main__':
	main()
		


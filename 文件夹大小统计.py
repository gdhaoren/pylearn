import os

# 指定路径
path = input('请输入文件夹路径：')

# 统计函数
def dir_size(path):
	'''
	统计文件夹大小
	'''
	# 初始化统计文件大小的变量
	file_size = 0
	# 获取文件夹内容
	dirlist = os.listdir(path)
	# 遍历文件
	for file in dirlist :
		# 文件绝对路径
		fpath = os.path.join(path,file)
		# 判断是文件还是文件夹
		if os.path.isfile(fpath) :
			# 统计所有文件的总大小
			file_size += os.path.getsize(fpath)
		else :
			# 递归计算子目录大小
			file_size += dir_size(fpath)
	# 返回统计文件夹大小
	return file_size

print(f'文件夹的大小为{dir_size(path)/1024**2:.1f}mb')




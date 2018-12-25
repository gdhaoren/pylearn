# ATM机任务

user_message={'12345':{'密码':888888,'余额':1000.23},'678463':{'密码':666666,'余额':783000.23}}

# 登录页面
while True :
	print('==================================================')
	print('==============欢迎使用本机 id: 10000===============')
	print('==================================================')
	print('继续请按1',end='           ')
	print('退出请按q')
	a = input('请选择您要执行的操作：')
	if a == '1' :
		while True :
			a = input('返回上层菜单请按q,按任意键继续: ')
			if a == 'q' :
				break
			print('==============================================')
			user_id = input('请输入您的账号：')
			pasword = input('请输入您的密码：')
			if user_id in user_message.keys() :
				if int(pasword) == user_message[user_id]['密码'] :
					while True:
						print('==============================================')
						print('=============请选择您需要的服务================')
						print('==============================================')
						client = user_message[user_id]
						print ('查询余额请按1')
						print('存款请按2')
						print('取款请按3')
						print('退出请按q')
						operate = input('请选择您要执行的操作：')
						if operate == '1' :
							print(f"您的当前余额为:{client['余额']:.2f}")
							a = input('按任意键返回上层菜单')
						elif operate == '2':
							money = input('请输入您的存款金额：')
							client['余额'] += int(money)
							print(f"您的当前余额为:{client['余额']:.2f}")
							a = input('按任意键返回上层菜单')
						elif operate == '3' :
							money = input('请输入您的取款金额：')
							if int(money) > client['余额'] :
								print('抱歉您的余额不足')
								a = input('按任意键返回上层菜单')
							else :
								client['余额'] -= int(money)
								print(f"您的当前余额为:{client['余额']:.2f}")
								a = input('按任意键返回上层菜单')
						elif operate == 'q' :
							break
						else :
							print('没有该项操作，请重新输入')
				else :
					print('密码错误')
			else :
				print('账户名不存在')
	elif a == 'q' :
		break
	else :
		print('没有该项操作，请重新输入')
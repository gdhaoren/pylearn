# 导入模块
import pygame
from pygame.locals import *
import random

# 飞机类
class Object:
	'''物体类'''
	def __init__(self,screen_temp,x_position,y_position,i_path):
		self.x = x_position
		self.y = y_position
		self.screen = screen_temp
		self.image = pygame.image.load(i_path)
	
	def display(self):
		'''绘制物体'''
		self.screen.blit(self.image,(self.x,self.y))



class HeroPlane(Object):
	'''玩家飞机'''
	def __init__(self,screen_temp,x_position,y_position,i_path):
		# 继承父类的构造方法
		super(HeroPlane,self).__init__(screen_temp,x_position,y_position,i_path)
		self.bullet_list=[]

	def move_right(self):
		'''飞机右移并防止越界'''
		self.x += 5
		if self.x > 406:
			self.x=406
	
	def move_left(self):
		'''飞机左移并防止越界'''
		self.x -= 5
		if self.x < 0:
			self.x=0

	def fire(self):
		'''生成子弹'''
		b_image = r".\images\pd.png"
		self.bullet_list.append(Bullet(self.screen,self.x+51,self.y,b_image))

	def display(self):
		'''显示子弹和飞机,并进行碰撞检测'''
		for bullet in self.bullet_list:
			bullet.display()
			if bullet.move():
				self.bullet_list.remove(bullet)
		# 显示飞机
		self.screen.blit(self.image,(self.x,self.y))

	def bo_test(self,enemy_plane):
		'''检测英雄飞机是否被击落'''
		for bo in enemy_plane.bullet_list:
			if bo.x>self.x+12 and bo.x<self.x+64 and bo.y+17>self.y:
				# 记录我方飞机爆炸位置和显示帧数
				hero_boom = [bo.x+50,self.y+50,50]
				return True


class Bullet(Object):
	'''子弹'''
	def __init__(self,screen_temp,x_position,y_position,i_path):
		# 继承父类的构造方法
		super(Bullet,self).__init__(screen_temp,x_position,y_position,i_path)

	def move(self):
		'''向前运动'''
		self.y-=10
		if self.y<-20:
			return True

	def move_b(self):
		'''向后运动'''
		self.y+=5
		if self.y > 512:
			return True

class EnemyPlane(Object):
	'''敌机'''
	def __init__(self,screen_temp,x_position,y_position,i_path):
		# 继承父类的构造方法
		super(EnemyPlane,self).__init__(screen_temp,x_position,y_position,i_path)
		self.bullet_list = []

	def move(self,hero_plane):
		'''敌机前进并发射子弹'''
		self.y += 4
		# 检测敌机是否飞出屏幕
		if self.y > 512:
			return True
		# 检测敌机是否被击落
		if hero_plane.bullet_list:
			for bo in hero_plane.bullet_list:
				if bo.x>self.x+12 and bo.x<self.x+90 and bo.y>self.y+20 and bo.y<self.y+60:
					# 记录爆炸位置和显示帧数
					enemy_boom_list.append([bo.x-50,bo.y-40,20])
					return True
		# 敌机发射子弹
		b_image = r".\images\enemy_bullet.png"
		self.bullet_list.append(Bullet(self.screen,self.x+50,self.y+75,b_image)) 

	def display(self):
		'''绘制敌机和子弹'''
		for indx,bullet in enumerate(self.bullet_list):
			# 每隔8个子弹显示一个
			if indx%20 == 0:
				bullet.display()
			if bullet.move_b():
				self.bullet_list.remove(bullet)

		self.screen.blit(self.image,(self.x,self.y))


# 设置键盘控制
def keyboard_control(hero_plane):
	# 获取按键信息
	pressed_keys = pygame.key.get_pressed()

	# 检测是否按下a或者left按键
	if pressed_keys[K_LEFT] or pressed_keys[K_a]:
		hero_plane.move_left()

	# 检测是否按下d或者right按键
	elif pressed_keys[K_RIGHT] or pressed_keys[K_d]:
		hero_plane.move_right()

	# 检查是否按下空格键
	if pressed_keys[K_SPACE]:
		hero_plane.fire()

# 主程序入口
def main():
	# 生成背景动画
	# 创建主窗口
	screen = pygame.display.set_mode((512,568))
	# 读入背景图片
	background = pygame.image.load(r".\images\bg2.jpg").convert()
	# 初始化背景图片位置
	y_position = -968
	# 初始化一个玩家飞机
	h_image = r".\images\me.png"
	hero_plane = HeroPlane(screen,200,400,h_image)
	# 敌机列表
	enemy_list=[]
	# 敌方爆炸点列表
	# 声明爆炸点列表为全局变量
	global enemy_boom_list
	enemy_boom_list=[]
	# 我方爆炸点
	# 声明爆炸点为全局变量
	global hero_boom
	# 爆炸画面
	boom = pygame.image.load(r"./images/boom2.png")
	# 循环显示内容
	while True:
		# 生成背景显示
		screen.blit(background,(0,y_position))
		# 设置退出事件
		for event in pygame.event.get():
			if event.type == QUIT:
				exit()
		# 移动画布
		y_position+=2
		if y_position == -200 :
			y_position=-968
		# 显示玩家飞机
		hero_plane.display()
		# 调用键盘控制
		keyboard_control(hero_plane)
		# 随机生成敌机
		if random.choice(range(50))==10:
			e_path=".\\images\\e"+str(random.choice(range(3)))+".png"
			x = random.choice(range(398))
			enemy_list.append(EnemyPlane(screen,x,-76,e_path))
		# 绘制敌机, 并检测敌方子弹与我方碰撞
		for enemy in enemy_list:
			enemy.display()
			if enemy.move(hero_plane):
				enemy_list.remove(enemy)
			if hero_plane.bo_test(enemy):
				exit()
			
		if enemy_boom_list :
			for pos in enemy_boom_list:
				screen.blit(boom,pos[:2])
				pos[2]-=1
				# 显示满10帧就移除这个爆炸画面
				if pos[2] ==0 :
					enemy_boom_list.remove(pos)
					
		# 更新显示
		pygame.display.update()
		# 设置显示间歇为0.02s
		pygame.time.delay(20)
	

if __name__=='__main__':
	main()
#导入相应的模块
import pygame
from pygame.locals import *
from sys import exit
import time,random
import os
import math

class HeroPlane(pygame.sprite.Sprite):
	'''玩家飞机（英雄）'''
	def __init__(self, hero_surface, hero_init_pos):
		pygame.sprite.Sprite.__init__(self)
		self.image = hero_surface
		self.rect = self.image.get_rect()
		self.rect.topleft = hero_init_pos
		self.mask = pygame.mask.from_surface(self.image)
		self.living = True
		self.life = 5

		self.speed = 5
		
		self.bullets = pygame.sprite.Group() #用于存放玩家的子弹列表
		self.missles = pygame.sprite.Group() #用于存放玩家的导弹列表
		
	def move(self,offset,offset_1):
		x = self.rect.left + offset[pygame.K_RIGHT] + offset_1[pygame.K_d] - offset[pygame.K_LEFT] - offset_1[pygame.K_a]
		y = self.rect.top + offset[pygame.K_DOWN] + offset_1[pygame.K_s] - offset[pygame.K_UP] - offset_1[pygame.K_w]

		if x < 0:
			self.rect.left = 0
		elif x > SCREEN_WIDTH - self.rect.width:
			self.rect.left = SCREEN_WIDTH - self.rect.width
		else:
			self.rect.left = x

		if y < 0:
			self.rect.top = 0
		elif y > SCREEN_HEIGHT - self.rect.height:
			self.rect.top = SCREEN_HEIGHT - self.rect.height
		else:
			self.rect.top = y
		
	def fire(self, bullet_surface, hero_level):
		if hero_level == 0:
			self.bullets.add(Bullet(bullet_surface, self.rect.midtop))
		elif hero_level == 1:
			self.bullets.add(Bullet(bullet_surface, (self.rect.center[0]-28,self.rect.center[1])),
			Bullet(bullet_surface, (self.rect.center[0]+25,self.rect.center[1])))
		elif hero_level == 2:
			self.bullets.add(Bullet(bullet_surface, (self.rect.midtop[0]-14,self.rect.midtop[1])),
			Bullet(bullet_surface, (self.rect.midtop[0]+12,self.rect.midtop[1])),
			Bullet_Towards_Right(bullet_surface, self.rect.center),
			Bullet_Towards_Left(bullet_surface, self.rect.center))
		elif hero_level == 3:
			self.bullets.add(Bullet(bullet_surface, (self.rect.midtop[0]-9,self.rect.midtop[1])),
			Bullet(bullet_surface, (self.rect.midtop[0]+19,self.rect.midtop[1])),
			Bullet(bullet_surface, (self.rect.center[0]-40,self.rect.center[1])),
			Bullet(bullet_surface, (self.rect.center[0]+49,self.rect.center[1])),
			Bullet_Towards_Right(bullet_surface, self.rect.center),
			Bullet_Towards_Left(bullet_surface, self.rect.center))
	
	def fire_missle(self, missle_surface, missle_init_pos, hero_level):
		if hero_level == 2:
			self.missles.add(Missle(missle_surface,missle_init_pos))
		if hero_level == 3:
			self.missles.add(Missle(missle_surface,(missle_init_pos[0]-40,missle_init_pos[1]+80)),
			Missle(missle_surface,(missle_init_pos[0]+40,missle_init_pos[1]+80)))

	def hitted(self):
		self.life -= 1
		if self.life < 0:
			self.life = 0
		#应有闪光

class Bullet(pygame.sprite.Sprite):
	'''子弹类'''
	def __init__(self, bullet_surface, bullet_init_pos):
		pygame.sprite.Sprite.__init__(self)
		self.image = bullet_surface
		self.rect = self.image.get_rect()
		self.rect.topleft = bullet_init_pos
		self.mask = pygame.mask.from_surface(self.image)

		self.speed = 8
	
	def update(self):
		self.rect.top -= self.speed
		if(self.rect.top < - self.rect.height):
			self.kill()

class Bullet_Towards_Right(pygame.sprite.Sprite):
	'''
	向右发射的子弹
	从飞机center发出
	'''
	def __init__(self, bullet_surface, bullet_init_pos):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.transform.rotate(bullet_surface, 315)
		self.rect = self.image.get_rect()
		self.rect.center = bullet_init_pos
		self.mask = pygame.mask.from_surface(self.image)

		self.speed = 12

	def update(self):
		self.rect.top -= (self.speed**0.5)/(2**0.5)
		self.rect.right += (self.speed**0.5)

		if(self.rect.left > self.rect.width + SCREEN_WIDTH or self.rect.top < - self.rect.height):
			self.kill()

class Bullet_Towards_Left(pygame.sprite.Sprite):
	'''
	向左发射的子弹
	从飞机center发出
	'''
	def __init__(self, bullet_surface, bullet_init_pos):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.transform.rotate(bullet_surface, 45)
		self.rect = self.image.get_rect()
		self.rect.center = bullet_init_pos
		self.mask = pygame.mask.from_surface(self.image)

		self.speed = 12

	def update(self):
		self.rect.top -= (self.speed**0.5)/(2**0.5)
		self.rect.left -= (self.speed**0.5)/(2**0.5)

		if(self.rect.right < - self.rect.right or self.rect.top < - self.rect.height):
			self.kill()

class EnemyBullet(pygame.sprite.Sprite):
	'''子弹类'''
	def __init__(self, bullet_surface, bullet_init_pos):
		pygame.sprite.Sprite.__init__(self)
		self.image = bullet_surface
		self.rect = self.image.get_rect()
		self.rect.topleft = bullet_init_pos
		self.mask = pygame.mask.from_surface(self.image)

		self.speed = 4
	
	def update(self):
		self.rect.top += self.speed
		if self.rect.top > SCREEN_HEIGHT:
			self.kill()

class Missle(pygame.sprite.Sprite):
	'''
	导弹
	自动瞄准最近的敌机
	'''
	def __init__(self, missle_surface, missle_init_pos):
		pygame.sprite.Sprite.__init__(self)
		self.image_instance = missle_surface
		self.image = missle_surface
		self.rect = self.image.get_rect()
		self.rect.center = missle_init_pos
		self.mask = pygame.mask.from_surface(self.image)
		self.vector = (0,-2) #初始向量
		self.angle = 0 #初始角度，取值范围[-180,180)

		self.speed = 2
		self.angular_speed = 2 #角速度
	
	def update(self, enemylist):
		if self.rect.top < - self.rect.top or self.rect.left < - self.rect.left or self.rect.left > SCREEN_WIDTH:
			self.kill()
			return

		#锁定距离最短的敌机,没有敌机时，竖直向前运动
		#没有敌机
		if not enemylist:
			if self.angle > 0 and self.angle < 180:
				self.angle -= self.angular_speed
			elif self.angle >= -180 and self.angle < 0:
				self.angle += self.angular_speed
		else:
			#距离
			distance = 20000
			#锁定的飞机
			focused_enemy = None
			for single_enemy in enemylist:
				distance_temp = ((self.rect.center[0]-single_enemy.rect.center[0])**2+(self.rect.center[1]-single_enemy.rect.center[1])**2)**0.5
				if distance > distance_temp:
					distance = distance_temp
					focused_enemy = single_enemy
			#确定旋转方向
			vector_temp = (focused_enemy.rect.center[0] - self.rect.center[0], focused_enemy.rect.center[1] - self.rect.center[1])#导弹指向敌机向量
			angle_temp = math.degrees(math.acos((self.vector[0]*vector_temp[0] + self.vector[1]*vector_temp[1])/(4*(vector_temp[0]**2+vector_temp[1]**2)**0.5)))#指向敌机向量与当前向量的角度
			if angle_temp < 90 and angle_temp > -90:
				self.angle += self.angular_speed
			elif angle_temp > 90 or angle_temp < -90:
				self.angle -= self.angular_speed
			#考虑边界
			if self.angle >= 180:
				self.angle -= 360
			elif self.angle < -180:
				self.angle += 360


		self.image = pygame.transform.rotate(self.image_instance,self.angle)
		self.rect.top -= math.cos(math.radians(self.angle))*self.speed
		self.rect.left -= math.sin(math.radians(self.angle))*self.speed
		self.vector = (math.cos(math.radians(self.angle))*self.speed, math.sin(math.radians(self.angle))*self.speed)
	

class EnemyPlane(pygame.sprite.Sprite):
	'''敌机类'''
	def __init__(self, enemy_surface, enemy_init_pos):
		pygame.sprite.Sprite.__init__(self)
		self.image = enemy_surface
		self.rect = self.image.get_rect()
		self.rect.center = enemy_init_pos
		self.mask = pygame.mask.from_surface(self.image)
		self.bullets = pygame.sprite.Group() #用于存放单一敌机的子弹列表
		self.life = 5

		self.down_index = 0#指示爆炸索引

		self.speed = 2
	
	def update(self):
		self.rect.top += self.speed
		if self.rect.top > SCREEN_HEIGHT:
			self.kill()

	def fire(self, bullet_surface):
		self.bullets.add(EnemyBullet(bullet_surface, self.rect.midbottom))
	
	def hitted(self):
		self.life -= 1
		if self.life < 0:
			self.life = 0
		#应有闪光

class Create_Enemy():
	'''
	主要用于确定敌机位置，避免重叠
	'''
	def __init__(self,enemylist):
		self.enemylist = enemylist
	def get_new_enemy(self):
		enemy_surface_temp = pygame.image.load("./images/e"+str(random.choice(range(3)))+".png")
		self.left = enemy_surface_temp.get_rect().width / 2
		self.right = SCREEN_WIDTH - enemy_surface_temp.get_rect().width / 2
		enemy_plane = EnemyPlane(enemy_surface_temp, (random.choice(range(int(self.left),int(self.right)+1)),-75))
		if pygame.sprite.spritecollide(enemy_plane,self.enemylist,False,pygame.sprite.collide_mask):
			return self.get_new_enemy()
		return enemy_plane
		

# 定义窗口的分辨率
SCREEN_WIDTH = 512
SCREEN_HEIGHT = 568

#玩家等级
hero_level = 0

def main():
	'''主程序函数 '''


	# 定义画面帧率
	FRAME_RATE = 60

	# 定义动画周期（帧数）
	ANIMATE_CYCLE = 30

	ticks = 0
	clock = pygame.time.Clock()
	#程序两套控制
	offset = {pygame.K_LEFT : 0, pygame.K_RIGHT : 0, pygame.K_UP : 0, pygame.K_DOWN : 0}
	offset_1 = {pygame.K_a : 0, pygame.K_d : 0, pygame.K_w : 0, pygame.K_s : 0}

	#初始化游戏
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
	pygame.display.set_caption('Fight of Flights')

	# 载入飞机图片
	shoot_img = pygame.image.load('./images/Heros.png')
	# 载入子弹图片
	bullet_surface = pygame.image.load("./images/pd.png")
	# 载入导弹图片
	missle_surface = pygame.image.load("./images/missle.png")

	# 用subsurface剪切读入的图片
	hero_surface = []
	#basic
	hero_surface.append(shoot_img.subsurface(pygame.Rect(393, 102, 116, 93)))
	#level_1
	hero_surface.append(shoot_img.subsurface(pygame.Rect(127, 107, 116, 94)))
	#level_2
	hero_surface.append(shoot_img.subsurface(pygame.Rect(393, 0, 119, 100)))
	#level_3
	hero_surface.append(shoot_img.subsurface(pygame.Rect(137, 0, 131, 106)))

	hero_pos = [200, 450]
	hero_level = 0
	
	# 创建玩家飞机（英雄）
	hero = HeroPlane(hero_surface[0], hero_pos)

	#存放敌机的列表
	enemylist = pygame.sprite.Group()
	#存放坠毁敌机的列表
	enemy_down_list = pygame.sprite.Group()
	#存放所有敌机子弹
	enemy_bullets = pygame.sprite.Group()
	# 载入敌机子弹图片
	enemy_bullet_surface = pygame.image.load("./images/enemy_bullet.png")
	#载入爆炸切图
	enemy1_down_surface = []
	enemy1_down_surface.append(pygame.image.load("./images/boom1.png"))
	enemy1_down_surface.append(pygame.image.load("./images/boom2.png"))
	enemy1_down_surface.append(pygame.image.load("./images/boom3.png"))
	enemy1_down_surface.append(pygame.image.load("./images/boom4.png"))


	# 创建一个游戏背景
	background = pygame.image.load("./images/bg2.png")

	m = -968
	while True:
		#控制最大帧数
		clock.tick(FRAME_RATE)

		#绘制画面
		screen.blit(background,(0,m))
		m+=2
		if m>=-200:
			m = -968

		#射击
		if ticks % 10 == 0:
			hero.fire(bullet_surface, hero_level)
		#控制子弹飞行
		hero.bullets.update()
		#绘制子弹
		hero.bullets.draw(screen)

		if ticks % 50 == 0:
			hero.fire_missle(missle_surface,hero.rect.midtop, hero_level)
		for missle in hero.missles:
			missle.update(enemylist)
		hero.missles.draw(screen)

		#绘制敌机
		if random.choice(range(50)) == 10:
			enemylist.add(Create_Enemy(enemylist).get_new_enemy())

		for each_plane in enemylist:
			each_plane.update()
			if ticks % 100 == 0:
				each_plane.fire(enemy_bullet_surface)
			for each_bullet in each_plane.bullets:
				enemy_bullets.add(each_bullet)
		
		enemy_bullets.update()
		enemy_bullets.draw(screen)
		
		enemylist.draw(screen)

		#检测敌机与子弹的碰撞
		enemies_hitted = pygame.sprite.groupcollide(enemylist,hero.bullets,False,pygame.sprite.collide_mask)
		if enemies_hitted: #若非空
			for enemy in enemies_hitted:
				enemy.hitted()
				enemies_hitted[enemy][0].kill()

		#检测敌机与子弹的碰撞
		enemies_hitted = pygame.sprite.groupcollide(enemylist,hero.missles,False,pygame.sprite.collide_mask)
		if enemies_hitted: #若非空
			for enemy in enemies_hitted:
				enemy.hitted()
				enemies_hitted[enemy][0].kill()

		#检测本机与敌子弹的碰撞
		hero_hitted = pygame.sprite.spritecollide(hero,enemy_bullets,False,pygame.sprite.collide_mask)
		if hero_hitted:
			for hit in hero_hitted:
				hero.hitted()
				enemy_bullets.remove(hit)
				hit.kill()


		#绘制玩家飞机
		hero.image = hero_surface[hero_level]
		screen.blit(hero.image, hero.rect)
		ticks += 1
		
		#消灭生命值为0的敌机
		for enemy in enemylist:
			if enemy.life == 0:
				enemy_down_list.add(enemy)
				enemylist.remove(enemy)
		
		for enemy in enemy_down_list:
			screen.blit(enemy1_down_surface[enemy.down_index], enemy.rect)
			if ticks % (ANIMATE_CYCLE//2) == 0:
				if enemy.down_index < 3:
					enemy.down_index += 1
				else:
					enemy_down_list.remove(enemy)
					enemy.kill()
		
		#更新显示
		pygame.display.update()

		'''
		#执行键盘控制
		key_control(hero)
		'''
		#键盘事件响应
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()

			# 控制方向 
			if event.type == pygame.KEYDOWN:
				if event.key in offset:
					offset[event.key] = hero.speed
				elif event.key in offset_1:
					offset_1[event.key] = hero.speed
				
				if event.key == pygame.K_u and hero_level < 3:
					hero_level += 1
				if event.key == pygame.K_l and hero_level > 0:
					hero_level -= 1
			elif event.type == pygame.KEYUP:
				if event.key in offset:
					offset[event.key] = 0
				elif event.key in offset_1:
					offset_1[event.key] = 0

		#移动飞机
		hero.move(offset, offset_1)

		'''
		#定时显示
		time.sleep(0.04)
		'''



#判断当前是否是主运行程序，并调用
if __name__ == "__main__":
	main()

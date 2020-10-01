import random
from pynput import keyboard
import time

class PlayGround:
	# Розміри екрану
	WIDTH = 200
	HEIGHT = 45

	BULLETS = [] # массив куль
	ENEMIES = [] # массив ворогів
	MATRIX = [] # головна матриця
	def __init__(self):
		for i in range(self.HEIGHT):
			self.MATRIX.append([])
			for j in range(self.WIDTH):
				self.MATRIX[i].append('.')
		self.write_line_center_onrow(line = 'ДЛЯ НАЧАЛА ИГРЫ, НАЧНИТЕ ДВИГАТЬСЯ',row=int(self.HEIGHT/2),fill='.')

	def write_line_center_onrow(self,line,row,fill): # Функція для написання центру посередені матриці на потрібному рядку
		line_by_sym = list(line)
		to_del_len = len(self.MATRIX[row][int(self.WIDTH/2-len(line)/2):-1])-len(line)
		del self.MATRIX[row][int(self.WIDTH/2-len(line)/2):-1]
		for s in line_by_sym:
			self.MATRIX[row].append(s)
		for i in range(to_del_len):
			self.MATRIX[row].append(fill)

	def empty_matrix(self): #Функція очищення матриці
		for i in range(self.HEIGHT-1):
			for j in range(self.WIDTH):
				self.MATRIX[i][j] = ' '

	def draw(self,hits,misses): #Функція малювання матриці у консолі
		print("Total hits: ",hits)
		print("Total misses: ",misses)
		for i in range(self.HEIGHT):
			print(''.join(self.MATRIX[i]))


class Hero(PlayGround):
	def __init__(self):
		self.hits = 0
		self.misses = 0
		self.left = self.WIDTH/2 #Розміщуємо гравця по центру

	def move(self,key,value = 3): #рухаємо гравця
		move_range=value
		if key=='left' or key==keyboard.Key.left:
			self.left=self.left-move_range if self.left-move_range>0 else 0
		elif key=='right' or key==keyboard.Key.right:
			self.left=self.left+move_range if self.left+move_range<self.WIDTH else self.WIDTH-1
		
		self.MATRIX[-1] = [' ' for i in self.MATRIX[-1]] # Очищуємо нижній рядок де знаходиться наша пушка
		self.MATRIX[-1][int(self.left)] = '🖲' # Малюємо нову пушку


	def get_total_score(self):
		print(f'Game over!\nTotal hits:{self.hits}\nTotal miss:{self.misses}')


class Bullet(PlayGround):
	def __init__(self,left_pos):
		self.position = (self.HEIGHT-2,int(left_pos))

	def show(self): # Малюємо кулю
		self.MATRIX[self.position[0]][self.position[1]] = '♦️'

	def move(self): # Рухаємо кулю
		self.MATRIX[self.position[0]][self.position[1]] = ' '
		#print(f'movin at {self.position}')
		self.position = (self.position[0]-1,self.position[1])
		if self.position[0]<=0: # Якщо куля вийшла за межі екрану
			return 'OUT'
		self.show()
	
	def disapear(self): # Видаляємо кулю з матриці
		self.MATRIX[self.position[0]][self.position[1]] = ' '



class Enemy(PlayGround):
	ENEMIES_STYLE = ['🦀','🐡','🐺','🧛','🐸','🐛','🕷️','🦂','🦟'] # Різні типи ворогів
	def __init__(self):
		self.enemy_icon = random.choice(self.ENEMIES_STYLE)
		self.position = (random.randint(0,self.HEIGHT-6),random.randint(3,self.WIDTH-3))
		self.speed = 1 # Швидкість руху по екрану
		self.direction = random.choice(['left','right','top','bot'])

	def show(self): #Показати ворога
		self.MATRIX[self.position[0]][self.position[1]] = self.enemy_icon

	def move(self): #Рухати ворога
		self.MATRIX[self.position[0]][self.position[1]] = ' '
		if self.direction=='left':
			self.position = (self.position[0],self.position[1]-self.speed)
		elif self.direction=='right':
			self.position = (self.position[0],self.position[1]+self.speed)
		elif self.direction=='top':
			self.position = (self.position[0]+self.speed,self.position[1])
		elif self.direction=='bot':
			self.position = (self.position[0]-self.speed,self.position[1])
		if self.position[0] not in range(1,self.HEIGHT) or self.position[1] not in range(0,self.WIDTH):
			return 'Miss'
		self.show()

	def die(self): #Вбити ворога
		self.MATRIX[self.position[0]][self.position[1]] = '💀'
		time.sleep(0.5)
		self.MATRIX[self.position[0]][self.position[1]] = ' '













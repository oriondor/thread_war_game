import _thread
import time

from clear_screen import clear_scr
from ground import Enemy

from pynput.keyboard import Key, Controller
keyboard = Controller()

# Функція, яка відповідає за створення нових ворогів
def spawner(field,hero):
	s_time = 5
	times = 0
	while True:
		time.sleep(s_time)
		times+=1
		if times>8:
			s_time=4
		elif times>14:
			s_time=3
		elif times>23:
			s_time=2
		elif times>35:
			s_time=1
		enemy = Enemy()
		field.ENEMIES.append(enemy)
		enemy.show()

# Функція, яка відповідає за переміщення ворогів
def mover(field,hero):
	while True:
		time.sleep(1)
		for enemy in field.ENEMIES:
			if enemy.move() == "Miss": # У випадку якщо при русі ворога ми вийшли за границю поля, зараховуємо miss
				hero.misses+=1
				field.ENEMIES.remove(enemy)
				if hero.misses>29: # У випадку, якщо ми пропустили більше 29 ворогів, імітуємо натискання клавіші Esc
					keyboard.press(Key.esc)
					keyboard.release(Key.esc)
		clear_scr()
		field.draw(hero.hits,hero.misses)

# Функція, яка відповідає за переміщення куль та перевірку чи влучила куля
def shooter(field,hero):
	while True:
		time.sleep(0.1)
		for bullet in field.BULLETS: # Перевіряємо кулю
			for enemy in field.ENEMIES: # Перевіряємо чи пролітає куля біля ворогу
				if abs(enemy.position[0]-bullet.position[0])<2 and abs(enemy.position[1]-bullet.position[1])<2: # Якщо куля достатньо близько
					enemy.die()
					field.ENEMIES.remove(enemy) # Вбиваємо ворога
					hero.hits+=1 # Зараховуємо влучання
					bullet.disapear()
					field.BULLETS.remove(bullet) # Видаляємо кулю
					break
			if bullet in field.BULLETS:
				if bullet.move() == "OUT":
					field.BULLETS.remove(bullet)
		clear_scr()
		field.draw(hero.hits,hero.misses)








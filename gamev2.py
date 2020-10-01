from ground import Hero, PlayGround, Enemy, Bullet
from clear_screen import clear_scr
from threader import spawner,mover,shooter

from pynput import keyboard
import _thread

game_started = False # Визначає чи була почата гра, якщо так, то запускаються відповідні потоки

field = PlayGround()
hero = Hero()

field.draw(hero.hits,hero.misses)


def on_press(key):
	global game_started
	try:
		if key.char=='q':
			print(hero.get_total_score())
			return False
	except AttributeError:
		if not game_started: #Якщо гра не була запущена, то при натисканні на будь-яку клавішу - запускаємо гру (усі потоки)
			_thread.start_new_thread(spawner,(field,hero))
			_thread.start_new_thread(mover,(field,hero))
			_thread.start_new_thread(shooter,(field,hero))
			game_started = True
			field.empty_matrix() # Очищуємо матрицю
		if key==keyboard.Key.space: # Вистріл якщо нажато Пробіл
			if len(field.BULLETS)<3: # Якщо на екрані менше 3 куль
				bullet = Bullet(hero.left)
				field.BULLETS.append(bullet)
		else: # Якщо нажато іншу клавішу
			hero.move(key=key) # Перемістити гравця
		clear_scr()
		field.draw(hero.hits,hero.misses)


def on_release(key):
	if key == keyboard.Key.esc:
		print(hero.get_total_score())
		return False


with keyboard.Listener(
		on_press=on_press,
		on_release=on_release) as listener:
	listener.join()
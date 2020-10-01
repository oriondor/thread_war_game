from os import name 
import subprocess as sp

def clear_scr():
	if name == 'nt': 
		clear_the_screen = sp.call('cls', shell=True)
	else:
		clear_the_screen = sp.call('clear', shell=True)

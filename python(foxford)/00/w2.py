import os

while True:
	try:
		a = float(input('введи 1 значение: '))
		b = float(input('введи 2 значение: '))
		ss = (a + b)/2
		os.system('clear')
		print(ss)
	except:
		os.system('clear')
		print('введите число')
import os

while True:
	try:
		a = int(input('введи 1 значение: '))
		b = int(input('введи 2 значение: '))
		ss = (a + b)/2
		os.system('clear')
		print(ss)
	except:
		os.system('clear')
		print('введите число')
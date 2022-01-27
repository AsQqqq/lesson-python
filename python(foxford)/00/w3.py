import os

while True:
	try:
		a = int(input('введите начальную позицию змейки: '))
		b = int(input('ввелите колличество секунд змейки: '))
		ss = (b * 3) + a
		os.system('clear')
		print(ss)
	except:
		os.system('clear')
		print('введите число')
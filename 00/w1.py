import os

while True:
	try:
		a = int(input('сколько гномиков?: '))
		b = a * 10
		os.system('clear')
		print(b)
	except:
		os.system('clear')
		print('введите число')
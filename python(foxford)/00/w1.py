#импорт системных команд
import os

#запуск цикла
while True:
	#проверка на ошибки
	try:
		#ввод числа гномиков
		a = int(input('сколько гномиков?: '))
		#формула вычисления количество алмазов
		b = a * 10
		#запуск отчистки консоли
		try:
			#для линукс
			os.system('clear')
		except:
			#для виндовс
			os.system('cls')
		#вывод данных
		print(b)
	#если введены не правильные значения(например строка)
	except:
		#запуск отчистки консоли
		try:
			#для линукс
			os.system('clear')
		except:
			#для виндовс
			os.system('cls')
		#вывод ошибки
		print('введите число')
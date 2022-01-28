summa = 0

a = int(input("число: "))

while a >= 0:
	summa = summa + a
	a = int(input("число: "))

if summa == 0:
	print('вы не велли числа')
else:
	print(summa)	
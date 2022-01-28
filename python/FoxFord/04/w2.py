count = 0

a = input("введите строку: ")

while a != 'СТОП' and a != 'стоп' and a != 'чо':
	count += 1
	a = input("введите строку: ")

print(count)
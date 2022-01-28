s = 10000
p = 25

count = 0

while s <= 15000:
	s = s + s/100 * p
	count = count + 1
print('ссумма достигла 15к рублей')
print(count)
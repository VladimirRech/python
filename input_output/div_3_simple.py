# números menores que 904 divisíveis por 3

# start = 903
start = 500
numbers = 0

while start > 2:
#	print(start)
	if start % 3 == 0:
		numbers = numbers + 1
	
	start = start - 1
		
print("Numbers: ", numbers)

# Para encontrar o número, pegar o número desejad
# se for múltiplo de 3, dividir por 3
# se não for, diminuir 1 até chegar no múltiplo de 3

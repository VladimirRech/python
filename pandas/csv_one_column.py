# processa um arquivo csv com apenas uma coluna
# importando pandas
import pandas as pd
filename = 'csv_date.csv'

# lendo o arquivo
df = pd.read_csv(filename, sep=';')
# convertendo para uma lista
lst = df['date'].tolist()

# contagem 
print('\n\nContagem\n')

# executa o agrupamento
# funciona bem com datasets pequenos
freq = {x: lst.count(x) for x in lst}
print(freq)

for i in freq.keys():
	print(i, '-', freq[i])

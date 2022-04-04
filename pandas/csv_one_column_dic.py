#
# Transforma lista em dictionary
# Usa Counter para datasets maiores
#
from collections import Counter
import pandas as pd
filename = 'csv_date.csv'

# lendo o arquivo
df = pd.read_csv(filename, sep=';')
# convertendo para uma lista
lst = df['date'].tolist()

# Realiza contagem armazenando em um dictionary
counter = Counter(lst)

for item in counter.keys():
	print(item, ';', counter[item])

# converter dictionary para dataframe para poder ordenar
# é necessário realizar a conversão para usar os métodos da biblioteca pandas
# para a criação do dataframe, precisamos criar os nomes das colunas
df_new = pd.DataFrame(list(counter.items()), columns = ['date', 'occurrences'])
print(df_new)
print(type(df_new))

# Ordenando pelo número de ocorrências
print('\nOrdenando pelo número de ocorrências\n')
print(df_new.sort_values(by='occurrences', ascending=False))

# Ordenando pela data
print('\nOrdenando pela data\n')
print(df_new.sort_values(by='date', ascending=False))

# Valor máximo
print('\n** Resumos **')
print('\nOcorrências:\n')
print('\tValor máximo: ', df_new['occurrences'].max())
print('\tValor mínimo: ', df_new['occurrences'].min())
print('\tValor médio: ',  df_new['occurrences'].mean())

print('\nData:\n')
print('\tValor máximo: ', df_new['date'].max())
print('\tValor mínimo: ', df_new['date'].min())

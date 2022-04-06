#
# Transforma lista em dictionary
# Usa Counter para datasets maiores
#
import pandas as pd
from collections import Counter

filename = 'csv_integer.csv'
df = pd.read_csv(filename, sep=';')
print('Leu arquivo.', filename)

lst = df['id'].to_list()
print('Transformou em lista.')

dic = Counter(lst)
print('Fez a contagem.')

print('\nResultados da contagem:\n')
for x in dic.keys():
	print(x, ': ', dic[x])

# transforma novamente o dictionary em dataframe
df_new = pd.DataFrame(list(dic.items()), columns = ['id', 'occurrences'])
print(df_new)
print(type(df_new))

# Ordenando pelo número de ocorrências
print('\nOrdenando pelo número de ocorrências e exibindo os 20 principais\n')
print('\nMaior para o menor\n')
print(df_new.sort_values(by='occurrences', ascending=False).head(20))

print('\nOrdenando pelo número de ocorrências e exibindo os 20 principais\n')
print('\nMenor para o maior\n')
print(df_new.sort_values(by='occurrences', ascending=True).head(20))


# Ordenando pela data
print('\nOrdenando pelo id e exibindo os 20 principais\n')
print(df_new.sort_values(by='id', ascending=False).head(20))

# Valor máximo
print('\n** Resumos **')
print('\nOcorrências:\n')
print('\tValor máximo: ', df_new['occurrences'].max())
print('\tValor mínimo: ', df_new['occurrences'].min())
print('\tValor médio: ',  df_new['occurrences'].mean())

print('\nData:\n')
print('\tValor máximo: ', df_new['id'].max())
print('\tValor mínimo: ', df_new['id'].min())


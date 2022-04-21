#
# Contar palavras em uma coluna
#
import pandas as pd
from collections import Counter

file_name = '/home/vladimir/git/python/pandas/csv_many_columns.csv'
df = pd.read_csv(file_name, sep = ';')
print('Leu arquivo.')

# Resumo por ocorrêrncia de nomes
swap = df['firstname'].value_counts()
print(swap)

# O nome deve estar contido na coluna, caso contrário, causa exception
# swap = df['firstname'].value_counts()['Amalie']
# print('\nAmalie: ', swap)

# converte em lista o dataset
#lst = df['firstname'].to_list()
#dic = {'john': 0, 'Amalie': 0}

# percorre o dicionário para realizar a contagem
# for key in dic.keys():
#     swap = list(filter(lambda item: key.lower() in item.lower(), lst))
#     dic[key] += len(swap)

# exibe a contagem
# for key in dic.keys():
#     print(key, ': ', dic[key], '\n')

# repete a operação para a a coluna 'lastname'
#lst2 = df['lastname'].to_list()

# for key in dic.keys():
#     swap = list(filter(lambda item: key.lower() in item.lower(), lst2))
#     dic[key] += len(swap)

# # exibe a contagem
# for key in dic.keys():
#     print(key, ': ', dic[key], '\n')

# procresso final
lst_columns = [ 'firstname', 'lastname', 'email']
dic_words = { 'john': 0, 'amalie': 0, 'Jack': 0, 'vladimir': 0 }

for col_name in lst_columns:
    lst = df[col_name].to_list()

    for key in dic_words.keys():
        dic_words[key] += len(list(filter(lambda item: key.lower() in item.lower(), lst)))


# Exibe o resultado
print('\n* * * Resultados * * *\n')
for key in dic_words.keys():
    print(key, ': ', dic_words[key])
#
# vários exemplos de filtros
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
# converter dictionary para dataframe para poder ordenar
# é necessário realizar a conversão para usar os métodos da biblioteca pandas
# para a criação do dataframe, precisamos criar os nomes das colunas
df_new = pd.DataFrame(list(counter.items()), columns = ['date', 'occurrences'])

# iniciando alguns filtros
df_max_values = df_new[df_new.occurrences > 4]
print('\nCom 4+ ocorrências\n')
print(df_max_values.head(20))

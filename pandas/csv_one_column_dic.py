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

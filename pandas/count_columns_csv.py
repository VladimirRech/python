#
# Totaliza a contagem por colunas no arquivo CSV.
#
import pandas as pd
from collections import Counter

# recebe o nome do arquivo e variáveis para trabalhar
file_name = 'dataset1.csv'
col_sep = ';'
col_tot = 'code'
# carrega o arquivo para um DataFrame
df = pd.read_csv(file_name, sep = col_sep)
# gera p resumo
swap = df[col_tot].value_counts();
print(swap)

print('Done!')

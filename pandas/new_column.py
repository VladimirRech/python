import pandas as pd
file = 'elapsed.csv'

# Carrega arquivo fazendo conversão dos valores decimais
csv = pd.read_csv(file, sep='\t', engine="c", float_precision="round_trip")
print(csv.info())
print(csv.head(50))

# Cria uma nova coluna baseada nas existentes
# O nome das colunas é case sensitive
csv['calc'] = csv.Intervalo * csv.Custo
print(csv.head(50))

#
# Trabalhar com tempo decorrido
#
import pandas as pd
from datetime import datetime

fi = 'dataset2.csv'

csv = pd.read_csv(fi, sep=';')

print('File before transformation...\n')
print(csv.info())

csv['elapsed'] = pd.to_datetime(csv['end'], dayfirst=True) - pd.to_datetime(csv['start'], dayfirst=True)

print('File after transformation:\n')
print(csv.info())
print(csv.head())
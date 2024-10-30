#
# Trabalhar com tempo decorrido
#
import pandas as pd
from datetime import datetime

# Função para conversão de timedelta
# https://stackoverflow.com/questions/62103547/how-to-convert-timedelta-to-hours#62104474
def convert_to_hours(delta):
    total_seconds = delta.total_seconds()
    hours = str(int(total_seconds // 3600)).zfill(2)
    minutes = str(int((total_seconds % 3600) // 60)).zfill(2)
    seconds = str(int(total_seconds % 60)).zfill(2)
    return f"{hours}:{minutes}:{seconds}"

# lê arquivo
fi = 'dataset2.csv'
csv = pd.read_csv(fi, sep=';')

print('File before transformation...\n')
print(csv.info())

csv['elapsed'] = pd.to_datetime(csv['end'], dayfirst=True) - pd.to_datetime(csv['start'], dayfirst=True)
csv['elapsed1'] = '00:00:00'

print('File after first transformation:\n')
print(csv.info())
print(csv.head())
print('\n\n')

# transform
# iteration between elementso to can convert.
# https://bobbyhadz.com/blog/pandas-update-dataframe-while-iterating
for index, row in csv.iterrows():
    try:
        csv.at[index, 'elapsed1'] = convert_to_hours(csv.at[index, 'elapsed'])
    except:
        print('Ops...')

print('File after second transformation:\n')
print(csv.info())
print(csv.head())
print('\n\n')

csv.to_csv('temp.csv', index=False)
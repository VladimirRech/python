""""

1. Leia o arquivo.
2. Crie uma coluna que calcule a diferença entre as colunas "hire_date" e "fire_date"
   e armazene em uma coluna chamada "duration".
2. Faça o filtro apenas para os registros com os países "Brazil",
   "Portugal" e "Croatia".
3. Com os dados filtrados, traga o valor máximo para a coluna "duration"
   e o conteúdo das colunas "full_name" e "country".
4. Com os dados filtrados, traga o valor mínimo para a coluna "duration"
   e o conteúdo das colunas "full_name" e "country".
3. Com os dados filtrados, traga o valor médio para a coluna "duration"

Milestone 1
- Implantar conforme lista de funcionalidades.

Milestone 2
- Implantar tratamento de erros com exception.

Milestone 3
- Mostrar duração em anos, dias e meses.

"""
import pandas as pd
import sys
from datetime import timedelta

#
# Convert time delta to string containg Year, Months and days
# Input: timedelta value, return: string with year, months and days
#
def delta_to_string(delta):
    YEAR_DAYS = 365
    MONTH_DAYS = 30
    total_days = delta.days
    elapsed_years = total_days // YEAR_DAYS
    elapsed_months = (total_days % YEAR_DAYS) // MONTH_DAYS
    elapsed_days = (total_days % YEAR_DAYS) % MONTH_DAYS 
    str_ret = f"years: {elapsed_years}" if elapsed_years > 0 else ""
    str_ret = str_ret + f", " if len(str_ret) > 0 and elapsed_months > 0 else ""
    str_ret = str_ret + f"months: {elapsed_months}" if elapsed_months > 0 else ""
    str_ret = str_ret + f", " if len(str_ret) > 0 and elapsed_days > 0 else ""
    str_ret = str_ret + f"days: {elapsed_days}" if elapsed_days > 0 else ""
    return str_ret

filename = "job_duration.csv"
filter_column = "country"
filter_values = ["Brazil", "Portugal", "Croatia"]
duration_column = "duration"
has_error = False


try:
   df = pd.read_csv(filename, sep=';')
   df[duration_column] = pd.to_datetime(df["fire_date"]) - \
      pd.to_datetime(df["hire_date"])
   df_filtered = df[df[filter_column].isin(filter_values)]

   max_duration = df_filtered[duration_column].max()
   max_country = df_filtered[df_filtered[duration_column] == max_duration]["country"].values[0]
   max_full_name = df_filtered[df_filtered[duration_column] == max_duration]["full_name"].values[0]

   min_duration = df_filtered[duration_column].min()
   min_country = df_filtered[df_filtered[duration_column] == min_duration]["country"].values[0]
   min_full_name = df_filtered[df_filtered[duration_column] == min_duration]["full_name"].values[0]

   mean_duration = df_filtered[duration_column].mean()

except FileNotFoundError:
   has_error = True
   print(f"File {filename} not found.")

except Exception as e:
   has_error = True
   print(f"Ops, an error has ocurred: {e}")

finally:
   if has_error:
      sys.exit()

print("Results:\n")
print("\tMax values:\n")
print(f"\t\tDuration: {max_duration}, ({delta_to_string(max_duration)})\n\t\tCountry: {max_country}\n\t\tFull name: {max_full_name}\n\n")

print("\tMin values:\n")
print(f"\t\tDuration: {min_duration}, ({delta_to_string(min_duration)})\n\t\tCountry: {min_country}\n\t\tFull name: {min_full_name}\n\n")

print(f"\tMean: {mean_duration}, ({delta_to_string(mean_duration)})\n")

print("Done")
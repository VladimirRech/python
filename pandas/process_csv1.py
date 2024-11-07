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
print(f"\t\tDuration: {max_duration}\n\t\tCountry: {max_country}\n\t\tFull name: {max_full_name}\n\n")
print("Done")

print("\tMin values:\n")
print(f"\t\tDuration: {min_duration}\n\t\tCountry: {min_country}\n\t\tFull name: {min_full_name}\n\n")

print(f"\tMean: {mean_duration}\n")

print("Done")
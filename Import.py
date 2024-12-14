import pandas as pd

df = pd.read_csv("Datasets/SaludMental.csv", encoding='latin1')
# También puedes probar con 'ISO-8859-1' si el problema persiste:
# df = pd.read_csv("Datasets/SaludMental.csv", encoding='ISO-8859-1')

print(df.head())





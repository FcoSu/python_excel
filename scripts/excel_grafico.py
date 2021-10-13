import pandas as pd






workbook1 = "..\input\historico-accidente-mineria.xlsx"

input_cols= [1,2,3,7,6,13]

df = pd.read_excel(workbook1,sheet_name="hoja_1",header=0, usecols=input_cols)

print(df.shape)

df_cols= df.columns

for col in df_cols:
    print(df[col].head())



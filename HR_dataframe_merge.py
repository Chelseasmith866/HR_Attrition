import pandas as pd
df1 = pd.read_csv('HR_Baseline_Data.csv')
df2 = pd.read_csv('HRData (1).csv')
df3 = pd.read_csv('HRData (2).csv')
df4 = pd.read_csv('HRData (3).csv')
df5 = pd.read_csv('HRData (4).csv')
df6 = pd.read_csv('HRData (5).csv')
df7 = pd.read_csv('HRData (6).csv')
df8 = pd.read_csv('HRData (7).csv')
df9 = pd.read_csv('HRData (8).csv')
df10 = pd.read_csv('HRData (9).csv')
df11 = pd.read_csv('HRData (10).csv')
df12 = pd.read_csv('HRData (11).csv')
df13 = pd.read_csv('HRData (12).csv')
df14 = pd.read_csv('HRData (13).csv')
df15 = pd.read_csv('HRData (14).csv')

merged_df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15])

print(merged_df)

merged_df.to_csv('Merged_HRData.csv')

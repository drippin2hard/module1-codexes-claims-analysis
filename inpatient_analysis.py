import pandas as pd

df = pd.read_csv ('https://data.cms.gov/sites/default/files/2023-04/67157de9-d962-4af0-bf0e-3578b3afec58/inpatient.csv', sep='|')

print(df.head())

print(df.info())

print(df.columns)

# Identify codex-related columns (modify based on actual column names)
codex_columns = [col for col in df.columns if 'ICD' in col or 'DRG' in col or 'HCPCS' in col]
print(codex_columns)

for col in codex_columns:
    print(f"Frequency of values in {col}:")
    print(df[col].value_counts())

for col in codex_columns:
    print(f"Most common values in {col}:")
    print(df[col].value_counts().head())

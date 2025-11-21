import pandas as pd

# 1. Datei laden
file_path = 'C:/Users/justu/PycharmProjects/algo-trading-project/experiments/1/data/congress-trading-all_raw.csv' # Dateinamen anpassen
df = pd.read_csv(file_path, sep=';')

print(f"Gesamtzeilen geladen: {len(df)}")

# ---------------------------------------------------------
# A) Die sauberen Aktien filtern (ST, Stock, CS)
# ---------------------------------------------------------
clean_types = ['ST', 'Stock', 'CS']

# Filter: TickerType muss in der Liste sein
df_clean = df[df['TickerType'].isin(clean_types)]

# Speichern
df_clean.to_csv('C:/Users/justu/PycharmProjects/algo-trading-project/experiments/1/data/only_stock_purchases.csv', index=False)
print(f"--> 'clean_stocks.csv' erstellt mit {len(df_clean)} Zeilen.")

# ---------------------------------------------------------
# B) Die NaN-Werte isolieren (zum manuellen Check)
# ---------------------------------------------------------
# Filter: TickerType ist NaN (Not a Number / Leer)
df_nan = df[df['TickerType'].isna()]

# Speichern
df_nan.to_csv('C:/Users/justu/PycharmProjects/algo-trading-project/experiments/1/data/empty_tickerTyp.csv', index=False)
print(f"--> 'manual_check_nan.csv' erstellt mit {len(df_nan)} Zeilen.")

# ---------------------------------------------------------
# Optional: Zeige mal ein paar Beispiele aus den NaN-Daten
# oft erkennt man am Ticker, was es ist
# ---------------------------------------------------------
print("\n--- Beispielwerte aus den NaN-Daten (Ticker-Spalte) ---")
print(df_nan['Ticker'].value_counts().head(10))

# ---------------------------------------------------------
# C) Die Optionen filtern (Einfach nur speichern)
# ---------------------------------------------------------
option_types = ['OP', 'Stock Option', 'OI', 'OL', 'Call', 'Put']

# Filter: Behalte nur Zeilen, wo der Typ in der Liste ist
df_options = df[df['TickerType'].isin(option_types)]

# Speichern
output_path_opt = 'C:/Users/justu/PycharmProjects/algo-trading-project/experiments/1/data/optionTrades.csv'
df_options.to_csv(output_path_opt, index=False)

print(f"--> 'optionTrades.csv' erstellt mit {len(df_options)} Zeilen.")
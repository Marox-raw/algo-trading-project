import pandas as pd

# 1. Datei laden
file_path = 'C:/Users/justu/PycharmProjects/algo-trading-project/experiments/1/data/congress-trading-all_raw.csv' # Dateinamen anpassen
df = pd.read_csv(file_path, sep=';')

print(f"Gesamtzeilen geladen: {len(df)}")

# ---------------------------------------------------------
# A) Die saubere spalten mit Aktientrades filtern und in eine extra CSV packen (TradeType= ST, Stock, CS)
# ---------------------------------------------------------
clean_types = ['ST', 'Stock', 'CS']

# 1. Filter: TickerType muss in der Liste sein
df_clean = df[df['TickerType'].isin(clean_types)]

# 2. Filter: Alles rauswerfen, was "Exchange" ist, da dies oft keine aktiven Trades sind
# Das Symbol ~ bedeutet "NICHT". Wir behalten also alles, was NICHT "Exchange" enthält.
df_clean = df_clean[~df_clean['Transaction'].astype(str).str.contains('Exchange', case=False, na=False)]

# Speichern
df_clean.to_csv('C:/Users/justu/PycharmProjects/algo-trading-project/experiments/1/data/stockTrades.csv', index=False)
print(f"--> 'stockTrades.csv' erstellt mit {len(df_clean)} Zeilen.")

# ---------------------------------------------------------
# B) Die Spalten mitNaN-Werten in der TickerTyp Spalte in eine extra CSV File packen und alle spalten mit unset werten repepaieren
# ---------------------------------------------------------
print("Isoliere Zeilen ohne TickerType...")
df_nan = df[df['TickerType'].isna()].copy()

col_ticker = 'Ticker' if 'Ticker' in df_nan.columns else 'chehTicker'
print(f"Analysiere Spalte '{col_ticker}' auf Fehler...")


# Speichern
output_path_nan = 'C:/Users/justu/PycharmProjects/algo-trading-project/experiments/1/data/noTypDeclaredTrades.csv'
df_nan.to_csv(output_path_nan, index=False)

print(f"--> 'noTypDeclaredTrades.csv' erstellt mit {len(df_nan)} Zeilen.")

# Check
print(df_nan[col_ticker].head(5).values)

# ---------------------------------------------------------
# C) Die Optionen filtern und in einem neuen csv File speichern
# ---------------------------------------------------------
option_types = ['OP', 'Stock Option', 'OI', 'OL', 'Call', 'Put']

# 1. Filter: Behalte nur Zeilen, wo der Typ in der Liste ist
df_options = df[df['TickerType'].isin(option_types)]

# 2. Filter: Alles rauswerfen, was "Exchange" ist da dies oft keine aktiven Options-Trades sind
# Wir konvertieren zu string (.astype(str)), damit es nicht abstürzt, falls mal eine Zahl drinsteht
df_options = df_options[~df_options['Transaction'].astype(str).str.contains('Exchange', case=False, na=False)]

# 3. Alle Spalten die Unset sind rauswerfen
# Wir filtern die Spalte 'Transaction' auf das Wort 'Unset'
df_options = df_options[~df_options['Ticker'].astype(str).str.contains('Unset', case=False, na=False)]

# Speichern

# Speichern
output_path_opt = 'C:/Users/justu/PycharmProjects/algo-trading-project/experiments/1/data/optionTrades.csv'
df_options.to_csv(output_path_opt, index=False)

print(f"--> 'optionTrades.csv' erstellt mit {len(df_options)} Zeilen.")
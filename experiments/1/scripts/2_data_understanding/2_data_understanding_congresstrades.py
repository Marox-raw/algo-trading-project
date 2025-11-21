import pandas as pd

# 1. Datei laden (mit dem korrekten Trennzeichen ';')
file_path = 'C:/Users/justu/PycharmProjects/algo-trading-project/experiments/1/data/congress-trading-all_raw.csv'  # Pfad zur CSV-Datei
df = pd.read_csv(file_path, sep=';')

# -------------------------------------------------------
# ANALYSE 1: TickerType (Was wird gehandelt?)
# -------------------------------------------------------
print("=== VERTEILUNG DER ASSET-TYPEN (TickerType) ===")
# .value_counts() ist besser als unique(), weil du sofort siehst,
# ob 90% Aktien sind oder ob viel Müll dabei ist.
print(df['TickerType'].value_counts(dropna=False))

print("\n" + "-"*40 + "\n")

# -------------------------------------------------------
# ANALYSE 2: Ticker Symbole (chehTicker)
# -------------------------------------------------------
unique_tickers = df['Ticker'].unique()
num_tickers = len(unique_tickers)

print(f"=== ANZAHL UNTERSCHIEDLICHER AKTIEN: {num_tickers} ===")

print("\n--- Die Top 20 meistgehandelten Aktien ---")
# Zeigt die 20 Aktien, die am häufigsten in der Liste auftauchen
print(df['Ticker'].value_counts().head(20))

print("\n" + "-"*40 + "\n")

# -------------------------------------------------------
# ANALYSE 3: Transaktionsart (Transaction)
# -------------------------------------------------------
print("=== TRANSAKTIONSARTEN ===")
# Wichtig um zu sehen, wie 'Purchase' genau geschrieben wird
print(df['Transaction'].value_counts(dropna=False))
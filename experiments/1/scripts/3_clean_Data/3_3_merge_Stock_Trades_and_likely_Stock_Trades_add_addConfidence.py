import pandas as pd

# PFADE (Pass sie ggf. an)
path_verified = r"C:\Users\justu\PycharmProjects\algo-trading-project\experiments\1\data\stockTrades.csv"
path_inferred = r"C:\Users\justu\PycharmProjects\algo-trading-project\experiments\1\data\likely_stockTrades_from_noTypDeclared.csv"
path_output = r"C:\Users\justu\PycharmProjects\algo-trading-project\experiments\1\data\ALL_STOCK_TRADES_MERGED.csv"

# 1. Laden
print("Lade Dateien...")

try:
    df_ver = pd.read_csv(path_verified, sep=',')
    if len(df_ver.columns) < 2: df_ver = pd.read_csv(path_verified, sep=';')

    df_inf = pd.read_csv(path_inferred, sep=',')
    if len(df_inf.columns) < 2: df_inf = pd.read_csv(path_inferred, sep=';')
except Exception as e:
    print("Fehler beim Laden:", e)
    exit()

print(f"Verifizierte Stocks: {len(df_ver)}")
print(f"Wahrscheinliche Stocks: {len(df_inf)}")


# 2. Spalten angleichen (wichtig!)
# Manchmal heißt es 'chehTicker', manchmal 'Ticker'. Wir benennen um, falls nötig.
def standardize_cols(df):
    cols = df.columns
    if 'chehTicker' in cols:
        df.rename(columns={'chehTicker': 'Ticker'}, inplace=True)
    return df


df_ver = standardize_cols(df_ver)
df_inf = standardize_cols(df_inf)

# 3. Confidence Feature hinzufügen (Der Profi-Trick)
df_ver['Source_Confidence'] = 1.0  # 100% sicher
df_inf['Source_Confidence'] = 0.9  # 90% sicher (da gefiltert)

# 4. Zusammenfügen
df_total = pd.concat([df_ver, df_inf], ignore_index=True)

# 5. Duplikate entfernen
# Es kann passieren, dass ein Trade in beiden Listen auftaucht.
# Wir löschen Duplikate basierend auf Datum, Ticker und Betrag.
print(f"Zeilen vor Deduplizierung: {len(df_total)}")
df_total.drop_duplicates(subset=['Filed', 'Ticker', 'Trade_Size_USD', 'Transaction', 'Description'], keep='first',
                         inplace=True)
print(f"Zeilen nach Deduplizierung: {len(df_total)}")

# 6. Sortieren nach Datum (Filed Date)
# Sicherstellen, dass es ein Datetime-Objekt ist
df_total['Filed'] = pd.to_datetime(df_total['Filed'], errors='coerce')
df_total.sort_values(by='Filed', inplace=True)

# 7. Speichern
df_total.to_csv(path_output, index=False)

print("-" * 30)
print(f"FERTIG! Trainings-Set erstellt: {path_output}")
print(f"Gesamtanzahl Trades für das Training: {len(df_total)}")
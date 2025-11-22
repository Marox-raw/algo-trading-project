import pandas as pd

# ---------------------------------------------------------
# PFADE
# ---------------------------------------------------------
# Hier wird deine Datei geladen, in der die Typen fehlen
input_path = r"C:\Users\justu\PycharmProjects\algo-trading-project\experiments\1\data\noTypDeclaredTrades.csv"

# Hier wird das Ergebnis gespeichert
output_path = r"C:\Users\justu\PycharmProjects\algo-trading-project\experiments\1\data\likely_stockTrades_from_noTypDeclared.csv"

# Wörter, die wir NICHT haben wollen (Optionen)
bad_words = ['CALL', 'PUT', 'OPTION', 'EXP ', 'EXPIRES', 'STRIKE', 'WARRANT']

# ---------------------------------------------------------
# LOGIK
# ---------------------------------------------------------
print("Lade Daten...")
# Falls deine Datei mit Semikolon getrennt ist, ändere sep=',' zu sep=';'
df = pd.read_csv(input_path, sep=',')

print(f"Einträge gesamt: {len(df)}")
# ---------------------------------------------------------

# 2. Die Filter-Funktion
def is_likely_stock(row):
    # Hole Werte (nutze .get, falls Spalte fehlt, um Absturz zu vermeiden)
    ticker = str(row.get('Ticker', row.get('Ticker', ''))).upper()
    desc = str(row.get('Description', '')).upper()

    # REGEL A: Ticker darf keine Zahlen enthalten (Aktien haben nur Buchstaben)
    # (Optionen haben oft sowas wie 'AAPL2201...')
    if any(char.isdigit() for char in ticker):
        return False

    # REGEL B: Description darf keine Options-Wörter enthalten
    for word in bad_words:
        if word in desc:
            return False

    return True


# 3. Filter anwenden
df_rescued = df[df.apply(is_likely_stock, axis=1)].copy()

#Transaktiontyp "Exchange" rausfiltern, da dies oft keine aktiven Aktien-Trades sind

# Wir nehmen das Ergebnis von eben und werfen alles raus, was "Exchange" im Namen hat
df_rescued = df_rescued[~df_rescued['Transaction'].astype(str).str.contains('Exchange', case=False, na=False)]

# 4. Speichern
df_rescued.to_csv(output_path, index=False)

print("-" * 30)
print(f"FERTIG! Datei gespeichert unter:\n{output_path}")
print(f"Gerettete Aktien-Trades: {len(df_rescued)}")
print("-" * 30)
if not df_rescued.empty:
    print("Es wurden so viele Zeilen gerettet:")
    print(len(df_rescued))
    print("Beispiel für gerettete Beschreibung:")
    print(df_rescued['Description'].head(3).values)


# ---------------------------------------------------------
# Die wahrscheinlich OptionTrades extrahieren und speichern
# ---------------------------------------------------------
output_path_opt = r"C:\Users\justu\PycharmProjects\algo-trading-project\experiments\1\data\likely_optionTrades_from_noTypDeclared.csv"


def is_likely_option(row):
    val = row.get('Ticker', '')

    # Sicherheits-Check: Wenn Ticker leer ist, ist es auch keine Option (sondern Müll)
    if pd.isna(val) or str(val).strip() == '':
        return False

    ticker = str(val).upper().strip()
    desc = str(row.get('Description', '')).upper()

    # Es ist eine Option, wenn:
    # A: Zahlen im Ticker sind (z.B. AAPL22...) ODER
    # B: Ein "Bad Word" (Call, Put, Exp...) in der Description vorkommt
    is_digit_ticker = any(char.isdigit() for char in ticker)
    has_option_word = any(word in desc for word in bad_words)  # bad_words von oben nutzen

    return is_digit_ticker or has_option_word


# Filter anwenden
df_options = df[df.apply(is_likely_option, axis=1)].copy()

# TransaktionTyp "Exchange" rausfiltern, da dies oft keine aktiven Options-Trades sind
# Alles rauswerfen, was "Exchange" in der Spalte Transaction hat
df_options = df_options[~df_options['Transaction'].astype(str).str.contains('Exchange', case=False, na=False)]

# Speichern
df_options.to_csv(output_path_opt, index=False)

print("-" * 30)
print(f"FERTIG! Option-Datei erstellt unter:\n{output_path_opt}")
print(f"Gefundene wahrscheinliche Optionen: {len(df_options)}")
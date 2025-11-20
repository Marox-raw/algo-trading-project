In dem Experiment 1 wir probiert durch das kaufen und Verkaufen von Aktion von US-Congressmitgliedern und deren Familienmitgliedern Gewinne zu erzielen. 
Die Daten wurden von der Seite [quiverquant.com](https://www.quiverquant.com/) bezogen, die Informationen über die Aktienkäufe und -verkäufe von US-Kongressmitgliedern 
bereitstellt.
Dabei wird der Zeitpunkt, zu dem der Kauf getätigt, der Zeitpunkt der Veröffentlichung der Transaktion und die gekaufte Menge berücksichtigt.
Da wir keine kurzfristigen Trades durchführen wollen, wird immer nur jeder Tag einzeln betrachtet. Wir nehmen einfach den Preis der Aktie um 16:00 Uhr.
Darauf soll dann entscheidet werden, ob die Aktie gekauft oder verkauft wird. Es wird 16:00 Uhr gewählt, da dies der Zeitpunkt ist, an dem der Markt kurz 
vor dem Schließen steht und somit die meisten Informationen über den Tag bereits im Preis enthalten sind. Außerdem ist zu dieser Zeit noch ein geringer Spread vorhanden,
was Gewinne maximieren kann.
Das Ziel des Experiments war es, eine Handelsstrategie zu entwickeln, die auf diesen Daten basiert und den Markt outperformt (über 7% pro Jahr).
[]: # 
[]: # ## Datenvorbereitung
[]: # 
[]: # Die Daten wurden bereinigt und in ein geeignetes Format gebracht, um sie für die Analyse und das Modelltraining verwenden zu können
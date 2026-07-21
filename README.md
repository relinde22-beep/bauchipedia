# Bauchipedia – Interaktives Gefühlsraster

Ein einzelnes, in sich geschlossenes HTML-Widget (`index.html`), das die 184
Gefühlsbegriffe aus den vier Quadranten-Tabellen (angenehm/unangenehm ×
aktivierend/deaktivierend) als anklickbares, zoombares Raster darstellt.

## Funktionen

- Klick auf einen Begriff → Popup mit Beschreibung, Beispielsatz und Quadrant
- Verwandte Begriffe werden im Raster hervorgehoben
- Zoomen (Scrollen/Pinch/Buttons) und Verschieben (Ziehen) im Raster
- Suchfeld zum schnellen Finden eines Begriffs

Keine externen Abhängigkeiten (kein CDN, kein Plugin) – die Datei kann direkt
per WPBakery "Raw HTML"-Element eingebettet werden.

## Daten aktualisieren

Die Ausgangsdaten liegen als vier Excel-Tabellen in `data/*.xlsx` (Spalten:
Gefühlsbegriff, Beschreibung, Beispielsatz, Verwandte Begriffe). Nach einer
Änderung an den Tabellen:

```bash
pip install openpyxl rapidfuzz
python3 scripts/build_data.py      # erzeugt data/terms.json
python3 scripts/generate_html.py   # erzeugt index.html
```

`build_data.py` löst die "Verwandte Begriffe"-Spalte per Fuzzy-Matching gegen
die anderen Begriffe auf (toleriert kleine Tippfehler). Begriffe, die nur als
Verweis vorkommen aber keine eigene Zeile/Beschreibung haben, werden im Popup
als reiner Text (nicht anklickbar) angezeigt.

Die genaue Position jedes Begriffs im Raster wird beim Laden der Seite per
einfacher Kräftesimulation berechnet (verwandte Begriffe ziehen sich an,
alle Begriffe stoßen sich ab, jeder bleibt in seinem Quadranten) – es gibt
keine fest hinterlegten Koordinaten, das Layout aus dem Referenz-PDF wird
nicht pixelgenau nachgebaut.

## Einbindung in WordPress (WPBakery)

1. Seite/Beitrag bearbeiten → WPBakery-Element **"Raw HTML"** hinzufügen
2. Inhalt von `index.html` komplett hineinkopieren
3. Speichern/Aktualisieren

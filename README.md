# Bauchipedia – Interaktives Gefühlsraster

Ein in sich geschlossenes HTML-Widget, das die 184 Gefühlsbegriffe aus den
vier Quadranten-Tabellen (angenehm/unangenehm × aktivierend/deaktivierend)
als anklickbares, zoombares Raster darstellt.

Es gibt zwei Dateien mit demselben Inhalt, für zwei Zwecke:

- **`embed.html`** – nur der Widget-Code (Style + Markup + Script, ohne
  `<html>/<head>/<body>`). **Das ist die Datei zum Einbetten in WordPress.**
- **`index.html`** – dieselbe Sache als vollständige, eigenständige Seite,
  nur zum lokalen Anschauen im Browser (Doppelklick öffnen).

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
python3 scripts/generate_html.py   # erzeugt index.html und embed.html
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

**Wichtig:** `embed.html` niemals per Doppelklick öffnen bzw. in einem
Rich-Text-Programm (TextEdit im Rich-Text-Modus, Word, Pages, …) öffnen –
diese Programme interpretieren die HTML-Tags statt sie als Text anzuzeigen
und zerschießen dabei den Code (Sonderzeichen wie ü/− werden z. B. zu
"Ã¼"/"â^'"). Deshalb liegt zusätzlich `embed-code.txt` bei – exakt derselbe
Inhalt, nur mit `.txt`-Endung, damit jeder Editor ihn garantiert als reinen
Text öffnet.

1. `embed-code.txt` öffnen, kompletten Inhalt markieren und kopieren
   (Strg/Cmd+A, dann kopieren)
2. Seite/Beitrag im WPBakery-Backend bearbeiten → mit "+" ein Element
   hinzufügen → nach **"Raw HTML"** suchen und einfügen
3. Den kopierten Inhalt in das Textfeld einfügen
4. Speichern/Aktualisieren, dann die Seite ansehen

Das Widget passt sich in der Breite der Spalte an, in der es liegt, und ist
in der Höhe auf max. 760px begrenzt (Rand mit abgerundeten Ecken), damit es
sich wie ein normaler Seitenabschnitt einfügt statt den ganzen Bildschirm zu
beanspruchen.

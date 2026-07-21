import openpyxl, json, re
from rapidfuzz import process, fuzz

BASE = "/root/.claude/uploads/3f722902-a4d6-55d0-b13a-9e6c4eafbf65/"
FILES = [
    ("24cb98e4-Angenehm_hoch_Gefu_hlsbegriffe_Tabelle.xlsx", "angenehm", "hoch"),
    ("a93226ae-Angenehm_niedrig_Gefu_hlsbegriffe_Tabelle.xlsx", "angenehm", "niedrig"),
    ("d2d4fad3-unangenehmhoch_Gefu_hlsbegriffe_Tabelle.xlsx", "unangenehm", "hoch"),
    ("83f5bc35-unangenehmniedrig_Gefu_hlsbegriffe_Tabelle.xlsx", "unangenehm", "niedrig"),
]

def clean(s):
    if s is None:
        return ""
    return re.sub(r"\s+", " ", str(s).replace("\xa0", " ")).strip()

terms = []
seen_names = set()
for fname, valence, arousal in FILES:
    wb = openpyxl.load_workbook(BASE + fname, data_only=True)
    ws = wb.worksheets[0]
    rows = list(ws.iter_rows(min_row=2, values_only=True))
    for row in rows:
        term, desc, example, related = (row + (None, None, None, None))[:4]
        term = clean(term)
        if not term:
            continue
        desc = clean(desc)
        example = clean(example)
        related_raw = clean(related)
        related_list = [clean(x) for x in related_raw.split(",") if clean(x)]
        tid = f"{valence}-{arousal}-{len(terms)}"
        entry = {
            "id": tid,
            "term": term,
            "valence": valence,
            "arousal": arousal,
            "description": desc,
            "example": example,
            "related_raw": related_list,
        }
        terms.append(entry)

print("total terms:", len(terms))

# dedupe check
names = [t["term"] for t in terms]
dupes = set([n for n in names if names.count(n) > 1])
print("duplicate names:", dupes)

# build lookup for fuzzy matching related terms to actual term ids
name_to_id = {}
for t in terms:
    key = t["term"].strip().lower()
    name_to_id.setdefault(key, t["id"])

choices = list(name_to_id.keys())

unmatched = set()
for t in terms:
    resolved = []
    for r in t["related_raw"]:
        key = r.strip().lower()
        if key in name_to_id and name_to_id[key] != t["id"]:
            resolved.append(name_to_id[key])
            continue
        # fuzzy match
        match = process.extractOne(key, choices, scorer=fuzz.ratio, score_cutoff=82)
        if match:
            mid = name_to_id[match[0]]
            if mid != t["id"]:
                resolved.append(mid)
            continue
        unmatched.add(r)
    t["related"] = list(dict.fromkeys(resolved))  # dedupe preserve order
    del t["related_raw"]

print("unmatched related terms (kept as text-only, no link):", len(unmatched))
for u in sorted(unmatched):
    print("  -", u)

with open("/tmp/claude-0/-home-user-bauchipedia/3f722902-a4d6-55d0-b13a-9e6c4eafbf65/scratchpad/terms.json", "w", encoding="utf-8") as f:
    json.dump(terms, f, ensure_ascii=False, indent=None)

print("wrote terms.json, size(chars)=", len(json.dumps(terms, ensure_ascii=False)))

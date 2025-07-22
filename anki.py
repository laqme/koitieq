import genanki  # pip install genanki
import re
from pathlib import Path

koitieq_model = genanki.Model(
    1242756152,
    "Kóıtıeq Model",
    fields=[
        {"name": "Toaq"},
        {"name": "English"},
        {"name": "Chapter"},
    ],
    templates=[
        {
            "name": "Toaq to English",
            "qfmt": "<h1 class=t>{{Toaq}}</h1>",
            "afmt": '{{FrontSide}}<hr id="answer"><div class="ans">{{English}}</div>',
        },
        {
            "name": "English to Toaq",
            "qfmt": "<h1>{{English}}</h1>",
            "afmt": '{{FrontSide}}<hr id="answer"><div class="ans t">{{Toaq}}</div>',
        },
    ],
    css=r"""
        body { font-family: "Fira Sans", Verdana, Arial, sans-serif; text-align: center; }
        h1 { font-size: 24px; }
        .ans { font-size: 20px; }
        .t { color: #27e; }
        .v { font-weight: normal; padding: 0.1em 0.2em; margin: -0.1em 0; border: 1px solid currentColor; border-radius: 2px; font-size: 0.8em; }
    """,
)

deck = genanki.Deck(1472446179, "Kóıtıeq")

re_vocab_item = re.compile(r"^\| _([^_]+)_\{:\.t\} \| (.+) \|$")

vocab_dict = {}

for fn in Path("./_chapters").glob("*.md"):
    chapter = int(fn.name[:2])
    if chapter <= 2:  # Skip phonology
        continue
    with open(fn) as f:
        for line in f:
            line = re.sub(r"\*\*([^*]+)\*\*\{:\.v\}", r"<span class=v>\1</span>", line)
            line = line.replace("...", "…")
            m = re.match(re_vocab_item, line)
            if not m:
                continue

            toaq = m[1]
            english = re.sub(r"_([^_]+)_", r"<em>\1</em>", m[2])
            if chapter == 15 and "–" in m[2]:
                continue  # Skip fancy month names

            fields = [toaq, english, str(chapter)]
            deck.add_note(genanki.Note(model=koitieq_model, fields=fields))
            if toaq in vocab_dict:
                print(f"!!! Duplicate word: {toaq} in {vocab_dict[toaq]} and {chapter}")
            vocab_dict[toaq] = chapter

genanki.Package(deck).write_to_file("Koitieq.apkg")

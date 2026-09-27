#!/usr/bin/env python3
"""
Export flashcards from Obsidian vault to Anki .apkg format.
Run weekly to sync new/updated cards to mobile.
"""

import genanki
import yaml
import re
from pathlib import Path
import hashlib

VAULT_ROOT = Path('/Users/sukesh/Documents/GitHub/Obsidian')
OUTPUT_DIR = VAULT_ROOT / '_exports' / 'anki'
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Anki model for basic Q&A cards
BASIC_MODEL = genanki.Model(
    1607392319,
    'Obsidian Basic',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
        {'name': 'Source'},
        {'name': 'Tags'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Question}}<br><br><small>{{Source}}</small>',
            'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}<br><br><small>{{Tags}}</small>',
        },
    ],
    css="""
.card { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto; font-size: 16px; line-height: 1.5; }
hr { border: 0; border-top: 1px solid #ddd; margin: 15px 0; }
small { color: #666; font-size: 12px; }
.code { background: #f5f5f5; padding: 2px 6px; border-radius: 4px; font-family: monospace; }
""")

# Anki model for cloze deletion
CLOZE_MODEL = genanki.Model(
    998877665,
    'Obsidian Cloze',
    fields=[
        {'name': 'Text'},
        {'name': 'Extra'},
        {'name': 'Source'},
        {'name': 'Tags'},
    ],
    templates=[
        {
            'name': 'Cloze',
            'qfmt': '{{cloze:Text}}<br><br><small>{{Source}}</small>',
            'afmt': '{{cloze:Text}}<br><br>{{Extra}}<br><br><small>{{Tags}}</small>',
        },
    ],
    model_type=genanki.Model.CLOZE,
    css=BASIC_MODEL.css)


def extract_flashcards_from_file(file_path: Path):
    """Extract #flashcard blocks from a markdown file."""
    content = file_path.read_text(encoding='utf-8')
    if not content.startswith('---'):
        return []

    parts = content.split('---', 2)
    if len(parts) < 3:
        return []

    try:
        fm = yaml.safe_load(parts[1]) or {}
    except Exception:
        fm = {}

    body = parts[2]
    rel_path = file_path.relative_to(VAULT_ROOT)
    source = str(rel_path)
    tags = fm.get('tags', [])
    if isinstance(tags, str):
        tags = [tags]
    tag_str = ' '.join(f'obsidian:{t}' for t in tags)
    tag_str += f' vault:{rel_path.parts[0]}'

    cards = []

    # Pattern 1: #flashcard\n**Q:** ... :: **A:** ... #flashcard
    pattern1 = r'#flashcard\s*\n\*\*Q:\*\*\s*(.+?)\s*::\s*\*\*A:\*\*\s*(.+?)\s*#flashcard'
    for match in re.finditer(pattern1, body, re.DOTALL):
        q = match.group(1).strip()
        a = match.group(2).strip()
        cards.append({
            'question': q,
            'answer': a,
            'source': source,
            'tags': tag_str,
            'type': 'basic'
        })

    # Pattern 2: > **Q:** ... :: **A:** ...
    pattern2 = r'> \*\*Q:\*\*\s*(.+?)\s*::\s*\*\*A:\*\*\s*(.+?)(?:\n|$)'
    for match in re.finditer(pattern2, body, re.DOTALL):
        q = match.group(1).strip()
        a = match.group(2).strip()
        cards.append({
            'question': q,
            'answer': a,
            'source': source,
            'tags': tag_str,
            'type': 'basic'
        })

    # Pattern 3: Cloze deletions {{c1::text}}
    for para in body.split('\n\n'):
        if '{{c' in para:
            cards.append({
                'text': para.strip(),
                'extra': '',
                'source': source,
                'tags': tag_str,
                'type': 'cloze'
            })

    return cards


def generate_deck_name(vault_name: str, category: str = None):
    """Generate Anki deck name."""
    if category:
        return f'Obsidian::{vault_name}::{category}'
    return f'Obsidian::{vault_name}'


def build_deck(vault_path: Path, vault_name: str):
    """Build Anki deck for a vault."""
    categories = {}

    # Collect all flashcards
    all_cards = []
    for md_file in vault_path.rglob('*.md'):
        if '_templates' in md_file.parts or '_attachments' in md_file.parts:
            continue
        if md_file.name in ('README.md', 'IMPROVEMENT_PLAN.md'):
            continue

        cards = extract_flashcards_from_file(md_file)
        all_cards.extend(cards)

    # Group by category (first folder)
    for card in all_cards:
        cat = card['source'].split('/')[1] if '/' in card['source'] else 'General'
        if cat not in categories:
            categories[cat] = genanki.Deck(
                abs(hash(f'{vault_name}::{cat}')) % (10**10),
                generate_deck_name(vault_name, cat)
            )

    # Add cards to category decks
    for cat_name, cat_deck in categories.items():
        cat_cards = [c for c in all_cards if c['source'].split('/')[1] == cat_name]
        for card in cat_cards:
            if card['type'] == 'basic':
                note = genanki.Note(
                    model=BASIC_MODEL,
                    fields=[card['question'], card['answer'], card['source'], card['tags']],
                    tags=card['tags'].split()
                )
            else:
                note = genanki.Note(
                    model=CLOZE_MODEL,
                    fields=[card['text'], card['extra'], card['source'], card['tags']],
                    tags=card['tags'].split()
                )
            cat_deck.add_note(note)

    return categories


def main():
    print("Building Anki decks from Obsidian vaults...")

    vaults = {
        'Java': VAULT_ROOT / 'Java',
        'Architect': VAULT_ROOT / 'Architect',
        'AI': VAULT_ROOT / 'AI',
        'CodingPatterns': VAULT_ROOT / 'Coding Patterns',
    }

    all_decks = []
    total_cards = 0

    for vault_name, vault_path in vaults.items():
        if not vault_path.exists():
            print(f"  Skipping {vault_name}: not found")
            continue

        print(f"  Processing {vault_name}...")
        categories = build_deck(vault_path, vault_name)

        for cat_name, cat_deck in categories.items():
            if len(cat_deck.notes) > 0:
                output_file = OUTPUT_DIR / f'{vault_name}_{cat_name}.apkg'
                genanki.Package(cat_deck).write_to_file(str(output_file))
                print(f"    {cat_name}: {len(cat_deck.notes)} cards -> {output_file.name}")
                total_cards += len(cat_deck.notes)
                all_decks.append(cat_deck)

    # Combined deck
    combined = genanki.Deck(
        1234567890,
        'Obsidian::All'
    )
    for deck in all_decks:
        for note in deck.notes:
            combined.add_note(note)

    if len(combined.notes) > 0:
        combined_file = OUTPUT_DIR / 'Obsidian_All.apkg'
        genanki.Package(combined).write_to_file(str(combined_file))
        print(f"\n  Combined: {len(combined.notes)} cards -> {combined_file.name}")

    print(f"\nTotal cards exported: {total_cards}")
    print(f"Output directory: {OUTPUT_DIR}")


if __name__ == '__main__':
    main()
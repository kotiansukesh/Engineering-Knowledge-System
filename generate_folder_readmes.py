#!/usr/bin/env python3
"""
Generate folder README.md files for all vaults using the Folder-README-Template.
"""

import os
from pathlib import Path
from datetime import datetime

VAULT_ROOT = Path('/Users/sukesh/Documents/GitHub/Obsidian')
TEMPLATE_PATH = VAULT_ROOT / '_templates' / 'Folder-README-Template.md'

# Read template
template = TEMPLATE_PATH.read_text(encoding='utf-8')

# Vaults and their folder structures
VAULT_FOLDERS = {
    'Java': [
        '00_Java-25-Overview',
        '01_Core-Java',
        '02_OOP',
        '03_Collections',
        '04_Concurrency',
        '05_Spring',
        '06_Design-Patterns',
        '07_DSA',
        '08_Modern-Java',
        '09_Java-21-LTS',
        '10_LLD-Machine-Coding',
        '99_Revision',
    ],
    'Architect': [
        '01_Architecture-Foundations',
        '02_Requirements-Quality-Attributes',
        '03_Architecture-Styles',
        '04_Design-Patterns-Building-Blocks',
        '05_DDD-Modeling',
        '06_Data-Architecture',
        '07_Integration-APIs',
        '08_NonFunctional-Ops',
        '09_Governance-Documentation',
        '10_System-Design-Interviews',
        '11_Real-World-Case-Studies',
        '99_Revision',
    ],
    'AI': [
        '01_Fundamentals',
        '02_RAG-Engineering',
        '03_Agentic-AI',
        '04_Production-Platform',
        '05_Kubernetes-Operations',
        '06_Architecture-Governance',
        '07_Cross-Cutting',
        '99_Revision',
    ],
    'Coding Patterns': [
        '01_Array',
        '02_LinkedList',
        '03_Stack_Heap',
        '04_Intervals_Search',
        '05_Trees_Graphs',
        '06_Matrix',
        '07_Backtracking_DP',
        '08_Bit_Manipulation',
        '99_Revision',
    ],
}

def generate_readme(vault: str, folder: str):
    """Generate README for a folder."""
    folder_path = VAULT_ROOT / vault / folder
    readme_path = folder_path / 'README.md'
    
    # Skip if folder doesn't exist
    if not folder_path.exists():
        print(f"  SKIP (no folder): {vault}/{folder}")
        return False
    
    # Count notes in folder
    notes = list(folder_path.glob('*.md'))
    notes = [n for n in notes if n.name != 'README.md' and not n.name.startswith('.')]
    
    # Get subfolder names
    subfolders = [d.name for d in folder_path.iterdir() if d.is_dir() and not d.name.startswith('.')]
    
    # Replace template variables
    folder_name = folder.replace('_', ' ').replace('-', ' ').title()
    category = f"{vault}/{folder}"
    vault_name = vault
    date_str = datetime.now().strftime('%Y-%m-%d')
    
    content = template
    content = content.replace('{{folder_name}}', folder_name)
    content = content.replace('{{category}}', category)
    content = content.replace('{{vault_name}}', vault_name)
    content = content.replace('{{date:YYYY-MM-DD}}', date_str)
    content = content.replace('{{FOLDER_TITLE}}', folder_name)
    content = content.replace('{{NOTE_COUNT}}', str(len(notes)))
    content = content.replace('{{SUBFOLDER_LIST}}', '\n'.join([f'- [[{vault}/{folder}/{sf}/README|{sf}]]' for sf in subfolders]) if subfolders else '*(no subfolders)*')
    content = content.replace('{{VAULT_MOC}}', f'[[{vault}/README|{vault} MOC]]')
    
    # Write
    readme_path.write_text(content, encoding='utf-8')
    print(f"  GENERATED: {vault}/{folder}/README.md ({len(notes)} notes)")
    return True

def main():
    print("Generating folder READMEs...")
    total = 0
    for vault, folders in VAULT_FOLDERS.items():
        print(f"\n{vault}:")
        for folder in folders:
            if generate_readme(vault, folder):
                total += 1
    print(f"\nTotal generated: {total}")

if __name__ == '__main__':
    main()
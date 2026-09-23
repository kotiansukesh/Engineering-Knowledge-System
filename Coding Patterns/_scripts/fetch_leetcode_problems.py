#!/usr/bin/env python3
"""
Fetch LeetCode problem details and update Obsidian pattern notes.

Usage:
  python fetch_leetcode_problems.py                    # Update all notes in Coding Patterns
  python fetch_leetcode_problems.py --note "01_Array/03 - Sliding Window.md"  # Single note
  python fetch_leetcode_problems.py --dry-run          # Preview changes
"""

import os
import json
import re
import yaml
import requests
import time
import argparse
from html import unescape

# Paths
NOTES_DIR = "/Users/sukesh/Documents/GitHub/Obsidian/Coding Patterns"
CACHE_FILE = "/tmp/leetcode_problems_cache.json"

# LeetCode GraphQL query
QUERY = """
query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId
    title
    titleSlug
    content
    difficulty
    exampleTestcases
    sampleTestCase
    hints
    similarQuestions
    stats
    topicTags {
      name
      slug
    }
  }
}
"""

def get_slug_mapping():
    """Get mapping from problem ID to titleSlug"""
    url = "https://leetcode.com/api/problems/all/"
    resp = requests.get(url, timeout=30)
    data = resp.json()
    mapping = {}
    for p in data['stat_status_pairs']:
        mapping[str(p['stat']['frontend_question_id'])] = p['stat']['question__title_slug']
    return mapping

def fetch_problem(pid, slug_map, session):
    """Fetch a single problem from LeetCode"""
    if str(pid) not in slug_map:
        return None
    slug = slug_map[str(pid)]
    variables = {"titleSlug": slug}
    resp = session.post(
        "https://leetcode.com/graphql",
        json={"query": QUERY, "variables": variables},
        timeout=30
    )
    data = resp.json()
    if 'data' in data and data['data']['question']:
        return data['data']['question']
    return None

def clean_html(html):
    """Clean LeetCode HTML content"""
    if not html:
        return ""
    html = re.sub(r'<sup>(.*?)</sup>', r'^\1^', html)
    html = re.sub(r'<sub>(.*?)</sub>', r'_\1_', html)
    html = re.sub(r'<br\s*/?>', '\n', html)
    html = html.replace('&nbsp;', ' ')
    html = re.sub(r'<[^>]+>', '', html)
    html = unescape(html)
    html = re.sub(r'\n{3,}', '\n\n', html)
    return html.strip()

def extract_problem_statement(content):
    """Extract problem statement (before first Example)"""
    match = re.search(r'(Example \d+:|Constraints:)', content)
    if match:
        return content[:match.start()].strip()
    return content.strip()

def extract_examples(content):
    """Extract examples - up to 3"""
    examples = []
    pattern = r'(Example \d+:.*?)(?=Example \d+:|Constraints:|$)'
    matches = re.findall(pattern, content, re.DOTALL)
    for m in matches[:3]:
        examples.append(m.strip())
    return examples

def generate_problems_section(problem_ids, problems_data):
    """Generate the Problems markdown section"""
    lines = ["## Problems", ""]
    for pid in problem_ids:
        pid_str = str(pid)
        if pid_str not in problems_data:
            lines.append(f"### {pid}. Problem Not Found")
            lines.append(f"> [LeetCode {pid}](https://leetcode.com/problems/) • Could not fetch")
            lines.append("")
            lines.append("---")
            lines.append("")
            continue
        
        q = problems_data[pid_str]
        content = clean_html(q['content'])
        statement = extract_problem_statement(content)
        examples = extract_examples(content)
        tags = [t['name'] for t in q.get('topicTags', [])]
        tag_str = ', '.join(tags) if tags else 'N/A'
        
        lines.append(f"### {pid}. {q['title']} ({q['difficulty']})")
        lines.append(f"> [LeetCode {pid}](https://leetcode.com/problems/{q['titleSlug']}/) • Tags: {tag_str}")
        lines.append("")
        lines.append("**Problem Statement:**")
        lines.append("")
        lines.append(statement)
        lines.append("")
        if examples:
            lines.append("**Examples:**")
            lines.append("")
            for ex in examples:
                lines.append(ex)
                lines.append("")
        lines.append("---")
        lines.append("")
    return "\n".join(lines)

def update_note(note_path, problems_data, dry_run=False):
    """Update a single note with Problems section"""
    with open(note_path, 'r') as f:
        content = f.read()
    
    # Extract leetcode IDs from frontmatter
    fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not fm_match:
        print(f"  ⚠ No frontmatter in {note_path}")
        return False
    
    fm = yaml.safe_load(fm_match.group(1))
    problem_ids = fm.get('leetcode', [])
    if not problem_ids:
        print(f"  ⚠ No leetcode problems in {note_path}")
        return False
    
    # Generate new Problems section
    new_problems_section = generate_problems_section(problem_ids, problems_data)
    
    # Replace existing Problems section or insert after Diagram
    pattern = r'(## Problems\n).*?(?=\n## )'
    if re.search(pattern, content, re.DOTALL):
        # Replace existing
        new_content = re.sub(pattern, new_problems_section + "\n", content, flags=re.DOTALL)
    else:
        # Insert after Diagram
        diagram_pattern = r'(## Diagram\n.*?)(?=\n## )'
        match = re.search(diagram_pattern, content, re.DOTALL)
        if match:
            end_pos = match.end()
            new_content = content[:end_pos] + "\n\n" + new_problems_section + "\n" + content[end_pos:]
        else:
            print(f"  ⚠ Could not find insertion point in {note_path}")
            return False
    
    if dry_run:
        print(f"  Would update: {note_path}")
        # Show first 200 chars of new section
        idx = new_content.find("## Problems")
        print(f"  Preview: {new_content[idx:idx+300]}...")
        return True
    
    with open(note_path, 'w') as f:
        f.write(new_content)
    print(f"  ✓ Updated: {note_path}")
    return True

def main():
    parser = argparse.ArgumentParser(description="Fetch LeetCode problems and update Obsidian notes")
    parser.add_argument("--note", help="Specific note to update (relative to NOTES_DIR)")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without writing")
    parser.add_argument("--force-refresh", action="store_true", help="Ignore cache and re-fetch")
    args = parser.parse_args()
    
    # Load or fetch problem data
    if os.path.exists(CACHE_FILE) and not args.force_refresh:
        print("Loading cached problem data...")
        with open(CACHE_FILE, 'r') as f:
            problems_data = json.load(f)
    else:
        print("Fetching problem data from LeetCode...")
        slug_map = get_slug_mapping()
        
        # Collect all unique problem IDs from all notes
        all_pids = set()
        for root, dirs, files in os.walk(NOTES_DIR):
            for f in files:
                if f.endswith('.md') and not f.startswith('_') and f not in ['README.md', 'Cheat Sheet.md', 'DSA-Roadmap-AlgoMaster.md', 'Interview-Bank.md', 'Dashboard.md', 'Study Plan.md']:
                    path = os.path.join(root, f)
                    with open(path, 'r') as fp:
                        c = fp.read()
                    fm_match = re.match(r'^---\n(.*?)\n---', c, re.DOTALL)
                    if fm_match:
                        fm = yaml.safe_load(fm_match.group(1))
                        if fm.get('leetcode'):
                            all_pids.update(str(p) for p in fm['leetcode'])
        
        print(f"Found {len(all_pids)} unique problems across notes")
        
        session = requests.Session()
        problems_data = {}
        for pid in sorted(all_pids, key=int):
            print(f"  Fetching {pid}...", end=" ", flush=True)
            q = fetch_problem(pid, slug_map, session)
            if q:
                problems_data[pid] = q
                print(f"✓ {q['title']}")
            else:
                print(f"✗ Failed")
            time.sleep(0.1)
        
        with open(CACHE_FILE, 'w') as f:
            json.dump(problems_data, f, indent=2)
        print(f"Cached {len(problems_data)} problems to {CACHE_FILE}")
    
    # Update notes
    if args.note:
        note_path = os.path.join(NOTES_DIR, args.note)
        if os.path.exists(note_path):
            update_note(note_path, problems_data, args.dry_run)
        else:
            print(f"Note not found: {note_path}")
    else:
        # Update all pattern notes
        for root, dirs, files in os.walk(NOTES_DIR):
            for f in files:
                if f.endswith('.md') and not f.startswith('_') and f not in ['README.md', 'Cheat Sheet.md', 'DSA-Roadmap-AlgoMaster.md', 'Interview-Bank.md', 'Dashboard.md', 'Study Plan.md']:
                    path = os.path.join(root, f)
                    update_note(path, problems_data, args.dry_run)

if __name__ == "__main__":
    main()
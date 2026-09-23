#!/usr/bin/env node
/**
 * Retrofit Coding Patterns notes with Templater-compatible frontmatter.
 * 
 * Parses existing frontmatter, ensures all required fields exist with defaults,
 * standardizes date format to YYYY-MM-DD, ensures tags are arrays with pattern/ prefix,
 * ensures leetcode is array of integers, adds missing reviewed/sr-due fields.
 * Keeps body content unchanged. Writes back to same file.
 */

const fs = require('fs');
const path = require('path');
const matter = require('gray-matter');

// Required frontmatter fields with their default values
const REQUIRED_FIELDS = {
  title: '',
  pattern: 0,
  category: '',
  tags: [],
  leetcode: [],
  created: '',           // Will default to today if missing
  completed: false,
  reviewed: '',          // Empty string default
  'sr-due': '',          // Empty string default
  difficulty: 'Medium',
  source: ''
};

// Pattern-specific tag prefixes
const PATTERN_TAG_PREFIXES = {
  '01_Array': 'pattern/array',
  '02_LinkedList': 'pattern/linkedlist',
  '03_Stack_Heap': 'pattern/stack',
  '04_Intervals_Search': 'pattern/intervals',
  '05_Trees_Graphs': 'pattern/tree',
  '06_Matrix': 'pattern/matrix',
  '07_Backtracking_DP': 'pattern/dp',
  '08_Bit_Manipulation': 'pattern/bit-manipulation'
};

/**
 * Normalize date to YYYY-MM-DD format
 */
function normalizeDate(dateStr) {
  if (!dateStr) return '';
  
  const str = String(dateStr).trim();
  
  // Already in YYYY-MM-DD
  if (/^\d{4}-\d{2}-\d{2}$/.test(str)) {
    return str;
  }
  
  // Try parsing various formats
  const date = new Date(str);
  if (isNaN(date.getTime())) {
    console.warn(`  ⚠ Could not parse date: "${dateStr}", using today`);
    return new Date().toISOString().split('T')[0];
  }
  
  return date.toISOString().split('T')[0];
}

/**
 * Ensure tags is an array with pattern/ prefix
 */
function normalizeTags(tags, patternDir) {
  if (!tags) return [];
  
  let tagArray;
  if (Array.isArray(tags)) {
    tagArray = tags;
  } else if (typeof tags === 'string') {
    // Handle comma-separated or space-separated strings
    tagArray = tags.split(/[,\s]+/).filter(t => t);
  } else {
    tagArray = [];
  }
  
  // Normalize each tag
  const normalized = tagArray.map(tag => {
    const t = String(tag).trim();
    // Ensure pattern/ prefix
    if (!t.startsWith('pattern/')) {
      // Use pattern directory to get proper prefix
      const prefix = PATTERN_TAG_PREFIXES[patternDir] || 'pattern/unknown';
      return `${prefix}/${t}`;
    }
    return t;
  });
  
  // Deduplicate
  return [...new Set(normalized)];
}

/**
 * Ensure leetcode is array of integers
 */
function normalizeLeetcode(leetcode) {
  if (!leetcode) return [];
  
  let arr;
  if (Array.isArray(leetcode)) {
    arr = leetcode;
  } else if (typeof leetcode === 'string') {
    arr = leetcode.split(/[,\s]+/).filter(s => s);
  } else if (typeof leetcode === 'number') {
    arr = [leetcode];
  } else {
    arr = [];
  }
  
  return arr.map(v => {
    const num = parseInt(v, 10);
    return isNaN(num) ? null : num;
  }).filter(v => v !== null);
}

/**
 * Process a single markdown file
 */
function processFile(filePath, baseDir) {
  const content = fs.readFileSync(filePath, 'utf8');
  const parsed = matter(content);
  
  let data = parsed.data;
  let modified = false;
  
  // Ensure all required fields exist
  for (const [key, defaultValue] of Object.entries(REQUIRED_FIELDS)) {
    if (!(key in data) || data[key] === undefined || data[key] === null) {
      data[key] = defaultValue;
      modified = true;
    }
  }
  
  // Normalize created date
  if (data.created) {
    const normalized = normalizeDate(data.created);
    if (normalized !== data.created) {
      data.created = normalized;
      modified = true;
    }
  } else {
    data.created = new Date().toISOString().split('T')[0];
    modified = true;
  }
  
  // Normalize tags with pattern/ prefix
  // Extract pattern category from file path (e.g., "01_Array", "02_LinkedList")
  const relativePath = path.relative(baseDir, filePath);
  const patternDir = relativePath.split(path.sep)[0]; // e.g., "01_Array"
  const normalizedTags = normalizeTags(data.tags, patternDir);
  if (JSON.stringify(normalizedTags) !== JSON.stringify(data.tags || [])) {
    data.tags = normalizedTags;
    modified = true;
  }
  
  // Normalize leetcode to array of integers
  const normalizedLeetcode = normalizeLeetcode(data.leetcode);
  if (JSON.stringify(normalizedLeetcode) !== JSON.stringify(data.leetcode || [])) {
    data.leetcode = normalizedLeetcode;
    modified = true;
  }
  
  // Ensure reviewed and sr-due exist (empty string if missing)
  if (!data.reviewed || data.reviewed === '') {
    data.reviewed = '';
    modified = true;
  }
  if (!data['sr-due'] || data['sr-due'] === '') {
    data['sr-due'] = '';
    modified = true;
  }
  
  // Ensure difficulty is valid
  const validDifficulties = ['Easy', 'Medium', 'Hard'];
  if (!validDifficulties.includes(data.difficulty)) {
    data.difficulty = 'Medium';
    modified = true;
  }
  
  // Ensure pattern is a number
  if (typeof data.pattern === 'string') {
    data.pattern = parseInt(data.pattern, 10) || 0;
    modified = true;
  }
  
  // Ensure completed is boolean
  if (typeof data.completed === 'string') {
    data.completed = data.completed.toLowerCase() === 'true';
    modified = true;
  }
  
  // Write back if modified
  if (modified) {
    const output = matter.stringify(parsed.content, data);
    fs.writeFileSync(filePath, output, 'utf8');
    console.log(`  ✓ Updated: ${path.relative(process.cwd(), filePath)}`);
    return true;
  } else {
    console.log(`  - No changes: ${path.relative(process.cwd(), filePath)}`);
    return false;
  }
}

/**
 * Find all pattern markdown files (excluding READMEs and template)
 */
function findPatternFiles() {
  // Get the actual workspace root (where Coding Patterns folder lives)
  const workspaceRoot = path.resolve(__dirname, '..');
  const baseDir = path.join(workspaceRoot, 'Coding Patterns');
  const patternDirs = [
    '01_Array',
    '02_LinkedList', 
    '03_Stack_Heap',
    '04_Intervals_Search',
    '05_Trees_Graphs',
    '06_Matrix',
    '07_Backtracking_DP',
    '08_Bit_Manipulation'
  ];
  
  const files = [];
  
  for (const dir of patternDirs) {
    const dirPath = path.join(baseDir, dir);
    if (!fs.existsSync(dirPath)) continue;
    
    const entries = fs.readdirSync(dirPath);
    for (const entry of entries) {
      if (entry.endsWith('.md') && entry !== 'README.md') {
        files.push(path.join(dirPath, entry));
      }
    }
  }
  
  return { files, baseDir };
}

/**
 * Main
 */
function main() {
  console.log('🔧 Retrofitting Coding Patterns frontmatter...\n');
  
  const { files, baseDir } = findPatternFiles();
  console.log(`Found ${files.length} pattern files to process:\n`);
  
  let updated = 0;
  let errors = 0;
  
  for (const file of files) {
    try {
      if (processFile(file, baseDir)) updated++;
    } catch (err) {
      console.error(`  ✗ Error processing ${file}:`, err.message);
      errors++;
    }
  }
  
  console.log(`\n✅ Done! Updated: ${updated}, Errors: ${errors}, Total: ${files.length}`);
}

main();
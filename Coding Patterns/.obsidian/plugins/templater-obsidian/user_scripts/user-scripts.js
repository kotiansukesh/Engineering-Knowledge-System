/**
 * Templater User Scripts for Coding Patterns Vault
 * 
 * Place this file in your Templater config folder (usually .obsidian/plugins/templater/scripts/)
 * Or embed functions directly in templates using <%* ... %> syntax
 * 
 * Usage in templates:
 * <%* const { getNextPatternNumber, generateLeetCodeLinks, getFolderCategory, generateProblemSection, getRelatedPatterns } = require('./user-scripts'); %>
 * <%* const nextNum = await getNextPatternNumber(tp, "Coding Patterns/01_Array"); %>
 * <%* const leetcodeLinks = await generateLeetCodeLinks(tp, [303, 525, 560]); %>
 * <%* const category = await getFolderCategory(tp, tp.file.folder(true)); %>
 * <%* const problemsSection = await generateProblemSection(tp, [303, 525, 560]); %>
 * <%* const relatedPatterns = await getRelatedPatterns(tp, "Coding Patterns/01_Array"); %>
 */

const fs = require('fs');
const path = require('path');

/**
 * Scans folder for existing pattern files (NN - Title.md) and returns next number as zero-padded string "01", "02", etc.
 * @param {Templater} tp - Templater object
 * @param {string} folderPath - Path to folder (relative to vault root)
 * @returns {Promise<string>} Next pattern number as zero-padded string
 */
async function getNextPatternNumber(tp, folderPath) {
    const vaultPath = tp.app.vault.adapter.basePath;
    const fullPath = path.join(vaultPath, folderPath);
    
    if (!fs.existsSync(fullPath)) {
        return "01";
    }
    
    const files = fs.readdirSync(fullPath);
    const patternRegex = /^(\d{2})\s*-\s*.+\.md$/;
    let maxNum = 0;
    
    for (const file of files) {
        const match = file.match(patternRegex);
        if (match) {
            const num = parseInt(match[1], 10);
            if (num > maxNum) maxNum = num;
        }
    }
    
    const nextNum = maxNum + 1;
    return nextNum.toString().padStart(2, '0');
}

/**
 * Takes array like [303, 525, 560] and returns markdown list with links
 * @param {Templater} tp - Templater object
 * @param {number[]} leetcodeArray - Array of LeetCode problem numbers
 * @returns {Promise<string>} Markdown list with LeetCode links
 */
async function generateLeetCodeLinks(tp, leetcodeArray) {
    if (!Array.isArray(leetcodeArray) || leetcodeArray.length === 0) {
        return "";
    }
    
    // Problem title mapping - can be extended
    const problemTitles = {
        303: "Range Sum Query - Immutable",
        304: "Range Sum Query 2D - Immutable",
        525: "Contiguous Array",
        560: "Subarray Sum Equals K",
        1: "Two Sum",
        2: "Add Two Numbers",
        3: "Longest Substring Without Repeating Characters",
        5: "Longest Palindromic Substring",
        11: "Container With Most Water",
        15: "3Sum",
        26: "Remove Duplicates from Sorted Array",
        33: "Search in Rotated Sorted Array",
        42: "Trapping Rain Water",
        53: "Maximum Subarray",
        56: "Merge Intervals",
        70: "Climbing Stairs",
        73: "Set Matrix Zeroes",
        76: "Minimum Window Substring",
        88: "Merge Sorted Array",
        121: "Best Time to Buy and Sell Stock",
        125: "Valid Palindrome",
        128: "Longest Consecutive Sequence",
        141: "Linked List Cycle",
        142: "Linked List Cycle II",
        150: "Evaluate Reverse Polish Notation",
        155: "Min Stack",
        169: "Majority Element",
        189: "Rotate Array",
        200: "Number of Islands",
        206: "Reverse Linked List",
        217: "Contains Duplicate",
        226: "Invert Binary Tree",
        234: "Palindrome Linked List",
        238: "Product of Array Except Self",
        242: "Valid Anagram",
        283: "Move Zeroes",
        347: "Top K Frequent Elements",
        424: "Longest Repeating Character Replacement",
        435: "Non-overlapping Intervals",
        438: "Find All Anagrams in a String",
        454: "4Sum II",
        496: "Next Greater Element I",
        543: "Diameter of Binary Tree",
        567: "Permutation in String",
        643: "Maximum Average Subarray I",
        674: "Longest Continuous Increasing Subsequence",
        713: "Subarray Product Less Than K",
        739: "Daily Temperatures",
        763: "Partition Labels",
        904: "Fruit Into Baskets",
        977: "Squares of a Sorted Array",
        981: "Time Based Key-Value Store",
        1004: "Max Consecutive Ones III",
        1052: "Grumpy Bookstore Owner",
        1248: "Count Number of Nice Subarrays",
        1493: "Longest Subarray of 1's After Deleting One Element",
        1658: "Minimum Operations to Reduce X to Zero",
        1732: "Find the Highest Altitude",
        2090: "K Radius Subarray Averages",
        2270: "Number of Ways to Split Array",
        2381: "Shifting Letters II",
        2390: "Removing Stars From a String",
        2441: "Largest Positive Integer That Exists With Its Negative",
        2570: "Merge Two 2D Arrays by Summing Values",
        2653: "Sliding Subarray Beauty",
        2779: "Maximum Beauty of an Array After Applying Operation",
        2824: "Count Pairs Whose Sum is Less than Target",
        3000: "Maximum Area of Longest Subarray",
        3005: "Count Elements With Maximum Frequency",
        3074: "Minimum Number of Operations to Make Array Empty",
        3090: "Maximum Length Substring With Two Occurrences",
        3190: "Minimum Number of Operations to Make Array Empty",
        3258: "Count Subarrays That Satisfy Condition"
    };
    
    const lines = [];
    for (const num of leetcodeArray) {
        const title = problemTitles[num] || `Problem ${num}`;
        const url = `https://leetcode.com/problems/${title.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/-+$/, '')}/`;
        lines.push(`- [${num}. ${title}](${url})`);
    }
    
    return lines.join('\n');
}

/**
 * Extracts category from folder path, e.g., "Coding Patterns/01_Array"
 * @param {Templater} tp - Templater object
 * @param {string} filePath - File path (relative to vault root)
 * @returns {Promise<string>} Category path
 */
async function getFolderCategory(tp, filePath) {
    // Normalize path separators
    const normalizedPath = filePath.replace(/\\/g, '/');
    
    // If it's a file path, get the folder
    let folderPath = normalizedPath;
    if (folderPath.endsWith('.md')) {
        folderPath = path.dirname(folderPath);
    }
    
    // Find the "Coding Patterns" root and return relative path from there
    const codingPatternsIndex = folderPath.indexOf('Coding Patterns');
    if (codingPatternsIndex !== -1) {
        return folderPath.substring(codingPatternsIndex);
    }
    
    // Fallback: return the folder path as-is
    return folderPath;
}

/**
 * Creates the full "## Problems" section with proper formatting
 * @param {Templater} tp - Templater object
 * @param {number[]} leetcodeArray - Array of LeetCode problem numbers
 * @returns {Promise<string>} Full Problems section markdown
 */
async function generateProblemSection(tp, leetcodeArray) {
    if (!Array.isArray(leetcodeArray) || leetcodeArray.length === 0) {
        return "## Problems\n\n_No LeetCode problems linked yet._\n";
    }
    
    // Problem details mapping - can be extended
    const problemDetails = {
        303: { title: "Range Sum Query - Immutable", difficulty: "Easy", tags: ["Array", "Design", "Prefix Sum"] },
        304: { title: "Range Sum Query 2D - Immutable", difficulty: "Hard", tags: ["Array", "Design", "Matrix", "Prefix Sum"] },
        525: { title: "Contiguous Array", difficulty: "Medium", tags: ["Array", "Hash Table", "Prefix Sum"] },
        560: { title: "Subarray Sum Equals K", difficulty: "Medium", tags: ["Array", "Hash Table", "Prefix Sum"] },
        1: { title: "Two Sum", difficulty: "Easy", tags: ["Array", "Hash Table"] },
        2: { title: "Add Two Numbers", difficulty: "Medium", tags: ["Linked List", "Math", "Recursion"] },
        11: { title: "Container With Most Water", difficulty: "Medium", tags: ["Array", "Two Pointers", "Greedy"] },
        15: { title: "3Sum", difficulty: "Medium", tags: ["Array", "Two Pointers", "Sorting"] },
        26: { title: "Remove Duplicates from Sorted Array", difficulty: "Easy", tags: ["Array", "Two Pointers"] },
        42: { title: "Trapping Rain Water", difficulty: "Hard", tags: ["Array", "Two Pointers", "Stack", "Monotonic Stack"] },
        53: { title: "Maximum Subarray", difficulty: "Medium", tags: ["Array", "Divide and Conquer", "Dynamic Programming"] },
        56: { title: "Merge Intervals", difficulty: "Medium", tags: ["Array", "Sorting"] },
        70: { title: "Climbing Stairs", difficulty: "Easy", tags: ["Math", "Dynamic Programming", "Memoization"] },
        76: { title: "Minimum Window Substring", difficulty: "Hard", tags: ["Hash Table", "String", "Sliding Window"] },
        88: { title: "Merge Sorted Array", difficulty: "Easy", tags: ["Array", "Two Pointers", "Sorting"] },
        121: { title: "Best Time to Buy and Sell Stock", difficulty: "Easy", tags: ["Array", "Dynamic Programming"] },
        128: { title: "Longest Consecutive Sequence", difficulty: "Medium", tags: ["Array", "Hash Table"] },
        141: { title: "Linked List Cycle", difficulty: "Easy", tags: ["Hash Table", "Linked List", "Two Pointers"] },
        142: { title: "Linked List Cycle II", difficulty: "Medium", tags: ["Hash Table", "Linked List", "Two Pointers"] },
        169: { title: "Majority Element", difficulty: "Easy", tags: ["Array", "Hash Table", "Divide and Conquer", "Sorting", "Counting"] },
        200: { title: "Number of Islands", difficulty: "Medium", tags: ["Array", "Depth-First Search", "Breadth-First Search", "Union Find", "Matrix"] },
        206: { title: "Reverse Linked List", difficulty: "Easy", tags: ["Linked List", "Recursion"] },
        217: { title: "Contains Duplicate", difficulty: "Easy", tags: ["Array", "Hash Table", "Sorting"] },
        226: { title: "Invert Binary Tree", difficulty: "Easy", tags: ["Tree", "Depth-First Search", "Breadth-First Search", "Binary Tree"] },
        238: { title: "Product of Array Except Self", difficulty: "Medium", tags: ["Array", "Prefix Sum"] },
        242: { title: "Valid Anagram", difficulty: "Easy", tags: ["Hash Table", "String", "Sorting"] },
        283: { title: "Move Zeroes", difficulty: "Easy", tags: ["Array", "Two Pointers"] },
        347: { title: "Top K Frequent Elements", difficulty: "Medium", tags: ["Array", "Hash Table", "Divide and Conquer", "Sorting", "Heap", "Bucket Sort", "Counting"] },
        424: { title: "Longest Repeating Character Replacement", difficulty: "Medium", tags: ["Hash Table", "String", "Sliding Window"] },
        435: { title: "Non-overlapping Intervals", difficulty: "Medium", tags: ["Array", "Dynamic Programming", "Greedy", "Sorting"] },
        438: { title: "Find All Anagrams in a String", difficulty: "Medium", tags: ["Hash Table", "String", "Sliding Window"] },
        496: { title: "Next Greater Element I", difficulty: "Easy", tags: ["Array", "Hash Table", "Stack", "Monotonic Stack"] },
        543: { title: "Diameter of Binary Tree", difficulty: "Easy", tags: ["Tree", "Depth-First Search", "Binary Tree"] },
        567: { title: "Permutation in String", difficulty: "Medium", tags: ["Hash Table", "String", "Two Pointers", "Sliding Window"] },
        643: { title: "Maximum Average Subarray I", difficulty: "Easy", tags: ["Array", "Sliding Window"] },
        674: { title: "Longest Continuous Increasing Subsequence", difficulty: "Easy", tags: ["Array"] },
        713: { title: "Subarray Product Less Than K", difficulty: "Medium", tags: ["Array", "Sliding Window"] },
        739: { title: "Daily Temperatures", difficulty: "Medium", tags: ["Array", "Stack", "Monotonic Stack"] },
        763: { title: "Partition Labels", difficulty: "Medium", tags: ["Hash Table", "String", "Greedy", "Two Pointers"] },
        904: { title: "Fruit Into Baskets", difficulty: "Medium", tags: ["Array", "Hash Table", "Sliding Window"] },
        977: { title: "Squares of a Sorted Array", difficulty: "Easy", tags: ["Array", "Two Pointers", "Sorting"] },
        981: { title: "Time Based Key-Value Store", difficulty: "Medium", tags: ["Hash Table", "String", "Binary Search", "Design"] },
        1004: { title: "Max Consecutive Ones III", difficulty: "Medium", tags: ["Array", "Sliding Window"] },
        1052: { title: "Grumpy Bookstore Owner", difficulty: "Medium", tags: ["Array", "Sliding Window"] },
        1248: { title: "Count Number of Nice Subarrays", difficulty: "Medium", tags: ["Array", "Hash Table", "Math", "Sliding Window"] },
    };
    
    const lines = ["## Problems\n"];
    
    for (const num of leetcodeArray) {
        const details = problemDetails[num] || { title: `Problem ${num}`, difficulty: "Unknown", tags: [] };
        const url = `https://leetcode.com/problems/${details.title.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/-+$/, '')}/`;
        const tagsStr = details.tags.length > 0 ? ` • ${details.tags.join(', ')}` : '';
        
        lines.push(`### ${num}. ${details.title} (${details.difficulty})`);
        lines.push(`> [LeetCode ${num}](${url})${tagsStr}`);
        lines.push("");
        lines.push("**Examples:**");
        lines.push("");
        lines.push("**Example 1:**");
        lines.push("- **Input:** ");
        lines.push("- **Output:** ");
        lines.push("- **Explanation:** ");
        lines.push("");
        lines.push("---");
        lines.push("");
    }
    
    // Remove trailing separator
    if (lines[lines.length - 1] === "") lines.pop();
    if (lines[lines.length - 1] === "---") lines.pop();
    
    return lines.join('\n');
}

/**
 * Finds other pattern files in same folder and returns wikilinks
 * @param {Templater} tp - Templater object
 * @param {string} folderPath - Path to folder (relative to vault root)
 * @returns {Promise<string>} Wikilinks to related patterns
 */
async function getRelatedPatterns(tp, folderPath) {
    const vaultPath = tp.app.vault.adapter.basePath;
    const fullPath = path.join(vaultPath, folderPath);
    
    if (!fs.existsSync(fullPath)) {
        return "- No related patterns found";
    }
    
    const files = fs.readdirSync(fullPath);
    const patternRegex = /^(\d{2})\s*-\s*(.+)\.md$/;
    const patterns = [];
    
    for (const file of files) {
        const match = file.match(patternRegex);
        if (match) {
            const num = match[1];
            const title = match[2];
            // Create wikilink using the folder structure
            const folderName = path.basename(folderPath);
            const linkPath = `${folderName}/${num} - ${title}`;
            patterns.push(`- [[${linkPath}|${num} - ${title}]]`);
        }
    }
    
    if (patterns.length === 0) {
        return "- No related patterns found";
    }
    
    return patterns.join('\n');
}

module.exports = {
    getNextPatternNumber,
    generateLeetCodeLinks,
    getFolderCategory,
    generateProblemSection,
    getRelatedPatterns
};
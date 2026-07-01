import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const cssPath = path.join(__dirname, '..', 'public', 'ctc', 'assets', 'index-C58Bc2af.css');
const content = fs.readFileSync(cssPath, 'utf8');

// Search in the original CSS part
const originalCss = content.substring(0, 112715);

// Let's search for "::before" or ":before" or anything with "content:"
const regex = /[^\{\}]*content:[^;\}]*/g;
let match;
while ((match = regex.exec(originalCss)) !== null) {
    console.log(`Found content rule at index ${match.index}:`);
    console.log(originalCss.substring(match.index - 100, match.index + 150));
    console.log('-'.repeat(80));
}

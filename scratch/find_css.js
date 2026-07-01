import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const cssPath = path.join(__dirname, '..', 'public', 'ctc', 'assets', 'index-C58Bc2af.css');
const content = fs.readFileSync(cssPath, 'utf8');

const regex = /li[^\{]*before|before[^\{]*li|content/g;
let match;
while ((match = regex.exec(content)) !== null) {
    console.log(`Found match at index ${match.index}:`);
    console.log(content.substring(match.index - 50, match.index + 150));
    console.log('-'.repeat(80));
}

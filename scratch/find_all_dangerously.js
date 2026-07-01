import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const filePath = path.join(__dirname, '..', 'public', 'ctc', 'assets', 'index-Yw1fTNC7.js');
const content = fs.readFileSync(filePath, 'utf8');

const regex = /dangerouslySetInnerHTML/g;
let match;
while ((match = regex.exec(content)) !== null) {
    console.log(`Found dangerouslySetInnerHTML at index ${match.index}:`);
    console.log(content.substring(match.index - 300, match.index + 300));
    console.log('-'.repeat(80));
}

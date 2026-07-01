import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const filePath = path.join(__dirname, '..', 'public', 'ctc', 'assets', 'index-Yw1fTNC7.js');
const content = fs.readFileSync(filePath, 'utf8');

const searches = ['June 28, 2026', 'June 28', 'From Outsourcing to Co-Sourcing', 'advantages-of-co-sourcing', ' श्रीलंका'];
searches.forEach(q => {
    const idx = content.indexOf(q);
    if (idx !== -1) {
        console.log(`Found "${q}" in JS bundle at index ${idx}!`);
        console.log(content.substring(idx - 100, idx + 300));
        console.log('-'.repeat(80));
    } else {
        console.log(`"${q}" NOT found in JS bundle.`);
    }
});

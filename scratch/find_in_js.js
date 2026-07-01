import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const filePath = path.join(__dirname, '..', 'public', 'ctc', 'assets', 'index-Yw1fTNC7.js');
const content = fs.readFileSync(filePath, 'utf8');

const query = 'about';
console.log('File size:', content.length);
console.log('Contains query (case-insensitive):', content.toLowerCase().includes(query.toLowerCase()));

const searches = ['article', 'category', 'published', 'posts', 'success', 'dangerously', 'html', 'dangerouslySetInnerHTML'];
searches.forEach(q => {
    const idx = content.toLowerCase().indexOf(q.toLowerCase());
    if (idx !== -1) {
        console.log(`Found "${q}" at index ${idx}: ...${content.substring(idx - 40, idx + 60)}...`);
    } else {
        console.log(`"${q}" NOT found`);
    }
});

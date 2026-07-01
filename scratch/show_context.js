import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const filePath = path.join(__dirname, '..', 'public', 'ctc', 'assets', 'index-Yw1fTNC7.js');
const content = fs.readFileSync(filePath, 'utf8');

const targetIdx = 411684;
console.log(content.substring(targetIdx - 600, targetIdx + 1200));

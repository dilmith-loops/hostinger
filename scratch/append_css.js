import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const cssPath = path.join(__dirname, '..', 'public', 'ctc', 'assets', 'index-C58Bc2af.css');
let cssContent = fs.readFileSync(cssPath, 'utf8');

const customCss = `
/* Custom Blog Content Styles added by Antigravity */
.blog-content {
  font-family: 'Inter', system-ui, -apple-system, sans-serif;
  font-size: 1.1rem;
  line-height: 1.8;
  color: #374151; /* gray-700 */
}

.blog-content p {
  margin-top: 1.25rem !important;
  margin-bottom: 1.25rem !important;
}

.blog-content p strong {
  color: #0b192c; /* Brand dark blue */
  display: inline-block;
}

/* If a paragraph contains ONLY a strong tag, style it like a sub-heading */
.blog-content p:has(> strong:only-child) {
  font-size: 1.4rem;
  margin-top: 2rem !important;
  margin-bottom: 0.75rem !important;
  line-height: 1.35;
  color: #0b192c;
}

.blog-content h1, 
.blog-content h2, 
.blog-content h3, 
.blog-content h4 {
  font-weight: 800;
  color: #0b192c; /* Brand dark blue */
  margin-top: 2.25rem !important;
  margin-bottom: 1rem !important;
  line-height: 1.35;
}

.blog-content h1 {
  font-size: 2.25rem;
}

.blog-content h2 {
  font-size: 1.75rem;
  border-bottom: 1px solid #e5e7eb;
  padding-bottom: 0.5rem;
}

.blog-content h3 {
  font-size: 1.4rem;
}

.blog-content strong {
  font-weight: 700;
  color: #0b192c;
}

.blog-content ul {
  list-style-type: disc !important;
  margin-top: 1.25rem !important;
  margin-bottom: 1.25rem !important;
  padding-left: 1.75rem !important;
}

.blog-content ol {
  list-style-type: decimal !important;
  margin-top: 1.25rem !important;
  margin-bottom: 1.25rem !important;
  padding-left: 1.75rem !important;
}

.blog-content li {
  margin-top: 0.5rem !important;
  margin-bottom: 0.5rem !important;
  padding-left: 0.25rem;
}

.blog-content li p {
  margin: 0 !important;
  display: inline !important;
  font-size: inherit !important;
  color: inherit !important;
}

.blog-content ul li::marker {
  color: #ff8e25; /* Brand accent orange */
}

.blog-content ol li::marker {
  color: #ff8e25;
  font-weight: bold;
}

.blog-content blockquote {
  font-style: italic;
  border-left: 4px solid #ff8e25; /* Brand accent orange */
  padding-left: 1.25rem;
  margin: 1.75rem 0;
  color: #4b5563; /* gray-600 */
  font-size: 1.2rem;
}

.blog-content a {
  color: #ff8e25;
  text-decoration: underline;
  font-weight: 600;
  transition: color 0.2s ease;
}

.blog-content a:hover {
  color: #e07314;
}

.blog-content img {
  border-radius: 0.75rem;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  margin: 2.25rem auto;
  display: block;
  max-width: 100%;
}
`;

fs.writeFileSync(cssPath, cssContent + '\n' + customCss, 'utf8');
console.log('Successfully appended custom CSS to index-C58Bc2af.css');

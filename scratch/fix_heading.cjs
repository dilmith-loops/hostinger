const fs = require('fs');
let js = fs.readFileSync('public/ctc/assets/index-Yw1fTNC7.js', 'utf8');

// 1. Add <br> between the two parts of the heading
const oldRender = 'children: [A.slice(0, T), u.jsx("span", { className: "text-accent", children: A.slice(T) })]';
const newRender = 'children: [A.slice(0, T).trimEnd(), u.jsx("br", {}), u.jsx("span", { className: "text-accent", children: A.slice(T) })]';
console.log('Render found:', js.includes(oldRender));
js = js.replace(oldRender, newRender);

// 2. Remove max-w-lg from h1 and remove leftover mt-24
js = js.replace(
  'mt-24 text-3xl sm:text-4xl lg:text-[2.55rem] xl:text-5xl font-extrabold text-white leading-[1.06] tracking-tight max-w-lg',
  'text-3xl sm:text-4xl lg:text-[2.55rem] xl:text-5xl font-extrabold text-white leading-[1.06] tracking-tight'
);

fs.writeFileSync('public/ctc/assets/index-Yw1fTNC7.js', js, 'utf8');

const result = fs.readFileSync('public/ctc/assets/index-Yw1fTNC7.js', 'utf8');
console.log('br added:', result.includes('u.jsx("br", {})'));
console.log('max-w-lg removed:', !result.includes('tracking-tight max-w-lg'));
console.log('mt-24 removed:', !result.includes('mt-24 text-3xl'));

const fs = require('fs');
let js = fs.readFileSync('public/ctc/assets/index-Yw1fTNC7.js', 'utf8');

// 1. Replace the static window.innerWidth style with a CSS class
const oldStyle = 'className: "relative px-8 py-10 lg:px-16 flex flex-col items-center justify-start lg:h-full", style: (typeof window !== "undefined" && window.innerWidth >= 1024) ? { paddingTop: "17rem", paddingBottom: "4rem" } : {}';
const newStyle = 'className: "lp-hero-wrapper relative px-8 py-10 lg:px-16 flex flex-col items-center justify-start lg:h-full"';

console.log('Step 1 found:', js.includes(oldStyle));
js = js.replace(oldStyle, newStyle);

// 2. Inject a <style> tag into the TP component JSX output
// Find the specific pattern in the TP component's return statement
const oldReturn = 'className: "min-h-screen flex flex-col bg-background", children: [u.jsx(LO, {}),';
const newReturn = 'className: "min-h-screen flex flex-col bg-background", children: [u.jsx("style", { dangerouslySetInnerHTML: { __html: "@media (min-width: 1024px) { .lp-hero-wrapper { padding-top: 17rem !important; padding-bottom: 4rem !important; } }" } }), u.jsx(LO, {}),';

console.log('Step 2 found:', js.includes(oldReturn));
js = js.replace(oldReturn, newReturn);

fs.writeFileSync('public/ctc/assets/index-Yw1fTNC7.js', js, 'utf8');
const result = fs.readFileSync('public/ctc/assets/index-Yw1fTNC7.js', 'utf8');
console.log('Class applied:', result.includes('"lp-hero-wrapper relative'));
console.log('Style tag injected:', result.includes('@media (min-width: 1024px)'));

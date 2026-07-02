const fs = require('fs');
let js = fs.readFileSync('public/ctc/assets/index-Yw1fTNC7.js', 'utf8');

// Replace wrapper - add responsive inline style for desktop only
const oldWrapper = '"relative px-8 py-10 lg:pt-56 lg:pb-16 lg:px-16 flex flex-col items-center justify-center lg:justify-start lg:h-full"';
const newWrapper = '"relative px-8 py-10 lg:px-16 flex flex-col items-center justify-center lg:justify-start lg:h-full", style: (typeof window !== "undefined" && window.innerWidth >= 1024) ? { paddingTop: "17rem", paddingBottom: "4rem" } : {}';

console.log('Found:', js.includes(oldWrapper));
js = js.replace(oldWrapper, newWrapper);

fs.writeFileSync('public/ctc/assets/index-Yw1fTNC7.js', js, 'utf8');
const result = fs.readFileSync('public/ctc/assets/index-Yw1fTNC7.js', 'utf8');
console.log('Applied:', result.includes('paddingTop: "17rem"'));

const fs = require('fs');
let js = fs.readFileSync('public/ctc/assets/index-Yw1fTNC7.js', 'utf8');

const old = 'className: "relative px-8 pt-96 pb-16 lg:px-16 flex flex-col justify-start lg:h-full"';
const replacement = 'className: "relative px-8 pb-16 lg:px-16 flex flex-col justify-start lg:h-full", style: { paddingTop: "28rem" }';

console.log('Found:', js.includes(old));
js = js.replace(old, replacement);
fs.writeFileSync('public/ctc/assets/index-Yw1fTNC7.js', js, 'utf8');

const result = fs.readFileSync('public/ctc/assets/index-Yw1fTNC7.js', 'utf8');
console.log('Inline style applied:', result.includes('paddingTop: "28rem"'));

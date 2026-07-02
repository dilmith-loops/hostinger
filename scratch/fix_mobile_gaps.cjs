const fs = require('fs');
let js = fs.readFileSync('public/ctc/assets/index-Yw1fTNC7.js', 'utf8');

// Replace wrapper: remove inline style paddingTop, use py-10 + justify-center
const oldWrapper = 'className: "relative px-8 pb-16 lg:px-16 flex flex-col items-center justify-start lg:h-full", style: { paddingTop: "17rem" }';
const newWrapper = 'className: "relative px-8 py-10 lg:py-20 lg:px-16 flex flex-col items-center justify-center lg:h-full"';

console.log('Wrapper found:', js.includes(oldWrapper));
js = js.replace(oldWrapper, newWrapper);

fs.writeFileSync('public/ctc/assets/index-Yw1fTNC7.js', js, 'utf8');

const result = fs.readFileSync('public/ctc/assets/index-Yw1fTNC7.js', 'utf8');
console.log('Applied:', result.includes('py-10 lg:py-20'));
console.log('paddingTop gone:', !result.includes('paddingTop: "17rem"'));

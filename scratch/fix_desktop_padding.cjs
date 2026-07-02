const fs = require('fs');
let js = fs.readFileSync('public/ctc/assets/index-Yw1fTNC7.js', 'utf8');

// Change wrapper:
// Mobile: py-10, justify-center (small compact padding - user approved this)
// Desktop: lg:pt-56 lg:pb-16, lg:justify-start (push text down on desktop)
const oldWrapper = '"relative px-8 py-10 lg:py-20 lg:px-16 flex flex-col items-center justify-center lg:h-full"';
const newWrapper = '"relative px-8 py-10 lg:pt-56 lg:pb-16 lg:px-16 flex flex-col items-center justify-center lg:justify-start lg:h-full"';

console.log('Found:', js.includes(oldWrapper));
js = js.replace(oldWrapper, newWrapper);

fs.writeFileSync('public/ctc/assets/index-Yw1fTNC7.js', js, 'utf8');
const result = fs.readFileSync('public/ctc/assets/index-Yw1fTNC7.js', 'utf8');
console.log('Applied:', result.includes('lg:pt-56 lg:pb-16'));

const fs = require('fs');
let js = fs.readFileSync('public/ctc/assets/index-Yw1fTNC7.js', 'utf8');

// Fix: change justify-center (causes centering gap on mobile) to justify-start for all screens
const old = '"relative px-8 py-10 lg:px-16 flex flex-col items-center justify-center lg:justify-start lg:h-full"';
const updated = '"relative px-8 py-10 lg:px-16 flex flex-col items-center justify-start lg:h-full"';

console.log('Found:', js.includes(old));
js = js.replace(old, updated);

fs.writeFileSync('public/ctc/assets/index-Yw1fTNC7.js', js, 'utf8');
const result = fs.readFileSync('public/ctc/assets/index-Yw1fTNC7.js', 'utf8');
console.log('Applied:', result.includes('"relative px-8 py-10 lg:px-16 flex flex-col items-center justify-start lg:h-full"'));

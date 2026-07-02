const fs = require('fs');
let js = fs.readFileSync('public/ctc/assets/index-Yw1fTNC7.js', 'utf8');

// Find the h1 className and print surrounding context
const idx = js.indexOf('text-3xl sm:text-4xl lg:text-[2.55rem] xl:text-5xl font-extrabold text-white leading-[1.06] tracking-tight');
console.log('Found at:', idx);
if (idx !== -1) {
  console.log('Context:', js.substring(idx - 20, idx + 150));
}

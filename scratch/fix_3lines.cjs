const fs = require('fs');
let js = fs.readFileSync('public/ctc/assets/index-Yw1fTNC7.js', 'utf8');

// 1. Replace the 2-line render logic with 3-line version
const old2Line = 'children: [A.slice(0, T).trimEnd(), u.jsx("br", {}), u.jsx("span", { className: "text-accent", children: A.slice(T) })]';
const new3Line = `children: (() => {
  const s1 = A.indexOf("for your business");
  const s2 = A.lastIndexOf("free for");
  if (s1 === -1 || s2 === -1) return [A];
  return [
    A.slice(0, s1).trimEnd(),
    u.jsx("br", {}, "br1"),
    A.slice(s1, s2).trimEnd(),
    u.jsx("br", {}, "br2"),
    u.jsx("span", { className: "text-accent" }, "accent", A.slice(s2))
  ];
})()`;

// Simpler 3-line approach using jsxs Fragment children array
const new3LineSimple = 'children: [A.slice(0, A.indexOf("for your business")).trimEnd(), u.jsx("br", {}), A.slice(A.indexOf("for your business"), A.lastIndexOf("free for")).trimEnd(), u.jsx("br", {}), u.jsx("span", { className: "text-accent", children: A.slice(A.lastIndexOf("free for")) })]';

console.log('2-line found:', js.includes(old2Line));
js = js.replace(old2Line, new3LineSimple);

// 2. Add text-center to h1
js = js.replace(
  '"text-3xl sm:text-4xl lg:text-[2.55rem] xl:text-5xl font-extrabold text-white leading-[1.06] tracking-tight"',
  '"text-center text-3xl sm:text-4xl lg:text-[2.55rem] xl:text-5xl font-extrabold text-white leading-[1.06] tracking-tight"'
);

// 3. Center the subheadline paragraph too
js = js.replace(
  '"mt-8 text-base lg:text-lg text-white/75 font-medium max-w-md leading-relaxed"',
  '"mt-8 text-center text-base lg:text-lg text-white/75 font-medium leading-relaxed"'
);

// 4. Center the wrapper div (items-center on flex column)
js = js.replace(
  '"relative px-8 pb-16 lg:px-16 flex flex-col justify-start lg:h-full"',
  '"relative px-8 pb-16 lg:px-16 flex flex-col items-center justify-start lg:h-full"'
);

fs.writeFileSync('public/ctc/assets/index-Yw1fTNC7.js', js, 'utf8');

const result = fs.readFileSync('public/ctc/assets/index-Yw1fTNC7.js', 'utf8');
console.log('3-line applied:', result.includes('A.slice(A.indexOf("for your business")'));
console.log('text-center on h1:', result.includes('"text-center text-3xl'));
console.log('subheadline centered:', result.includes('"mt-8 text-center'));
console.log('wrapper centered:', result.includes('items-center justify-start'));

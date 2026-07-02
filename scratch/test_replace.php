<?php
$file = 'public/ctc/assets/index-Yw1fTNC7.js';
$content = file_get_contents($file);

$target = '[u.jsxs(rt, { to: "/blog", className: "inline-flex items-center gap-1.5 text-xs font-semibold text-white/60 hover:text-white transition mb-6 tracking-wide uppercase", children: [u.jsx(Jo, { className: "h-3.5 w-3.5" }), "All articles"] }), u.jsxs("span", { className: "inline-flex items-center gap-1.5 rounded-full bg-accent/20 border border-accent/40 px-3 py-1 text-xs font-semibold text-accent tracking-wide uppercase mb-5", children: [u.jsx(_g, { className: "h-3 w-3" }), e.category] })';

$replacement = '[u.jsxs("div", { className: "flex items-center gap-4 flex-wrap mb-6", children: [u.jsxs(rt, { to: "/blog", className: "inline-flex items-center gap-1.5 text-xs font-semibold text-white/60 hover:text-white transition tracking-wide uppercase", children: [u.jsx(Jo, { className: "h-3.5 w-3.5" }), "All articles"] }), u.jsxs("span", { className: "inline-flex items-center gap-1.5 rounded-full bg-accent/20 border border-accent/40 px-3 py-1 text-xs font-semibold text-accent tracking-wide uppercase", children: [u.jsx(_g, { className: "h-3 w-3" }), e.category] })] })';

if (strpos($content, $target) !== false) {
    echo "Target found!\n";
    $newContent = str_replace($target, $replacement, $content);
    file_put_contents('scratch/temp_check.js', $newContent);
    $output = shell_exec("node -e \"const fs = require('fs'); const vm = require('vm'); const code = fs.readFileSync('scratch/temp_check.js', 'utf8'); new vm.Script(code); console.log('PARSED_SUCCESSFULLY');\"");
    echo "Check: $output\n";
} else {
    echo "Target NOT found!\n";
}

<?php
$file = 'public/ctc/assets/index-Yw1fTNC7.js';
$content = file_get_contents($file);

$target = 'children: [u.jsx("img", { src: a.image || Aa, alt: a.title, className: "h-full w-full transition duration-500 group-hover:scale-105 " + ((a.image || "").toLowerCase().endsWith(".png") || (a.image || "").toLowerCase().includes("logo") ? "object-contain bg-white p-10" : "object-cover") }), u.jsx("span", { className: "absolute left-4 top-4 inline-flex items-center rounded-full bg-background/90 px-3 py-1 text-[11px] eyebrow text-accent backdrop-blur", children: a.category })]';

$replacement = 'children: u.jsx("img", { src: a.image || Aa, alt: a.title, className: "h-full w-full transition duration-500 group-hover:scale-105 " + ((a.image || "").toLowerCase().endsWith(".png") || (a.image || "").toLowerCase().includes("logo") ? "object-contain bg-white p-10" : "object-cover") })';

if (strpos($content, $target) !== false) {
    echo "Target found!\n";
    $newContent = str_replace($target, $replacement, $content);
    file_put_contents('scratch/temp_check.js', $newContent);
    $output = shell_exec("node -e \"const fs = require('fs'); const vm = require('vm'); const code = fs.readFileSync('scratch/temp_check.js', 'utf8'); new vm.Script(code); console.log('PARSED_SUCCESSFULLY');\"");
    echo "Check: $output\n";
} else {
    // Let's also check if u.jsxs wrapper can be matched
    $target2 = 'u.jsxs("div", { className: "relative aspect-[16/10] overflow-hidden", children: [u.jsx("img", { src: a.image || Aa, alt: a.title, className: "h-full w-full transition duration-500 group-hover:scale-105 " + ((a.image || "").toLowerCase().endsWith(".png") || (a.image || "").toLowerCase().includes("logo") ? "object-contain bg-white p-10" : "object-cover") }), u.jsx("span", { className: "absolute left-4 top-4 inline-flex items-center rounded-full bg-background/90 px-3 py-1 text-[11px] eyebrow text-accent backdrop-blur", children: a.category })] })';
    if (strpos($content, $target2) !== false) {
        echo "Target2 found!\n";
    } else {
        echo "Targets not found!\n";
    }
}

<?php
$file = 'public/ctc/assets/index-Yw1fTNC7.js';
$content = file_get_contents($file);

// Target content we want to replace
$target = 'const isBlack = darkLogos[p.src] || (p.name || "").toLowerCase().includes("awning") || (p.name || "").toLowerCase().includes("moorup") || (p.name || "").toLowerCase().includes("maroo") || (p.name || "").toLowerCase().includes("royal") || (p.name || "").toLowerCase().includes("shade") || (p.src || "").toLowerCase().includes("awning") || (p.src || "").toLowerCase().includes("moorup") || (p.src || "").toLowerCase().includes("maroo") || (p.src || "").toLowerCase().includes("royal") || (p.src || "").toLowerCase().includes("shade") || (p.src || "").toLowerCase().includes("black");';

// Replacement content with Eyeview exclusion
$replacement = 'const isBlack = (darkLogos[p.src] || (p.name || "").toLowerCase().includes("awning") || (p.name || "").toLowerCase().includes("moorup") || (p.name || "").toLowerCase().includes("maroo") || (p.name || "").toLowerCase().includes("royal") || (p.name || "").toLowerCase().includes("shade") || (p.src || "").toLowerCase().includes("awning") || (p.src || "").toLowerCase().includes("moorup") || (p.src || "").toLowerCase().includes("maroo") || (p.src || "").toLowerCase().includes("royal") || (p.src || "").toLowerCase().includes("shade") || (p.src || "").toLowerCase().includes("black")) && !((p.name || "").toLowerCase().includes("eyeview") || (p.name || "").toLowerCase().includes("evm") || (p.src || "").toLowerCase().includes("eyeview"));';

if (strpos($content, $target) !== false) {
    echo "Target found!\n";
    $newContent = str_replace($target, $replacement, $content);
    file_put_contents('scratch/temp_check.js', $newContent);
    $output = shell_exec("node -e \"const fs = require('fs'); const vm = require('vm'); const code = fs.readFileSync('scratch/temp_check.js', 'utf8'); new vm.Script(code); console.log('PARSED_SUCCESSFULLY');\"");
    echo "Check: $output\n";
} else {
    echo "Target NOT found!\n";
}

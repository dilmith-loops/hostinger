<?php
$content = file_get_contents('public/ctc/assets/index-Yw1fTNC7.js');

$pos = strpos($content, 'function TP()');
if ($pos !== false) {
    // Count curly braces to find the exact end of function TP()
    $len = strlen($content);
    $braceCount = 0;
    $started = false;
    $endPos = $pos;
    for ($i = $pos; $i < $len; $i++) {
        if ($content[$i] === '{') {
            $braceCount++;
            $started = true;
        } else if ($content[$i] === '}') {
            $braceCount--;
        }
        if ($started && $braceCount === 0) {
            $endPos = $i;
            break;
        }
    }
    $code = substr($content, $pos, $endPos - $pos + 1);
    file_put_contents('scratch/tp_code.txt', $code);
    echo "Dumped TP code, size: " . strlen($code) . " bytes\n";
} else {
    echo "TP not found\n";
}

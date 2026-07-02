<?php
$content = file_get_contents('public/ctc/assets/index-Yw1fTNC7.js');

$pos = strpos($content, 'function zr(');
if ($pos !== false) {
    echo "Found function zr:\n" . substr($content, $pos, 1000) . "\n\n";
} else {
    $pos2 = strpos($content, 'zr = ');
    if ($pos2 !== false) {
        echo "Found zr = :\n" . substr($content, $pos2 - 100, 500) . "\n\n";
    } else {
        echo "zr not found\n";
    }
}

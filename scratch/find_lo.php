<?php
$content = file_get_contents('public/ctc/assets/index-Yw1fTNC7.js');

$pos = 0;
while (($pos = strpos($content, 'No lock-in contract', $pos)) !== false) {
    echo "Found No lock-in contract at $pos:\n" . substr($content, $pos - 50, 150) . "\n\n";
    $pos += 10;
}

<?php
$lines = file('public/ctc/assets/index-C58Bc2af.css');
foreach ($lines as $index => $line) {
    if (strpos($line, 'glass-nav') !== false) {
        echo "Line " . ($index + 1) . ": " . substr($line, 0, 500) . "\n";
    }
}

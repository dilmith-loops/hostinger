<?php
$content = file_get_contents("d:\\laragon\\www\\hostinger\\public\\ctc\\assets\\index-Yw1fTNC7.js");

// Find the Save Edits button offset
$btn_pos = strpos($content, "Save Edits");
if ($btn_pos !== false) {
    echo "Found 'Save Edits' at $btn_pos\n";
    // Search backwards for he = or function he or const he
    $pos = $btn_pos;
    $found = false;
    for ($i = 0; $i < 10; $i++) {
        $pos = strrpos(substr($content, 0, $pos), " = async", 0);
        if ($pos !== false) {
            echo "Found ' = async' at $pos: " . substr($content, $pos - 50, 150) . "\n\n";
        }
    }
}

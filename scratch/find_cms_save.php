<?php
$content = file_get_contents("d:\\laragon\\www\\hostinger\\public\\ctc\\assets\\index-Yw1fTNC7.js");

function search($pattern) {
    global $content;
    $offset = 0;
    while (($pos = strpos($content, $pattern, $offset)) !== false) {
        echo "Found '$pattern' at offset $pos: " . substr($content, max(0, $pos - 100), 250) . "\n\n";
        $offset = $pos + strlen($pattern);
    }
}

search("/api/cms/content");
search("saveEdits");
search("Save Edits");

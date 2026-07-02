<?php
$file = 'public/ctc/assets/index-C58Bc2af.css';
$content = file_get_contents($file);

$target = '.glass-nav{-webkit-backdrop-filter:blur(16px)saturate(140%);background:#ffffffc7;border-bottom:1px solid oklch(36% .04 250/.06)}';
$replacement = '.glass-nav{-webkit-backdrop-filter:blur(16px)saturate(140%);background:#ffffff;border-bottom:1px solid oklch(36% .04 250/.06)}';

if (strpos($content, $target) !== false) {
    echo "Target found!\n";
    $newContent = str_replace($target, $replacement, $content);
    file_put_contents('scratch/temp_check.css', $newContent);
    echo "Replaced successfully in temp file!\n";
} else {
    echo "Target NOT found!\n";
}

<?php
$info = getimagesize('public/uploads/cms_6a45e837db5fb4.72744640.png');
echo json_encode($info, JSON_PRETTY_PRINT) . "\n";

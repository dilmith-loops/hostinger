<?php
// Fetch the rendered HTML of the landing page from the server
$html = file_get_contents('http://localhost:8000/ctc/lp/free-trial');
file_put_contents('scratch/rendered_lp.html', $html);
echo "Fetched HTML, size: " . strlen($html) . " bytes\n";

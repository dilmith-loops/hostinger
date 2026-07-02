<?php
try {
    $pdo = new PDO('mysql:host=127.0.0.1;dbname=ctc', 'root', '');
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    
    $q = $pdo->query("DESCRIBE page_contents");
    $cols = $q->fetchAll(PDO::FETCH_COLUMN);
    echo "Columns: " . implode(', ', $cols) . "\n\n";
    
    $rows = $pdo->query("SELECT * FROM page_contents WHERE page='lp_free-trial'")->fetchAll(PDO::FETCH_ASSOC);
    foreach ($rows as $row) {
        print_r($row);
    }
} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . "\n";
}

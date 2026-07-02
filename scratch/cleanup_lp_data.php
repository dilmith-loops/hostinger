<?php
// Clean up existing LP data in database
try {
    $pdo = new PDO('mysql:host=127.0.0.1;dbname=ctc', 'root', '');
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    
    // Delete footer rows for all landing pages
    $stmt = $pdo->prepare("DELETE FROM page_contents WHERE page LIKE 'lp_%' AND `key` = 'footer'");
    $stmt->execute();
    echo "Deleted " . $stmt->rowCount() . " footer rows for landing pages\n";
    
    // Update hero data for existing landing pages - remove eyebrow, description, trustPoints, stats
    $heroRows = $pdo->query("SELECT id, page, value FROM page_contents WHERE page LIKE 'lp_%' AND `key` = 'hero'")->fetchAll(PDO::FETCH_ASSOC);
    foreach ($heroRows as $row) {
        $hero = json_decode($row['value'], true);
        // Remove unused fields
        unset($hero['eyebrow']);
        unset($hero['description']);
        unset($hero['trustPoints']);
        unset($hero['stats']);
        
        $stmt = $pdo->prepare("UPDATE page_contents SET value = ? WHERE id = ?");
        $stmt->execute([json_encode($hero), $row['id']]);
        echo "Updated hero for {$row['page']} (ID: {$row['id']})\n";
    }
    
    echo "\nDone!\n";
} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . "\n";
}

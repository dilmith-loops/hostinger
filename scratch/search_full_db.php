<?php
use Illuminate\Contracts\Console\Kernel;
require __DIR__.'/../vendor/autoload.php';
$app = require_once __DIR__.'/../bootstrap/app.php';
$kernel = $app->make(Kernel::class);
$kernel->bootstrap();

$tables = \Illuminate\Support\Facades\DB::select('SHOW TABLES');
$dbName = config('database.connections.mysql.database');
$keyName = "Tables_in_" . $dbName;

echo "Searching database '{$dbName}' for 'June 28'...\n";

foreach ($tables as $table) {
    $tableName = $table->$keyName;
    $columns = \Illuminate\Support\Facades\Schema::getColumnListing($tableName);
    
    foreach ($columns as $column) {
        try {
            $results = \Illuminate\Support\Facades\DB::table($tableName)
                ->where($column, 'LIKE', '%June 28%')
                ->get();
            if ($results->count() > 0) {
                echo "Found in table '{$tableName}', column '{$column}':\n";
                foreach ($results as $row) {
                    // Print primary key or first column
                    $idVal = isset($row->id) ? $row->id : serialize($row);
                    echo "  -> Row ID: " . $idVal . "\n";
                }
            }
        } catch (\Exception $e) {
            // Ignore errors
        }
    }
}

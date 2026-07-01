<?php
use Illuminate\Contracts\Console\Kernel;
require __DIR__.'/../vendor/autoload.php';
$app = require_once __DIR__.'/../bootstrap/app.php';
$kernel = $app->make(Kernel::class);
$kernel->bootstrap();

config(['database.default' => 'sqlite']);
\Illuminate\Support\Facades\DB::purge();

try {
    $allRows = App\Models\PageContent::all();
    echo "Sqlite row count: " . $allRows->count() . "\n";
    foreach ($allRows as $row) {
        if ($row->page === 'blog' && $row->key === 'posts') {
            foreach ($row->value as $idx => $post) {
                echo "  -> SQLite POST [{$idx}]: Title='{$post['title']}', Date='{$post['date']}', Slug='{$post['slug']}', Category='{$post['category']}'\n";
            }
        }
    }
} catch (\Exception $e) {
    echo "SQLite Error: " . $e->getMessage() . "\n";
}

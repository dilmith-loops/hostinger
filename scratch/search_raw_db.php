<?php
use Illuminate\Contracts\Console\Kernel;
require __DIR__.'/../vendor/autoload.php';
$app = require_once __DIR__.'/../bootstrap/app.php';
$kernel = $app->make(Kernel::class);
$kernel->bootstrap();

$allRows = App\Models\PageContent::all();
foreach ($allRows as $row) {
    echo "ID: {$row->id} | Page: {$row->page} | Key: {$row->key}\n";
    if ($row->page === 'blog' && $row->key === 'posts') {
        $posts = $row->value;
        foreach ($posts as $idx => $post) {
            echo "  -> POST [{$idx}]: Title='{$post['title']}', Date='{$post['date']}', Slug='{$post['slug']}'\n";
        }
    }
}

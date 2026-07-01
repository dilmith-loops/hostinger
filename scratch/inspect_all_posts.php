<?php
use Illuminate\Contracts\Console\Kernel;
require __DIR__.'/../vendor/autoload.php';
$app = require_once __DIR__.'/../bootstrap/app.php';
$kernel = $app->make(Kernel::class);
$kernel->bootstrap();

$posts = App\Models\PageContent::where('page', 'blog')->where('key', 'posts')->first()->value;
foreach ($posts as $idx => $post) {
    echo "=== POST [{$idx}]: " . $post['title'] . " ===\n";
    echo "Slug: " . $post['slug'] . "\n";
    echo "Content Preview (first 1000 chars):\n";
    echo substr($post['content'], 0, 1000) . "\n";
    echo "--------------------------------------------------\n\n";
}

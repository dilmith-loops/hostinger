<?php
use Illuminate\Contracts\Console\Kernel;
require __DIR__.'/../vendor/autoload.php';
$app = require_once __DIR__.'/../bootstrap/app.php';
$kernel = $app->make(Kernel::class);
$kernel->bootstrap();

$posts = App\Models\PageContent::where('page', 'blog')->where('key', 'posts')->first()->value;
foreach ($posts as $post) {
    if (strpos($post['content'], 'Highly') !== false || strpos($post['content'], 'skilled') !== false) {
        echo "=== TITLE: " . $post['title'] . " ===\n";
        echo $post['content'] . "\n\n";
    }
}

<?php
use Illuminate\Contracts\Console\Kernel;
require __DIR__.'/../vendor/autoload.php';
$app = require_once __DIR__.'/../bootstrap/app.php';
$kernel = $app->make(Kernel::class);
$kernel->bootstrap();

$posts = App\Models\PageContent::where('page', 'blog')->where('key', 'posts')->first()->value;
foreach ($posts as $idx => $post) {
    echo "POST [{$idx}]: {$post['title']} | Date: {$post['date']} | Slug: {$post['slug']}\n";
}

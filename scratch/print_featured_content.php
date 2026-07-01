<?php
use Illuminate\Contracts\Console\Kernel;
require __DIR__.'/../vendor/autoload.php';
$app = require_once __DIR__.'/../bootstrap/app.php';
$kernel = $app->make(Kernel::class);
$kernel->bootstrap();

$row = App\Models\PageContent::find(29);
echo "Title: " . $row->value['title'] . "\n";
echo "HTML content:\n";
echo $row->value['content'] . "\n";

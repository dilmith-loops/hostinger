import { execSync } from 'child_process';

const cmd = `php -r "require 'vendor/autoload.php'; \\$app = require_once 'bootstrap/app.php'; \\$app->make('kernel')->bootstrap(); echo App\\Models\\PageContent::where('page', 'blog')->where('key', 'posts')->first()->value;"`;
try {
    const output = execSync(cmd, { encoding: 'utf8' });
    const posts = JSON.parse(output);
    const post = posts.find(p => p.title.includes('Outsourcing'));
    if (post) {
        console.log('--- POST CONTENT ---');
        console.log(post.content);
    } else {
        console.log('Post not found');
    }
} catch (e) {
    console.error('Error running command:', e.message);
}

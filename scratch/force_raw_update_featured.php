<?php
use Illuminate\Contracts\Console\Kernel;
require __DIR__.'/../vendor/autoload.php';
$app = require_once __DIR__.'/../bootstrap/app.php';
$kernel = $app->make(Kernel::class);
$kernel->bootstrap();

// Let's load Row 29 (featured)
$row29 = \Illuminate\Support\Facades\DB::table('page_contents')->where('id', 29)->first();
$featured = json_decode($row29->value, true);

// Let's load Row 30 (posts)
$row30 = \Illuminate\Support\Facades\DB::table('page_contents')->where('id', 30)->first();
$posts = json_decode($row30->value, true);

$cleanHtml = '<p>For years, outsourcing has carried a certain stigma.</p>' .
             '<p></p>' .
             '<ul>' .
             '<li><p>Loss of control.</p></li>' .
             '<li><p>Poor quality.</p></li>' .
             '<li><p>Disconnected teams operating offshore.</p></li>' .
             '</ul>' .
             '<p></p>' .
             '<p>But something has shifted.</p>' .
             '<p></p>' .
             '<p>A growing number of Australian businesses are no longer “outsourcing.”</p>' .
             '<p>They are rebuilding their teams, globally.</p>' .
             '<p></p>' .
             '<p>And they’re doing it through a model that looks very different.</p>' .
             '<p></p>' .
             '<p></p>' .
             '<p><strong>THE PROBLEM ISN’T TALENT. IT’S ACCESS.</strong></p>' .
             '<p>Speak to almost any SME or scale-up in Australia right now, and you’ll hear the same challenges:</p>' .
             '<ul>' .
             '<li><p>Hiring locally is expensive</p></li>' .
             '<li><p>Finding the right talent takes time</p></li>' .
             '<li><p>Teams are stretched thin doing work that doesn’t drive growth</p></li>' .
             '</ul>' .
             '<p></p>' .
             '<p>At the same time, there’s a large volume of work that is critical to operations, but not location dependent:</p>' .
             '<ul>' .
             '<li><p>Admin and back-office support</p></li>' .
             '<li><p>Bookkeeping and finance operations</p></li>' .
             '<li><p>Customer service</p></li>' .
             '<li><p>Digital marketing and content</p></li>' .
             '<li><p>Data entry and reporting</p></li>' .
             '</ul>' .
             '<p></p>' .
             '<p>This work needs to get done, but it doesn’t need to be done locally.</p>' .
             '<p></p>' .
             '<p></p>' .
             '<p><strong>THIS IS WHERE CO-SOURCING CHANGES THE GAME</strong></p>' .
             '<p>Co-sourcing is not outsourcing in the traditional sense.</p>' .
             '<p></p>' .
             '<p>You are not handing work off to a third party.</p>' .
             '<p></p>' .
             '<p>You are embedding offshore talent directly into your business, aligned to your:</p>' .
             '<ul>' .
             '<li><p>Systems</p></li>' .
             '<li><p>Processes</p></li>' .
             '<li><p>Culture</p></li>' .
             '<li><p>Goals</p></li>' .
             '</ul>' .
             '<p></p>' .
             '<p>They are not “external.”</p>' .
             '<p>They become part of your team.</p>' .
             '<p></p>' .
             '<p>The shift is subtle, but powerful.</p>' .
             '<p></p>' .
             '<p></p>' .
             '<p><strong>WHAT THIS LOOKS LIKE IN PRACTICE</strong></p>' .
             '<p>Instead of hiring one local admin at $70–80K, businesses are:</p>' .
             '<ul>' .
             '<li><p>Building distributed teams</p></li>' .
             '<li><p>Hiring specialists instead of generalists</p></li>' .
             '<li><p>Creating coverage across more functions</p></li>' .
             '<li><p>Scaling up or down based on demand</p></li>' .
             '</ul>' .
             '<p></p>' .
             '<p>One offshore team member might handle inbox management and scheduling.</p>' .
             '<p>Another might manage invoicing and reconciliations.</p>' .
             '<p>Another might support marketing or CRM updates.</p>' .
             '<p></p>' .
             '<p>Suddenly, the business isn’t just coping, it’s operating with leverage.</p>' .
             '<p></p>' .
             '<p></p>' .
             '<p><strong>WHY SRI LANKA IS EMERGING AS A KEY TALENT HUB</strong></p>' .
             '<p>While many countries offer offshore talent, Sri Lanka is starting to stand out, particularly for Australian businesses.</p>' .
             '<p></p>' .
             '<p>It offers a combination that is hard to replicate:</p>' .
             '<ul>' .
             '<li><p>Strong English proficiency</p></li>' .
             '<li><p>Highly educated graduates across multiple disciplines</p></li>' .
             '<li><p>A deeply ingrained service culture</p></li>' .
             '<li><p>Time zone alignment with Australia</p></li>' .
             '<li><p>Cost structures that make scaling viable</p></li>' .
             '</ul>' .
             '<p></p>' .
             '<p>But more importantly, the talent is adaptable, professional, and relationship-driven, which matters far more than cost alone.</p>' .
             '<p></p>' .
             '<p></p>' .
             '<p><strong>THIS ISN’T ABOUT CUTTING COSTS</strong></p>' .
             '<p>The biggest misconception about this model is that it’s purely about saving money.</p>' .
             '<p></p>' .
             '<p>The most successful businesses aren’t doing this to reduce cost.</p>' .
             '<p></p>' .
             '<p>They’re doing it to:</p>' .
             '<ul>' .
             '<li><p>Move faster</p></li>' .
             '<li><p>Focus their local teams on high-value work</p></li>' .
             '<li><p>Create capacity without long hiring cycles</p></li>' .
             '<li><p>Build resilience into their operations</p></li>' .
             '</ul>' .
             '<p></p>' .
             '<p>Cost is simply the enabler.</p>' .
             '<p></p>' .
             '<p>Capability is the outcome.</p>' .
             '<p></p>' .
             '<p></p>' .
             '<p><strong>THE BUSINESSES THAT WIN WILL BUILD GLOBAL TEAMS EARLY</strong></p>' .
             '<p>This shift is still under the radar.</p>' .
             '<p></p>' .
             '<p>But it won’t be for long.</p>' .
             '<p></p>' .
             '<p>In the same way cloud computing changed infrastructure, and remote work changed how teams operate…</p>' .
             '<p></p>' .
             '<p>Co-sourcing is changing how businesses build capability.</p>' .
             '<p></p>' .
             '<p>The companies that embrace this early will have a structural advantage:</p>' .
             '<ul>' .
             '<li><p>Leaner operations</p></li>' .
             '<li><p>More flexible cost bases</p></li>' .
             '<li><p>Access to broader talent pools</p></li>' .
             '<li><p>Faster execution</p></li>' .
             '</ul>' .
             '<p></p>' .
             '<strong>FINAL THOUGHT</strong>' .
             '<p></p>' .
             '<p>This is not about replacing local jobs.</p>' .
             '<p></p>' .
             '<p>It’s about unlocking capacity.</p>' .
             '<p></p>' .
             '<p>Because when your team is no longer constrained by geography, you stop asking “Who can we afford to hire?”</p>' .
             '<p></p>' .
             '<p>And start asking:</p>' .
             '<p>“What could we build if we had the right team?”</p>';

// Update featured post
$featured['content'] = $cleanHtml;
\Illuminate\Support\Facades\DB::table('page_contents')
    ->where('id', 29)
    ->update(['value' => json_encode($featured)]);

// Update posts array
foreach ($posts as &$post) {
    if (strpos($post['title'], 'Advantages') !== false) {
        $post['content'] = $cleanHtml;
    }
}
\Illuminate\Support\Facades\DB::table('page_contents')
    ->where('id', 30)
    ->update(['value' => json_encode($posts)]);

echo "Force raw SQL update completed successfully!\n";
?>

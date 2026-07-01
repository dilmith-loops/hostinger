<?php

namespace App\Http\Controllers;

use App\Models\SeoSetting;
use Illuminate\Http\Response;

class SitemapController extends Controller
{
    private static array $STATIC_PAGES = [
        ['loc' => '/',            'priority' => '1.0',  'changefreq' => 'daily'],
        ['loc' => '/about',       'priority' => '0.8',  'changefreq' => 'weekly'],
        ['loc' => '/solutions',   'priority' => '0.9',  'changefreq' => 'weekly'],
        ['loc' => '/solutions/virtual-assistants',  'priority' => '0.8', 'changefreq' => 'weekly'],
        ['loc' => '/solutions/customer-service',    'priority' => '0.8', 'changefreq' => 'weekly'],
        ['loc' => '/solutions/digital-marketers',   'priority' => '0.8', 'changefreq' => 'weekly'],
        ['loc' => '/solutions/it-helpdesk',         'priority' => '0.8', 'changefreq' => 'weekly'],
        ['loc' => '/solutions/book-keepers',        'priority' => '0.8', 'changefreq' => 'weekly'],
        ['loc' => '/solutions/call-centre',         'priority' => '0.8', 'changefreq' => 'weekly'],
        ['loc' => '/blog',        'priority' => '0.8',  'changefreq' => 'daily'],
        ['loc' => '/contact',     'priority' => '0.7',  'changefreq' => 'monthly'],
        ['loc' => '/faq',         'priority' => '0.7',  'changefreq' => 'monthly'],
        ['loc' => '/sri-lanka',   'priority' => '0.8',  'changefreq' => 'monthly'],
    ];

    public function index(): Response
    {
        $baseUrl = rtrim(config('app.url'), '/');
        $seoRows = SeoSetting::all()->keyBy('page')->toArray();
        $now     = now()->toAtomString();

        $xml = '<?xml version="1.0" encoding="UTF-8"?>' . "\n";
        $xml .= '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"' . "\n";
        $xml .= '        xmlns:xhtml="http://www.w3.org/1999/xhtml">' . "\n";

        foreach (self::$STATIC_PAGES as $page) {
            $slug = trim($page['loc'], '/') ?: 'home';
            $row  = $seoRows[$slug] ?? [];

            $priority   = $row['sitemap_priority']   ?? $page['priority'];
            $changefreq = $row['sitemap_changefreq'] ?? $page['changefreq'];
            $robotsIdx  = $row['robots_index']       ?? 'index';

            if ($robotsIdx === 'noindex') continue;

            $xml .= "  <url>\n";
            $xml .= "    <loc>" . e($baseUrl . $page['loc']) . "</loc>\n";
            $xml .= "    <lastmod>{$now}</lastmod>\n";
            $xml .= "    <changefreq>{$changefreq}</changefreq>\n";
            $xml .= "    <priority>{$priority}</priority>\n";
            $xml .= "  </url>\n";
        }

        $xml .= '</urlset>';

        return response($xml, 200, ['Content-Type' => 'application/xml']);
    }
}

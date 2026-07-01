<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class SeoSetting extends Model
{
    protected $fillable = [
        'page', 'meta_title', 'meta_description',
        'og_title', 'og_description', 'og_image',
        'canonical_url', 'focus_keyword',
        'robots_index', 'robots_follow',
        'schema_type', 'schema_data',
        'sitemap_priority', 'sitemap_changefreq',
    ];

    protected $casts = [
        'schema_data'      => 'array',
        'sitemap_priority' => 'float',
    ];
}

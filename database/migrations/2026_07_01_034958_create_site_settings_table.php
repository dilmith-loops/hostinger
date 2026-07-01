<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('site_settings', function (Blueprint $table) {
            $table->id();
            $table->string('key')->unique()->index();
            $table->text('value')->nullable();
            $table->timestamps();
        });

        // Seed sensible defaults
        $defaults = [
            'site_name'               => 'Ceylon Talent Connect',
            'site_tagline'            => 'Expert Co-sourcing for Australian Businesses',
            'default_meta_description'=> 'Ceylon Talent Connect connects Australian businesses with high-performing Sri Lankan professionals. Dedicated co-sourcing talent from $1,350/month, ready in 7 days.',
            'default_og_image'        => '',
            'twitter_handle'          => '',
            'ga4_id'                  => '',
            'gtm_id'                  => '',
            'gsc_verification'        => '',
            'meta_pixel_id'           => '',
            'robots_txt'              => "User-agent: *\nAllow: /\nDisallow: /admin\nDisallow: /api/\nSitemap: https://ceylontalentconnect.com/sitemap.xml",
            'org_phone'               => '1300 241 103',
            'org_email'               => 'info@ceylontalentconnect.com',
            'org_address'             => 'Melbourne, Australia & Colombo, Sri Lanka',
            'facebook_url'            => '',
            'linkedin_url'            => '',
            'instagram_url'           => '',
        ];

        foreach ($defaults as $key => $value) {
            \DB::table('site_settings')->insert([
                'key'        => $key,
                'value'      => $value,
                'created_at' => now(),
                'updated_at' => now(),
            ]);
        }
    }

    public function down(): void
    {
        Schema::dropIfExists('site_settings');
    }
};

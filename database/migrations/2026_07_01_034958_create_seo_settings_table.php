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
        Schema::create('seo_settings', function (Blueprint $table) {
            $table->id();
            $table->string('page')->unique()->index();
            $table->string('meta_title', 120)->nullable();
            $table->string('meta_description', 320)->nullable();
            $table->string('og_title', 120)->nullable();
            $table->string('og_description', 320)->nullable();
            $table->string('og_image', 512)->nullable();
            $table->string('canonical_url', 512)->nullable();
            $table->string('focus_keyword', 120)->nullable();
            $table->enum('robots_index', ['index', 'noindex'])->default('index');
            $table->enum('robots_follow', ['follow', 'nofollow'])->default('follow');
            $table->string('schema_type', 60)->default('WebPage');
            $table->json('schema_data')->nullable();
            $table->decimal('sitemap_priority', 2, 1)->default(0.8);
            $table->enum('sitemap_changefreq', ['always','hourly','daily','weekly','monthly','yearly','never'])->default('weekly');
            $table->timestamps();
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('seo_settings');
    }
};

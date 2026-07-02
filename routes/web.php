<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\CMSController;
use App\Http\Controllers\ContactController;
use App\Http\Controllers\SeoController;
use App\Http\Controllers\SitemapController;

// Redirect / to /ctc
Route::get('/', function () {
    return redirect('/ctc');
});

// Contact form
Route::post('/api/contact', [ContactController::class, 'store']);
Route::post('/api/leads', [ContactController::class, 'storeLead']);
Route::get('/api/contact/enquiries', [ContactController::class, 'index']);

// Public SEO endpoints (no auth required — read-only)
Route::get('/api/seo/global', [SeoController::class, 'globalSettings']);
Route::get('/api/seo/{page}', [SeoController::class, 'pageSettings']);

// Sitemap & robots
Route::get('/sitemap.xml', [SitemapController::class, 'index']);
Route::get('/robots.txt', function () {
    $txt = \App\Models\SiteSetting::get('robots_txt', "User-agent: *\nAllow: /");
    return response($txt, 200, ['Content-Type' => 'text/plain']);
});

// CMS APIs
Route::prefix('api/cms')->group(function () {
    Route::post('/auth/login', [CMSController::class, 'login']);
    Route::post('/auth/logout', [CMSController::class, 'logout']);
    Route::get('/auth/me', [CMSController::class, 'me']);

    Route::get('/content/{page}', [CMSController::class, 'getContent']);
    Route::post('/content/save', [CMSController::class, 'saveContent']);
    Route::post('/upload', [CMSController::class, 'upload']);

    // Landing pages APIs
    Route::get('/landing-pages', [CMSController::class, 'getLandingPages']);
    Route::post('/landing-pages', [CMSController::class, 'createLandingPage']);
    Route::delete('/landing-pages/{slug}', [CMSController::class, 'deleteLandingPage']);

    // SEO management (admin only — auth checked inside controller)
    Route::get('/seo/all', [SeoController::class, 'allPages']);
    Route::post('/seo/global', [SeoController::class, 'saveGlobal']);
    Route::post('/seo/page', [SeoController::class, 'savePage']);
});

// Wildcard routing to serve the TanStack prerendered static pages under /ctc
Route::get('/ctc/{any?}', function ($any = '') {
    // If requesting a specific file, check if it exists in public/ctc
    if (!empty($any)) {
        $filePath = public_path("ctc/{$any}");
        if (file_exists($filePath) && !is_dir($filePath)) {
            return response()->file($filePath);
        }
    }

    // Determine the route index.html location
    $routePath = empty($any) ? 'index.html' : "{$any}/index.html";
    $htmlPath = public_path("ctc/{$routePath}");

    if (file_exists($htmlPath)) {
        return response()->file($htmlPath);
    }

    // Fallback to primary index.html
    $fallbackPath = public_path('ctc/index.html');
    if (file_exists($fallbackPath)) {
        return response()->file($fallbackPath);
    }

    return response('CTC App frontend is not built. Please run "npm run build" to compile and deploy the assets.', 404);
})->where('any', '.*');

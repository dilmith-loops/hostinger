<?php

namespace App\Http\Controllers;

use App\Models\SeoSetting;
use App\Models\SiteSetting;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;

class SeoController extends Controller
{
    // ── Public endpoints ──────────────────────────────────────

    /** GET /api/seo/global — Returns site-wide SEO/analytics settings */
    public function globalSettings(): \Illuminate\Http\JsonResponse
    {
        return response()->json(SiteSetting::allAsArray());
    }

    /** GET /api/seo/{page} — Returns per-page SEO settings */
    public function pageSettings(string $page): \Illuminate\Http\JsonResponse
    {
        $row = SeoSetting::where('page', $page)->first();
        return response()->json($row ? $row->toArray() : ['page' => $page]);
    }

    // ── Admin endpoints (auth required) ──────────────────────

    /** POST /api/cms/seo/global — Save site-wide settings */
    public function saveGlobal(Request $request): \Illuminate\Http\JsonResponse
    {
        if (!Auth::check()) {
            return response()->json(['error' => 'Unauthorized'], 401);
        }

        $allowed = [
            'site_name', 'site_tagline', 'default_meta_description',
            'default_og_image', 'twitter_handle',
            'ga4_id', 'gtm_id', 'gsc_verification', 'meta_pixel_id',
            'robots_txt', 'org_phone', 'org_email', 'org_address',
            'facebook_url', 'linkedin_url', 'instagram_url',
        ];

        foreach ($allowed as $key) {
            if ($request->has($key)) {
                SiteSetting::set($key, (string) $request->input($key));
            }
        }

        return response()->json(['success' => true, 'message' => 'Global SEO settings saved.']);
    }

    /** POST /api/cms/seo/page — Save per-page SEO settings */
    public function savePage(Request $request): \Illuminate\Http\JsonResponse
    {
        if (!Auth::check()) {
            return response()->json(['error' => 'Unauthorized'], 401);
        }

        $request->validate(['page' => 'required|string|max:100']);

        $data = $request->only([
            'page', 'meta_title', 'meta_description',
            'og_title', 'og_description', 'og_image',
            'canonical_url', 'focus_keyword',
            'robots_index', 'robots_follow',
            'schema_type', 'schema_data',
            'sitemap_priority', 'sitemap_changefreq',
        ]);

        SeoSetting::updateOrCreate(['page' => $data['page']], $data);

        return response()->json(['success' => true, 'message' => 'Page SEO saved.']);
    }

    /** GET /api/cms/seo/all — All pages SEO for admin overview */
    public function allPages(): \Illuminate\Http\JsonResponse
    {
        if (!Auth::check()) {
            return response()->json(['error' => 'Unauthorized'], 401);
        }

        return response()->json(SeoSetting::all()->keyBy('page'));
    }
}

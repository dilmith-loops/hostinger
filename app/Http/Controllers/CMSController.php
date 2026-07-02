<?php

namespace App\Http\Controllers;

use App\Models\PageContent;
use App\Models\User;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;

class CMSController extends Controller
{
    /**
     * Authenticate admin.
     */
    public function login(Request $request)
    {
        $credentials = $request->validate([
            'email' => ['required', 'email'],
            'password' => ['required'],
        ]);

        if (Auth::attempt($credentials)) {
            $request->session()->regenerate();
            return response()->json([
                'success' => true,
                'user' => Auth::user()
            ]);
        }

        return response()->json([
            'success' => false,
            'message' => 'The provided credentials do not match our records.',
        ], 401);
    }

    /**
     * Log out admin.
     */
    public function logout(Request $request)
    {
        Auth::logout();
        $request->session()->invalidate();
        $request->session()->regenerateToken();

        return response()->json([
            'success' => true
        ]);
    }

    /**
     * Get authenticated admin details.
     */
    public function me()
    {
        $user = Auth::user();
        if ($user) {
            return response()->json([
                'authenticated' => true,
                'user' => $user
            ]);
        }

        return response()->json([
            'authenticated' => false
        ], 401);
    }

    /**
     * Fetch page content.
     */
    public function getContent($page)
    {
        $contents = PageContent::where('page', $page)->get();
        
        $data = [];
        foreach ($contents as $content) {
            $data[$content->key] = $content->value;
        }

        return response()->json($data);
    }

    /**
     * Save page content.
     */
    public function saveContent(Request $request)
    {
        if (!Auth::check()) {
            return response()->json(['error' => 'Unauthorized'], 401);
        }

        $request->validate([
            'page' => 'required|string',
            'data' => 'required|array',
        ]);

        $page = $request->input('page');
        $data = $request->input('data');

        // Support landing page slug routing changes
        if (str_starts_with($page, 'lp_')) {
            $oldSlug = substr($page, 3);
            $newSlug = isset($data['meta']['slug']) ? trim($data['meta']['slug']) : null;
            if ($newSlug && $newSlug !== $oldSlug) {
                if (!preg_match('/^[a-z0-9-]+$/', $newSlug)) {
                    return response()->json(['error' => 'Slug must contain only lowercase letters, numbers, and hyphens.'], 422);
                }
                $newPageName = 'lp_' . $newSlug;
                if (PageContent::where('page', $newPageName)->exists()) {
                    return response()->json(['error' => 'A landing page with this URL slug already exists.'], 422);
                }
                // Rename all rows in page_contents
                PageContent::where('page', $page)->update(['page' => $newPageName]);
                $page = $newPageName;
            }
        }

        foreach ($data as $key => $value) {
            PageContent::updateOrCreate(
                ['page' => $page, 'key' => $key],
                ['value' => $value]
            );
        }

        return response()->json([
            'success' => true,
            'message' => 'Content saved successfully.',
            'newPage' => $page
        ]);
    }

    /**
     * Handle file upload.
     */
    public function upload(Request $request)
    {
        if (!Auth::check()) {
            return response()->json(['error' => 'Unauthorized'], 401);
        }

        $request->validate([
            'file' => 'required|image|max:10240', // 10MB max
        ]);

        if ($request->hasFile('file')) {
            $file = $request->file('file');
            $extension = $file->getClientOriginalExtension();
            $filename = uniqid('cms_', true) . '.' . $extension;
            
            // Move file to public/uploads
            $file->move(public_path('uploads'), $filename);
            
            // Return public URL path
            $url = '/uploads/' . $filename;
            
            return response()->json([
                'success' => true,
                'url' => $url
            ]);
        }

        return response()->json([
            'success' => false,
            'message' => 'No file uploaded.'
        ], 400);
    }

    /**
     * Get distinct landing pages list.
     */
    public function getLandingPages()
    {
        if (!Auth::check()) {
            return response()->json(['error' => 'Unauthorized'], 401);
        }

        $pages = PageContent::where('page', 'like', 'lp_%')->get()->groupBy('page');
        $result = [];

        foreach ($pages as $pageName => $contents) {
            $slug = substr($pageName, 3); // Remove "lp_" prefix
            $name = '';
            $formTitle = 'Untitled';
            $metaTitle = '';
            foreach ($contents as $c) {
                if ($c->key === 'meta') {
                    if (isset($c->value['name'])) {
                        $name = $c->value['name'];
                    }
                    if (isset($c->value['title'])) {
                        $metaTitle = $c->value['title'];
                    }
                }
                if ($c->key === 'form' && isset($c->value['title'])) {
                    $formTitle = $c->value['title'];
                }
            }
            $result[] = [
                'slug' => $slug,
                'title' => $name ?: ($metaTitle ?: $formTitle),
            ];
        }

        return response()->json($result);
    }

    /**
     * Create a new landing page.
     */
     public function createLandingPage(Request $request)
     {
         if (!Auth::check()) {
             return response()->json(['error' => 'Unauthorized'], 401);
         }

         $validated = $request->validate([
             'slug' => ['required', 'string', 'regex:/^[a-z0-9-]+$/', 'max:100'],
         ]);

         $slug = $validated['slug'];
         $pageName = 'lp_' . $slug;

         // Check if it already exists
         if (PageContent::where('page', $pageName)->exists()) {
             return response()->json(['error' => 'Landing page with this slug already exists.'], 422);
         }

         // We populate with the default landing page data structure (jP)
         $defaultData = [
             'meta' => [
                 'name' => ucwords(str_replace('-', ' ', $slug)),
                 'title' => 'Free 2-Week VA Trial — Ceylon Talent Connect',
                 'description' => 'Get a professional virtual assistant for your business, free for 2 weeks. No contract. No commitment.'
             ],
             'hero' => [
                 'heading' => 'Get a professional virtual assistant for your business, free for 2 weeks.',
                 'subheadline' => 'No contract. No commitment. Just seamless support from day one.'
             ],
             'form' => [
                 'title' => 'Claim Your Free 2-Week Trial',
                 'ctaLabel' => 'Claim My Free Trial',
                 'businessTypes' => ['Medical / Allied Health', 'Legal / Professional Services', 'Trades / Construction', 'Real Estate', 'Retail / E-commerce', 'Other'],
                 'helpOptions' => ['Email and inbox management', 'Scheduling and calendar management', 'Data entry and admin tasks', 'Customer follow-ups', 'General business support'],
                 'privacyText' => 'By submitting this form, you agree to be contacted by Ceylon Talent Connect regarding your free trial enquiry. Your details will not be shared with third parties.'
             ],
             'thankYou' => [
                 'heading' => "You're on your way!",
                 'message' => 'Thanks! A member of our team will be in touch within 1 business day to get your trial started.',
                 'eta' => 'Within 1 business day'
             ]
         ];

         foreach ($defaultData as $key => $value) {
             PageContent::create([
                 'page' => $pageName,
                 'key' => $key,
                 'value' => $value
             ]);
         }

         return response()->json(['success' => true, 'slug' => $slug]);
     }

    /**
     * Delete a landing page.
     */
    public function deleteLandingPage($slug)
    {
        if (!Auth::check()) {
            return response()->json(['error' => 'Unauthorized'], 401);
        }

        PageContent::where('page', 'lp_' . $slug)->delete();

        return response()->json(['success' => true]);
    }
}

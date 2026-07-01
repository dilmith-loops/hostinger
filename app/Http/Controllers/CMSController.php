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

        foreach ($data as $key => $value) {
            PageContent::updateOrCreate(
                ['page' => $page, 'key' => $key],
                ['value' => $value]
            );
        }

        return response()->json([
            'success' => true,
            'message' => 'Content saved successfully.'
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
}

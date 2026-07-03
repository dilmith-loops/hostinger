import re

js_file = r"d:\laragon\www\hostinger\public\ctc\assets\index-Yw1fTNC7.js"
web_file = r"d:\laragon\www\hostinger\routes\web.php"

# --- 1. Modify routes/web.php ---
print("Modifying routes/web.php...")
with open(web_file, "r", encoding="utf-8") as f:
    web_content = f.read()

# Replace the redirect at the beginning
old_redirect = """// Redirect / to /ctc
Route::get('/', function () {
    return redirect('/ctc');
});"""

# We can replace the redirect with nothing or a comment, because the fallback route at the bottom will handle /
new_redirect = "// Serve React app directly from the root domain"
if old_redirect in web_content:
    web_content = web_content.replace(old_redirect, new_redirect)
    print("  Removed / to /ctc redirect.")
else:
    # Let's try matching with different spacing/newlines
    pattern = r"//\s*Redirect\s*/\s*to\s*/ctc\s*Route::get\('/',\s*function\s*\(\)\s*\{\s*return\s*redirect\('/ctc'\);\s*\}\);"
    if re.search(pattern, web_content):
        web_content = re.sub(pattern, new_redirect, web_content)
        print("  Removed / to /ctc redirect (regex).")
    else:
        print("  Warning: / to /ctc redirect pattern not found in routes/web.php.")

# Replace the wildcard route
old_route = """// Wildcard routing to serve the TanStack prerendered static pages under /ctc
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
})->where('any', '.*');"""

new_route = """// Wildcard routing to serve the TanStack prerendered static pages under the root domain
Route::get('/{any?}', function ($any = '') {
    // If requesting a specific file, check if it exists in public/ctc
    if (!empty($any)) {
        $cleanPath = str_starts_with($any, 'ctc/') ? substr($any, 4) : $any;
        $filePath = public_path("ctc/{$cleanPath}");
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
})->where('any', '.*');"""

if old_route in web_content:
    web_content = web_content.replace(old_route, new_route)
    print("  Updated wildcard route to handle root path /.")
else:
    # Try generic find-and-replace for the Route::get('/ctc/{any?}' block
    start_pattern = "Route::get('/ctc/{any?}'"
    end_pattern = "->where('any', '.*');"
    start_idx = web_content.find(start_pattern)
    end_idx = web_content.find(end_pattern, start_idx)
    if start_idx != -1 and end_idx != -1:
        web_content = web_content[:start_idx] + new_route + web_content[end_idx + len(end_pattern):]
        print("  Updated wildcard route via index location.")
    else:
        print("  Error: Could not find wildcard route in routes/web.php.")
        exit(1)

with open(web_file, "w", encoding="utf-8") as f:
    f.write(web_content)


# --- 2. Modify public/ctc/assets/index-Yw1fTNC7.js ---
print("Modifying public/ctc/assets/index-Yw1fTNC7.js...")
with open(js_file, "r", encoding="utf-8") as f:
    js_content = f.read()

replacements = [
    # Router basepath
    ('basepath: "/ctc"', 'basepath: "/"'),
    
    # Route path definitions
    ('id: "/lp/$slug", path: "/lp/$slug"', 'id: "/landing_$slug", path: "/$slug"'),
    ('"/ctc/lp/"', '"/"'),
    ('`/ctc/lp/${o.slug}`', '`/${o.slug}`'),
    ('`/ctc/lp/${m.replace("lp_", "")}`', '`/${m.replace("lp_", "")}`'),
    ('"/ctc/lp/your-slug"', '"/your-slug"'),
    
    # Live preview main link
    ('href: "/ctc"', 'href: "/"'),
    
    # Blog route paths
    ('`/ctc/blog/${y.featured.slug}`', '`/blog/${y.featured.slug}`'),
    ('`/ctc/blog/${j.slug}`', '`/blog/${j.slug}`'),
    
    # Solutions route paths
    ('`/ctc/solutions/${m.replace("solutions_", "")}`', '`/solutions/${m.replace("solutions_", "")}`'),
    ('`/ctc/solutions/${m.replace("solution_", "")}`', '`/solutions/${m.replace("solution_", "")}`'),
]

for old, new in replacements:
    occurrences = js_content.count(old)
    if occurrences > 0:
        js_content = js_content.replace(old, new)
        print(f"  Replaced '{old}' -> '{new}' ({occurrences} times).")
    else:
        print(f"  Warning: '{old}' not found in JS file.")

with open(js_file, "w", encoding="utf-8") as f:
    f.write(js_content)

print("All modifications completed successfully!")

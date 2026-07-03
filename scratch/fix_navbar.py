js_file = r"d:\laragon\www\hostinger\public\ctc\assets\index-Yw1fTNC7.js"

with open(js_file, "r", encoding="utf-8") as f:
    content = f.read()

# We look for the exact pattern around index 1277084:
# u.jsx("style", { dangerouslySetInnerHTML: { __html: "@media (min-width: 1024px) { .lp-hero-wrapper { padding-top: 17rem !important; padding-bottom: 4rem !important; } }" } }), u.jsx(LO, {}), u.jsxs("main"
target = 'u.jsx("style", { dangerouslySetInnerHTML: { __html: "@media (min-width: 1024px) { .lp-hero-wrapper { padding-top: 17rem !important; padding-bottom: 4rem !important; } }" } }), u.jsx(LO, {}), u.jsxs("main"'
replacement = 'u.jsx("style", { dangerouslySetInnerHTML: { __html: "@media (min-width: 1024px) { .lp-hero-wrapper { padding-top: 17rem !important; padding-bottom: 4rem !important; } }" } }), u.jsxs("main"'

if target in content:
    content = content.replace(target, replacement)
    print("Navbar issue fixed in landing page component!")
else:
    # Try finding target with fewer constraints or index matching
    idx = content.find('.lp-hero-wrapper { padding-top: 17rem !important;')
    if idx != -1:
        print("Found partial match at index:", idx)
        context = content[idx-100:idx+300]
        print("Context:", context)
    else:
        print("Error: Could not find target pattern in JS file.")
        exit(1)

with open(js_file, "w", encoding="utf-8") as f:
    f.write(content)

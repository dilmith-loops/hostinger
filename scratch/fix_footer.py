import sys

js_file = "public/ctc/assets/index-Yw1fTNC7.js"

with open(js_file, "r", encoding="utf-8") as f:
    content = f.read()

print("Original length:", len(content))

# 1. In VO(), make t only check for /admin so global header/footer wrap all client pages
vo_target = 't = e.startsWith("/admin") || e.startsWith("/lp/"),'
vo_replace = 't = e.startsWith("/admin"),'
if vo_target not in content:
    print("Error: vo_target not found!")
    sys.exit(1)

content = content.replace(vo_target, vo_replace, 1)
print("Updated VO() condition.")

# 2. In TP(), remove the duplicate inner footer
idx = content.find('function TP()')
footer_target = ', u.jsx("footer", { className: "border-t border-border bg-background"'
f_start = content.find(footer_target, idx)
f_end = content.find('] }) } function Ro(', f_start)

if f_start == -1 or f_end == -1:
    print("Error: could not find footer block in TP()!")
    sys.exit(1)

print("Removing footer snippet of length:", f_end - f_start)
content = content[:f_start] + content[f_end:]

with open(js_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Saved updated index-Yw1fTNC7.js successfully!")

import sys

with open("scratch/inject_testimonials.py", "r", encoding="utf-8") as f:
    text = f.read()

# Load the new video and client blocks from update_testimonials_order.py
with open("scratch/update_testimonials_order.py", "r", encoding="utf-8") as f:
    order_script = f.read()

new_client_marker = "new_client_block = '''"
nc_start = order_script.find(new_client_marker) + len(new_client_marker)
nc_end = order_script.find("'''", nc_start)
new_client_block = order_script[nc_start:nc_end]

new_video_marker = "new_video_block = '''"
nv_start = order_script.find(new_video_marker) + len(new_video_marker)
nv_end = order_script.find("'''", nv_start)
new_video_block = order_script[nv_start:nv_end]

# In inject_testimonials.py:
# Replace videoReviews
old_video_target = 'children: (y.videoReviews?.items || []).map((vItem, vIdx) => {'
v_start = text.find(old_video_target)
v_end_marker = '        })\n      ]\n    }),\n\n    u.jsxs("div", {\n      className: "bg-[#0B192C]'
v_end = text.find(v_end_marker, v_start)

if v_start == -1 or v_end == -1:
    print("Error locating video block in inject_testimonials.py")
    sys.exit(1)

text = text[:v_start] + new_video_block + text[v_end:]

# Replace clientReviews
old_client_target = 'children: (y.clientReviews?.items || []).map((cItem, cIdx) => {'
c_start = text.find(old_client_target)
c_end_marker = '        })\n      ]\n    })\n  ]\n}),\n\'\'\''
c_end = text.find(c_end_marker, c_start)

if c_start == -1 or c_end == -1:
    print("Error locating client block in inject_testimonials.py")
    sys.exit(1)

text = text[:c_start] + new_client_block + text[c_end:]

with open("scratch/inject_testimonials.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Updated scratch/inject_testimonials.py successfully!")

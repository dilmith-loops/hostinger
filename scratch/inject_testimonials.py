import sys

js_file = "public/ctc/assets/index-Yw1fTNC7.js"

with open(js_file, "r", encoding="utf-8") as f:
    content = f.read()

print("Original content size:", len(content))

# 1. Update d2 navigation
d2_old = 'd2 = [{ to: "/", label: "Home" }, { to: "/about", label: "About Us" }, { to: "/solutions", label: "Our Solutions" }, { to: "/sri-lanka", label: "Sri Lanka" }, { to: "/blog", label: "Blogs" }, { to: "/faq", label: "FAQs" }];'
d2_new = 'd2 = [{ to: "/", label: "Home" }, { to: "/about", label: "About Us" }, { to: "/solutions", label: "Our Solutions" }, { to: "/sri-lanka", label: "Sri Lanka" }, { to: "/blog", label: "Blogs" }, { to: "/faq", label: "FAQs" }, { to: "/testimonials", label: "Testimonials" }];'

if d2_old not in content:
    print("Error: d2_old pattern not found!")
    sys.exit(1)
content = content.replace(d2_old, d2_new, 1)
print("1. Updated d2 navigation.")

# 2. Update Se sidebar in CMS
se_old = 'const Se = [{ id: "home", label: "Home Page", icon: o_ }, { id: "about", label: "About Page", icon: Ks }, { id: "solutions", label: "Solutions", icon: qt }, { id: "sri_lanka", label: "Sri Lanka", icon: _s }, { id: "faq", label: "FAQ Page", icon: Cx },'
se_new = 'const Se = [{ id: "home", label: "Home Page", icon: o_ }, { id: "about", label: "About Page", icon: Ks }, { id: "solutions", label: "Solutions", icon: qt }, { id: "sri_lanka", label: "Sri Lanka", icon: _s }, { id: "faq", label: "FAQ Page", icon: Cx }, { id: "testimonials", label: "Testimonials", icon: qt },'

if se_old not in content:
    print("Error: se_old pattern not found!")
    sys.exit(1)
content = content.replace(se_old, se_new, 1)
print("2. Updated Se sidebar.")

# 3. Update tP SEO selector
tp_old = 'const tP = [{ key: "home", label: "Home" }, { key: "about", label: "About" }, { key: "solutions", label: "Solutions" }, { key: "solutions/virtual-assistants", label: "Solutions — Virtual Assistants" }, { key: "solutions/customer-service", label: "Solutions — Customer Service" }, { key: "solutions/digital-marketers", label: "Solutions — Digital Marketers" }, { key: "solutions/it-helpdesk", label: "Solutions — IT Helpdesk" }, { key: "solutions/book-keepers", label: "Solutions — Book-Keepers" }, { key: "solutions/call-centre", label: "Solutions — Call Centre" }, { key: "blog", label: "Blog" }, { key: "contact", label: "Contact" }, { key: "faq", label: "FAQs" }, { key: "sri-lanka", label: "Sri Lanka" }],'
tp_new = 'const tP = [{ key: "home", label: "Home" }, { key: "about", label: "About" }, { key: "solutions", label: "Solutions" }, { key: "solutions/virtual-assistants", label: "Solutions — Virtual Assistants" }, { key: "solutions/customer-service", label: "Solutions — Customer Service" }, { key: "solutions/digital-marketers", label: "Solutions — Digital Marketers" }, { key: "solutions/it-helpdesk", label: "Solutions — IT Helpdesk" }, { key: "solutions/book-keepers", label: "Solutions — Book-Keepers" }, { key: "solutions/call-centre", label: "Solutions — Call Centre" }, { key: "blog", label: "Blog" }, { key: "contact", label: "Contact" }, { key: "faq", label: "FAQs" }, { key: "sri-lanka", label: "Sri Lanka" }, { key: "testimonials", label: "Testimonials" }],'

if tp_old not in content:
    print("Error: tp_old pattern not found!")
    sys.exit(1)
content = content.replace(tp_old, tp_new, 1)
print("3. Updated tP SEO selector.")

# 4. Update gy default content
gy_old = 'gy = {\n  home: {'
gy_new = '''gy = {
  testimonials: {
    hero: {
      heading: "Client Success",
      highlight: "Stories",
      subheadline: "Hear directly from our partners about how Ceylon Talent Connect has helped them build high-performing teams and scale their operations successfully."
    },
    videoReviews: {
      sectionTitle: "Video Reviews",
      items: [
        {
          id: 1,
          title: "ShadeLux",
          videoUrl: "https://youtu.be/wMmSQ7eGjeU?si=Mi_AaoppMAHVb_mH",
          thumbnail: "/uploads/testimonials/shadelux_card.png",
          quote: "A fantastic experience working with Ceylon Talent Connect.",
          authorName: "Shade Lux",
          authorRole: "Client",
          avatarInitials: "SL",
          avatarBg: "#EF4444"
        }
      ]
    },
    clientReviews: {
      sectionTitle: "Client Reviews",
      items: [
        {
          id: 1,
          clientName: "Caleb Hughes",
          clientRole: "Owner, Shadelux",
          company: "Shadelux",
          cardImage: "/uploads/testimonials/caleb_card.png",
          rating: 5,
          quote: "I am so pleased that I took a leap of faith and decided to give CTC a go. I must admit to being a little sceptical at first, but from the first meeting I felt completely at ease. Since then, my experience has been nothing other than professional, and very rewarding. Everyone in the team has been great to deal with, and my expectations have been exceeded. I have no hesitations in highly recommending."
        },
        {
          id: 2,
          clientName: "Peter Solomon",
          clientRole: "COO, Moorup",
          company: "Moorup",
          cardImage: "/uploads/testimonials/solomon_card_hq.png",
          rating: 5,
          quote: "As a small business, outsourcing to CTC has been one of our best decisions. Over the last few years they\\'ve helped us with admin, pricing, invoicing, and customer support, freeing up our time to focus on growing the business. Importantly, they are an integral part of our team. I would highly recommend to anyone involved in a SME business."
        },
        {
          id: 3,
          clientName: "Zac Freidin",
          clientRole: "Owner, Eye View Media",
          company: "Eye View Media",
          cardImage: "/uploads/testimonials/zac_card.png",
          rating: 5,
          quote: "The team at CTC have really helped me and my business over the last year. Their wide range of services like Virtual Assistants have created efficiency within my business doing all the admin work. I would highly recommend them to anyone with a service based business."
        }
      ]
    }
  },
  home: {'''

if gy_old not in content:
    print("Error: gy_old pattern not found!")
    sys.exit(1)
content = content.replace(gy_old, gy_new, 1)
print("4. Updated gy default content.")

# 5. Add CMS testimonials editor into sP
cms_faq_target = 'm === "faq" && y.hero &&'
cms_testimonials_code = '''m === "testimonials" && y.hero && u.jsxs(u.Fragment, {
  children: [
    u.jsxs("div", {
      className: "bg-[#0B192C] border border-[#1E3E62] rounded-xl p-6 space-y-4",
      children: [
        u.jsxs("h3", {
          className: "text-sm font-bold text-white border-b border-[#1E3E62] pb-2 flex items-center gap-2",
          children: [u.jsx(qt, { className: "h-4 w-4 text-[#FF8E25]" }), "Hero Section"]
        }),
        u.jsxs("div", {
          className: "grid md:grid-cols-2 gap-4",
          children: [
            u.jsxs("div", {
              children: [
                u.jsx("label", { className: "block text-xs font-semibold text-gray-400 mb-1", children: "Headline (Main Text)" }),
                u.jsx("input", {
                  type: "text",
                  value: y.hero.heading || "",
                  onChange: j => X("hero", "heading", j.target.value),
                  className: "w-full bg-[#060D17] border border-[#1E3E62] rounded-lg px-3 py-2 text-sm text-white focus:outline-none focus:border-[#FF8E25]"
                })
              ]
            }),
            u.jsxs("div", {
              children: [
                u.jsx("label", { className: "block text-xs font-semibold text-gray-400 mb-1", children: "Highlight Word (e.g. Stories in Coral Red)" }),
                u.jsx("input", {
                  type: "text",
                  value: y.hero.highlight || "",
                  onChange: j => X("hero", "highlight", j.target.value),
                  className: "w-full bg-[#060D17] border border-[#1E3E62] rounded-lg px-3 py-2 text-sm text-white focus:outline-none focus:border-[#FF8E25]"
                })
              ]
            })
          ]
        }),
        u.jsxs("div", {
          children: [
            u.jsx("label", { className: "block text-xs font-semibold text-gray-400 mb-1", children: "Subheadline Description" }),
            u.jsx("textarea", {
              rows: 2,
              value: y.hero.subheadline || "",
              onChange: j => X("hero", "subheadline", j.target.value),
              className: "w-full bg-[#060D17] border border-[#1E3E62] rounded-lg px-3 py-2 text-sm text-white focus:outline-none focus:border-[#FF8E25]"
            })
          ]
        })
      ]
    }),

    u.jsxs("div", {
      className: "bg-[#0B192C] border border-[#1E3E62] rounded-xl p-6 space-y-4",
      children: [
        u.jsxs("div", {
          className: "border-b border-[#1E3E62] pb-2 flex items-center justify-between",
          children: [
            u.jsxs("h3", {
              className: "text-sm font-bold text-white flex items-center gap-2",
              children: [u.jsx(qt, { className: "h-4 w-4 text-[#FF8E25]" }), "Video Reviews"]
            }),
            u.jsxs("button", {
              onClick: () => {
                const newItems = [...(y.videoReviews?.items || [])];
                newItems.push({
                  id: Date.now(),
                  title: "New Video",
                  videoUrl: "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                  thumbnail: "/uploads/testimonials/shadelux_card.png",
                  quote: "A fantastic experience working with Ceylon Talent Connect.",
                  authorName: "Client Name",
                  authorRole: "Client",
                  avatarInitials: "CN",
                  avatarBg: "#EF4444"
                });
                X("videoReviews", "items", newItems);
              },
              className: "bg-[#1E3E62] hover:bg-[#FF8E25] text-white px-3 py-1 rounded text-xs font-bold transition flex items-center gap-1",
              children: ["+ Add Video Review"]
            })
          ]
        }),
        u.jsxs("div", {
          children: [
            u.jsx("label", { className: "block text-xs font-semibold text-gray-400 mb-1", children: "Section Title" }),
            u.jsx("input", {
              type: "text",
              value: y.videoReviews?.sectionTitle || "Video Reviews",
              onChange: j => X("videoReviews", "sectionTitle", j.target.value),
              className: "w-full bg-[#060D17] border border-[#1E3E62] rounded-lg px-3 py-2 text-sm text-white focus:outline-none focus:border-[#FF8E25]"
            })
          ]
        }),
        u.jsx("div", {
          className: "space-y-4 pt-2",
          children: (y.videoReviews?.items || []).map((vItem, vIdx) => {
            return u.jsxs("div", {
              key: vItem.id || vIdx,
              draggable: true,
              onDragStart: j => {
                j.dataTransfer.setData("text/plain", vIdx.toString());
                j.dataTransfer.effectAllowed = "move";
              },
              onDragOver: j => {
                j.preventDefault();
                j.dataTransfer.dropEffect = "move";
              },
              onDrop: j => {
                j.preventDefault();
                const srcIdx = parseInt(j.dataTransfer.getData("text/plain"), 10);
                if (!isNaN(srcIdx) && srcIdx !== vIdx) {
                  const items = [...(y.videoReviews?.items || [])];
                  const [moved] = items.splice(srcIdx, 1);
                  items.splice(vIdx, 0, moved);
                  X("videoReviews", "items", items);
                }
              },
              className: "bg-[#060D17] border border-[#1E3E62] hover:border-[#2A5282] rounded-xl p-4 space-y-3 relative transition",
              children: [
                u.jsxs("div", {
                  className: "flex items-center justify-between pb-2 border-b border-[#1E3E62] gap-2 flex-wrap",
                  children: [
                    u.jsxs("div", {
                      className: "flex items-center gap-2 min-w-0",
                      children: [
                        u.jsx("span", {
                          className: "cursor-grab active:cursor-grabbing text-gray-400 hover:text-[#FF8E25] select-none text-xs px-1.5 py-0.5 rounded bg-[#1E3E62]/40 border border-[#1E3E62]/60 font-mono tracking-tighter",
                          title: "Drag to reorder",
                          children: "⠿⠿"
                        }),
                        vItem.thumbnail ? u.jsx("img", {
                          src: vItem.thumbnail,
                          alt: "",
                          className: "w-6 h-6 rounded object-cover border border-[#1E3E62] shrink-0"
                        }) : null,
                        u.jsxs("span", {
                          className: "text-xs font-bold text-gray-300 truncate",
                          children: ["Video #", vIdx + 1, " — ", vItem.title || "Video"]
                        })
                      ]
                    }),
                    u.jsxs("div", {
                      className: "flex items-center gap-1.5 shrink-0",
                      children: [
                        u.jsxs("div", {
                          className: "flex items-center gap-1 bg-[#0B192C] border border-[#1E3E62] rounded px-2 py-0.5 text-xs text-gray-300",
                          title: "Change position order directly",
                          children: [
                            u.jsx("span", { className: "text-[10px] text-gray-400 font-semibold uppercase tracking-wider", children: "Order:" }),
                            u.jsx("select", {
                              value: vIdx + 1,
                              onChange: j => {
                                const targetIdx = parseInt(j.target.value, 10) - 1;
                                if (targetIdx === vIdx) return;
                                const items = [...(y.videoReviews?.items || [])];
                                const [moved] = items.splice(vIdx, 1);
                                items.splice(targetIdx, 0, moved);
                                X("videoReviews", "items", items);
                              },
                              className: "bg-transparent text-white text-xs font-bold focus:outline-none cursor-pointer",
                              children: (y.videoReviews?.items || []).map((_, i) =>
                                u.jsx("option", { key: i + 1, value: i + 1, className: "bg-[#060D17] text-white", children: `${i + 1}` }, i + 1)
                              )
                            })
                          ]
                        }),
                        u.jsxs("button", {
                          type: "button",
                          disabled: vIdx === 0,
                          onClick: () => {
                            if (vIdx <= 0) return;
                            const items = [...(y.videoReviews?.items || [])];
                            const temp = items[vIdx];
                            items[vIdx] = items[vIdx - 1];
                            items[vIdx - 1] = temp;
                            X("videoReviews", "items", items);
                          },
                          className: `px-2 py-1 rounded text-xs font-semibold flex items-center gap-1 transition ${
                            vIdx === 0
                              ? "text-gray-600 bg-gray-900/30 cursor-not-allowed border border-transparent"
                              : "text-gray-200 bg-[#1E3E62] hover:bg-[#FF8E25] hover:text-white cursor-pointer border border-[#1E3E62]"
                          }`,
                          title: "Move video up in order",
                          children: [
                            u.jsx("svg", {
                              className: "w-3 h-3",
                              fill: "none",
                              stroke: "currentColor",
                              viewBox: "0 0 24 24",
                              children: u.jsx("path", { strokeLinecap: "round", strokeLinejoin: "round", strokeWidth: "2.5", d: "M5 15l7-7 7 7" })
                            }),
                            "Up"
                          ]
                        }),
                        u.jsxs("button", {
                          type: "button",
                          disabled: vIdx === (y.videoReviews?.items || []).length - 1,
                          onClick: () => {
                            const items = [...(y.videoReviews?.items || [])];
                            if (vIdx >= items.length - 1) return;
                            const temp = items[vIdx];
                            items[vIdx] = items[vIdx + 1];
                            items[vIdx + 1] = temp;
                            X("videoReviews", "items", items);
                          },
                          className: `px-2 py-1 rounded text-xs font-semibold flex items-center gap-1 transition ${
                            vIdx === (y.videoReviews?.items || []).length - 1
                              ? "text-gray-600 bg-gray-900/30 cursor-not-allowed border border-transparent"
                              : "text-gray-200 bg-[#1E3E62] hover:bg-[#FF8E25] hover:text-white cursor-pointer border border-[#1E3E62]"
                          }`,
                          title: "Move video down in order",
                          children: [
                            u.jsx("svg", {
                              className: "w-3 h-3",
                              fill: "none",
                              stroke: "currentColor",
                              viewBox: "0 0 24 24",
                              children: u.jsx("path", { strokeLinecap: "round", strokeLinejoin: "round", strokeWidth: "2.5", d: "M19 9l-7 7-7-7" })
                            }),
                            "Down"
                          ]
                        }),
                        u.jsx("button", {
                          type: "button",
                          onClick: () => {
                            const newItems = (y.videoReviews?.items || []).filter((_, i) => i !== vIdx);
                            X("videoReviews", "items", newItems);
                          },
                          className: "text-red-400 hover:text-red-300 text-xs font-semibold ml-1 px-2 py-1 rounded hover:bg-red-950/40 transition",
                          children: "Remove"
                        })
                      ]
                    })
                  ]
                }),
                u.jsxs("div", {
                  className: "grid md:grid-cols-2 gap-3",
                  children: [
                    u.jsxs("div", {
                      children: [
                        u.jsx("label", { className: "block text-[11px] text-gray-400 mb-1", children: "Video / YouTube URL" }),
                        u.jsx("input", {
                          type: "text",
                          value: vItem.videoUrl || "",
                          onChange: j => {
                            const newItems = [...y.videoReviews.items];
                            newItems[vIdx] = { ...newItems[vIdx], videoUrl: j.target.value };
                            X("videoReviews", "items", newItems);
                          },
                          placeholder: "https://www.youtube.com/watch?v=...",
                          className: "w-full bg-[#0B192C] border border-[#1E3E62] rounded px-3 py-1.5 text-xs text-white"
                        })
                      ]
                    }),
                    u.jsxs("div", {
                      children: [
                        u.jsx("label", { className: "block text-[11px] text-gray-400 mb-1", children: "Thumbnail Image" }),
                        u.jsxs("div", {
                          className: "flex gap-2 items-center",
                          children: [
                            vItem.thumbnail ? u.jsx("img", {
                              src: vItem.thumbnail,
                              alt: "Preview",
                              className: "h-9 w-9 rounded object-cover border border-[#1E3E62] shrink-0 bg-[#0B192C]"
                            }) : null,
                            u.jsx("input", {
                              type: "text",
                              value: vItem.thumbnail || "",
                              onChange: j => {
                                const newItems = [...y.videoReviews.items];
                                newItems[vIdx] = { ...newItems[vIdx], thumbnail: j.target.value };
                                X("videoReviews", "items", newItems);
                              },
                              className: "flex-1 bg-[#0B192C] border border-[#1E3E62] rounded px-3 py-1.5 text-xs text-white"
                            }),
                            u.jsxs("label", {
                              className: "bg-[#1E3E62] hover:bg-[#FF8E25] text-white px-2.5 py-1.5 rounded text-xs font-bold cursor-pointer transition shrink-0 flex items-center gap-1",
                              children: [
                                "Upload",
                                u.jsx("input", {
                                  type: "file",
                                  accept: "image/*",
                                  className: "hidden",
                                  onChange: j => {
                                    if (j.target.files?.[0]) {
                                      const file = j.target.files[0];
                                      const fd = new FormData();
                                      fd.append("file", file);
                                      Rn.promise(
                                        fetch("/api/cms/upload", { method: "POST", body: fd }).then(async r => {
                                          if (!r.ok) throw new Error("Upload failed");
                                          const data = await r.json();
                                          const newItems = [...y.videoReviews.items];
                                          newItems[vIdx] = { ...newItems[vIdx], thumbnail: data.url };
                                          X("videoReviews", "items", newItems);
                                          return data.url;
                                        }),
                                        { loading: "Uploading...", success: "Thumbnail uploaded!", error: "Upload failed" }
                                      );
                                    }
                                  }
                                })
                              ]
                            })
                          ]
                        })
                      ]
                    })
                  ]
                }),
                u.jsxs("div", {
                  children: [
                    u.jsx("label", { className: "block text-[11px] text-gray-400 mb-1", children: "Quote" }),
                    u.jsx("textarea", {
                      rows: 2,
                      value: vItem.quote || "",
                      onChange: j => {
                        const newItems = [...y.videoReviews.items];
                        newItems[vIdx] = { ...newItems[vIdx], quote: j.target.value };
                        X("videoReviews", "items", newItems);
                      },
                      className: "w-full bg-[#0B192C] border border-[#1E3E62] rounded px-3 py-1.5 text-xs text-white"
                    })
                  ]
                }),
                u.jsxs("div", {
                  className: "grid md:grid-cols-3 gap-3",
                  children: [
                    u.jsxs("div", {
                      children: [
                        u.jsx("label", { className: "block text-[11px] text-gray-400 mb-1", children: "Author Name" }),
                        u.jsx("input", {
                          type: "text",
                          value: vItem.authorName || "",
                          onChange: j => {
                            const newItems = [...y.videoReviews.items];
                            newItems[vIdx] = { ...newItems[vIdx], authorName: j.target.value };
                            X("videoReviews", "items", newItems);
                          },
                          className: "w-full bg-[#0B192C] border border-[#1E3E62] rounded px-3 py-1.5 text-xs text-white"
                        })
                      ]
                    }),
                    u.jsxs("div", {
                      children: [
                        u.jsx("label", { className: "block text-[11px] text-gray-400 mb-1", children: "Author Role" }),
                        u.jsx("input", {
                          type: "text",
                          value: vItem.authorRole || "",
                          onChange: j => {
                            const newItems = [...y.videoReviews.items];
                            newItems[vIdx] = { ...newItems[vIdx], authorRole: j.target.value };
                            X("videoReviews", "items", newItems);
                          },
                          className: "w-full bg-[#0B192C] border border-[#1E3E62] rounded px-3 py-1.5 text-xs text-white"
                        })
                      ]
                    }),
                    u.jsxs("div", {
                      children: [
                        u.jsx("label", { className: "block text-[11px] text-gray-400 mb-1", children: "Avatar Initials" }),
                        u.jsx("input", {
                          type: "text",
                          value: vItem.avatarInitials || "",
                          onChange: j => {
                            const newItems = [...y.videoReviews.items];
                            newItems[vIdx] = { ...newItems[vIdx], avatarInitials: j.target.value };
                            X("videoReviews", "items", newItems);
                          },
                          className: "w-full bg-[#0B192C] border border-[#1E3E62] rounded px-3 py-1.5 text-xs text-white"
                        })
                      ]
                    })
                  ]
                })
              ]
            });
          })        })
      ]
    }),

    u.jsxs("div", {
      className: "bg-[#0B192C] border border-[#1E3E62] rounded-xl p-6 space-y-4",
      children: [
        u.jsxs("div", {
          className: "border-b border-[#1E3E62] pb-2 flex items-center justify-between",
          children: [
            u.jsxs("h3", {
              className: "text-sm font-bold text-white flex items-center gap-2",
              children: [u.jsx(qt, { className: "h-4 w-4 text-[#FF8E25]" }), "Client Reviews"]
            }),
            u.jsxs("button", {
              onClick: () => {
                const newItems = [...(y.clientReviews?.items || [])];
                newItems.push({
                  id: Date.now(),
                  clientName: "New Client",
                  clientRole: "CEO, Company",
                  company: "Company",
                  cardImage: "",
                  rating: 5,
                  quote: "Working with Ceylon Talent Connect has been a transformative experience for our operations."
                });
                X("clientReviews", "items", newItems);
              },
              className: "bg-[#1E3E62] hover:bg-[#FF8E25] text-white px-3 py-1 rounded text-xs font-bold transition flex items-center gap-1",
              children: ["+ Add Client Review"]
            })
          ]
        }),
        u.jsxs("div", {
          children: [
            u.jsx("label", { className: "block text-xs font-semibold text-gray-400 mb-1", children: "Section Title" }),
            u.jsx("input", {
              type: "text",
              value: y.clientReviews?.sectionTitle || "Client Reviews",
              onChange: j => X("clientReviews", "sectionTitle", j.target.value),
              className: "w-full bg-[#060D17] border border-[#1E3E62] rounded-lg px-3 py-2 text-sm text-white focus:outline-none focus:border-[#FF8E25]"
            })
          ]
        }),
        u.jsx("div", {
          className: "space-y-4 pt-2",
          children: (y.clientReviews?.items || []).map((cItem, cIdx) => {
            return u.jsxs("div", {
              key: cItem.id || cIdx,
              draggable: true,
              onDragStart: j => {
                j.dataTransfer.setData("text/plain", cIdx.toString());
                j.dataTransfer.effectAllowed = "move";
              },
              onDragOver: j => {
                j.preventDefault();
                j.dataTransfer.dropEffect = "move";
              },
              onDrop: j => {
                j.preventDefault();
                const srcIdx = parseInt(j.dataTransfer.getData("text/plain"), 10);
                if (!isNaN(srcIdx) && srcIdx !== cIdx) {
                  const items = [...(y.clientReviews?.items || [])];
                  const [moved] = items.splice(srcIdx, 1);
                  items.splice(cIdx, 0, moved);
                  X("clientReviews", "items", items);
                }
              },
              className: "bg-[#060D17] border border-[#1E3E62] hover:border-[#2A5282] rounded-xl p-4 space-y-3 relative transition",
              children: [
                u.jsxs("div", {
                  className: "flex items-center justify-between pb-2 border-b border-[#1E3E62] gap-2 flex-wrap",
                  children: [
                    u.jsxs("div", {
                      className: "flex items-center gap-2 min-w-0",
                      children: [
                        u.jsx("span", {
                          className: "cursor-grab active:cursor-grabbing text-gray-400 hover:text-[#FF8E25] select-none text-xs px-1.5 py-0.5 rounded bg-[#1E3E62]/40 border border-[#1E3E62]/60 font-mono tracking-tighter",
                          title: "Drag to reorder",
                          children: "⠿⠿"
                        }),
                        cItem.cardImage ? u.jsx("img", {
                          src: cItem.cardImage,
                          alt: "",
                          className: "w-6 h-6 rounded object-cover border border-[#1E3E62] shrink-0"
                        }) : null,
                        u.jsxs("span", {
                          className: "text-xs font-bold text-gray-300 truncate",
                          children: ["Review #", cIdx + 1, " — ", cItem.clientName || "Client"]
                        })
                      ]
                    }),
                    u.jsxs("div", {
                      className: "flex items-center gap-1.5 shrink-0",
                      children: [
                        u.jsxs("div", {
                          className: "flex items-center gap-1 bg-[#0B192C] border border-[#1E3E62] rounded px-2 py-0.5 text-xs text-gray-300",
                          title: "Change position order directly",
                          children: [
                            u.jsx("span", { className: "text-[10px] text-gray-400 font-semibold uppercase tracking-wider", children: "Order:" }),
                            u.jsx("select", {
                              value: cIdx + 1,
                              onChange: j => {
                                const targetIdx = parseInt(j.target.value, 10) - 1;
                                if (targetIdx === cIdx) return;
                                const items = [...(y.clientReviews?.items || [])];
                                const [moved] = items.splice(cIdx, 1);
                                items.splice(targetIdx, 0, moved);
                                X("clientReviews", "items", items);
                              },
                              className: "bg-transparent text-white text-xs font-bold focus:outline-none cursor-pointer",
                              children: (y.clientReviews?.items || []).map((_, i) =>
                                u.jsx("option", { key: i + 1, value: i + 1, className: "bg-[#060D17] text-white", children: `${i + 1}` }, i + 1)
                              )
                            })
                          ]
                        }),
                        u.jsxs("button", {
                          type: "button",
                          disabled: cIdx === 0,
                          onClick: () => {
                            if (cIdx <= 0) return;
                            const items = [...(y.clientReviews?.items || [])];
                            const temp = items[cIdx];
                            items[cIdx] = items[cIdx - 1];
                            items[cIdx - 1] = temp;
                            X("clientReviews", "items", items);
                          },
                          className: `px-2 py-1 rounded text-xs font-semibold flex items-center gap-1 transition ${
                            cIdx === 0
                              ? "text-gray-600 bg-gray-900/30 cursor-not-allowed border border-transparent"
                              : "text-gray-200 bg-[#1E3E62] hover:bg-[#FF8E25] hover:text-white cursor-pointer border border-[#1E3E62]"
                          }`,
                          title: "Move review up in order",
                          children: [
                            u.jsx("svg", {
                              className: "w-3 h-3",
                              fill: "none",
                              stroke: "currentColor",
                              viewBox: "0 0 24 24",
                              children: u.jsx("path", { strokeLinecap: "round", strokeLinejoin: "round", strokeWidth: "2.5", d: "M5 15l7-7 7 7" })
                            }),
                            "Up"
                          ]
                        }),
                        u.jsxs("button", {
                          type: "button",
                          disabled: cIdx === (y.clientReviews?.items || []).length - 1,
                          onClick: () => {
                            const items = [...(y.clientReviews?.items || [])];
                            if (cIdx >= items.length - 1) return;
                            const temp = items[cIdx];
                            items[cIdx] = items[cIdx + 1];
                            items[cIdx + 1] = temp;
                            X("clientReviews", "items", items);
                          },
                          className: `px-2 py-1 rounded text-xs font-semibold flex items-center gap-1 transition ${
                            cIdx === (y.clientReviews?.items || []).length - 1
                              ? "text-gray-600 bg-gray-900/30 cursor-not-allowed border border-transparent"
                              : "text-gray-200 bg-[#1E3E62] hover:bg-[#FF8E25] hover:text-white cursor-pointer border border-[#1E3E62]"
                          }`,
                          title: "Move review down in order",
                          children: [
                            u.jsx("svg", {
                              className: "w-3 h-3",
                              fill: "none",
                              stroke: "currentColor",
                              viewBox: "0 0 24 24",
                              children: u.jsx("path", { strokeLinecap: "round", strokeLinejoin: "round", strokeWidth: "2.5", d: "M19 9l-7 7-7-7" })
                            }),
                            "Down"
                          ]
                        }),
                        u.jsx("button", {
                          type: "button",
                          onClick: () => {
                            const newItems = (y.clientReviews?.items || []).filter((_, i) => i !== cIdx);
                            X("clientReviews", "items", newItems);
                          },
                          className: "text-red-400 hover:text-red-300 text-xs font-semibold ml-1 px-2 py-1 rounded hover:bg-red-950/40 transition",
                          children: "Remove"
                        })
                      ]
                    })
                  ]
                }),
                u.jsxs("div", {
                  className: "grid md:grid-cols-2 gap-3",
                  children: [
                    u.jsxs("div", {
                      children: [
                        u.jsx("label", { className: "block text-[11px] text-gray-400 mb-1", children: "Review Graphic Card Image" }),
                        u.jsxs("div", {
                          className: "flex gap-2 items-center",
                          children: [
                            cItem.cardImage ? u.jsx("img", {
                              src: cItem.cardImage,
                              alt: "Preview",
                              className: "h-9 w-9 rounded object-cover border border-[#1E3E62] shrink-0 bg-[#0B192C]"
                            }) : null,
                            u.jsx("input", {
                              type: "text",
                              value: cItem.cardImage || "",
                              onChange: j => {
                                const newItems = [...y.clientReviews.items];
                                newItems[cIdx] = { ...newItems[cIdx], cardImage: j.target.value };
                                X("clientReviews", "items", newItems);
                              },
                              placeholder: "/uploads/testimonials/...",
                              className: "flex-1 bg-[#0B192C] border border-[#1E3E62] rounded px-3 py-1.5 text-xs text-white"
                            }),
                            u.jsxs("label", {
                              className: "bg-[#1E3E62] hover:bg-[#FF8E25] text-white px-2.5 py-1.5 rounded text-xs font-bold cursor-pointer transition shrink-0 flex items-center gap-1",
                              children: [
                                "Upload Card",
                                u.jsx("input", {
                                  type: "file",
                                  accept: "image/*",
                                  className: "hidden",
                                  onChange: j => {
                                    if (j.target.files?.[0]) {
                                      const file = j.target.files[0];
                                      const fd = new FormData();
                                      fd.append("file", file);
                                      Rn.promise(
                                        fetch("/api/cms/upload", { method: "POST", body: fd }).then(async r => {
                                          if (!r.ok) throw new Error("Upload failed");
                                          const data = await r.json();
                                          const newItems = [...y.clientReviews.items];
                                          newItems[cIdx] = { ...newItems[cIdx], cardImage: data.url };
                                          X("clientReviews", "items", newItems);
                                          return data.url;
                                        }),
                                        { loading: "Uploading card...", success: "Card image uploaded!", error: "Upload failed" }
                                      );
                                    }
                                  }
                                })
                              ]
                            })
                          ]
                        })
                      ]
                    }),
                    u.jsxs("div", {
                      className: "grid grid-cols-2 gap-2",
                      children: [
                        u.jsxs("div", {
                          children: [
                            u.jsx("label", { className: "block text-[11px] text-gray-400 mb-1", children: "Client Name" }),
                            u.jsx("input", {
                              type: "text",
                              value: cItem.clientName || "",
                              onChange: j => {
                                const newItems = [...y.clientReviews.items];
                                newItems[cIdx] = { ...newItems[cIdx], clientName: j.target.value };
                                X("clientReviews", "items", newItems);
                              },
                              className: "w-full bg-[#0B192C] border border-[#1E3E62] rounded px-3 py-1.5 text-xs text-white"
                            })
                          ]
                        }),
                        u.jsxs("div", {
                          children: [
                            u.jsx("label", { className: "block text-[11px] text-gray-400 mb-1", children: "Role / Company" }),
                            u.jsx("input", {
                              type: "text",
                              value: cItem.clientRole || "",
                              onChange: j => {
                                const newItems = [...y.clientReviews.items];
                                newItems[cIdx] = { ...newItems[cIdx], clientRole: j.target.value };
                                X("clientReviews", "items", newItems);
                              },
                              className: "w-full bg-[#0B192C] border border-[#1E3E62] rounded px-3 py-1.5 text-xs text-white"
                            })
                          ]
                        })
                      ]
                    })
                  ]
                }),
                u.jsxs("div", {
                  children: [
                    u.jsx("label", { className: "block text-[11px] text-gray-400 mb-1", children: "Review Quote" }),
                    u.jsx("textarea", {
                      rows: 2,
                      value: cItem.quote || "",
                      onChange: j => {
                        const newItems = [...y.clientReviews.items];
                        newItems[cIdx] = { ...newItems[cIdx], quote: j.target.value };
                        X("clientReviews", "items", newItems);
                      },
                      className: "w-full bg-[#0B192C] border border-[#1E3E62] rounded px-3 py-1.5 text-xs text-white"
                    })
                  ]
                })
              ]
            });
          })        })
      ]
    })
  ]
}),
'''

if cms_faq_target not in content:
    print("Error: cms_faq_target not found!")
    sys.exit(1)
content = content.replace(cms_faq_target, cms_testimonials_code + cms_faq_target, 1)
print("5. Injected CMS testimonials editor into sP.")

# 6. Add TestimonialsPageComp component & Route Definition
testimonials_page_code = '''
function TestimonialsPageComp() {
  const defaultData = {
    hero: {
      heading: "Client Success",
      highlight: "Stories",
      subheadline: "Hear directly from our partners about how Ceylon Talent Connect has helped them build high-performing teams and scale their operations successfully."
    },
    videoReviews: {
      sectionTitle: "Video Reviews",
      items: [
        {
          id: 1,
          title: "ShadeLux",
          videoUrl: "https://youtu.be/wMmSQ7eGjeU?si=Mi_AaoppMAHVb_mH",
          thumbnail: "/uploads/testimonials/shadelux_card.png",
          quote: "A fantastic experience working with Ceylon Talent Connect.",
          authorName: "Shade Lux",
          authorRole: "Client",
          avatarInitials: "SL",
          avatarBg: "#EF4444"
        }
      ]
    },
    clientReviews: {
      sectionTitle: "Client Reviews",
      items: [
        {
          id: 1,
          clientName: "Caleb Hughes",
          clientRole: "Owner, Shadelux",
          company: "Shadelux",
          cardImage: "/uploads/testimonials/caleb_card.png",
          rating: 5,
          quote: "I am so pleased that I took a leap of faith and decided to give CTC a go. I must admit to being a little sceptical at first, but from the first meeting I felt completely at ease. Since then, my experience has been nothing other than professional, and very rewarding. Everyone in the team has been great to deal with, and my expectations have been exceeded. I have no hesitations in highly recommending."
        },
        {
          id: 2,
          clientName: "Peter Solomon",
          clientRole: "COO, Moorup",
          company: "Moorup",
          cardImage: "/uploads/testimonials/solomon_card_hq.png",
          rating: 5,
          quote: "As a small business, outsourcing to CTC has been one of our best decisions. Over the last few years they\\'ve helped us with admin, pricing, invoicing, and customer support, freeing up our time to focus on growing the business. Importantly, they are an integral part of our team. I would highly recommend to anyone involved in a SME business."
        },
        {
          id: 3,
          clientName: "Zac Freidin",
          clientRole: "Owner, Eye View Media",
          company: "Eye View Media",
          cardImage: "/uploads/testimonials/zac_card.png",
          rating: 5,
          quote: "The team at CTC have really helped me and my business over the last year. Their wide range of services like Virtual Assistants have created efficiency within my business doing all the admin work. I would highly recommend them to anyone with a service based business."
        }
      ]
    }
  };

  const { content: n } = bs("testimonials", defaultData);
  const hero = (n && n.hero) || defaultData.hero;
  const videoReviews = (n && n.videoReviews) || defaultData.videoReviews;
  const clientReviews = (n && n.clientReviews) || defaultData.clientReviews;
  const videoItems = (videoReviews && videoReviews.items) || defaultData.videoReviews.items;
  const reviewItems = (clientReviews && clientReviews.items) || defaultData.clientReviews.items;

  const [carouselIdx, setCarouselIdx] = F.useState(0);

  const prevReview = () => {
    setCarouselIdx(p => (p <= 0 ? reviewItems.length - 1 : p - 1));
  };
  const nextReview = () => {
    setCarouselIdx(p => (p >= reviewItems.length - 1 ? 0 : p + 1));
  };

  const visibleCards = F.useMemo(() => {
    if (!reviewItems || reviewItems.length === 0) return [];
    if (reviewItems.length === 1) return [reviewItems[0]];
    if (reviewItems.length === 2) {
      return carouselIdx % 2 === 0 ? [reviewItems[0], reviewItems[1]] : [reviewItems[1], reviewItems[0]];
    }
    const first = reviewItems[carouselIdx % reviewItems.length];
    const second = reviewItems[(carouselIdx + 1) % reviewItems.length];
    return [first, second];
  }, [reviewItems, carouselIdx]);

  const getEmbedUrl = url => {
    if (!url) return "";
    const m = url.match(/(?:youtu\\.be\\/|youtube\\.com\\/(?:embed\\/|v\\/|watch\\?v=|watch\\?.+&v=))([\\w-]{11})/);
    return m ? `https://www.youtube.com/embed/${m[1]}` : url;
  };

  const seo = Br("testimonials");
  const global = Qs();

  return u.jsxs(u.Fragment, {
    children: [
      u.jsx(zr, { page: "testimonials", seo: seo, global: global }),

      // Hero Section
      u.jsxs("section", {
        className: "relative overflow-hidden bg-[#0A192F] text-white py-20 lg:py-28 text-center",
        style: {
          background: "radial-gradient(ellipse at 50% 20%, #152C47 0%, #0A192F 70%, #060D17 100%)"
        },
        children: [
          u.jsxs("div", {
            className: "mx-auto max-w-[1000px] px-6",
            children: [
              u.jsxs("h1", {
                className: "text-4xl sm:text-5xl lg:text-6xl font-extrabold tracking-tight text-white",
                children: [
                  hero.heading || "Client Success",
                  " ",
                  u.jsx("span", {
                    style: { color: "#FF4D4D" },
                    children: hero.highlight || "Stories"
                  })
                ]
              }),
              u.jsx("p", {
                className: "mt-6 text-base sm:text-lg text-gray-300 max-w-2xl mx-auto leading-relaxed font-normal",
                children: hero.subheadline || "Hear directly from our partners about how Ceylon Talent Connect has helped them build high-performing teams and scale their operations successfully."
              })
            ]
          })
        ]
      }),

      // Video Reviews Section
      u.jsxs("section", {
        className: "py-16 sm:py-20",
        style: { backgroundColor: "#F9FAFC" },
        children: [
          u.jsxs("div", {
            className: "mx-auto px-6 sm:px-12",
            style: { maxWidth: "1040px", margin: "0 auto" },
            children: [
              u.jsx("h2", {
                className: "font-extrabold text-[#1E293B] text-center tracking-tight",
                style: { fontSize: "26px", fontWeight: "800", color: "#1E293B", textAlign: "center", marginBottom: "32px" },
                children: videoReviews.sectionTitle || "Video Reviews"
              }),
              u.jsx("div", {
                className: "flex flex-wrap justify-start gap-6 sm:gap-8",
                style: { display: "flex", flexWrap: "wrap", justifyContent: "flex-start", gap: "24px" },
                children: videoItems.map((item, idx) => {
                  const embedUrl = getEmbedUrl(item.videoUrl);
                  const rawQuote = (item.quote || "A fantastic experience working with Ceylon Talent Connect.").trim();
                  const displayQuote = rawQuote.startsWith('"') || rawQuote.startsWith('“') || rawQuote.startsWith("'") ? rawQuote : `"${rawQuote}"`;
                  const initials = item.avatarInitials || (item.authorName ? item.authorName.split(" ").map(w=>w[0]).join("").slice(0, 2).toUpperCase() : "SL");

                  return u.jsxs("div", {
                    key: item.id || idx,
                    className: "card-video-review bg-white rounded-2xl border border-gray-200/80 shadow-sm hover:shadow-md transition-all duration-300 overflow-hidden flex flex-col",
                    style: { width: "245px", maxWidth: "100%", flexShrink: 0, borderRadius: "16px", backgroundColor: "#FFFFFF", border: "1px solid rgba(229,231,235,0.8)" },
                    children: [
                      u.jsx("div", {
                        className: "relative bg-black overflow-hidden",
                        style: { width: "100%", height: "128px", borderTopLeftRadius: "16px", borderTopRightRadius: "16px", overflow: "hidden" },
                        children: embedUrl ? u.jsx("iframe", {
                          src: embedUrl,
                          title: item.title || "Video Review",
                          className: "border-0",
                          style: { width: "100%", height: "100%", display: "block", border: 0 },
                          allow: "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share",
                          allowFullScreen: true
                        }) : u.jsx("img", {
                          src: item.thumbnail || "/uploads/testimonials/shadelux_card.png",
                          alt: item.title || "Video thumbnail",
                          className: "object-cover",
                          style: { width: "100%", height: "100%", objectFit: "cover", display: "block" }
                        })
                      }),
                      u.jsxs("div", {
                        className: "flex-1 flex flex-col justify-between",
                        style: { padding: "16px" },
                        children: [
                          u.jsx("p", {
                            className: "font-normal leading-relaxed",
                            style: { fontSize: "13.5px", lineHeight: "1.45", color: "#374151", marginBottom: "16px" },
                            children: displayQuote
                          }),
                          u.jsxs("div", {
                            className: "flex items-center gap-3",
                            style: { display: "flex", alignItems: "center", gap: "12px" },
                            children: [
                              u.jsx("div", {
                                className: "rounded-full flex items-center justify-center text-white font-bold shrink-0 shadow-sm",
                                style: { width: "34px", height: "34px", minWidth: "34px", borderRadius: "9999px", backgroundColor: item.avatarBg || "#EF4444", fontSize: "11px" },
                                children: initials
                              }),
                              u.jsxs("div", {
                                children: [
                                  u.jsx("h4", {
                                    className: "font-bold text-gray-900 leading-snug",
                                    style: { fontSize: "13.5px", fontWeight: "700", color: "#111827", margin: 0 },
                                    children: item.authorName || "Shade Lux"
                                  }),
                                  u.jsx("p", {
                                    className: "text-gray-500 font-normal",
                                    style: { fontSize: "11.5px", color: "#6B7280", marginTop: "2px", margin: 0 },
                                    children: item.authorRole || "Client"
                                  })
                                ]
                              })
                            ]
                          })
                        ]
                      })
                    ]
                  });
                })
              })
            ]
          })
        ]
      }),

      // Client Reviews Section
      u.jsxs("section", {
        className: "py-16 sm:py-20",
        style: { backgroundColor: "#F9FAFC" },
        children: [
          u.jsxs("div", {
            className: "mx-auto px-4 sm:px-6 lg:px-8",
            style: { maxWidth: "1040px", margin: "0 auto" },
            children: [
              u.jsx("h2", {
                className: "font-extrabold text-[#1E293B] text-center tracking-tight",
                style: { fontSize: "26px", fontWeight: "800", color: "#1E293B", textAlign: "center", marginBottom: "36px" },
                children: clientReviews.sectionTitle || "Client Reviews"
              }),
              u.jsxs("div", {
                className: "client-reviews-container relative w-full flex items-center justify-center",
                style: { position: "relative", width: "100%", maxWidth: "760px", margin: "0 auto" },
                children: [
                  u.jsx("button", {
                    onClick: prevReview,
                    className: "absolute z-20 rounded-full bg-white border border-gray-200/90 shadow-md hover:shadow-lg flex items-center justify-center text-gray-700 hover:text-gray-950 transition-all duration-200 active:scale-95 cursor-pointer focus:outline-none",
                    style: {
                      position: "absolute",
                      left: "-18px",
                      top: "50%",
                      transform: "translateY(-50%)",
                      width: "38px",
                      height: "38px",
                      zIndex: 20,
                      backgroundColor: "#FFFFFF",
                      borderRadius: "9999px",
                      border: "1px solid #E5E7EB",
                      boxShadow: "0 2px 8px rgba(0,0,0,0.08)",
                      cursor: "pointer"
                    },
                    "aria-label": "Previous review",
                    children: u.jsx("svg", {
                      className: "w-4 h-4",
                      style: { width: "16px", height: "16px" },
                      fill: "none",
                      viewBox: "0 0 24 24",
                      stroke: "currentColor",
                      strokeWidth: "2.5",
                      children: u.jsx("path", { strokeLinecap: "round", strokeLinejoin: "round", d: "M15 19l-7-7 7-7" })
                    })
                  }),
                  u.jsx("div", {
                    className: "grid grid-cols-1 sm:grid-cols-2 gap-5 sm:gap-6 w-full justify-items-center",
                    style: {
                      display: "grid",
                      gridTemplateColumns: "repeat(auto-fit, minmax(280px, 1fr))",
                      gap: "20px",
                      width: "100%",
                      justifyItems: "center"
                    },
                    children: visibleCards.map((item, idx) => {
                      return u.jsxs("div", {
                        key: item.id || idx,
                        className: "card-client-review bg-white rounded-3xl border border-gray-200/90 shadow-sm hover:shadow-md transition-all duration-300 overflow-hidden flex flex-col p-2.5 sm:p-3",
                        style: {
                          width: "100%",
                          maxWidth: "355px",
                          backgroundColor: "#FFFFFF",
                          borderRadius: "20px",
                          border: "1px solid #E5E7EB",
                          boxShadow: "0 1px 4px rgba(0,0,0,0.05)",
                          padding: "10px",
                          display: "flex",
                          flexDirection: "column"
                        },
                        children: [
                          item.cardImage ? u.jsx("img", {
                            src: item.cardImage,
                            alt: `${item.clientName || 'Client'} Review`,
                            className: "w-full h-auto object-cover",
                            style: { width: "100%", height: "auto", borderRadius: "14px", display: "block" }
                          }) : u.jsxs("div", {
                            className: "p-6 flex flex-col justify-between h-full space-y-4",
                            style: { padding: "20px", display: "flex", flexDirection: "column", justifyContent: "space-between", height: "100%" },
                            children: [
                              u.jsxs("div", {
                                className: "flex items-center justify-between",
                                children: [
                                  u.jsx("span", { className: "text-xs font-bold text-gray-400 uppercase", children: "Google Reviews" }),
                                  u.jsx("div", {
                                    className: "flex text-[#FBBC05]",
                                    children: [1, 2, 3, 4, 5].map(s => u.jsx("span", { key: s, children: "★" }))
                                  })
                                ]
                              }),
                              u.jsxs("p", {
                                className: "text-sm text-gray-700 leading-relaxed italic",
                                children: ['"', item.quote, '"']
                              }),
                              u.jsxs("div", {
                                className: "pt-4 border-t border-gray-100",
                                children: [
                                  u.jsx("h4", { className: "font-bold text-gray-900 text-sm", children: item.clientName }),
                                  u.jsx("p", { className: "text-xs text-gray-500", children: item.clientRole || item.company })
                                ]
                              })
                            ]
                          })
                        ]
                      });
                    })
                  }),
                  u.jsx("button", {
                    onClick: nextReview,
                    className: "absolute z-20 rounded-full bg-white border border-gray-200/90 shadow-md hover:shadow-lg flex items-center justify-center text-gray-700 hover:text-gray-950 transition-all duration-200 active:scale-95 cursor-pointer focus:outline-none",
                    style: {
                      position: "absolute",
                      right: "-18px",
                      top: "50%",
                      transform: "translateY(-50%)",
                      width: "38px",
                      height: "38px",
                      zIndex: 20,
                      backgroundColor: "#FFFFFF",
                      borderRadius: "9999px",
                      border: "1px solid #E5E7EB",
                      boxShadow: "0 2px 8px rgba(0,0,0,0.08)",
                      cursor: "pointer"
                    },
                    "aria-label": "Next review",
                    children: u.jsx("svg", {
                      className: "w-4 h-4",
                      style: { width: "16px", height: "16px" },
                      fill: "none",
                      viewBox: "0 0 24 24",
                      stroke: "currentColor",
                      strokeWidth: "2.5",
                      children: u.jsx("path", { strokeLinecap: "round", strokeLinejoin: "round", d: "M9 5l7 7-7 7" })
                    })
                  })
                ]
              })
            ]
          })
        ]
      })
    ]
  });
}

const TestimonialsRouteDef = ys("/testimonials")({
  component: TestimonialsPageComp,
  head: () => ({
    meta: [
      { title: "Client Testimonials & Success Stories | Ceylon Talent Connect" },
      { name: "description", content: "Hear directly from our partners about how Ceylon Talent Connect has helped them build high-performing teams and scale their operations successfully." }
    ]
  })
});
'''

# We insert TestimonialsPageComp and TestimonialsRouteDef right BEFORE `const DP = N6.update`
dp_target = 'const DP = N6.update({ id: "/sri-lanka", path: "/sri-lanka", getParentRoute: () => vs }),'
if dp_target not in content:
    print("Error: dp_target not found!")
    sys.exit(1)

# And right after `const DP = ...`, we add `TestimonialsRouteNode = TestimonialsRouteDef.update({ id: "/testimonials", path: "/testimonials", getParentRoute: () => vs }),`
tp_route_decl = 'TestimonialsRouteNode = TestimonialsRouteDef.update({ id: "/testimonials", path: "/testimonials", getParentRoute: () => vs }), '

content = content.replace(dp_target, testimonials_page_code + "\n" + dp_target + " " + tp_route_decl, 1)
print("6. Injected TestimonialsPageComp component and TestimonialsRouteNode route declaration.")

# 7. Update KP route tree
kp_old = 'KP = { IndexRoute: PP, AboutRoute: IP, AdminRoute: zP, BlogRoute: VP, ContactRoute: BP, FaqRoute: LP, SolutionsRoute: WP, SriLankaRoute: DP, Campaign_landingSlugRoute: qP, LpSlugRoute: HP }'
kp_new = 'KP = { IndexRoute: PP, AboutRoute: IP, AdminRoute: zP, BlogRoute: VP, ContactRoute: BP, FaqRoute: LP, SolutionsRoute: WP, SriLankaRoute: DP, Campaign_landingSlugRoute: qP, LpSlugRoute: HP, TestimonialsRoute: TestimonialsRouteNode }'

if kp_old not in content:
    print("Error: kp_old pattern not found!")
    sys.exit(1)
content = content.replace(kp_old, kp_new, 1)
print("7. Updated KP route tree.")

with open(js_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Successfully wrote updated JS bundle! New size:", len(content))

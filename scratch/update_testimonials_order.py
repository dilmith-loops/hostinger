import sys

js_file = "public/ctc/assets/index-Yw1fTNC7.js"

with open(js_file, "r", encoding="utf-8") as f:
    content = f.read()

print("File size:", len(content))

# 1. Replacement for clientReviews mapping
old_client_target = 'children: (y.clientReviews?.items || []).map((cItem, cIdx) => {'
if old_client_target not in content:
    print("Error: old_client_target not found!")
    sys.exit(1)

# Find the start of clientReviews item map
c_start = content.find(old_client_target)
# Find the end of this map block: it ends right before '        })\n      ]\n    })\n  ]\n}),\n'
c_end_marker = '        })\n      ]\n    })\n  ]\n}),\n'
c_end = content.find(c_end_marker, c_start)

if c_end == -1:
    print("Error: c_end not found!")
    sys.exit(1)

old_client_block = content[c_start:c_end]

new_client_block = '''children: (y.clientReviews?.items || []).map((cItem, cIdx) => {
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
          })'''

content = content[:c_start] + new_client_block + content[c_end:]
print("Updated clientReviews editor block successfully!")

# 2. Replacement for videoReviews mapping
old_video_target = 'children: (y.videoReviews?.items || []).map((vItem, vIdx) => {'
if old_video_target not in content:
    print("Error: old_video_target not found!")
    sys.exit(1)

v_start = content.find(old_video_target)
v_end_marker = '        })\n      ]\n    }),\n\n    u.jsxs("div", {\n      className: "bg-[#0B192C]'
v_end = content.find(v_end_marker, v_start)

if v_end == -1:
    print("Error: v_end not found!")
    sys.exit(1)

new_video_block = '''children: (y.videoReviews?.items || []).map((vItem, vIdx) => {
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
          })'''

content = content[:v_start] + new_video_block + content[v_end:]
print("Updated videoReviews editor block successfully!")

with open(js_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Saved updated index-Yw1fTNC7.js successfully!")

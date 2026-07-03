
$filePath = "d:\laragon\www\hostinger\public\ctc\assets\index-Yw1fTNC7.js"
$content = Get-Content $filePath -Raw -Encoding UTF8

$startPattern = '"enquiries" && u.jsxs("div", { className: "space-y-4"'
$endPattern = '), m === "landing_pages"'

$startIdx = $content.IndexOf($startPattern)
$endIdx = $content.IndexOf($endPattern, $startIdx)

Write-Output "Start: $startIdx, End: $endIdx"

$before = $content.Substring(0, $startIdx)
$after = $content.Substring($endIdx)

# New table-based enquiries panel with search + filter
$newCode = @'
"enquiries" && u.jsxs(u.Fragment, { children: [
  u.jsxs("style", { children: [`.enq-table-wrap{overflow-x:auto;border-radius:12px;border:1px solid #1E3E62;}.enq-table{width:100%;border-collapse:collapse;font-size:12px;}.enq-table thead tr{background:#0B192C;border-bottom:2px solid #1E3E62;}.enq-table th{padding:10px 14px;text-align:left;font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:#9ca3af;white-space:nowrap;}.enq-table tbody tr{border-bottom:1px solid #1E3E62;transition:background .15s;cursor:default;}.enq-table tbody tr:last-child{border-bottom:none;}.enq-table tbody tr:hover{background:#0E243E;}.enq-table td{padding:10px 14px;vertical-align:top;color:#e5e7eb;}.enq-table td.name-cell{white-space:nowrap;font-weight:600;color:#fff;}.enq-table td.email-cell a,.enq-table td.phone-cell a{color:#9ca3af;text-decoration:none;transition:color .15s;}.enq-table td.email-cell a:hover,.enq-table td.phone-cell a:hover{color:#FF8E25;}.enq-chip{display:inline-block;padding:2px 8px;border-radius:9999px;font-size:10px;font-weight:500;background:#1E3E62;color:#d1d5db;margin:1px 2px 1px 0;}.enq-chip-biz{background:#0E243E;border:1px solid rgba(30,62,98,.6);color:#9ca3af;}.enq-timeline{font-size:11px;font-weight:600;color:#FF8E25;white-space:nowrap;}.enq-date{font-size:10px;color:#6b7280;white-space:nowrap;}.enq-notes{font-size:11px;color:#9ca3af;max-width:200px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}.enq-notes-expanded{white-space:pre-wrap;max-width:none;overflow:visible;text-overflow:unset;}.enq-search{width:100%;background:#060D17;border:1px solid #1E3E62;border-radius:8px;padding:8px 12px 8px 34px;font-size:13px;color:#fff;outline:none;transition:border-color .15s;}.enq-search:focus{border-color:#FF8E25;}.enq-search-wrap{position:relative;flex:1;}.enq-search-icon{position:absolute;left:10px;top:50%;transform:translateY(-50%);color:#6b7280;pointer-events:none;}.enq-select{background:#060D17;border:1px solid #1E3E62;border-radius:8px;padding:8px 10px;font-size:12px;color:#d1d5db;outline:none;cursor:pointer;transition:border-color .15s;}.enq-select:focus{border-color:#FF8E25;}.enq-badge-total{background:#1E3E62;color:#d1d5db;font-size:11px;font-weight:600;padding:3px 10px;border-radius:9999px;}.enq-sort-btn{background:none;border:none;cursor:pointer;color:#6b7280;padding:0 4px;font-size:10px;transition:color .15s;}.enq-sort-btn:hover,.enq-sort-btn.active{color:#FF8E25;}.enq-empty{text-align:center;padding:60px 20px;color:#6b7280;}.enq-expand-btn{background:none;border:none;cursor:pointer;color:#FF8E25;font-size:10px;padding:2px 4px;text-decoration:underline;}.enq-row-num{color:#4b5563;font-size:10px;font-family:monospace;}`] }),
  u.jsxs("div", { style:{display:"flex",alignItems:"center",gap:"12px",flexWrap:"wrap",marginBottom:"14px"}, children: [
    u.jsxs("div", { className:"enq-search-wrap", children: [
      u.jsx("svg", { className:"enq-search-icon", width:"14", height:"14", viewBox:"0 0 24 24", fill:"none", stroke:"currentColor", strokeWidth:"2", children: u.jsx("path", { strokeLinecap:"round", strokeLinejoin:"round", d:"M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0" }) }),
      u.jsx("input", { id:"enq-search-input", type:"text", placeholder:"Search by name, email, phone, notes...", className:"enq-search", value:window.__enqSearch||"", onChange:ev=>{window.__enqSearch=ev.target.value;window.__enqForceUpdate&&window.__enqForceUpdate();} })
    ] }),
    u.jsx("select", { id:"enq-filter-timeline", className:"enq-select", value:window.__enqTimeline||"", onChange:ev=>{window.__enqTimeline=ev.target.value;window.__enqForceUpdate&&window.__enqForceUpdate();}, children: [
      u.jsx("option", {value:"", children:"All Timelines"}),
      ...[...new Set((U||[]).map(r=>r.timeline).filter(Boolean))].map(t=>u.jsx("option",{value:t,children:t},t))
    ] }),
    u.jsx("select", { id:"enq-filter-biz", className:"enq-select", value:window.__enqBiz||"", onChange:ev=>{window.__enqBiz=ev.target.value;window.__enqForceUpdate&&window.__enqForceUpdate();}, children: [
      u.jsx("option", {value:"", children:"All Business Types"}),
      ...[...new Set((U||[]).map(r=>r.business_type).filter(Boolean))].map(b=>u.jsx("option",{value:b,children:b},b))
    ] }),
    u.jsxs("button", { onClick:ke, disabled:z, className:"flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-[#1E3E62] hover:bg-[#FF8E25] text-white text-xs font-bold transition disabled:opacity-50", style:{whiteSpace:"nowrap"}, children:[u.jsx(Sk,{className:`h-3.5 w-3.5 ${z?"animate-spin":""}`}),"Refresh"] })
  ] }),
  z ? u.jsxs("div", { className:"h-64 flex flex-col items-center justify-center gap-3", children:[u.jsx(Er,{className:"h-8 w-8 text-[#FF8E25] animate-spin"}),u.jsx("p",{className:"text-sm text-gray-400",children:"Loading enquiries..."})] }) :
  u.jsx(EnquiriesTable, { enquiries: U, l2icon: l2 })
] })
'@

$newContent = $before + $newCode + $after

# Also inject the EnquiriesTable component before the main component. Find a good injection point.
$injectMarker = 'const Se = [{ id: "home"'
$injectIdx = $newContent.IndexOf($injectMarker)

Write-Output "Inject marker found at: $injectIdx"

$componentCode = @'
const EnquiriesTable = ({ enquiries, l2icon }) => {
  const [search, setSearch] = F.useState("");
  const [filterTimeline, setFilterTimeline] = F.useState("");
  const [filterBiz, setFilterBiz] = F.useState("");
  const [sortCol, setSortCol] = F.useState("created_at");
  const [sortDir, setSortDir] = F.useState("desc");
  const [expandedNotes, setExpandedNotes] = F.useState({});

  const timelines = F.useMemo(() => [...new Set((enquiries||[]).map(r=>r.timeline).filter(Boolean))], [enquiries]);
  const bizTypes = F.useMemo(() => [...new Set((enquiries||[]).map(r=>r.business_type).filter(Boolean))], [enquiries]);

  const filtered = F.useMemo(() => {
    let rows = enquiries || [];
    if (search.trim()) {
      const q = search.toLowerCase();
      rows = rows.filter(r =>
        (`${r.first_name} ${r.last_name}`).toLowerCase().includes(q) ||
        (r.email||"").toLowerCase().includes(q) ||
        (r.phone||"").toLowerCase().includes(q) ||
        (r.notes||"").toLowerCase().includes(q) ||
        (r.business_type||"").toLowerCase().includes(q) ||
        ((Array.isArray(r.support)?r.support:JSON.parse(r.support||"[]")).join(" ")).toLowerCase().includes(q)
      );
    }
    if (filterTimeline) rows = rows.filter(r => r.timeline === filterTimeline);
    if (filterBiz) rows = rows.filter(r => r.business_type === filterBiz);
    rows = [...rows].sort((a, b) => {
      let av = a[sortCol]||"", bv = b[sortCol]||"";
      if (sortCol === "created_at") { av = new Date(av); bv = new Date(bv); }
      else { av = String(av).toLowerCase(); bv = String(bv).toLowerCase(); }
      if (av < bv) return sortDir === "asc" ? -1 : 1;
      if (av > bv) return sortDir === "asc" ? 1 : -1;
      return 0;
    });
    return rows;
  }, [enquiries, search, filterTimeline, filterBiz, sortCol, sortDir]);

  const toggleSort = col => { if (sortCol === col) setSortDir(d => d === "asc" ? "desc" : "asc"); else { setSortCol(col); setSortDir("asc"); } };
  const sortIcon = col => sortCol === col ? (sortDir === "asc" ? " ▲" : " ▼") : " ⇅";

  if (!enquiries || enquiries.length === 0) return u.jsxs("div", { className:"h-64 flex flex-col items-center justify-center gap-3 bg-[#0B192C] rounded-xl border border-[#1E3E62]", children:[u.jsx(l2icon,{className:"h-10 w-10 text-gray-600"}),u.jsx("p",{className:"text-sm text-gray-500",children:"No enquiries received yet."})] });

  return u.jsxs("div", { style:{display:"flex",flexDirection:"column",gap:"12px"}, children: [
    u.jsxs("style", { children:[`.enq-table-wrap{overflow-x:auto;border-radius:12px;border:1px solid #1E3E62;}.enq-table{width:100%;border-collapse:collapse;font-size:12px;}.enq-table thead tr{background:#0B192C;border-bottom:2px solid #1E3E62;}.enq-table th{padding:10px 14px;text-align:left;font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:#9ca3af;white-space:nowrap;cursor:pointer;user-select:none;}.enq-table th:hover{color:#FF8E25;}.enq-table tbody tr{border-bottom:1px solid #1E3E62;transition:background .15s;}.enq-table tbody tr:last-child{border-bottom:none;}.enq-table tbody tr:hover{background:#0E243E;}.enq-table td{padding:10px 14px;vertical-align:top;color:#e5e7eb;}.enq-chip{display:inline-block;padding:2px 8px;border-radius:9999px;font-size:10px;font-weight:500;background:#1E3E62;color:#d1d5db;margin:1px 2px 1px 0;}.enq-chip-biz{background:#0E243E;border:1px solid rgba(30,62,98,.6);color:#9ca3af;}.enq-expand-btn{background:none;border:none;cursor:pointer;color:#FF8E25;font-size:10px;padding:2px 0;text-decoration:underline;display:block;margin-top:2px;}.enq-search{width:100%;background:#060D17;border:1px solid #1E3E62;border-radius:8px;padding:8px 12px 8px 34px;font-size:13px;color:#fff;outline:none;transition:border-color .15s;}.enq-search:focus{border-color:#FF8E25;}.enq-search-wrap{position:relative;flex:1;min-width:180px;}.enq-search-icon{position:absolute;left:10px;top:50%;transform:translateY(-50%);color:#6b7280;pointer-events:none;}.enq-select{background:#060D17;border:1px solid #1E3E62;border-radius:8px;padding:8px 10px;font-size:12px;color:#d1d5db;outline:none;cursor:pointer;transition:border-color .15s;}.enq-select:focus{border-color:#FF8E25;}`] }),
    u.jsxs("div", { style:{display:"flex",alignItems:"center",gap:"10px",flexWrap:"wrap"}, children:[
      u.jsxs("div", { className:"enq-search-wrap", children:[
        u.jsx("svg",{className:"enq-search-icon",width:"14",height:"14",viewBox:"0 0 24 24",fill:"none",stroke:"currentColor",strokeWidth:"2",children:u.jsx("path",{strokeLinecap:"round",strokeLinejoin:"round",d:"M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0"})}),
        u.jsx("input",{type:"text",placeholder:"Search name, email, phone, notes...",className:"enq-search",value:search,onChange:ev=>setSearch(ev.target.value)})
      ]}),
      u.jsx("select",{className:"enq-select",value:filterTimeline,onChange:ev=>setFilterTimeline(ev.target.value),children:[u.jsx("option",{value:"",children:"All Timelines"}),...timelines.map(t=>u.jsx("option",{value:t,children:t},t))]}),
      u.jsx("select",{className:"enq-select",value:filterBiz,onChange:ev=>setFilterBiz(ev.target.value),children:[u.jsx("option",{value:"",children:"All Business Types"}),...bizTypes.map(b=>u.jsx("option",{value:b,children:b},b))]}),
      u.jsxs("span",{style:{fontSize:"11px",color:"#9ca3af",whiteSpace:"nowrap",background:"#1E3E62",padding:"4px 10px",borderRadius:"9999px",fontWeight:600},children:[filtered.length," / ",enquiries.length," shown"]})
    ]}),
    filtered.length === 0 ?
      u.jsxs("div",{style:{textAlign:"center",padding:"60px 20px",color:"#6b7280"},children:[u.jsx("p",{style:{fontSize:"14px"},children:"No enquiries match your search/filter criteria."}),u.jsx("button",{style:{marginTop:"10px",background:"none",border:"1px solid #1E3E62",color:"#FF8E25",padding:"6px 14px",borderRadius:"8px",cursor:"pointer",fontSize:"12px"},onClick:()=>{setSearch("");setFilterTimeline("");setFilterBiz("");},children:"Clear Filters"})]}) :
      u.jsx("div",{className:"enq-table-wrap",children:
        u.jsxs("table",{className:"enq-table",children:[
          u.jsx("thead",{children:u.jsxs("tr",{children:[
            u.jsx("th",{style:{width:"28px"},children:"#"}),
            u.jsx("th",{onClick:()=>toggleSort("first_name"),children:`Name${sortIcon("first_name")}`}),
            u.jsx("th",{onClick:()=>toggleSort("email"),children:`Email${sortIcon("email")}`}),
            u.jsx("th",{children:"Phone"}),
            u.jsx("th",{children:"Support Needed"}),
            u.jsx("th",{onClick:()=>toggleSort("business_type"),children:`Business Type${sortIcon("business_type")}`}),
            u.jsx("th",{onClick:()=>toggleSort("timeline"),children:`Timeline${sortIcon("timeline")}`}),
            u.jsx("th",{onClick:()=>toggleSort("created_at"),children:`Date${sortIcon("created_at")}`}),
            u.jsx("th",{children:"Notes"})
          ]})}),
          u.jsx("tbody",{children:filtered.map((j,idx)=>{
            const supArr = Array.isArray(j.support)?j.support:JSON.parse(j.support||"[]");
            const noteExpanded = expandedNotes[j.id];
            return u.jsxs("tr",{key:j.id,children:[
              u.jsx("td",{style:{color:"#4b5563",fontFamily:"monospace",fontSize:"10px"},children:idx+1}),
              u.jsxs("td",{style:{whiteSpace:"nowrap"},children:[
                u.jsxs("span",{style:{fontWeight:600,color:"#fff"},children:[j.first_name," ",j.last_name]}),
              ]}),
              u.jsx("td",{children:u.jsx("a",{href:`mailto:${j.email}`,style:{color:"#9ca3af",textDecoration:"none",transition:"color .15s"},onMouseEnter:e=>e.target.style.color="#FF8E25",onMouseLeave:e=>e.target.style.color="#9ca3af",children:j.email})}),
              u.jsx("td",{style:{whiteSpace:"nowrap"},children:u.jsx("a",{href:`tel:${j.phone}`,style:{color:"#9ca3af",textDecoration:"none",transition:"color .15s"},onMouseEnter:e=>e.target.style.color="#FF8E25",onMouseLeave:e=>e.target.style.color="#9ca3af",children:j.phone})}),
              u.jsx("td",{children:u.jsx("div",{style:{display:"flex",flexWrap:"wrap",gap:"2px",minWidth:"120px"},children:supArr.map((s,i)=>u.jsx("span",{className:"enq-chip",children:s},i))})}),
              u.jsx("td",{children:u.jsx("span",{className:"enq-chip enq-chip-biz",children:j.business_type})}),
              u.jsx("td",{style:{whiteSpace:"nowrap",color:"#FF8E25",fontWeight:600,fontSize:"11px"},children:j.timeline}),
              u.jsx("td",{style:{whiteSpace:"nowrap",color:"#6b7280",fontSize:"10px"},children:new Date(j.created_at).toLocaleDateString("en-AU",{day:"numeric",month:"short",year:"numeric"})}),
              u.jsx("td",{children:j.notes?u.jsxs("div",{children:[u.jsx("p",{style:{fontSize:"11px",color:"#9ca3af",maxWidth:"180px",overflow:noteExpanded?"visible":"hidden",textOverflow:noteExpanded?"unset":"ellipsis",whiteSpace:noteExpanded?"pre-wrap":"nowrap"},children:j.notes}),u.jsx("button",{className:"enq-expand-btn",onClick:()=>setExpandedNotes(p=>({...p,[j.id]:!p[j.id]})),children:noteExpanded?"Show less":"Show more"})]}):u.jsx("span",{style:{color:"#374151",fontSize:"10px"},children:"—"})})
            ]},j.id);
          })})
        ]})
      })
  ]});
};

'@

$beforeInject = $newContent.Substring(0, $injectIdx)
$afterInject = $newContent.Substring($injectIdx)

$finalContent = $beforeInject + $componentCode + $afterInject

# Write back
[System.IO.File]::WriteAllText($filePath, $finalContent, [System.Text.Encoding]::UTF8)
Write-Output "Done! File written successfully."
Write-Output "New file size: $((Get-Item $filePath).Length) bytes"

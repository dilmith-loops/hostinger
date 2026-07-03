import os

file_path = r"d:\laragon\www\hostinger\public\ctc\assets\index-Yw1fTNC7.js"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Replace the EnquiriesTable component
start_marker = "const EnquiriesTable = "
next_marker = "const Se = "

start_idx = content.find(start_marker)
end_idx = content.find(next_marker)

if start_idx == -1 or end_idx == -1:
    print(f"Error: Markers for EnquiriesTable not found. Start: {start_idx}, End: {end_idx}")
    exit(1)

new_component_code = """const EnquiriesTable = ({ enquiries, l2icon }) => {
  const [search, setSearch] = F.useState("");
  const [filterTimeline, setFilterTimeline] = F.useState("");
  const [filterBiz, setFilterBiz] = F.useState("");
  const [filterCampaign, setFilterCampaign] = F.useState("");
  const [sortCol, setSortCol] = F.useState("created_at");
  const [sortDir, setSortDir] = F.useState("desc");
  const [expandedNotes, setExpandedNotes] = F.useState({});

  const timelines = F.useMemo(() => [...new Set((enquiries||[]).map(r=>r.timeline).filter(Boolean))], [enquiries]);
  const bizTypes = F.useMemo(() => [...new Set((enquiries||[]).map(r=>r.business_type).filter(Boolean))], [enquiries]);
  
  const campaigns = F.useMemo(() => {
    const list = (enquiries || [])
      .filter(r => r.timeline === "Immediate (Landing Page)")
      .map(r => {
        if (!r.notes) return "";
        const m = r.notes.match(/Campaign:\\s*(.+)/i);
        return m ? m[1].trim() : "";
      })
      .filter(Boolean);
    return [...new Set(list)];
  }, [enquiries]);

  // Reset campaign filter when timeline changes
  F.useEffect(() => {
    if (filterTimeline !== "Immediate (Landing Page)") {
      setFilterCampaign("");
    }
  }, [filterTimeline]);

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
    if (filterTimeline === "Immediate (Landing Page)" && filterCampaign) {
      rows = rows.filter(r => {
        if (!r.notes) return false;
        const m = r.notes.match(/Campaign:\\s*(.+)/i);
        const c = m ? m[1].trim() : "";
        return c === filterCampaign;
      });
    }
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
  }, [enquiries, search, filterTimeline, filterCampaign, filterBiz, sortCol, sortDir]);

  const toggleSort = col => { if (sortCol === col) setSortDir(d => d === "asc" ? "desc" : "asc"); else { setSortCol(col); setSortDir("asc"); } };
  const sortIcon = col => sortCol === col ? (sortDir === "asc" ? "\\u00a0\\u25B2" : "\\u00a0\\u25BC") : "\\u00a0\\u21D5";

  if (!enquiries || enquiries.length === 0) return u.jsxs("div", { className:"h-64 flex flex-col items-center justify-center gap-3 bg-[#0B192C] rounded-xl border border-[#1E3E62]", children:[u.jsx(l2icon,{className:"h-10 w-10 text-gray-600"}),u.jsx("p",{className:"text-sm text-gray-500",children:"No enquiries received yet."})] });

  return u.jsxs("div", { style:{display:"flex",flexDirection:"column",gap:"14px"}, children: [
    u.jsx("style", { children:[`.enq-table-wrap{overflow-x:auto;border-radius:12px;border:1px solid #1E3E62;background:#0B192C;}.enq-table{width:100%;border-collapse:collapse;font-size:12px;}.enq-table thead tr{background:#0B192C;border-bottom:2px solid #1E3E62;}.enq-table th{padding:12px 14px;text-align:left;font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:#9ca3af;white-space:nowrap;cursor:pointer;user-select:none;transition:color .15s;}.enq-table th:hover{color:#FF8E25;}.enq-table tbody tr{border-bottom:1px solid #1E3E62;transition:background .15s;}.enq-table tbody tr:last-child{border-bottom:none;}.enq-table tbody tr:hover{background:#0E243E;}.enq-table td{padding:12px 14px;vertical-align:top;color:#e5e7eb;}.enq-chip{display:inline-block;padding:2px 8px;border-radius:9999px;font-size:10px;font-weight:500;background:#1E3E62;color:#d1d5db;margin:1px 2px 1px 0;}.enq-chip-biz{background:#0E243E;border:1px solid rgba(30,62,98,.6);color:#9ca3af;}.enq-expand-btn{background:none;border:none;cursor:pointer;color:#FF8E25;font-size:10px;padding:2px 0;text-decoration:underline;display:block;margin-top:2px;}.enq-search{width:100%;background:#060D17;border:1px solid #1E3E62;border-radius:8px;padding:8px 12px 8px 34px;font-size:13px;color:#fff;outline:none;transition:border-color .15s;}.enq-search:focus{border-color:#FF8E25;}.enq-search-wrap{position:relative;flex:1;min-width:240px;}.enq-search-icon{position:absolute;left:12px;top:50%;transform:translateY(-50%);color:#6b7280;pointer-events:none;}.enq-select{background:#060D17;border:1px solid #1E3E62;border-radius:8px;padding:8px 10px;font-size:12px;color:#d1d5db;outline:none;cursor:pointer;transition:border-color .15s;min-width:150px;}.enq-select:focus{border-color:#FF8E25;}`] }),
    u.jsxs("div", { style:{display:"flex",alignItems:"center",gap:"10px",flexWrap:"wrap"}, children:[
      u.jsxs("div", { className:"enq-search-wrap", children:[
        u.jsx("svg",{className:"enq-search-icon",width:"14",height:"14",viewBox:"0 0 24 24",fill:"none",stroke:"currentColor",strokeWidth:"2",children:u.jsx("path",{strokeLinecap:"round",strokeLinejoin:"round",d:"M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0"})}),
        u.jsx("input",{type:"text",placeholder:"Search by name, email, phone, notes...",className:"enq-search",value:search,onChange:ev=>setSearch(ev.target.value)})
      ]}),
      u.jsx("select",{className:"enq-select",value:filterTimeline,onChange:ev=>setFilterTimeline(ev.target.value),children:[u.jsx("option",{value:"",children:"All Timelines"}),...timelines.map(t=>u.jsx("option",{value:t,children:t},t))]}),
      filterTimeline === "Immediate (Landing Page)" && u.jsx("select",{className:"enq-select",value:filterCampaign,onChange:ev=>setFilterCampaign(ev.target.value),children:[u.jsx("option",{value:"",children:"All Landing Pages"}),...campaigns.map(c=>u.jsx("option",{value:c,children:c},c))]}),
      u.jsx("select",{className:"enq-select",value:filterBiz,onChange:ev=>setFilterBiz(ev.target.value),children:[u.jsx("option",{value:"",children:"All Business Types"}),...bizTypes.map(b=>u.jsx("option",{value:b,children:b},b))]}),
      u.jsxs("span",{style:{fontSize:"11px",color:"#9ca3af",whiteSpace:"nowrap",background:"#1E3E62",padding:"6px 12px",borderRadius:"9999px",fontWeight:600},children:[filtered.length," / ",enquiries.length," shown"]})
    ]}),
    filtered.length === 0 ?
      u.jsxs("div",{style:{textAlign:"center",padding:"60px 20px",color:"#6b7280"},children:[u.jsx("p",{style:{fontSize:"14px"},children:"No enquiries match your search/filter criteria."}),u.jsx("button",{style:{marginTop:"10px",background:"none",border:"1px solid #1E3E62",color:"#FF8E25",padding:"6px 14px",borderRadius:"8px",cursor:"pointer",fontSize:"12px"},onClick:()=>{setSearch("");setFilterTimeline("");setFilterCampaign("");setFilterBiz("");},children:"Clear Filters"})]}) :
      u.jsx("div",{className:"enq-table-wrap",children:
        u.jsxs("table",{className:"enq-table",children:[
          u.jsx("thead",{children:u.jsxs("tr",{children:[
            u.jsx("th",{style:{width:"28px"},children:"#"}),
            u.jsx("th",{onClick:()=>toggleSort("first_name"),children:"Name"+sortIcon("first_name")}),
            u.jsx("th",{onClick:()=>toggleSort("email"),children:"Email"+sortIcon("email")}),
            u.jsx("th",{children:"Phone"}),
            u.jsx("th",{children:"Support Needed"}),
            u.jsx("th",{onClick:()=>toggleSort("business_type"),children:"Business Type"+sortIcon("business_type")}),
            u.jsx("th",{onClick:()=>toggleSort("timeline"),children:"Timeline"+sortIcon("timeline")}),
            u.jsx("th",{onClick:()=>toggleSort("created_at"),children:"Date"+sortIcon("created_at")}),
            u.jsx("th",{children:"Notes"})
          ]})}),
          u.jsx("tbody",{children:filtered.map((j,idx)=>{
            const supArr = Array.isArray(j.support)?j.support:JSON.parse(j.support||"[]");
            const noteExpanded = expandedNotes[j.id];
            return u.jsxs("tr",{key:j.id,children:[
              u.jsx("td",{style:{color:"#4b5563",fontFamily:"monospace",fontSize:"10px"},children:idx+1}),
              u.jsx("td",{style:{whiteSpace:"nowrap",fontWeight:600,color:"#fff"},children:[j.first_name," ",j.last_name]}),
              u.jsx("td",{children:u.jsx("a",{href:`mailto:${j.email}`,style:{color:"#9ca3af",textDecoration:"none",transition:"color .15s"},onMouseEnter:e=>e.target.style.color="#FF8E25",onMouseLeave:e=>e.target.style.color="#9ca3af",children:j.email})}),
              u.jsx("td",{style:{whiteSpace:"nowrap"},children:u.jsx("a",{href:`tel:${j.phone}`,style:{color:"#9ca3af",textDecoration:"none",transition:"color .15s"},onMouseEnter:e=>e.target.style.color="#FF8E25",onMouseLeave:e=>e.target.style.color="#9ca3af",children:j.phone})}),
              u.jsx("td",{children:u.jsx("div",{style:{display:"flex",flexWrap:"wrap",gap:"2px",minWidth:"120px"},children:supArr.map((s,i)=>u.jsx("span",{className:"enq-chip",children:s},i))})}),
              u.jsx("td",{children:u.jsx("span",{className:"enq-chip enq-chip-biz",children:j.business_type})}),
              u.jsx("td",{style:{whiteSpace:"nowrap",color:"#FF8E25",fontWeight:600,fontSize:"11px"},children:j.timeline}),
              u.jsx("td",{style:{whiteSpace:"nowrap",color:"#6b7280",fontSize:"10px"},children:new Date(j.created_at).toLocaleDateString("en-AU",{day:"numeric",month:"short",year:"numeric"})}),
              u.jsx("td",{children:j.notes?u.jsxs("div",{children:[u.jsx("p",{style:{fontSize:"11px",color:"#9ca3af",maxWidth:"180px",overflow:noteExpanded?"visible":"hidden",textOverflow:noteExpanded?"unset":"ellipsis",whiteSpace:noteExpanded?"pre-wrap":"nowrap"},children:j.notes}),u.jsx("button",{className:"enq-expand-btn",onClick:()=>setExpandedNotes(p=>({...p,[j.id]:!p[j.id]})),children:noteExpanded?"Show less":"Show more"})]}):u.jsx("span",{style:{color:"#374151",fontSize:"10px"},children:"\\u2014"})})
            ]},j.id);
          })})
        ]})
      })
  ]});
};
"""

content = content[:start_idx] + new_component_code + content[end_idx:]

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Landing page campaign filter logic updated successfully!")

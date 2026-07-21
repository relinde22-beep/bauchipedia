import json

with open("/tmp/claude-0/-home-user-bauchipedia/3f722902-a4d6-55d0-b13a-9e6c4eafbf65/scratchpad/terms.json", encoding="utf-8") as f:
    terms = json.load(f)

terms_json = json.dumps(terms, ensure_ascii=False).replace("</script", "<\\/script")

html = """<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<title>Bauchipedia – Interaktives Gefühlsraster</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
  :root {
    --unangenehm: #6a3fa0;
    --angenehm: #21b39a;
    --ink: #16234a;
    --chip-bg: rgba(255,255,255,0.92);
    --chip-border: rgba(22,35,74,0.15);
    --serif: Georgia, "Iowan Old Style", "Palatino Linotype", "Times New Roman", serif;
    --sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  }
  * { box-sizing: border-box; }
  html, body {
    margin: 0; padding: 0; height: 100%;
    font-family: var(--sans);
    background: #0d1220;
    color: var(--ink);
  }
  @media (prefers-reduced-motion: reduce) {
    .chip, .chip:hover { transition: none !important; transform: translate(-50%, -50%) !important; }
  }
  button:focus-visible, input:focus-visible, .chip:focus-visible {
    outline: 2px solid #7fe0d0;
    outline-offset: 2px;
  }
  #app {
    position: relative;
    width: 100%;
    height: 100vh;
    overflow: hidden;
    background: #0d1220;
  }
  #toolbar {
    position: absolute;
    top: 12px; left: 12px; right: 12px;
    z-index: 30;
    display: flex;
    gap: 10px;
    align-items: flex-start;
    flex-wrap: wrap;
    pointer-events: none;
  }
  #toolbar > * { pointer-events: auto; }
  #wordmark {
    background: rgba(13,18,32,0.85);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 10px;
    padding: 8px 14px;
    color: #fff;
    backdrop-filter: blur(4px);
  }
  #wordmark .title {
    font-family: var(--serif);
    font-size: 15px;
    font-weight: 600;
    letter-spacing: 0.01em;
  }
  #wordmark .sub {
    font-size: 11px;
    color: rgba(255,255,255,0.55);
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-top: 2px;
  }
  #search-wrap {
    position: relative;
    background: rgba(13,18,32,0.85);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 10px;
    padding: 8px 10px;
    backdrop-filter: blur(4px);
  }
  #search {
    background: transparent;
    border: none;
    outline: none;
    color: #fff;
    font-size: 14px;
    width: 220px;
  }
  #search::placeholder { color: rgba(255,255,255,0.5); }
  #search-results {
    position: absolute;
    top: 100%; left: 0; right: 0;
    margin-top: 6px;
    background: #131a2e;
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 8px;
    overflow: hidden;
    display: none;
    max-height: 260px;
    overflow-y: auto;
  }
  #search-results button {
    display: block;
    width: 100%;
    text-align: left;
    background: transparent;
    border: none;
    color: #fff;
    padding: 8px 10px;
    font-size: 14px;
    cursor: pointer;
  }
  #search-results button:hover { background: rgba(255,255,255,0.1); }
  .toolbtn {
    background: rgba(13,18,32,0.85);
    border: 1px solid rgba(255,255,255,0.15);
    color: #fff;
    border-radius: 10px;
    padding: 8px 12px;
    font-size: 14px;
    cursor: pointer;
    backdrop-filter: blur(4px);
  }
  .toolbtn:hover { background: rgba(255,255,255,0.12); }
  #zoomctl {
    display: flex;
    gap: 4px;
    margin-left: auto;
  }
  #hint {
    position: absolute;
    bottom: 10px; left: 12px;
    z-index: 30;
    color: rgba(255,255,255,0.55);
    font-size: 12px;
    background: rgba(13,18,32,0.6);
    padding: 6px 10px;
    border-radius: 8px;
    pointer-events: none;
  }
  #viewport {
    position: absolute;
    inset: 0;
    overflow: hidden;
    cursor: grab;
  }
  #viewport.dragging { cursor: grabbing; }
  #world {
    position: absolute;
    left: 0; top: 0;
    width: WORLD_Wpx;
    height: WORLD_Hpx;
    transform-origin: 0 0;
    background:
      radial-gradient(ellipse at 15% 15%, rgba(120,60,170,0.9), rgba(120,60,170,0) 60%),
      radial-gradient(ellipse at 85% 15%, rgba(30,180,160,0.9), rgba(30,180,160,0) 60%),
      radial-gradient(ellipse at 15% 85%, rgba(150,110,190,0.55), rgba(150,110,190,0) 60%),
      radial-gradient(ellipse at 85% 85%, rgba(90,190,175,0.55), rgba(90,190,175,0) 60%),
      linear-gradient(135deg, #4a2f7a 0%, #35407a 35%, #2b6f7e 65%, #1f9a86 100%);
  }
  .axis-label {
    position: absolute;
    color: rgba(255,255,255,0.92);
    font-weight: 700;
    letter-spacing: 0.1em;
    font-size: 26px;
    text-transform: uppercase;
    pointer-events: none;
    text-shadow: 0 1px 3px rgba(0,0,0,0.4);
    background: rgba(13,18,32,0.32);
    padding: 5px 14px;
    border-radius: 10px;
    backdrop-filter: blur(2px);
    white-space: nowrap;
  }
  #label-top, #label-bottom { transform: translate(-50%, -50%); }
  #label-left { transform: translate(-50%, -50%) rotate(-90deg); }
  #label-right { transform: translate(-50%, -50%) rotate(90deg); }
  .axis-line {
    position: absolute;
    background: rgba(255,255,255,0.25);
    pointer-events: none;
  }
  .chip {
    position: absolute;
    transform: translate(-50%, -50%);
    background: var(--chip-bg);
    border: 1px solid var(--chip-border);
    color: var(--ink);
    padding: 6px 12px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 600;
    white-space: nowrap;
    cursor: pointer;
    box-shadow: 0 1px 4px rgba(0,0,0,0.25);
    transition: opacity .2s ease, transform .15s ease, box-shadow .15s ease;
    user-select: none;
  }
  .chip:hover { transform: translate(-50%, -50%) scale(1.08); }
  .chip.dim { opacity: 0.18; }
  .chip.related {
    background: #ffe9a8;
    border-color: #d9a600;
    box-shadow: 0 0 0 2px #ffcf4d, 0 2px 8px rgba(0,0,0,0.3);
    opacity: 1;
  }
  .chip.active {
    background: #16234a;
    color: #fff;
    box-shadow: 0 0 0 3px #7fe0d0, 0 2px 10px rgba(0,0,0,0.4);
    opacity: 1;
    z-index: 5;
  }
  #overlay {
    position: fixed;
    inset: 0;
    z-index: 100;
    pointer-events: none;
  }
  #popup {
    background: #fff;
    color: var(--ink);
    width: min(380px, 92vw);
    padding: 24px 24px 28px;
    box-shadow: -12px 0 40px rgba(0,0,0,0.35);
    position: absolute;
    top: 0; right: 0; bottom: 0;
    overflow-y: auto;
    pointer-events: auto;
    transform: translateX(100%);
    transition: transform .25s ease;
  }
  #overlay.show #popup { transform: translateX(0); }
  #popup h2 { margin: 0 0 4px; font-size: 26px; font-family: var(--serif); font-weight: 600; letter-spacing: 0.01em; }
  #popup .badge {
    display: inline-block;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    padding: 3px 9px;
    border-radius: 999px;
    margin-bottom: 12px;
    color: #fff;
  }
  #popup .desc { line-height: 1.55; font-size: 15px; margin: 0 0 14px; }
  #popup .example {
    font-style: italic;
    color: #445;
    background: #f4f5fb;
    border-left: 3px solid var(--angenehm);
    padding: 10px 12px;
    border-radius: 6px;
    font-size: 14px;
    margin: 0 0 16px;
  }
  #popup .related-title {
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #888;
    margin-bottom: 8px;
  }
  #popup .related-list { display: flex; flex-wrap: wrap; gap: 6px; }
  #popup .related-list button {
    border: 1px solid var(--chip-border);
    background: #f0f1f7;
    border-radius: 999px;
    padding: 5px 11px;
    font-size: 13px;
    cursor: pointer;
    font-weight: 600;
    color: var(--ink);
  }
  #popup .related-list button:hover { background: #e2e4f2; }
  #popup .related-list span.plain {
    border: 1px dashed #ccc;
    border-radius: 999px;
    padding: 5px 11px;
    font-size: 13px;
    color: #999;
  }
  #popup .close {
    position: absolute;
    top: 14px; right: 14px;
    background: #f0f1f7;
    border: none;
    width: 30px; height: 30px;
    border-radius: 50%;
    font-size: 16px;
    cursor: pointer;
    color: #555;
  }
  #popup .close:hover { background: #e2e4f2; }
</style>
</head>
<body>
<div id="app">
  <div id="viewport">
    <div id="world">
      <div class="axis-label" id="label-top">Aktivierend</div>
      <div class="axis-label" id="label-bottom">Deaktivierend</div>
      <div class="axis-label" id="label-left">Unangenehm</div>
      <div class="axis-label" id="label-right">Angenehm</div>
      <div class="axis-line" style="left:50%; top:0; width:1px; height:100%;"></div>
      <div class="axis-line" style="top:50%; left:0; height:1px; width:100%;"></div>
    </div>
  </div>
  <div id="toolbar">
    <div id="wordmark">
      <div class="title">Bauchipedia</div>
      <div class="sub">Gefühlsraster</div>
    </div>
    <div id="search-wrap">
      <input id="search" type="text" placeholder="Begriff suchen…" autocomplete="off">
      <div id="search-results"></div>
    </div>
    <div id="zoomctl">
      <button class="toolbtn" id="zoom-out">−</button>
      <button class="toolbtn" id="zoom-reset">Reset</button>
      <button class="toolbtn" id="zoom-in">+</button>
    </div>
  </div>
  <div id="hint">Ziehen zum Verschieben · Scrollen/Pinch zum Zoomen · Klick für Details</div>
</div>

<div id="overlay">
  <div id="popup"></div>
</div>

<script>
const TERMS = TERMS_JSON_PLACEHOLDER;

const WORLD_W = WORLD_W_PLACEHOLDER;
const WORLD_H = WORLD_H_PLACEHOLDER;

const byId = {};
TERMS.forEach(t => byId[t.id] = t);

const world = document.getElementById('world');
const viewport = document.getElementById('viewport');

// ---- build chip elements (initial position = zone center, refined by simulation) ----
const margin = 60;
const gap = 30;
const halfW = WORLD_W/2, halfH = WORLD_H/2;

function zoneRect(valence, arousal){
  const x0 = valence === 'unangenehm' ? margin : halfW + gap/2;
  const x1 = valence === 'unangenehm' ? halfW - gap/2 : WORLD_W - margin;
  const y0 = arousal === 'hoch' ? margin : halfH + gap/2;
  const y1 = arousal === 'hoch' ? halfH - gap/2 : WORLD_H - margin;
  return {x0,y0,x1,y1};
}

const nodes = TERMS.map(t => {
  const r = zoneRect(t.valence, t.arousal);
  return {
    id: t.id,
    x: r.x0 + Math.random()*(r.x1-r.x0),
    y: r.y0 + Math.random()*(r.y1-r.y0),
    zone: r,
    vx: 0, vy: 0,
    w: 0, h: 0,
    el: null
  };
});
const nodeById = {};
nodes.forEach(n => nodeById[n.id] = n);

nodes.forEach(n => {
  const t = byId[n.id];
  const el = document.createElement('div');
  el.className = 'chip';
  el.textContent = t.term;
  el.style.left = n.x + 'px';
  el.style.top = n.y + 'px';
  el.dataset.id = n.id;
  el.tabIndex = 0;
  el.setAttribute('role', 'button');
  el.addEventListener('keydown', e => {
    if (e.key === 'Enter' || e.key === ' '){ e.preventDefault(); openPopup(n.id); }
  });
  world.appendChild(el);
  n.el = el;
});

// measure
nodes.forEach(n => {
  n.w = n.el.offsetWidth;
  n.h = n.el.offsetHeight;
});

// ---- simple force simulation (repulsion + related-link springs + zone containment) ----
function simulate(iterations){
  for (let iter=0; iter<iterations; iter++){
    // repulsion
    for (let i=0;i<nodes.length;i++){
      const a = nodes[i];
      for (let j=i+1;j<nodes.length;j++){
        const b = nodes[j];
        let dx = a.x-b.x, dy = a.y-b.y;
        let dist = Math.sqrt(dx*dx+dy*dy) || 0.001;
        const minDistX = (a.w+b.w)/2 + 6;
        const minDistY = (a.h+b.h)/2 + 6;
        const overlapX = minDistX - Math.abs(dx);
        const overlapY = minDistY - Math.abs(dy);
        if (overlapX > 0 && overlapY > 0){
          const pushX = (overlapX/2) * (dx>=0?1:-1) * 0.5;
          const pushY = (overlapY/2) * (dy>=0?1:-1) * 0.5;
          if (Math.abs(overlapX) < Math.abs(overlapY)){
            a.x += pushX; b.x -= pushX;
          } else {
            a.y += pushY; b.y -= pushY;
          }
        } else {
          const desired = 90;
          if (dist < desired){
            const f = (desired-dist)/dist * 0.04;
            a.x += dx*f; a.y += dy*f;
            b.x -= dx*f; b.y -= dy*f;
          }
        }
      }
    }
    // related springs
    nodes.forEach(a => {
      const t = byId[a.id];
      (t.related||[]).forEach(rid => {
        const b = nodeById[rid];
        if (!b) return;
        let dx = b.x-a.x, dy = b.y-a.y;
        let dist = Math.sqrt(dx*dx+dy*dy) || 0.001;
        const desired = 110;
        const f = (dist-desired) * 0.015;
        a.x += dx/dist*f; a.y += dy/dist*f;
      });
    });
    // zone containment + weak center pull
    nodes.forEach(n => {
      const cx = (n.zone.x0+n.zone.x1)/2, cy=(n.zone.y0+n.zone.y1)/2;
      n.x += (cx-n.x)*0.006;
      n.y += (cy-n.y)*0.006;
      const hw = n.w/2, hh = n.h/2;
      n.x = Math.min(n.zone.x1-hw, Math.max(n.zone.x0+hw, n.x));
      n.y = Math.min(n.zone.y1-hh, Math.max(n.zone.y0+hh, n.y));
    });
  }
}
simulate(260);
nodes.forEach(n => {
  n.el.style.left = n.x + 'px';
  n.el.style.top = n.y + 'px';
});

// ---- content bounding box: keeps axis labels close to the actual clusters ----
let contentMinX=Infinity, contentMaxX=-Infinity, contentMinY=Infinity, contentMaxY=-Infinity;
nodes.forEach(n => {
  contentMinX = Math.min(contentMinX, n.x - n.w/2);
  contentMaxX = Math.max(contentMaxX, n.x + n.w/2);
  contentMinY = Math.min(contentMinY, n.y - n.h/2);
  contentMaxY = Math.max(contentMaxY, n.y + n.h/2);
});
const labelGap = 46;
const midX = (contentMinX+contentMaxX)/2, midY = (contentMinY+contentMaxY)/2;
document.getElementById('label-top').style.left = midX + 'px';
document.getElementById('label-top').style.top = (contentMinY - labelGap) + 'px';
document.getElementById('label-bottom').style.left = midX + 'px';
document.getElementById('label-bottom').style.top = (contentMaxY + labelGap) + 'px';
document.getElementById('label-left').style.left = (contentMinX - labelGap) + 'px';
document.getElementById('label-left').style.top = midY + 'px';
document.getElementById('label-right').style.left = (contentMaxX + labelGap) + 'px';
document.getElementById('label-right').style.top = midY + 'px';

// ---- pan & zoom ----
let scale = 0.5, tx = 0, ty = 0;
function applyTransform(){
  world.style.transform = `translate(${tx}px, ${ty}px) scale(${scale})`;
}
function fitInitial(){
  const vw = viewport.clientWidth, vh = viewport.clientHeight;
  const pad = 90;
  const x0 = contentMinX - labelGap - pad, x1 = contentMaxX + labelGap + pad;
  const y0 = contentMinY - labelGap - pad, y1 = contentMaxY + labelGap + pad;
  scale = Math.min(vw/(x1-x0), vh/(y1-y0));
  tx = vw/2 - ((x0+x1)/2)*scale;
  ty = vh/2 - ((y0+y1)/2)*scale;
  applyTransform();
}
window.addEventListener('resize', fitInitial);
fitInitial();

let isDragging = false, dragStart = null, moved = false;
viewport.addEventListener('mousedown', e => {
  isDragging = true; moved = false;
  dragStart = {x: e.clientX, y: e.clientY, tx, ty};
  viewport.classList.add('dragging');
});
window.addEventListener('mousemove', e => {
  if (!isDragging) return;
  const dx = e.clientX - dragStart.x, dy = e.clientY - dragStart.y;
  if (Math.abs(dx)+Math.abs(dy) > 4) moved = true;
  tx = dragStart.tx + dx; ty = dragStart.ty + dy;
  applyTransform();
});
window.addEventListener('mouseup', () => { isDragging=false; viewport.classList.remove('dragging'); });

function zoomAt(clientX, clientY, factor){
  const rect = viewport.getBoundingClientRect();
  const px = clientX-rect.left, py = clientY-rect.top;
  const wx = (px-tx)/scale, wy = (py-ty)/scale;
  scale = Math.min(3, Math.max(0.15, scale*factor));
  tx = px - wx*scale;
  ty = py - wy*scale;
  applyTransform();
}
viewport.addEventListener('wheel', e => {
  e.preventDefault();
  const factor = e.deltaY < 0 ? 1.12 : 1/1.12;
  zoomAt(e.clientX, e.clientY, factor);
}, {passive:false});

document.getElementById('zoom-in').addEventListener('click', () => {
  const r = viewport.getBoundingClientRect();
  zoomAt(r.left+r.width/2, r.top+r.height/2, 1.25);
});
document.getElementById('zoom-out').addEventListener('click', () => {
  const r = viewport.getBoundingClientRect();
  zoomAt(r.left+r.width/2, r.top+r.height/2, 1/1.25);
});
document.getElementById('zoom-reset').addEventListener('click', fitInitial);

// touch support
let touchState = null;
viewport.addEventListener('touchstart', e => {
  if (e.touches.length === 1){
    touchState = {mode:'pan', x:e.touches[0].clientX, y:e.touches[0].clientY, tx, ty};
  } else if (e.touches.length === 2){
    const [a,b] = e.touches;
    const dist = Math.hypot(a.clientX-b.clientX, a.clientY-b.clientY);
    touchState = {mode:'pinch', dist, scale};
  }
}, {passive:true});
viewport.addEventListener('touchmove', e => {
  if (!touchState) return;
  if (touchState.mode === 'pan' && e.touches.length === 1){
    const dx = e.touches[0].clientX - touchState.x;
    const dy = e.touches[0].clientY - touchState.y;
    tx = touchState.tx + dx; ty = touchState.ty + dy;
    applyTransform();
  } else if (touchState.mode === 'pinch' && e.touches.length === 2){
    const [a,b] = e.touches;
    const dist = Math.hypot(a.clientX-b.clientX, a.clientY-b.clientY);
    const factor = dist/touchState.dist;
    const cx = (a.clientX+b.clientX)/2, cy=(a.clientY+b.clientY)/2;
    scale = Math.min(3, Math.max(0.15, touchState.scale*factor));
    applyTransform();
  }
}, {passive:true});
viewport.addEventListener('touchend', () => { touchState = null; });

// ---- click / highlight / popup ----
const overlay = document.getElementById('overlay');
const popup = document.getElementById('popup');

function clearHighlight(){
  nodes.forEach(n => n.el.classList.remove('dim','related','active'));
}

function highlight(id){
  const t = byId[id];
  clearHighlight();
  nodes.forEach(n => n.el.classList.add('dim'));
  nodeById[id].el.classList.remove('dim');
  nodeById[id].el.classList.add('active');
  (t.related||[]).forEach(rid => {
    const rn = nodeById[rid];
    if (rn){ rn.el.classList.remove('dim'); rn.el.classList.add('related'); }
  });
}

function focusOn(ids){
  const relevant = ids.map(i => nodeById[i]).filter(Boolean);
  if (!relevant.length) return;
  let minX=Infinity, maxX=-Infinity, minY=Infinity, maxY=-Infinity;
  relevant.forEach(n => {
    minX = Math.min(minX, n.x-n.w/2); maxX = Math.max(maxX, n.x+n.w/2);
    minY = Math.min(minY, n.y-n.h/2); maxY = Math.max(maxY, n.y+n.h/2);
  });
  const pad = 80;
  minX -= pad; maxX += pad; minY -= pad; maxY += pad;
  const vw = viewport.clientWidth, vh = viewport.clientHeight;
  const panelWidth = Math.min(380, vw*0.92);
  const availW = Math.max(200, vw - panelWidth);
  const fitScale = Math.min(availW/(maxX-minX), vh/(maxY-minY));
  scale = Math.min(1.3, Math.max(0.3, fitScale));
  tx = availW/2 - ((minX+maxX)/2)*scale;
  ty = vh/2 - ((minY+maxY)/2)*scale;
  world.style.transition = 'transform .45s cubic-bezier(.2,.7,.3,1)';
  applyTransform();
  clearTimeout(focusOn._t);
  focusOn._t = setTimeout(() => { world.style.transition = ''; }, 460);
}

function openPopup(id){
  const t = byId[id];
  highlight(id);
  focusOn([id, ...(t.related||[])]);
  const color = t.valence === 'angenehm' ? 'var(--angenehm)' : 'var(--unangenehm)';
  const relatedHtml = (t.related||[]).map(rid => {
    const rt = byId[rid];
    return `<button data-id="${rid}">${rt.term}</button>`;
  }).join('') || '<span class="plain">Keine verlinkten Begriffe</span>';
  popup.innerHTML = `
    <button class="close" id="popup-close">✕</button>
    <span class="badge" style="background:${color}">${t.valence} · ${t.arousal === 'hoch' ? 'aktivierend' : 'deaktivierend'}</span>
    <h2>${t.term}</h2>
    <p class="desc">${t.description}</p>
    ${t.example ? `<p class="example">${t.example}</p>` : ''}
    <div class="related-title">Verwandte Begriffe</div>
    <div class="related-list">${relatedHtml}</div>
  `;
  overlay.classList.add('show');
  popup.querySelector('#popup-close').addEventListener('click', closePopup);
  popup.querySelectorAll('.related-list button').forEach(btn => {
    btn.addEventListener('click', () => openPopup(btn.dataset.id));
  });
}
function closePopup(){
  overlay.classList.remove('show');
  clearHighlight();
}
document.addEventListener('keydown', e => { if (e.key === 'Escape') closePopup(); });

world.addEventListener('click', e => {
  const chip = e.target.closest('.chip');
  if (moved) return;
  if (chip){ openPopup(chip.dataset.id); return; }
  if (overlay.classList.contains('show')) closePopup();
});

// ---- search ----
const searchInput = document.getElementById('search');
const searchResults = document.getElementById('search-results');
function panToNode(id){
  const n = nodeById[id];
  const vw = viewport.clientWidth, vh = viewport.clientHeight;
  scale = Math.max(scale, 0.9);
  tx = vw/2 - n.x*scale;
  ty = vh/2 - n.y*scale;
  applyTransform();
}
searchInput.addEventListener('input', () => {
  const q = searchInput.value.trim().toLowerCase();
  if (!q){ searchResults.style.display='none'; searchResults.innerHTML=''; return; }
  const matches = TERMS.filter(t => t.term.toLowerCase().includes(q)).slice(0,8);
  if (!matches.length){ searchResults.style.display='none'; searchResults.innerHTML=''; return; }
  searchResults.innerHTML = matches.map(m => `<button data-id="${m.id}">${m.term}</button>`).join('');
  searchResults.style.display = 'block';
  searchResults.querySelectorAll('button').forEach(btn => {
    btn.addEventListener('click', () => {
      panToNode(btn.dataset.id);
      openPopup(btn.dataset.id);
      searchResults.style.display = 'none';
      searchInput.value = '';
    });
  });
});
</script>
</body>
</html>
"""

html = html.replace("TERMS_JSON_PLACEHOLDER", terms_json)
html = html.replace("WORLD_W_PLACEHOLDER", "2600")
html = html.replace("WORLD_H_PLACEHOLDER", "2000")
html = html.replace("WORLD_Wpx", "2600px")
html = html.replace("WORLD_Hpx", "2000px")

out_path = "/tmp/claude-0/-home-user-bauchipedia/3f722902-a4d6-55d0-b13a-9e6c4eafbf65/scratchpad/bauchipedia-grid.html"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(html)
print("wrote", out_path, len(html), "chars")

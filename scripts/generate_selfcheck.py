WIDGET_CSS = """
.bp-self {
  --unangenehm: #6a3fa0;
  --angenehm: #21b39a;
  --ink: #16234a;
  --serif: Georgia, "Iowan Old Style", "Palatino Linotype", "Times New Roman", serif;
  --sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  font-family: var(--sans);
  color: var(--ink);
}
.bp-self, .bp-self * { box-sizing: border-box; }
.bp-self button:focus-visible, .bp-self textarea:focus-visible {
  outline: 2px solid #21b39a;
  outline-offset: 2px;
}
.bp-self #sc-app {
  position: relative;
  display: flex;
  width: 100%;
  height: min(80vh, 720px);
  min-height: 480px;
  overflow: hidden;
  background: #eef0f5;
  border-radius: 18px;
  box-shadow: 0 10px 40px rgba(0,0,0,0.18);
}
.bp-self #sc-stage {
  position: relative;
  flex: 1 1 auto;
  min-width: 0;
  min-height: 0;
  display: flex;
  flex-direction: column;
}
.bp-self #sc-toolbar {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  flex-wrap: wrap;
  padding: 14px 14px 0;
}
.bp-self #sc-wordmark {
  background: rgba(22,35,74,0.06);
  border: 1px solid rgba(22,35,74,0.1);
  border-radius: 10px;
  padding: 8px 14px;
}
.bp-self #sc-wordmark .title {
  font-family: var(--serif);
  font-size: 15px;
  font-weight: 600;
}
.bp-self #sc-wordmark .sub {
  font-size: 11px;
  color: #6b7280;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  margin-top: 2px;
}
.bp-self #sc-meta {
  margin-left: auto;
  display: flex;
  align-items: center;
  gap: 8px;
}
.bp-self #sc-count {
  font-size: 12px;
  color: #6b7280;
  background: rgba(22,35,74,0.06);
  border-radius: 999px;
  padding: 7px 12px;
}
.bp-self .sc-btn {
  background: #fff;
  border: 1px solid rgba(22,35,74,0.15);
  color: var(--ink);
  border-radius: 10px;
  padding: 7px 12px;
  font-size: 13px;
  cursor: pointer;
}
.bp-self .sc-btn:hover { background: #f3f4f8; }
.bp-self .sc-btn.primary {
  background: var(--ink);
  border-color: var(--ink);
  color: #fff;
}
.bp-self .sc-btn.primary:hover { background: #223061; }
.bp-self .sc-btn.danger { color: #a33; border-color: #e3b8b8; }
.bp-self .sc-btn.danger:hover { background: #fdf1f1; }
.bp-self #sc-privacy {
  font-size: 11.5px;
  color: #8a93a6;
  padding: 6px 18px 0;
}
.bp-self #sc-gridwrap {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 56px 96px;
  min-height: 0;
}
.bp-self #sc-grid {
  position: relative;
  width: min(100%, 100%);
  height: 100%;
  max-width: 620px;
  max-height: 620px;
  aspect-ratio: 1 / 1;
  border-radius: 6px;
  cursor: crosshair;
  background-image:
    repeating-linear-gradient(to right, rgba(255,255,255,0.4) 0, rgba(255,255,255,0.4) 1px, transparent 1px, transparent calc(100% / 12)),
    repeating-linear-gradient(to bottom, rgba(255,255,255,0.4) 0, rgba(255,255,255,0.4) 1px, transparent 1px, transparent calc(100% / 12)),
    linear-gradient(to bottom, rgba(233,235,240,0) 0%, rgba(233,235,240,0.55) 58%, rgba(233,235,240,0.96) 100%),
    linear-gradient(to right, #7a3fa0 0%, #46528f 50%, #1f9a86 100%);
  box-shadow: 0 2px 18px rgba(0,0,0,0.12);
}
.bp-self .sc-axis-line {
  position: absolute;
  background: rgba(22,35,74,0.18);
  pointer-events: none;
}
.bp-self .sc-label {
  position: absolute;
  color: #3a4a7a;
  font-weight: 700;
  letter-spacing: 0.09em;
  font-size: 13px;
  text-transform: uppercase;
  white-space: nowrap;
  pointer-events: none;
}
.bp-self .sc-label.top { top: -32px; left: 50%; transform: translateX(-50%); }
.bp-self .sc-label.bottom { bottom: -32px; left: 50%; transform: translateX(-50%); }
.bp-self .sc-label.left { left: -14px; top: 50%; transform: translateY(-50%) rotate(-90deg); }
.bp-self .sc-label.right { right: -14px; top: 50%; transform: translateY(-50%) rotate(90deg); }
.bp-self .sc-meta-label {
  position: absolute;
  color: #9aa3b8;
  font-weight: 600;
  letter-spacing: 0.12em;
  font-size: 10px;
  text-transform: uppercase;
  white-space: nowrap;
  pointer-events: none;
}
.bp-self .sc-meta-label.top { top: -54px; left: 50%; transform: translateX(-50%); }
.bp-self .sc-meta-label.bottom { bottom: -54px; left: 50%; transform: translateX(-50%); }
.bp-self .sc-meta-label.left { left: -78px; top: 50%; transform: translateY(-50%); }
.bp-self .sc-meta-label.right { right: -78px; top: 50%; transform: translateY(-50%); }
.bp-self #sc-hint {
  text-align: center;
  font-size: 12px;
  color: #8a93a6;
  padding: 0 18px 14px;
}
.bp-self .sc-dot {
  position: absolute;
  width: 16px; height: 16px;
  border-radius: 50%;
  transform: translate(-50%, -50%);
  cursor: pointer;
  border: 2px solid #fff;
  box-shadow: 0 1px 5px rgba(0,0,0,0.35);
  transition: transform .15s ease;
}
.bp-self .sc-dot:hover { transform: translate(-50%, -50%) scale(1.25); }
.bp-self .sc-dot.unangenehm { background: var(--unangenehm); }
.bp-self .sc-dot.angenehm { background: var(--angenehm); }
.bp-self .sc-dot.active { box-shadow: 0 0 0 3px #ffcf4d, 0 2px 8px rgba(0,0,0,0.35); }
.bp-self .sc-dot.pending {
  border: 2px dashed #16234a;
  background: rgba(255,255,255,0.85);
  animation: sc-pulse 1.4s ease-in-out infinite;
}
@keyframes sc-pulse {
  0%, 100% { box-shadow: 0 0 0 0 rgba(22,35,74,0.35); }
  50% { box-shadow: 0 0 0 7px rgba(22,35,74,0); }
}
.bp-self #sc-panel {
  width: 0;
  flex: 0 0 auto;
  overflow: hidden;
  background: #fff;
  box-shadow: -8px 0 30px rgba(0,0,0,0.12);
  transition: width .28s ease;
}
.bp-self #sc-panel.show { width: min(320px, 80vw); }
.bp-self #sc-panel-inner {
  width: min(320px, 80vw);
  height: 100%;
  overflow-y: auto;
  padding: 22px 20px;
  position: relative;
}
.bp-self #sc-panel .close {
  position: absolute;
  top: 12px; right: 12px;
  background: #f0f1f7;
  border: none;
  width: 28px; height: 28px;
  border-radius: 50%;
  cursor: pointer;
  color: #555;
  font-size: 14px;
}
.bp-self #sc-panel .close:hover { background: #e2e4f2; }
.bp-self #sc-panel .badge {
  display: inline-block;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  padding: 3px 9px;
  border-radius: 999px;
  color: #fff;
  margin-bottom: 10px;
}
.bp-self #sc-panel .intensity {
  font-size: 13px;
  color: #6b7280;
  margin: 0 0 14px;
}
.bp-self #sc-panel .ts {
  font-size: 12px;
  color: #9aa3b8;
  margin: 2px 0 16px;
}
.bp-self #sc-panel textarea {
  width: 100%;
  min-height: 100px;
  border: 1px solid rgba(22,35,74,0.18);
  border-radius: 10px;
  padding: 10px 12px;
  font-family: var(--sans);
  font-size: 14px;
  resize: vertical;
  margin-bottom: 14px;
}
.bp-self #sc-panel .note-view {
  font-size: 14.5px;
  line-height: 1.5;
  margin: 0 0 18px;
  white-space: pre-wrap;
}
.bp-self #sc-panel .row { display: flex; gap: 8px; }

@media (max-width: 640px) {
  .bp-self #sc-app { flex-direction: column; height: min(90vh, 700px); }
  .bp-self #sc-toolbar { padding: 10px 10px 0; }
  .bp-self #sc-gridwrap { padding: 22px 20px; }
  .bp-self .sc-meta-label { display: none; }
  .bp-self .sc-label.top { top: -24px; font-size: 12px; }
  .bp-self .sc-label.bottom { bottom: -24px; font-size: 12px; }
  .bp-self #sc-hint { padding: 0 12px 8px; }
  .bp-self #sc-app.panel-open #sc-privacy,
  .bp-self #sc-app.panel-open #sc-hint { display: none; }
  .bp-self #sc-panel {
    width: 100% !important;
    height: 0;
    flex: 0 0 auto;
    box-shadow: 0 -8px 24px rgba(0,0,0,0.15);
    transition: height .28s ease;
  }
  .bp-self #sc-panel.show { height: min(46%, 320px); }
  .bp-self #sc-panel-inner { width: 100%; padding: 16px 18px; }
  .bp-self #sc-panel textarea { min-height: 70px; }
}
"""

BODY = """
<div class="bp-self">
  <div id="sc-app">
    <div id="sc-stage">
      <div id="sc-toolbar">
        <div id="sc-wordmark">
          <div class="title">Bauchipedia</div>
          <div class="sub">Selbsteinschätzung</div>
        </div>
        <div id="sc-meta">
          <span id="sc-count"></span>
          <button class="sc-btn" id="sc-clear">Verlauf löschen</button>
        </div>
      </div>
      <div id="sc-privacy">Deine Einträge werden nur in diesem Browser gespeichert – nicht auf einem Server und für niemand sonst sichtbar.</div>
      <div id="sc-gridwrap">
        <div id="sc-grid">
          <div class="sc-label top">Aktivierend</div>
          <div class="sc-label bottom">Deaktivierend</div>
          <div class="sc-label left">Unangenehm</div>
          <div class="sc-label right">Angenehm</div>
          <div class="sc-meta-label top">↑ Arousal</div>
          <div class="sc-meta-label bottom">↓ Arousal</div>
          <div class="sc-meta-label left">← Valenz</div>
          <div class="sc-meta-label right">Valenz →</div>
          <div class="sc-axis-line" style="left:50%; top:0; width:1px; height:100%;"></div>
          <div class="sc-axis-line" style="top:50%; left:0; height:1px; width:100%;"></div>
        </div>
      </div>
      <div id="sc-hint">Klicke ins Raster, um festzuhalten, wie du dich gerade fühlst</div>
    </div>
    <div id="sc-panel"><div id="sc-panel-inner"></div></div>
  </div>
</div>
"""

JS = """
(function(){
const widget = document.currentScript.previousElementSibling;
const app = widget.querySelector('#sc-app');
const grid = widget.querySelector('#sc-grid');
const panel = widget.querySelector('#sc-panel');
const panelInner = widget.querySelector('#sc-panel-inner');
const countEl = widget.querySelector('#sc-count');
const STORAGE_KEY = 'bp_selfcheck_entries_v1';

function loadEntries(){
  try { return JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]'); }
  catch(e){ return []; }
}
function saveEntries(entries){
  localStorage.setItem(STORAGE_KEY, JSON.stringify(entries));
}
let entries = loadEntries();
let pending = null; // {x,y,el}
let activeId = null;

function quadrantOf(x, y){
  const valence = x < 50 ? 'unangenehm' : 'angenehm';
  const arousal = y < 50 ? 'hoch' : 'niedrig';
  return { valence, arousal };
}
function intensityOf(x, y){
  const d = Math.hypot(x-50, y-50) / 70.71 * 100;
  if (d < 33) return 'leicht ausgeprägt';
  if (d < 66) return 'deutlich ausgeprägt';
  return 'stark ausgeprägt';
}
function fmtDate(ts){
  return new Date(ts).toLocaleString('de-DE', { day:'2-digit', month:'long', year:'numeric', hour:'2-digit', minute:'2-digit' });
}

function renderCount(){
  countEl.textContent = entries.length === 0 ? 'Noch keine Einträge' : entries.length + (entries.length===1 ? ' Eintrag' : ' Einträge');
}

function renderDots(){
  grid.querySelectorAll('.sc-dot:not(.pending)').forEach(el => el.remove());
  entries.forEach(e => {
    const q = quadrantOf(e.x, e.y);
    const el = document.createElement('div');
    el.className = 'sc-dot ' + q.valence;
    if (e.id === activeId) el.classList.add('active');
    el.style.left = e.x + '%';
    el.style.top = e.y + '%';
    el.addEventListener('click', ev => { ev.stopPropagation(); openView(e.id); });
    grid.appendChild(el);
  });
}

function clearPending(){
  if (pending && pending.el) pending.el.remove();
  pending = null;
}

function closePanel(){
  panel.classList.remove('show');
  app.classList.remove('panel-open');
  activeId = null;
  clearPending();
  renderDots();
}

function openNew(x, y){
  clearPending();
  activeId = null;
  renderDots();
  const el = document.createElement('div');
  el.className = 'sc-dot pending';
  el.style.left = x + '%';
  el.style.top = y + '%';
  grid.appendChild(el);
  pending = { x, y, el };

  const q = quadrantOf(x, y);
  const color = q.valence === 'angenehm' ? 'var(--angenehm)' : 'var(--unangenehm)';
  panelInner.innerHTML = `
    <button class="close" id="sc-close">✕</button>
    <span class="badge" style="background:${color}">${q.valence} · ${q.arousal === 'hoch' ? 'aktivierend' : 'deaktivierend'}</span>
    <div class="intensity">${intensityOf(x,y)}</div>
    <textarea id="sc-note" placeholder="Was ist gerade los? (optional)"></textarea>
    <div class="row">
      <button class="sc-btn primary" id="sc-save">Speichern</button>
      <button class="sc-btn" id="sc-cancel">Abbrechen</button>
    </div>
  `;
  panel.classList.add('show'); app.classList.add('panel-open');
  panelInner.querySelector('#sc-close').addEventListener('click', closePanel);
  panelInner.querySelector('#sc-cancel').addEventListener('click', closePanel);
  panelInner.querySelector('#sc-save').addEventListener('click', () => {
    const note = panelInner.querySelector('#sc-note').value.trim();
    const entry = { id: 'e' + Date.now() + Math.random().toString(36).slice(2,7), x, y, note, ts: Date.now() };
    entries.push(entry);
    saveEntries(entries);
    renderCount();
    clearPending();
    openView(entry.id);
  });
}

function openView(id){
  clearPending();
  activeId = id;
  renderDots();
  const e = entries.find(x => x.id === id);
  if (!e) return;
  const q = quadrantOf(e.x, e.y);
  const color = q.valence === 'angenehm' ? 'var(--angenehm)' : 'var(--unangenehm)';
  panelInner.innerHTML = `
    <button class="close" id="sc-close">✕</button>
    <span class="badge" style="background:${color}">${q.valence} · ${q.arousal === 'hoch' ? 'aktivierend' : 'deaktivierend'}</span>
    <div class="intensity">${intensityOf(e.x,e.y)}</div>
    <div class="ts">${fmtDate(e.ts)}</div>
    <div class="note-view" id="sc-note-view">${e.note ? e.note.replace(/</g,'&lt;') : '<span style="color:#aab">Keine Notiz</span>'}</div>
    <div class="row">
      <button class="sc-btn" id="sc-edit">Bearbeiten</button>
      <button class="sc-btn danger" id="sc-delete">Löschen</button>
    </div>
  `;
  panel.classList.add('show'); app.classList.add('panel-open');
  panelInner.querySelector('#sc-close').addEventListener('click', closePanel);
  panelInner.querySelector('#sc-delete').addEventListener('click', () => {
    entries = entries.filter(x => x.id !== id);
    saveEntries(entries);
    renderCount();
    closePanel();
  });
  panelInner.querySelector('#sc-edit').addEventListener('click', () => {
    panelInner.innerHTML = `
      <button class="close" id="sc-close">✕</button>
      <span class="badge" style="background:${color}">${q.valence} · ${q.arousal === 'hoch' ? 'aktivierend' : 'deaktivierend'}</span>
      <div class="intensity">${intensityOf(e.x,e.y)}</div>
      <div class="ts">${fmtDate(e.ts)}</div>
      <textarea id="sc-note">${e.note || ''}</textarea>
      <div class="row">
        <button class="sc-btn primary" id="sc-save-edit">Speichern</button>
        <button class="sc-btn" id="sc-cancel-edit">Abbrechen</button>
      </div>
    `;
    panelInner.querySelector('#sc-close').addEventListener('click', closePanel);
    panelInner.querySelector('#sc-cancel-edit').addEventListener('click', () => openView(id));
    panelInner.querySelector('#sc-save-edit').addEventListener('click', () => {
      e.note = panelInner.querySelector('#sc-note').value.trim();
      saveEntries(entries);
      openView(id);
    });
  });
}

let dragMoved = false, dragStart = null;
grid.addEventListener('mousedown', e => { dragMoved = false; dragStart = {x:e.clientX, y:e.clientY}; });
grid.addEventListener('mousemove', e => {
  if (!dragStart) return;
  if (Math.abs(e.clientX-dragStart.x) + Math.abs(e.clientY-dragStart.y) > 4) dragMoved = true;
});
grid.addEventListener('click', e => {
  if (dragMoved) { dragMoved = false; return; }
  if (e.target.closest('.sc-dot')) return;
  const rect = grid.getBoundingClientRect();
  const x = Math.min(100, Math.max(0, (e.clientX - rect.left) / rect.width * 100));
  const y = Math.min(100, Math.max(0, (e.clientY - rect.top) / rect.height * 100));
  openNew(x, y);
});

widget.querySelector('#sc-clear').addEventListener('click', () => {
  if (!entries.length) return;
  if (confirm('Wirklich alle ' + entries.length + ' Einträge unwiderruflich löschen?')){
    entries = [];
    saveEntries(entries);
    renderCount();
    closePanel();
  }
});

document.addEventListener('keydown', e => { if (e.key === 'Escape') closePanel(); });

renderCount();
renderDots();
})();
"""

EMBED_FRAGMENT = f'<meta charset="utf-8">\n<style>{WIDGET_CSS}</style>\n{BODY}\n<script>{JS}</script>\n'

FULL_HTML = f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<title>Bauchipedia – Selbsteinschätzung</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
  html, body {{ margin: 0; padding: 16px; background: #eef0f5; }}
</style>
</head>
<body>
{EMBED_FRAGMENT}
</body>
</html>
"""

out_dir = "/tmp/claude-0/-home-user-bauchipedia/3f722902-a4d6-55d0-b13a-9e6c4eafbf65/scratchpad/"
with open(out_dir + "selfcheck-index.html", "w", encoding="utf-8") as f:
    f.write(FULL_HTML)
with open(out_dir + "selfcheck-embed.html", "w", encoding="utf-8") as f:
    f.write(EMBED_FRAGMENT)
print("wrote index (full):", len(FULL_HTML), "chars")
print("wrote embed fragment:", len(EMBED_FRAGMENT), "chars")

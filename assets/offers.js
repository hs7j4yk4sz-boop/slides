/* NFC Summit 2027 — viewer for the vertical offer decks. Keys: ← → change page, G all pages, F full screen. */
(function () {
  var pages = Array.prototype.slice.call(document.querySelectorAll('#pages img'));
  var n = pages.length, i = 0;
  var count = document.getElementById('v-count'), bar = document.getElementById('v-progress');
  var grid = document.getElementById('o-grid'), gridBtn = document.getElementById('v-grid');

  function fromHash() {
    var m = /^#p(\d+)$/.exec(location.hash);
    return m ? Math.min(Math.max(parseInt(m[1], 10) - 1, 0), n - 1) : 0;
  }
  function show(k, push) {
    i = Math.min(Math.max(k, 0), n - 1);
    pages.forEach(function (p, j) {
      p.classList.toggle('active', j === i);
      if (Math.abs(j - i) <= 1 && p.dataset.src) { p.src = p.dataset.src; delete p.dataset.src; }
    });
    count.innerHTML = '<b>' + String(i + 1).padStart(2, '0') + '</b> / ' + String(n).padStart(2, '0');
    bar.style.width = ((i + 1) / n * 100) + '%';
    grid.querySelectorAll('button').forEach(function (b, j) { b.setAttribute('aria-current', j === i ? 'true' : 'false'); });
    if (push !== false) { try { history.replaceState(null, '', '#p' + (i + 1)); } catch (e) {} }
  }
  function toggleGrid(open) {
    var on = typeof open === 'boolean' ? open : grid.hidden;
    grid.hidden = !on; gridBtn.setAttribute('aria-pressed', on ? 'true' : 'false');
    if (on) { var cur = grid.querySelector('[aria-current="true"]'); if (cur) cur.focus(); }
  }
  function fullscreen() {
    var d = document.documentElement;
    if (!document.fullscreenElement) { if (d.requestFullscreen) d.requestFullscreen().catch(function () {}); }
    else if (document.exitFullscreen) document.exitFullscreen();
  }

  document.getElementById('v-prev').addEventListener('click', function () { show(i - 1); });
  document.getElementById('v-next').addEventListener('click', function () { show(i + 1); });
  gridBtn.addEventListener('click', function () { toggleGrid(); });
  document.getElementById('v-fs').addEventListener('click', fullscreen);
  grid.addEventListener('click', function (e) {
    if (e.target.closest('[data-close]')) { toggleGrid(false); return; }
    var b = e.target.closest('button[data-i]'); if (!b) return;
    show(parseInt(b.getAttribute('data-i'), 10)); toggleGrid(false);
  });
  document.getElementById('pages').addEventListener('click', function (e) {
    var x = e.clientX / window.innerWidth; show(x < 0.35 ? i - 1 : i + 1);
  });
  document.addEventListener('keydown', function (e) {
    if (e.metaKey || e.ctrlKey || e.altKey) return;
    var k = e.key;
    if (k === 'Escape') { toggleGrid(false); return; }
    if (!grid.hidden) return;
    if (k === 'ArrowRight' || k === 'ArrowDown' || k === 'PageDown' || k === ' ') { e.preventDefault(); show(i + 1); }
    else if (k === 'ArrowLeft' || k === 'ArrowUp' || k === 'PageUp') { e.preventDefault(); show(i - 1); }
    else if (k === 'Home') show(0);
    else if (k === 'End') show(n - 1);
    else if (k === 'g' || k === 'G') toggleGrid(true);
    else if (k === 'f' || k === 'F') fullscreen();
  });
  var x0 = null, y0 = null;
  document.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; y0 = e.touches[0].clientY; }, { passive: true });
  document.addEventListener('touchend', function (e) {
    if (x0 === null || !grid.hidden) return;
    var dx = e.changedTouches[0].clientX - x0, dy = e.changedTouches[0].clientY - y0;
    if (Math.abs(dx) > 40 && Math.abs(dx) > Math.abs(dy)) show(dx < 0 ? i + 1 : i - 1);
    x0 = null;
  }, { passive: true });
  window.addEventListener('hashchange', function () { show(fromHash(), false); });

  var idle;
  function wake() { document.body.classList.remove('idle'); clearTimeout(idle); idle = setTimeout(function () { if (grid.hidden) document.body.classList.add('idle'); }, 2600); }
  ['mousemove', 'keydown', 'touchstart'].forEach(function (ev) { document.addEventListener(ev, wake, { passive: true }); });
  wake();
  show(fromHash(), false);
})();

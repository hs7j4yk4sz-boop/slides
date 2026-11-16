// NFC Summit 2027 — deck viewer: one 1920 x 1080 slide at a time, scaled to the window.
// Keys: arrows / space / PageUp-PageDown, Home / End, F full screen, G overview, N notes, Esc.
(function () {
  var deck = document.getElementById('deck');
  var slides = Array.prototype.slice.call(deck.querySelectorAll(':scope > section'));
  var total = slides.length;
  var body = document.body;
  var params = new URLSearchParams(location.search);

  // ?print renders every slide one after the other (used to make the PDF)
  if (params.has('print')) {
    body.classList.add('print');
    return;
  }

  var cur = 0;
  var countEl = document.getElementById('v-count');
  var progress = document.getElementById('v-progress');
  var notes = document.getElementById('notes');
  var notesBtn = document.getElementById('v-notes');
  var grid = document.getElementById('grid');
  var gridBtn = document.getElementById('v-grid');
  var fsBtn = document.getElementById('v-fs');

  // scale the 1920 x 1080 stage into the window, letterboxed
  function fit() {
    var w = window.innerWidth, h = window.innerHeight;
    var s = Math.min(w / 1920, h / 1080);
    deck.style.transform = 'translate(' + ((w - 1920 * s) / 2) + 'px,' + ((h - 1080 * s) / 2) + 'px) scale(' + s + ')';
  }
  window.addEventListener('resize', fit);
  fit();

  // background loops: an <img data-video> becomes a muted looping <video> when its slide is shown
  function videosOf(sec) {
    return Array.prototype.slice.call(sec.querySelectorAll('img[data-video]')).map(function (img) {
      if (!img._video) {
        var v = document.createElement('video');
        v.muted = true; v.loop = true; v.playsInline = true; v.preload = 'auto';
        v.setAttribute('muted', ''); v.setAttribute('playsinline', '');
        v.poster = img.src;
        v.className = img.className + ' bg-video';
        v.style.cssText = img.style.cssText;
        v.style.objectFit = v.style.objectFit || 'cover';
        v.setAttribute('aria-hidden', 'true');
        v.src = img.getAttribute('data-video');
        img.parentNode.insertBefore(v, img.nextSibling);
        v.addEventListener('playing', function () { img.style.visibility = 'hidden'; });
        img._video = v;
      }
      return img._video;
    });
  }
  function warm(i) { if (slides[i]) videosOf(slides[i]); }

  function show(i, instant) {
    i = Math.max(0, Math.min(total - 1, i));
    var prev = slides[cur];
    if (prev && prev !== slides[i]) {
      prev.classList.remove('active');
      prev.querySelectorAll('video.bg-video').forEach(function (v) { v.pause(); });
    }
    cur = i;
    var sec = slides[i];
    sec.classList.add('active');
    videosOf(sec).forEach(function (v) {
      try { v.currentTime = 0; } catch (e) {}
      var p = v.play(); if (p && p.catch) p.catch(function () {});
    });
    warm(i + 1);
    countEl.innerHTML = '<b>' + (i + 1) + '</b> / ' + total;
    progress.style.width = ((i + 1) / total * 100) + '%';
    var aside = sec.querySelector('aside');
    notes.querySelector('p').textContent = aside ? aside.textContent.trim() : '';
    if (history.replaceState) history.replaceState(null, '', '#' + (i + 1));
    if (!grid.hidden) markGrid();
  }

  function next() { show(cur + 1); }
  function prev() { show(cur - 1); }

  // notes
  function toggleNotes(force) {
    var on = typeof force === 'boolean' ? force : notes.hidden;
    notes.hidden = !on;
    notesBtn.setAttribute('aria-pressed', on ? 'true' : 'false');
  }

  // overview
  function markGrid() {
    grid.querySelectorAll('button[data-i]').forEach(function (b) {
      b.classList.toggle('cur', +b.getAttribute('data-i') === cur);
    });
  }
  function toggleGrid(force) {
    var on = typeof force === 'boolean' ? force : grid.hidden;
    grid.hidden = !on;
    gridBtn.setAttribute('aria-pressed', on ? 'true' : 'false');
    if (on) {
      markGrid();
      var c = grid.querySelector('button.cur'); if (c) { c.focus({ preventScroll: true }); c.scrollIntoView({ block: 'center' }); }
    }
  }
  grid.addEventListener('click', function (e) {
    var b = e.target.closest('button[data-i]');
    if (b) { show(+b.getAttribute('data-i')); toggleGrid(false); }
    if (e.target.closest('[data-close]')) toggleGrid(false);
  });

  // full screen
  function toggleFs() {
    var d = document, el = d.documentElement;
    if (d.fullscreenElement || d.webkitFullscreenElement) {
      (d.exitFullscreen || d.webkitExitFullscreen).call(d);
    } else if (el.requestFullscreen) {
      el.requestFullscreen().catch(function () {});
    } else if (el.webkitRequestFullscreen) {
      el.webkitRequestFullscreen();
    }
  }
  if (!(document.documentElement.requestFullscreen || document.documentElement.webkitRequestFullscreen)) fsBtn.hidden = true;

  document.getElementById('v-prev').addEventListener('click', prev);
  document.getElementById('v-next').addEventListener('click', next);
  notesBtn.addEventListener('click', function () { toggleNotes(); });
  gridBtn.addEventListener('click', function () { toggleGrid(); });
  fsBtn.addEventListener('click', toggleFs);

  document.addEventListener('keydown', function (e) {
    if (e.metaKey || e.ctrlKey || e.altKey) return;
    var k = e.key;
    if (!grid.hidden) {
      if (k === 'Escape' || k === 'g' || k === 'G') { toggleGrid(false); e.preventDefault(); }
      return;
    }
    if (k === 'ArrowRight' || k === 'ArrowDown' || k === 'PageDown' || k === ' ' || k === 'Enter') { next(); e.preventDefault(); }
    else if (k === 'ArrowLeft' || k === 'ArrowUp' || k === 'PageUp' || k === 'Backspace') { prev(); e.preventDefault(); }
    else if (k === 'Home') { show(0); e.preventDefault(); }
    else if (k === 'End') { show(total - 1); e.preventDefault(); }
    else if (k === 'f' || k === 'F') { toggleFs(); }
    else if (k === 'n' || k === 'N') { toggleNotes(); }
    else if (k === 'g' || k === 'G') { toggleGrid(true); }
    else if (k === 'Escape') { toggleNotes(false); }
    wake();
  });

  // click on the slide: right two thirds forward, left third back
  document.getElementById('stage').addEventListener('click', function (e) {
    if (e.clientX < window.innerWidth / 3) prev(); else next();
  });

  // swipe
  var sx = null, sy = null;
  document.addEventListener('touchstart', function (e) { if (e.touches.length === 1) { sx = e.touches[0].clientX; sy = e.touches[0].clientY; } }, { passive: true });
  document.addEventListener('touchend', function (e) {
    if (sx === null || !grid.hidden) return;
    var dx = e.changedTouches[0].clientX - sx, dy = e.changedTouches[0].clientY - sy;
    if (Math.abs(dx) > 40 && Math.abs(dx) > Math.abs(dy)) { if (dx < 0) next(); else prev(); }
    sx = null;
  }, { passive: true });

  // the controls fade out when the mouse rests
  var idleT;
  function wake() {
    body.classList.remove('idle');
    clearTimeout(idleT);
    idleT = setTimeout(function () { if (grid.hidden) body.classList.add('idle'); }, 2600);
  }
  ['mousemove', 'touchstart', 'pointerdown'].forEach(function (ev) { document.addEventListener(ev, wake, { passive: true }); });

  var start = parseInt((location.hash || '').replace('#', ''), 10);
  show(isNaN(start) ? 0 : start - 1, true);
  window.addEventListener('hashchange', function () {
    var n = parseInt(location.hash.replace('#', ''), 10);
    if (!isNaN(n) && n - 1 !== cur) show(n - 1);
  });
  wake();
})();

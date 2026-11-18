---
marp: true
paginate: true
header: "UFAZ · MARSQUAKES"
style: |
  @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;700&display=swap');
  :root{--bg:#0A0A0F;--card:#14141C;--line:rgba(255,255,255,.09);--rust:#D14905;--coral:#E05A47;--amber:#F5A83A;--text:#F3EEE6;--muted:#9C97A8;--cyan:#00E5FF;--mag:#FF2BD6}
  section{width:1280px;height:720px;padding:84px 64px 64px;color:var(--text);font:400 20px/1.4 Inter,sans-serif;
    background:radial-gradient(900px 500px at 90% -10%,rgba(209,73,5,.30),transparent 60%),radial-gradient(700px 500px at -10% 110%,rgba(124,58,237,.18),transparent 60%),var(--bg)}
  section::before{content:"";position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.07) 1px,transparent 1px);background-size:32px 32px;pointer-events:none}
  section>header,section>footer,section::after{position:absolute;font:500 13px 'JetBrains Mono',monospace;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
  section>header{top:30px;left:64px;color:var(--rust)} section>footer{bottom:26px;left:64px}
  section::after{content:attr(data-marpit-pagination) " / 12";bottom:26px;right:64px;top:auto;left:auto}
  h1,h2,h3{font-family:'Space Grotesk',sans-serif;font-weight:700;margin:0;letter-spacing:-.01em}
  h2{font-size:42px;margin-bottom:26px} h3{font-size:22px;margin-bottom:6px}
  p{margin:0;color:var(--muted);font-size:18px}
  .eyebrow{font:700 14px 'JetBrains Mono';letter-spacing:.2em;text-transform:uppercase;color:var(--rust);margin-bottom:10px}
  .grid{display:grid;gap:20px}.c2{grid-template-columns:1fr 1fr}.c3{grid-template-columns:repeat(3,1fr)}.c4{grid-template-columns:repeat(4,1fr)}
  .split{display:grid;grid-template-columns:1.25fr 1fr;gap:28px}.stack{display:grid;gap:16px}
  .card{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:20px 24px;position:relative}
  .card.rust{border-color:rgba(209,73,5,.65);box-shadow:0 0 36px rgba(209,73,5,.18)}
  .num{font:700 15px 'JetBrains Mono';color:var(--rust);letter-spacing:.15em;display:block;margin-bottom:6px}
  .stat b{display:block;font:700 44px/1.05 'Space Grotesk';color:var(--amber)}
  .stat small{font:500 13px 'JetBrains Mono';letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
  .stats{display:grid;gap:22px;align-content:center}
  .callout{margin-top:22px;border-left:4px solid var(--rust);background:rgba(209,73,5,.14);padding:16px 22px;border-radius:0 12px 12px 0;font:600 22px 'Space Grotesk';color:var(--amber)}
  .p{color:var(--cyan)}.s{color:var(--mag)}
  img.fig{width:100%;border-radius:12px;display:block}
  .neon{background:var(--cyan);border-radius:12px;isolation:isolate;overflow:hidden}
  .neon img{width:100%;display:block;filter:invert(1);mix-blend-mode:multiply}
  .cap{font:500 13px 'JetBrains Mono';color:var(--muted);margin-top:10px;letter-spacing:.04em}
  .chips span{display:inline-block;border:1px solid var(--line);background:var(--card);border-radius:999px;padding:6px 16px;margin:0 8px 8px 0;font-size:17px}
  .formula{margin-top:16px;display:inline-block;font:700 26px 'JetBrains Mono';color:var(--cyan);border:1px dashed var(--cyan);border-radius:10px;padding:8px 18px}
  .badge{position:absolute;top:-12px;right:16px;background:var(--mag);color:#000;font:700 12px 'JetBrains Mono';padding:3px 10px;border-radius:999px;letter-spacing:.1em}
  .tl{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;position:relative;padding-top:34px}
  .tl::before{content:"";position:absolute;top:10px;left:0;right:0;height:2px;background:linear-gradient(90deg,var(--cyan),var(--mag))}
  .tl .card::before{content:"";position:absolute;top:-30px;left:24px;width:14px;height:14px;border-radius:50%;background:var(--bg);border:3px solid var(--cyan);box-shadow:0 0 12px var(--cyan)}
  .year{font:700 16px 'JetBrains Mono';color:var(--rust);letter-spacing:.15em}
  table{width:100%;border-collapse:collapse;font-size:18px;border-radius:12px;overflow:hidden}
  th{background:var(--rust);text-align:left;padding:10px 14px;font:700 15px 'JetBrains Mono';letter-spacing:.1em;text-transform:uppercase}
  td{padding:10px 14px;background:var(--card);border-top:1px solid var(--line)} td:nth-child(2){color:var(--amber);font-weight:600}
  .title h1{font-size:56px;line-height:1.05;width:640px;margin:8px 0 18px}
  .title .sub{font-size:24px;width:520px;color:#CFC8D8;margin-bottom:26px}
  .hero{position:absolute;right:-50px;top:70px;width:640px}
  .wave{position:absolute;left:0;bottom:70px;width:1280px;filter:drop-shadow(0 0 6px var(--cyan))}
  .bleed{padding:0}.bleed img{width:1280px;height:720px;object-fit:cover}
  .end h1{font-size:76px;background:linear-gradient(90deg,var(--amber),var(--coral));-webkit-background-clip:text;color:transparent;margin-top:30px}
  .src{font:500 15px/1.6 'JetBrains Mono';color:var(--text)} .src b{color:var(--amber)}
---

<!-- _class: title -->
<!-- _paginate: false -->
<!-- _header: "" -->
<div class="eyebrow">UFAZ · Internal Envelopes</div>

# How Do Marsquakes Reveal the Interior of Mars?

<p class="sub">What NASA's InSight mission learned by listening to Mars</p>

<div class="chips"><span>Turab Jabiyev</span><span>Leyla Mukhtarzade</span><span>Aysu Nazarli</span><span>Ismayıl Huseynzade</span><span>Yusif Mammadzade</span></div>

<img class="hero" src="images/mars-cutaway.jpg">
<svg class="wave" viewBox="0 0 1280 120"><path d="M0 60H420l10-6 10 14 12-38 12 66 12-58 10 46 10-26 8 10H900l10-4 8 8 8-18 8 30 8-22 8 6H1280" stroke="#00E5FF" fill="none" stroke-width="2"/></svg>

---
<!-- _footer: "Source: NASA Mars Facts · NASA/JPL (InSight)" -->
<div class="eyebrow">01 / Why</div>

## Why look inside Mars?

<div class="split">
<div class="stack">
<div class="card"><span class="num">01</span><h3>We can't see inside</h3><p>The center is 3,390 km down. No drill can reach it.</p></div>
<div class="card"><span class="num">02</span><h3>The inside holds history</h3><p>Layers show how Mars formed, cooled and lost its magnetic field.</p></div>
<div class="card"><span class="num">03</span><h3>Quake waves are our probe</h3><p>They cross the planet and carry back data on every layer.</p></div>
</div>
<div class="card rust stats">
<div class="stat"><b>3,390 km</b><small>Radius · half of Earth</small></div>
<div class="stat"><b>−153→20 °C</b><small>Cold desert</small></div>
<div class="stat"><b>None</b><small>Global magnetic field</small></div>
</div>
</div>

---
<!-- _footer: "Source: NASA/JPL (InSight) · Astronomy magazine (2021)" -->
<div class="eyebrow">02 / Quakes</div>

## What are marsquakes?

<div class="grid c2">
<div class="card"><span class="num">01</span><h3>Cracking rock</h3><p>Mars cools and shrinks. The crust cracks along faults, causing most marsquakes.</p></div>
<div class="card"><span class="num">02</span><h3>Meteoroid impacts</h3><p>A space rock hits the ground and sends shock waves through it.</p></div>
</div>
<div class="grid c2" style="margin-top:20px">
<div class="card rust stat"><b>0</b><small>Tectonic plates</small></div>
<div class="card rust stat"><b>M 4.7</b><small>Biggest quake recorded by InSight</small></div>
</div>

---
<!-- _footer: "Source: NASA/JPL-Caltech · Oxford · CNES · InSight/SEIS data" -->
<div class="eyebrow">03 / InSight</div>

## InSight: listening to Mars

<div class="grid c2">
<div class="card"><img class="fig" src="images/seis.jpg"><div class="cap">SEIS seismometer · on Mars since Dec 2018</div></div>
<div class="card"><div class="neon"><img src="images/seismogram.png"></div><div class="cap">Real marsquake · 4 May 2022</div></div>
</div>
<div class="grid c3" style="margin-top:18px">
<div class="card stat"><b>1,319</b><small>Marsquakes recorded</small></div>
<div class="card stat"><b>&lt; 1 atom</b><small>Motion it can feel</small></div>
<div class="card stat"><b>Dec 2018</b><small>SEIS deployed</small></div>
</div>

---
<!-- _footer: "Source: Physical Geology (OpenText BC)" -->
<div class="eyebrow">04 / Waves</div>

## Two kinds of seismic waves

<div class="grid c2">
<div class="card" style="border-color:var(--cyan)"><h3 class="p">P-waves</h3><p>Faster. Push and pull the rock. Cross solids and liquids.</p>
<svg viewBox="0 0 520 110"><path d="M20 55H140M200 55H320M380 55H500" stroke="#00E5FF" stroke-width="44" stroke-dasharray="2 5" fill="none"/><text x="20" y="104" fill="#9C97A8" font-size="12" font-family="monospace">COMPRESSION · RAREFACTION →</text></svg></div>
<div class="card" style="border-color:var(--mag)"><h3 class="s">S-waves</h3><p>Slower. Shake the rock sideways. Cross solids only.</p>
<svg viewBox="0 0 520 110"><path d="M20 55q30-45 60 0t60 0 60 0 60 0 60 0 60 0 60 0 60 0" stroke="#FF2BD6" stroke-width="3" fill="none"/><text x="20" y="104" fill="#9C97A8" font-size="12" font-family="monospace">SIDEWAYS MOTION →</text></svg></div>
</div>
<div class="callout">S-waves can't cross a liquid. If they go missing, a liquid layer is in the way.</div>

---
<!-- _footer: "Source: Seismogram: InSight/SEIS data" -->
<div class="eyebrow">05 / Experiment</div>

## Live experiment: our own marsquake

<div class="grid c3">
<div class="card"><span class="num" style="font-size:34px">01</span><p style="color:var(--text)">Seismograph on the table.</p></div>
<div class="card"><span class="num" style="font-size:34px">02</span><p style="color:var(--text)">Tap the table. That's our marsquake.</p></div>
<div class="card"><span class="num" style="font-size:34px">03</span><p style="color:var(--text)">Record it. Compare with NASA.</p></div>
</div>
<div class="grid c2" style="margin-top:20px">
<div class="card"><div class="neon"><img src="images/seismogram.png" style="height:200px;object-fit:cover"></div><div class="cap">NASA · 4 May 2022</div></div>
<div class="card" style="border:2px dashed var(--cyan);display:grid;place-items:center;height:236px"><span class="cap" style="color:var(--cyan)">OURS · LIVE RECORDING</span></div>
</div>

---
<!-- _footer: "Source: NASA/JPL-Caltech · “How InSight studies Mars’ inner layers”" -->
<div class="eyebrow">06 / Method</div>

## How quakes reveal the interior

<div class="split">
<div>
<div class="grid c2">
<div class="card"><span class="num">SPEED</span><p>Waves move faster or slower in different rock.</p></div>
<div class="card"><span class="num">TIME</span><p>Distance = speed × time. Measure time, find depth.</p></div>
<div class="card"><span class="num">ECHOES</span><p>Waves bounce off layer boundaries.</p></div>
<div class="card"><span class="num">BENDING</span><p>When speed changes, the wave changes direction.</p></div>
</div>
<div class="formula">d = v × t</div>
</div>
<div><img class="fig" src="images/cutaway.jpg"><div class="cap">Wave goes down, bounces off the core, returns to InSight.</div></div>
</div>

---
<!-- _class: bleed -->
<!-- _paginate: false -->
<!-- _header: "" -->
<!-- _footer: "" -->
<img src="images/inside-mars.jpg">

---
<!-- _footer: "Source: Stähler 2021 · Samuel 2023 · Sun 2025" -->
<div class="eyebrow">07 / Discoveries</div>

## The biggest discoveries

<div class="tl">
<div class="card"><div class="year">2021</div><h3>A liquid core</h3><div class="stat"><b>1,830 km</b></div><p>Radius: more than half of Mars.</p></div>
<div class="card"><div class="year">2023</div><h3>A molten layer on top</h3><div class="stat"><b>1,650 km</b></div><p>The core is smaller than thought.</p></div>
<div class="card" style="border-color:var(--mag)"><span class="badge">STILL DEBATED</span><div class="year">2025</div><h3>A solid inner core?</h3><div class="stat"><b>613 km</b></div><p>Stacking 23 quakes reveals faint echoes.</p></div>
</div>
<div class="callout">If confirmed, Mars has an Earth-like core: liquid outside, solid inside.</div>

---
<!-- _footer: "Source: NASA Mars Facts · Stähler 2022 · Hong Kong Observatory" -->
<div class="eyebrow">08 / Impact</div>

## Why does this matter?

<div class="split">
<div class="stack">
<div class="card"><h3>How Mars formed</h3><p>Layers record the early days of a rocky planet.</p></div>
<div class="card"><h3>How Mars cooled</h3><p>The core may explain the missing magnetic field.</p></div>
<div class="card"><h3>Still active?</h3><p>Cerberus Fossae quakes hint at a warm source 30–50 km down.</p></div>
</div>
<table><tr><th>Measure</th><th>Mars</th><th>Earth</th></tr><tr><td>Radius</td><td>≈ 3,390 km</td><td>≈ 6,370 km</td></tr><tr><td>Core share</td><td>≈ 54%</td><td>≈ 55%</td></tr><tr><td>Plates</td><td>None</td><td>Yes</td></tr><tr><td>Magnetic field</td><td>None today</td><td>Yes</td></tr></table>
</div>
<div class="callout">Same core share as Earth, but no plates and no magnetic field today.</div>

---
<!-- _class: end -->
<!-- _footer: "Source: NASA/JPL · Science (2021) · Nature (2023, 2025)" -->
<div class="eyebrow">09 / Takeaways</div>

## Mission accomplished: what we learned

<div class="grid c3">
<div class="card"><span class="num">01</span><p style="color:var(--text)">Marsquakes send waves through the whole planet.</p></div>
<div class="card"><span class="num">02</span><p style="color:var(--text)">Speed, echoes and missing waves reveal crust, mantle and core.</p></div>
<div class="card"><span class="num">03</span><p style="color:var(--text)">InSight found a liquid core, and maybe a solid inner one.</p></div>
</div>

# Thank you! Questions?

---
<!-- _footer: "Full list of references used in this talk" -->
<div class="eyebrow">Sources</div>

## Sources

<div class="grid c3 src">
<div class="card"><h3 style="color:var(--rust)">Research papers</h3><b>Knapmeyer-Endrun</b> · Science 2021, crust<br><b>Khan</b> · Science 2021, mantle<br><b>Stähler</b> · Science 2021, core<br><b>Samuel</b> · Nature 2023, molten layer<br><b>Sun</b> · Nature 2025, inner core<br><b>Stähler</b> · Nat. Astron. 2022, Cerberus Fossae</div>
<div class="card"><h3 style="color:var(--rust)">Other sources</h3>NASA Mars Facts<br>NASA/JPL InSight news (2021, 2025)<br>NASA, “How InSight studies Mars’ inner layers”<br>Univ. of Oxford (2023) · CNES<br>Astronomy magazine · Eos (AGU)<br>EarthSky · Smithsonian · OpenText BC · HKO</div>
<div class="card"><h3 style="color:var(--rust)">Images</h3>NASA/JPL-Caltech: SEIS photo, “Inside Mars”, cutaway<br>agenciasinc.es: Mars render<br>InSight/SEIS data: seismogram<br>masterymind.co: wave diagram</div>
</div>
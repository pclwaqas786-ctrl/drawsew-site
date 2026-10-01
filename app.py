"""DrawSew — Embroidery Digitizing. Professional single-page business site (Streamlit)."""
import streamlit as st
import streamlit.components.v1 as components
import base64 as _b64
import re
from pathlib import Path as _Path

st.set_page_config(
    page_title="DrawSew — Embroidery Digitizing Service | DST, PES Files in 6-12 Hours",
    page_icon="🧵",
    layout="wide",
    initial_sidebar_state="collapsed",
)

EMAIL = "drawsew1@gmail.com"
MAILTO = "mailto:drawsew1@gmail.com?subject=Free%20Sample%20Request"
WHATSAPP_DISPLAY = "+92 332 3167915"
WHATSAPP_LINK = "https://wa.me/923323167915"
FB_PAGE = "https://www.facebook.com/profile.php?id=61594911263612"
IG_PAGE = "https://www.instagram.com/drawsew1/"
CALL_LINK = "tel:+923323167915"

_logo_b64 = _b64.b64encode((_Path(__file__).parent / "assets" / "drawsew-logo.png").read_bytes()).decode()

# ----------------------------------------------------------------------------
# Design system: deep navy + gold + warm ivory. Serif display, clean sans body.
# ----------------------------------------------------------------------------
st.markdown(
    """
<style>
:root {
  --navy: #0d1f2d;
  --navy2: #132a3f;
  --gold: #c9973f;
  --gold-lt: #e6c47c;
  --ivory: #faf7f0;
  --ink: #1d2b3a;
  --muted: #5d7183;
  --line: #e8e1d1;
  --serif: Georgia, 'Times New Roman', Times, serif;
}
html {scroll-behavior: smooth;}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.stApp {background: var(--ivory);}
.block-container {padding-top: 0rem; max-width: 1180px;}

/* full-bleed sections */
.full {width: 100vw; margin-left: calc(-50vw + 50%); padding: 72px 0;}
.inner {max-width: 1180px; margin: 0 auto; padding: 0 28px;}

/* ---------- navbar ---------- */
.navbar {
  position: sticky; top: 0; z-index: 999;
  width: 100vw; margin-left: calc(-50vw + 50%);
  background: rgba(13,31,45,0.97);
  border-bottom: 1px solid rgba(201,151,63,0.25);
  backdrop-filter: blur(6px);
}
.nav-inner {
  max-width: 1180px; margin: 0 auto; padding: 12px 28px;
  display: flex; align-items: center; gap: 26px;
}
.brand {display: flex; align-items: center; gap: 11px; text-decoration: none;}
.brand img {width: 38px; height: 38px; border-radius: 10px; background: #fff;}
.brand .wm {font-family: var(--serif); font-size: 1.35rem; color: #fff; letter-spacing: 0.5px;}
.brand .wm b {color: var(--gold-lt); font-weight: 700;}
.nav-links {display: flex; gap: 22px; margin-left: auto; align-items: center;}
.nav-links a.nl {color: #d8e2ea; text-decoration: none; font-size: 0.92rem; font-weight: 500;}
.nav-links a.nl:hover {color: var(--gold-lt);}
.btn-gold {
  display: inline-block; background: var(--gold); color: var(--navy) !important;
  font-weight: 700; font-size: 0.92rem; text-decoration: none;
  padding: 10px 24px; border-radius: 999px; white-space: nowrap;
}
.btn-gold:hover {background: var(--gold-lt);}
.btn-outline-w {
  display: inline-block; background: transparent; color: #fff !important;
  border: 1.5px solid rgba(255,255,255,0.55); font-weight: 600;
  padding: 12px 28px; border-radius: 999px; text-decoration: none; font-size: 1rem;
}
.btn-outline-w:hover {border-color: #fff; background: rgba(255,255,255,0.08);}

/* ---------- hero ---------- */
.hero {background: radial-gradient(1200px 600px at 75% 20%, #1a3a55 0%, var(--navy) 60%); color: #fff; padding: 84px 0 72px 0;}
.eyebrow {
  display: inline-block; color: var(--gold-lt); font-size: 0.78rem; font-weight: 700;
  letter-spacing: 3px; text-transform: uppercase; margin-bottom: 18px;
  border-bottom: 2px solid var(--gold); padding-bottom: 8px;
}
.hero h1 {
  font-family: var(--serif); font-weight: 700; color: #fff;
  font-size: 3rem; line-height: 1.15; margin: 0 0 18px 0; max-width: 640px;
}
.hero h1 .hl {color: var(--gold-lt); font-style: italic;}
.hero p.lead {color: #c3d2de; font-size: 1.15rem; line-height: 1.7; max-width: 600px; margin: 0 0 32px 0;}
.hero .btnrow {display: flex; gap: 14px; flex-wrap: wrap;}
.hero .btnrow .btn-gold {padding: 14px 34px; font-size: 1.02rem;}
.hero .btnrow .btn-outline-w {padding: 14px 34px; font-size: 1.02rem;}

/* ---------- trust strip ---------- */
.trust {background: var(--navy2); border-top: 1px solid rgba(201,151,63,0.25); padding: 26px 0;}
.trust .inner {display: flex; justify-content: space-between; gap: 18px; flex-wrap: wrap;}
.tstat {text-align: left;}
.tstat .n {font-family: var(--serif); font-size: 1.7rem; font-weight: 700; color: var(--gold-lt);}
.tstat .l {color: #9db0bf; font-size: 0.85rem; letter-spacing: 0.4px;}

/* ---------- sections ---------- */
.sec {padding: 72px 0 8px 0;}
.sec-head {max-width: 680px; margin-bottom: 40px;}
.sec-head.center {margin-left: auto; margin-right: auto; text-align: center;}
.kicker {color: var(--gold); font-size: 0.78rem; font-weight: 700; letter-spacing: 3px; text-transform: uppercase; margin-bottom: 12px;}
.sec-head h2 {font-family: var(--serif); font-size: 2.1rem; color: var(--ink); margin: 0 0 12px 0; line-height: 1.25;}
.sec-head p {color: var(--muted); font-size: 1.05rem; line-height: 1.65; margin: 0;}
section.anchor, div.anchor {scroll-margin-top: 84px;}

/* ---------- cards / grids ---------- */
.grid3 {display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px;}
.svc {
  background: #fff; border: 1px solid var(--line); border-radius: 14px;
  padding: 30px 26px; transition: transform .18s ease, box-shadow .18s ease;
}
.svc:hover {transform: translateY(-4px); box-shadow: 0 14px 34px rgba(13,31,45,0.10);}
.svc .idx {font-family: var(--serif); color: var(--gold); font-size: 0.95rem; font-weight: 700; letter-spacing: 2px; margin-bottom: 12px;}
.svc h3 {font-family: var(--serif); color: var(--ink); font-size: 1.22rem; margin: 0 0 10px 0;}
.svc p {color: var(--muted); font-size: 0.96rem; line-height: 1.65; margin: 0;}

/* ---------- portfolio ---------- */
.work {background: var(--navy); padding: 72px 0;}
.work .sec-head h2 {color: #fff;}
.work .sec-head p {color: #9db0bf;}
.work-grid {display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px;}
.work-item {position: relative; border-radius: 12px; overflow: hidden; background: var(--navy2);}
.work-item img {width: 100%; display: block; aspect-ratio: 1/1; object-fit: cover; transition: transform .25s ease;}
.work-item:hover img {transform: scale(1.05);}
.work-cap {
  position: absolute; bottom: 0; left: 0; right: 0;
  background: linear-gradient(transparent, rgba(13,31,45,0.88));
  color: #e8eef3; font-size: 0.75rem; letter-spacing: 0.6px;
  padding: 26px 12px 10px 12px; text-transform: uppercase;
}

/* ---------- formats ---------- */
.fmtrow {display: flex; flex-wrap: wrap; gap: 10px; justify-content: center; margin-top: 6px;}
.fmt {
  background: #fff; border: 1px solid var(--line); color: var(--navy);
  font-weight: 700; font-size: 0.95rem; letter-spacing: 1px;
  border-radius: 8px; padding: 12px 26px;
}

/* ---------- pricing ---------- */
.price {
  background: #fff; border: 1px solid var(--line); border-radius: 16px;
  padding: 36px 30px; text-align: center; position: relative;
  display: flex; flex-direction: column;
}
.price h3 {font-family: var(--serif); font-size: 1.25rem; color: var(--ink); margin: 0 0 6px 0;}
.price .amount {font-family: var(--serif); font-size: 2.6rem; font-weight: 700; color: var(--navy); margin: 8px 0 4px 0;}
.price ul {list-style: none; padding: 0; margin: 20px 0 26px 0; text-align: left;}
.price li {color: var(--muted); font-size: 0.95rem; padding: 7px 0; border-bottom: 1px solid #f0ebdd;}
.price li:last-child {border-bottom: none;}
.price li::before {content: "✓ "; color: var(--gold); font-weight: 700;}
.price .btn-ghost {
  margin-top: auto; display: inline-block; border: 1.5px solid var(--navy); color: var(--navy);
  font-weight: 700; padding: 11px 26px; border-radius: 999px; text-decoration: none; font-size: 0.95rem;
}
.price.dark {background: var(--navy); border-color: var(--navy);}
.price.dark h3, .price.dark .amount {color: #fff;}
.price.dark .amount {color: var(--gold-lt);}
.price.dark li {color: #c3d2de; border-bottom-color: rgba(255,255,255,0.10);}
.price.dark .btn-gold {margin-top: auto;}
.ptag {
  position: absolute; top: -14px; left: 50%; transform: translateX(-50%);
  background: var(--gold); color: var(--navy); font-size: 0.72rem; font-weight: 800;
  letter-spacing: 1.5px; padding: 5px 16px; border-radius: 999px; white-space: nowrap;
}
.pricenote {text-align: center; color: var(--muted); margin-top: 26px; font-size: 1rem;}
.pricenote b {color: var(--navy);}

/* ---------- process ---------- */
.steps3 {display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; counter-reset: step;}
.pstep {background: #fff; border: 1px solid var(--line); border-radius: 14px; padding: 32px 26px; position: relative;}
.pstep .snum {
  font-family: var(--serif); font-size: 2.6rem; font-weight: 700; color: var(--gold);
  opacity: 0.85; margin-bottom: 8px;
}
.pstep h3 {font-family: var(--serif); color: var(--ink); font-size: 1.2rem; margin: 0 0 10px 0;}
.pstep p {color: var(--muted); font-size: 0.96rem; line-height: 1.65; margin: 0;}

/* ---------- why ---------- */
.whygrid {display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px 28px;}
.whyitem {display: flex; gap: 14px; align-items: flex-start; background: #fff;
  border: 1px solid var(--line); border-radius: 12px; padding: 20px 22px;}
.whyitem .tick {
  flex: 0 0 auto; width: 30px; height: 30px; border-radius: 50%;
  background: var(--navy); color: var(--gold-lt);
  display: flex; align-items: center; justify-content: center; font-weight: 800;
}
.whyitem h4 {margin: 2px 0 6px 0; color: var(--ink); font-size: 1.02rem;}
.whyitem p {margin: 0; color: var(--muted); font-size: 0.93rem; line-height: 1.6;}

/* ---------- faq ---------- */
.faq details {background: #fff; border: 1px solid var(--line); border-radius: 12px; margin-bottom: 10px;}
.faq summary {
  padding: 17px 22px; cursor: pointer; font-weight: 600; color: var(--ink); font-size: 1rem;
  list-style: none; display: flex; justify-content: space-between; align-items: center; gap: 12px;
}
.faq summary::-webkit-details-marker {display: none;}
.faq summary::after {content: "+"; color: var(--gold); font-size: 1.5rem; font-weight: 400; line-height: 1;}
.faq details[open] summary::after {content: "–";}
.faq .a {padding: 0 22px 20px 22px; color: var(--muted); line-height: 1.7; font-size: 0.97rem;}

/* ---------- tips library ---------- */
.tiplib details {background: #fff; border: 1px solid var(--line); border-radius: 14px;}
.tiplib summary {
  padding: 20px 24px; cursor: pointer; font-weight: 700; color: var(--navy);
  font-size: 1.05rem; list-style: none; display: flex; justify-content: space-between; align-items: center;
}
.tiplib summary::-webkit-details-marker {display: none;}
.tiplib summary::after {content: "+"; color: var(--gold); font-size: 1.6rem; line-height: 1;}
.tiplib details[open] summary::after {content: "–";}
.tipgrid {display: grid; grid-template-columns: repeat(2, 1fr); gap: 18px; padding: 6px 24px 26px 24px;}
.tipcard {border: 1px solid var(--line); border-radius: 12px; overflow: hidden; background: #fff;}
.tipcard img {width: 100%; display: block; aspect-ratio: 16/9; object-fit: cover;}
.tipcard .tb {padding: 16px 18px; color: var(--muted); font-size: 0.92rem; line-height: 1.65;}
.tipcard .tn {font-family: var(--serif); color: var(--gold); font-weight: 700; font-size: 0.85rem; letter-spacing: 1.5px; margin-bottom: 8px;}

/* ---------- contact band ---------- */
.contactband {background: radial-gradient(900px 500px at 20% 30%, #1a3a55 0%, var(--navy) 65%); color: #fff; padding: 76px 0; text-align: center;}
.contactband h2 {font-family: var(--serif); color: #fff; font-size: 2.2rem; margin: 0 0 14px 0;}
.contactband p {color: #c3d2de; font-size: 1.08rem; max-width: 620px; margin: 0 auto 30px auto; line-height: 1.7;}
.contactband .btnrow {display: flex; gap: 14px; justify-content: center; flex-wrap: wrap;}
.contactband .btnrow .btn-gold, .contactband .btnrow .btn-outline-w {padding: 14px 30px; font-size: 1rem;}
.socrow {display: flex; gap: 12px; justify-content: center; margin-top: 30px;}
.socrow a {color: #c3d2de; text-decoration: none; font-size: 0.92rem; border: 1px solid rgba(255,255,255,0.25);
  padding: 9px 22px; border-radius: 999px;}
.socrow a:hover {color: #fff; border-color: var(--gold-lt);}

/* ---------- footer ---------- */
.sitefooter {background: #0a1722; color: #8fa3b5; padding: 56px 0 0 0;}
.fcols {display: grid; grid-template-columns: 1.4fr 1fr 1fr 1fr; gap: 32px; padding-bottom: 40px;}
.fcols h5 {color: #fff; font-size: 0.85rem; letter-spacing: 2px; text-transform: uppercase; margin: 0 0 16px 0;}
.fcols a, .fcols p {color: #8fa3b5; font-size: 0.93rem; text-decoration: none; line-height: 2;}
.fcols a:hover {color: var(--gold-lt);}
.fbrand {display: flex; align-items: center; gap: 10px; margin-bottom: 14px;}
.fbrand img {width: 34px; height: 34px; border-radius: 8px; background: #fff;}
.fbrand span {font-family: var(--serif); color: #fff; font-size: 1.2rem;}
.fbottom {border-top: 1px solid rgba(255,255,255,0.08); padding: 20px 0; text-align: center; font-size: 0.85rem; color: #6b7f91;}

@media (max-width: 860px) {
  .nav-links a.nl {display: none;}
  .hero h1 {font-size: 2.1rem;}
  .grid3, .steps3 {grid-template-columns: 1fr;}
  .work-grid {grid-template-columns: repeat(2, 1fr);}
  .whygrid {grid-template-columns: 1fr;}
  .fcols {grid-template-columns: 1fr 1fr;}
  .tipgrid {grid-template-columns: 1fr;}
  .full {padding: 52px 0;}
}
</style>
""",
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# Navbar
# ----------------------------------------------------------------------------
st.markdown(
    f"""
<div class="navbar"><div class="nav-inner">
  <a class="brand" href="#top">
    <img src="data:image/png;base64,{_logo_b64}" alt="DrawSew logo" />
    <span class="wm">Draw<b>Sew</b></span>
  </a>
  <div class="nav-links">
    <a class="nl" href="#services">Services</a>
    <a class="nl" href="#work">Work</a>
    <a class="nl" href="#pricing">Pricing</a>
    <a class="nl" href="#process">Process</a>
    <a class="nl" href="#faq">FAQ</a>
    <a class="btn-gold" href="{MAILTO}">Free Sample</a>
  </div>
</div></div>
<div id="top"></div>
""",
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# Hero
# ----------------------------------------------------------------------------
st.markdown(
    f"""
<div class="full hero"><div class="inner">
  <span class="eyebrow">Embroidery Digitizing Studio</span>
  <h1>Logo to stitch file, <span class="hl">perfected by hand.</span></h1>
  <p class="lead">DrawSew converts your artwork into clean, machine-ready embroidery files —
  DST, PES, EXP and more — delivered in 6&ndash;12 hours. First sample free, no obligation.</p>
  <div class="btnrow">
    <a class="btn-gold" href="{MAILTO}">Get My Free Sample</a>
    <a class="btn-outline-w" href="#pricing">See Pricing</a>
  </div>
</div></div>
<div class="full trust" style="padding:0;"><div class="inner" style="padding-top:26px;padding-bottom:26px;">
  <div class="tstat"><div class="n">800+</div><div class="l">Logos digitized</div></div>
  <div class="tstat"><div class="n">6&ndash;12 hrs</div><div class="l">Standard turnaround</div></div>
  <div class="tstat"><div class="n">100%</div><div class="l">Hand-digitized</div></div>
  <div class="tstat"><div class="n">6</div><div class="l">Machine formats</div></div>
</div></div>
""",
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# Services
# ----------------------------------------------------------------------------
_services = [
    ("01", "Cap Digitizing & 3D Puff",
     "Structured and unstructured caps with correct pull compensation — plus raised 3D puff foam lettering that pops."),
    ("02", "Embroidered Patches",
     "Merrowed-edge and laser-cut patches in any shape, digitized for crisp borders and clean trims."),
    ("03", "Left Chest Logos",
     "Small-placement polo and workshirt logos — tiny text, tight curves, zero distortion at small sizes."),
    ("04", "Jacket Back Designs",
     "Large-format back designs with proper density control — no puckering, no stiff thread patches."),
    ("05", "Appliqué Digitizing",
     "Multi-fabric appliqué with clean placement lines, tack-down and cover stitches that finish smooth."),
    ("06", "Workwear & Uniforms",
     "Company uniforms, hi-vis and service apparel — consistent branding across every garment and size."),
]
_cards = "".join(
    f'<div class="svc"><div class="idx">{i}</div><h3>{t}</h3><p>{d}</p></div>'
    for i, t, d in _services
)
st.markdown(
    f"""
<div class="sec anchor" id="services"><div class="inner">
  <div class="sec-head">
    <div class="kicker">What we do</div>
    <h2>Digitizing services, built for production.</h2>
    <p>Every design is hand-digitized stitch by stitch in Wilcom &amp; Pulse — never auto-punched —
    so it sews cleanly on your machine, the first time.</p>
  </div>
  <div class="grid3">{_cards}</div>
</div></div>
""",
    unsafe_allow_html=True,
)


# ----------------------------------------------------------------------------
# Portfolio
# ----------------------------------------------------------------------------
@st.cache_data
def _img_b64(name):
    p = _Path(__file__).parent / "assets" / "posts" / name
    return _b64.b64encode(p.read_bytes()).decode() if p.exists() else ""


_work_items = "".join(
    f'<div class="work-item"><img src="data:image/jpeg;base64,{_img_b64(f"post-{n:02d}.jpg")}" '
    f'alt="DrawSew design preview {n}" loading="lazy" />'
    f'<div class="work-cap">Design preview</div></div>'
    for n in range(1, 9) if _img_b64(f"post-{n:02d}.jpg")
)
st.markdown(
    f"""
<div class="full work anchor" id="work"><div class="inner">
  <div class="sec-head">
    <div class="kicker">Design previews</div>
    <h2>Digitizing concepts & stitch previews.</h2>
    <p>A sample of digitizing concepts from our studio. Preview images are illustrative — every order ships with a free sample preview of your own artwork before you pay.</p>
  </div>
  <div class="work-grid">{_work_items}</div>
</div></div>
""",
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# Formats
# ----------------------------------------------------------------------------
_fmts = "".join(f'<span class="fmt">{f}</span>' for f in ["DST", "PES", "EXP", "EMB", "JEF", "VP3"])
st.markdown(
    f"""
<div class="sec"><div class="inner">
  <div class="sec-head center">
    <div class="kicker">Compatibility</div>
    <h2>One logo. Every machine format.</h2>
    <p>We deliver the exact file your machine needs — converted free between formats.</p>
  </div>
  <div class="fmtrow">{_fmts}</div>
</div></div>
""",
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# Pricing
# ----------------------------------------------------------------------------
_tiers = [
    ("Simple", "$8",
     ["Text & small logos", "Up to 5,000 stitches", "1 machine format", "6–12 hr delivery"],
     False, "Start Simple"),
    ("Standard", "$15",
     ["Most logos & designs", "Caps, left chest, polos", "All formats included", "6–12 hr delivery"],
     True, "Get Standard"),
    ("Complex", "$25+",
     ["3D puff & jacket backs", "Detailed & large designs", "All formats included", "Priority turnaround"],
     False, "Get a Quote"),
]
_price_cards = ""
for t, price, feats, pop, cta in _tiers:
    feats_html = "".join(f"<li>{f}</li>" for f in feats)
    if pop:
        _price_cards += (
            f'<div class="price dark"><div class="ptag">MOST POPULAR</div><h3>{t}</h3>'
            f'<div class="amount">{price}</div><ul>{feats_html}</ul>'
            f'<a class="btn-gold" href="{MAILTO}">{cta}</a></div>'
        )
    else:
        _price_cards += (
            f'<div class="price"><h3>{t}</h3><div class="amount">{price}</div><ul>{feats_html}</ul>'
            f'<a class="btn-ghost" href="{MAILTO}">{cta}</a></div>'
        )
st.markdown(
    f"""
<div class="sec anchor" id="pricing"><div class="inner">
  <div class="sec-head center">
    <div class="kicker">Pricing</div>
    <h2>Simple, honest pricing.</h2>
    <p>No hidden fees. No surprises. Your first sample is always free.</p>
  </div>
  <div class="grid3">{_price_cards}</div>
  <p class="pricenote">Every new client gets their <b>first sample digitized free</b> — sew it,
  check it, then decide. Free revisions until it sews right on your machine.</p>
</div></div>
""",
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# Process
# ----------------------------------------------------------------------------
_steps = [
    ("01", "Send your artwork",
     "Any format works — JPG, PNG, PDF, even a phone photo of your logo. Email or WhatsApp it over."),
    ("02", "We digitize by hand",
     "A specialist builds your stitch paths manually in Wilcom & Pulse. No auto-digitizing shortcuts."),
    ("03", "Sew within hours",
     "Your stitch-ready file arrives in 6–12 hours, in every format your machines need."),
]
_steps_html = "".join(
    f'<div class="pstep"><div class="snum">{n}</div><h3>{t}</h3><p>{d}</p></div>'
    for n, t, d in _steps
)
st.markdown(
    f"""
<div class="sec anchor" id="process"><div class="inner">
  <div class="sec-head">
    <div class="kicker">How it works</div>
    <h2>From logo to stitch file in three steps.</h2>
  </div>
  <div class="steps3">{_steps_html}</div>
</div></div>
""",
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# Why DrawSew
# ----------------------------------------------------------------------------
_whys = [
    ("Hand-digitized, never auto-punched",
     "Every file is built stitch-by-stitch by a specialist — clean underlay, correct density, smooth trims."),
    ("6–12 hour turnaround",
     "Send your logo in the morning, sew it by evening. Rush jobs get priority."),
    ("First sample free",
     "Judge our quality on your own machine before you pay anything — no obligation."),
    ("Free revisions until it sews right",
     "If anything needs adjusting, we fix it free — no arguing, no extra charges."),
    ("Quality-checked before delivery",
     "Every file is reviewed stitch by stitch before it leaves the studio."),
    ("Direct line to your digitizer",
     "WhatsApp, email or call — fast replies from the person doing your work, not a ticket queue."),
]
_why_html = "".join(
    f'<div class="whyitem"><div class="tick">✓</div><div><h4>{t}</h4><p>{d}</p></div></div>'
    for t, d in _whys
)
st.markdown(
    f"""
<div class="sec anchor" id="why"><div class="inner">
  <div class="sec-head">
    <div class="kicker">Why DrawSew</div>
    <h2>Built for shops that can't afford rework.</h2>
  </div>
  <div class="whygrid">{_why_html}</div>
</div></div>
""",
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# FAQ
# ----------------------------------------------------------------------------
_faqs = [
    ("What is embroidery digitizing?",
     "Converting your logo into stitch data (a file like DST or PES) that an embroidery machine can sew."),
    ("Which formats do you deliver?",
     "DST, PES, EXP, EMB, JEF, VP3 — and others on request. Format conversion is always free."),
    ("How fast is delivery?",
     "Standard turnaround is 6–12 hours. Tell us your deadline and we will meet it."),
    ("Is the first sample really free?",
     "Yes — completely free, no charge and no obligation. Send any logo and judge the quality yourself."),
    ("How much does digitizing cost?",
     "Simple designs start at $8, standard logos $15, complex designs like 3D puff or jacket backs $25+. Your first sample is always free — exact quote before we start."),
    ("Do you offer free revisions?",
     "Yes. We revise free until the design sews cleanly on your machine — no extra charges."),
    ("What if I need it urgently?",
     "Tell us your deadline. Standard delivery is 6–12 hours, and rush jobs get priority."),
]
_faq_html = "".join(
    f'<details><summary>{q}</summary><div class="a">{a}</div></details>' for q, a in _faqs
)
st.markdown(
    f"""
<div class="sec anchor" id="faq"><div class="inner">
  <div class="sec-head">
    <div class="kicker">FAQ</div>
    <h2>Questions, answered.</h2>
  </div>
  <div class="faq" style="max-width:820px;">{_faq_html}</div>
</div></div>
""",
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# Tips library (the 40 posts, tucked into one expandable library)
# ----------------------------------------------------------------------------
@st.cache_data
def load_posts():
    text = (_Path(__file__).parent / "posts.md").read_text(encoding="utf-8")
    parts = re.split(r"^## POST ", text, flags=re.M)
    posts = []
    for p in parts[1:]:
        lines = p.strip().split("\n")
        header = lines[0].strip()
        body = "\n".join(lines[1:]).strip()
        body = re.sub(r"^\*\*Image:\*\*.*$", "", body, flags=re.M).strip()
        body = re.sub(r"\n-{3,}\n?", "\n", body).strip()
        num = header.split("—")[0].strip()
        posts.append({"num": num, "body": body})
    return posts


_posts = load_posts()
_tip_cards = ""
for _p in _posts:
    _img = _img_b64(f'post-{int(_p["num"]):02d}.jpg')
    _img_html = (
        f'<img src="data:image/jpeg;base64,{_img}" alt="DrawSew digitizing tip {_p["num"]}" loading="lazy" />'
        if _img else ""
    )
    _body_html = _p["body"].replace("\n", "<br>")
    _tip_cards += (
        f'<div class="tipcard">{_img_html}<div class="tb">'
        f'<div class="tn">TIP {_p["num"]}</div>{_body_html}</div></div>'
    )
st.markdown(
    f"""
<div class="sec anchor" id="tips"><div class="inner">
  <div class="sec-head">
    <div class="kicker">Learn</div>
    <h2>Free digitizing tips library.</h2>
    <p>40 practical embroidery tips from our studio — the same ones we share on social media.</p>
  </div>
  <div class="tiplib"><details>
    <summary>Browse all 40 free tips</summary>
    <div class="tipgrid">{_tip_cards}</div>
  </details></div>
</div></div>
""",
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# AI voice assistant (restyled)
# ----------------------------------------------------------------------------
st.markdown(
    """
<div class="sec"><div class="inner">
  <div class="sec-head center">
    <div class="kicker">Instant answers</div>
    <h2>Talk to Vicky, our AI assistant.</h2>
    <p>Tap the mic and ask about pricing, turnaround or file formats — answers instantly, no call charges.</p>
  </div>
</div></div>
""",
    unsafe_allow_html=True,
)

VOICE_HTML = """
<div style="max-width:640px;margin:0 auto;background:#fff;border:1px solid #e8e1d1;border-radius:16px;
     box-shadow:0 10px 30px rgba(13,31,45,.08);padding:20px;font-family:sans-serif;">
  <div id="vlog" style="height:220px;overflow-y:auto;border:1px solid #eee;border-radius:10px;
       padding:12px;margin-bottom:14px;font-size:.92rem;line-height:1.5;background:#faf7f0;"></div>
  <div style="display:flex;gap:10px;align-items:center;">
    <button id="vmic" style="flex:0 0 auto;background:#0d1f2d;color:#e6c47c;border:none;border-radius:50%;
            width:64px;height:64px;font-size:1.7rem;cursor:pointer;">🎤</button>
    <input id="vtext" placeholder="or type your question…" style="flex:1;padding:12px;border:1px solid #ddd;
           border-radius:10px;font-size:.95rem;" />
    <button id="vsend" style="background:#c9973f;color:#0d1f2d;border:none;border-radius:10px;
            padding:12px 18px;font-size:.95rem;font-weight:700;cursor:pointer;">Send</button>
  </div>
  <p id="vstatus" style="margin:10px 0 0;color:#0d1f2d;font-size:.85rem;min-height:1.2em;"></p>
</div>
<script>
(function(){
  var log = document.getElementById('vlog');
  var status = document.getElementById('vstatus');
  var mic = document.getElementById('vmic');
  var txt = document.getElementById('vtext');
  var send = document.getElementById('vsend');
  var SYSTEM = "You are Vicky, the friendly AI voice assistant of DrawSew, an embroidery digitizing service. "
    + "You convert customer logos into machine embroidery files (DST, PES, EXP, JEF, VP3, XXX) in 6-12 hours, "
    + "starting at $8, first sample FREE. Be warm and brief. ALWAYS reply in 1-2 short spoken sentences, under 40 words. "
    + "If they want to order, ask them to email drawsew1@gmail.com or WhatsApp +92 332 3167915 with their logo. "
    + "Never invent prices or make promises beyond the free sample and 6-12 hour turnaround.";
  function add(who, text){
    var d = document.createElement('div');
    d.style.margin = '0 0 8px 0';
    d.innerHTML = '<b style="color:#0d1f2d">' + who + ':</b> ' + text.replace(/</g,'&lt;');
    log.appendChild(d); log.scrollTop = log.scrollHeight;
  }
  function speak(text){
    try {
      speechSynthesis.cancel();
      var u = new SpeechSynthesisUtterance(text);
      u.lang = 'en-US'; u.rate = 1;
      speechSynthesis.speak(u);
    } catch(e){}
  }
  var busy = false;
  function ask(q){
    if(!q || busy) return;
    busy = true;
    add('You', q);
    status.textContent = '⏳ Vicky is thinking…';
    fetch('https://text.pollinations.ai/' + encodeURIComponent(SYSTEM + '\\nCustomer: ' + q + '\\nVicky:') + '?model=openai')
      .then(function(r){ return r.text(); })
      .then(function(a){
        a = (a||'').trim().slice(0, 400) || "Sorry, I didn't catch that. Please ask again!";
        add('Vicky', a);
        status.textContent = '🔊 Vicky is speaking… (tap mic to interrupt)';
        speak(a);
        status.textContent = '';
        busy = false;
      })
      .catch(function(){
        add('Vicky', "Sorry, I'm having trouble right now. Please email drawsew1@gmail.com — we reply fast!");
        status.textContent = ''; busy = false;
      });
  }
  var SR = window.SpeechRecognition || window.webkitSpeechRecognition;
  var rec = null, listening = false;
  if(SR){
    rec = new SR(); rec.lang = 'en-US'; rec.interimResults = false; rec.maxAlternatives = 1;
    rec.onresult = function(e){
      var t = e.results[0][0].transcript;
      listening = false; mic.textContent = '🎤'; mic.style.background = '#0d1f2d';
      ask(t);
    };
    rec.onerror = function(){ listening = false; mic.textContent = '🎤'; mic.style.background = '#0d1f2d'; status.textContent = ''; };
    rec.onend = function(){ if(listening){ listening = false; mic.textContent = '🎤'; mic.style.background = '#0d1f2d'; status.textContent = ''; } };
  }
  mic.onclick = function(){
    if(!rec){ status.textContent = '⚠️ Voice not supported in this browser — please type instead.'; return; }
    if(listening){ rec.stop(); return; }
    try{ speechSynthesis.cancel(); }catch(e){}
    listening = true; mic.textContent = '⏹️'; mic.style.background = '#c0392b';
    status.textContent = '🎙️ Listening… speak now';
    try{ rec.start(); }catch(e){ listening = false; mic.textContent = '🎤'; mic.style.background = '#0d1f2d'; }
  };
  send.onclick = function(){ ask(txt.value.trim()); txt.value=''; };
  txt.addEventListener('keydown', function(e){ if(e.key === 'Enter'){ ask(txt.value.trim()); txt.value=''; } });
  add('Vicky', "Hi! I'm Vicky, DrawSew's AI assistant. Tap the mic and ask me anything about digitizing!");
})();
</script>
"""
components.html(VOICE_HTML, height=560)

# ----------------------------------------------------------------------------
# Contact band
# ----------------------------------------------------------------------------
st.markdown(
    f"""
<div class="full contactband anchor" id="contact"><div class="inner">
  <span class="eyebrow">Get started</span>
  <h2>Get your free sample today.</h2>
  <p>Send your logo — any format works — and get a stitch-ready file back in 6&ndash;12 hours.
  No payment, no obligation.</p>
  <div class="btnrow">
    <a class="btn-gold" href="{MAILTO}">Email: {EMAIL}</a>
    <a class="btn-outline-w" href="{WHATSAPP_LINK}" target="_blank">WhatsApp {WHATSAPP_DISPLAY}</a>
  </div>
  <div class="socrow">
    <a href="{FB_PAGE}" target="_blank">Facebook</a>
    <a href="{IG_PAGE}" target="_blank">Instagram</a>
    <a href="{CALL_LINK}">Call {WHATSAPP_DISPLAY}</a>
  </div>
</div></div>
""",
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# Footer
# ----------------------------------------------------------------------------
st.markdown(
    f"""
<div class="full sitefooter" style="padding:0;"><div class="inner" style="padding-top:56px;">
  <div class="fcols">
    <div>
      <div class="fbrand">
        <img src="data:image/png;base64,{_logo_b64}" alt="DrawSew logo" />
        <span>DrawSew</span>
      </div>
      <p>Professional embroidery digitizing studio.<br>Hand-digitized files, delivered in 6&ndash;12 hours.<br>First sample always free.</p>
    </div>
    <div>
      <h5>Explore</h5>
      <a href="#services">Services</a><br>
      <a href="#work">Our Work</a><br>
      <a href="#pricing">Pricing</a><br>
      <a href="#faq">FAQ</a><br>
      <a href="#tips">Tips Library</a>
    </div>
    <div>
      <h5>Services</h5>
      <a href="#services">Cap Digitizing</a><br>
      <a href="#services">3D Puff</a><br>
      <a href="#services">Patches</a><br>
      <a href="#services">Left Chest Logos</a><br>
      <a href="#services">Jacket Backs</a>
    </div>
    <div>
      <h5>Contact</h5>
      <a href="{MAILTO}">{EMAIL}</a><br>
      <a href="{WHATSAPP_LINK}" target="_blank">WhatsApp {WHATSAPP_DISPLAY}</a><br>
      <a href="{FB_PAGE}" target="_blank">Facebook</a><br>
      <a href="{IG_PAGE}" target="_blank">Instagram</a>
    </div>
  </div>
  <div class="fbottom">© 2026 DrawSew — Elite Draw Sew Digitizing · Vicky, Digitizing Specialist</div>
</div></div>
""",
    unsafe_allow_html=True,
)

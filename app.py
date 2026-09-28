"""DrawSew — Embroidery Digitizing. Single-page business site (Streamlit)."""
import streamlit as st
import streamlit.components.v1 as components

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

st.markdown(
    """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.block-container {padding-top: 0rem; max-width: 1100px;}
.hero {
    background: linear-gradient(135deg, #0b6e4f 0%, #149a6d 55%, #1db386 100%);
    border-radius: 22px;
    padding: 56px 32px 48px 32px;
    text-align: center;
    color: white;
    margin-bottom: 28px;
}
.hero h1 {color: white; font-size: 2.6rem; margin-bottom: 12px;}
.hero h1 .hl {color: #ffe08a;}
.hero p {color: #eafff5; font-size: 1.15rem; max-width: 640px; margin: 0 auto 26px auto;}
.hero .btnrow {display: flex; gap: 14px; justify-content: center; flex-wrap: wrap;}
.abtn {
    display: inline-block; padding: 13px 30px; border-radius: 999px;
    font-weight: 700; font-size: 1.05rem; text-decoration: none;
}
.abtn-w {background: #ffffff; color: #0b6e4f;}
.abtn-o {background: transparent; color: #ffffff; border: 2px solid #ffffff;}
.card {
    background: #ffffff; border-radius: 16px; padding: 24px 20px;
    box-shadow: 0 4px 18px rgba(11,110,79,0.10);
    border: 1px solid #e6f2ec; height: 100%;
}
.card h3 {color: #0b6e4f; font-size: 1.2rem; margin-bottom: 8px;}
.card p {color: #3d4a45; font-size: 0.98rem;}
.sec-title {color: #0b6e4f; text-align: center; margin: 44px 0 6px 0;}
.sec-sub {text-align: center; color: #5a6b62; margin-bottom: 22px;}
.stat {text-align: center; padding: 18px 8px;}
.stat .n {font-size: 2rem; font-weight: 800; color: #0b6e4f;}
.stat .l {color: #5a6b62; font-size: 0.95rem;}
.step {
    background: #f2faf6; border-radius: 16px; padding: 24px 20px; text-align: center;
    border: 1px solid #dff0e6; height: 100%;
}
.step .num {
    display: inline-block; width: 44px; height: 44px; line-height: 44px;
    border-radius: 50%; background: #0b6e4f; color: white;
    font-weight: 800; font-size: 1.2rem; margin-bottom: 10px;
}
.step h3 {color: #0b6e4f; font-size: 1.1rem;}
.step p {color: #3d4a45; font-size: 0.95rem;}
.why {background: #ffffff; border-left: 5px solid #0b6e4f; border-radius: 12px;
      padding: 18px 20px; box-shadow: 0 3px 12px rgba(11,110,79,0.08); margin-bottom: 14px;}
.why h3 {color: #0b6e4f; font-size: 1.1rem; margin-bottom: 6px;}
.why p {color: #3d4a45; margin: 0;}
.contact {
    background: linear-gradient(135deg, #0b6e4f 0%, #149a6d 100%);
    border-radius: 22px; padding: 44px 28px; text-align: center; color: white;
    margin-top: 44px; margin-bottom: 10px;
}
.contact h2 {color: white;}
.contact p {color: #eafff5; max-width: 620px; margin: 0 auto 24px auto; font-size: 1.1rem;}
.contact .btnrow {display: flex; gap: 14px; justify-content: center; flex-wrap: wrap;}
.footer {text-align: center; color: #8aa096; font-size: 0.85rem; padding: 18px 0 30px 0;}
.fmt {display: inline-block; background: #eef7f2; color: #0b6e4f; font-weight: 700;
      border-radius: 999px; padding: 8px 20px; margin: 5px;}
.stExpander {border: 1px solid #e6f2ec !important; border-radius: 12px !important;}
</style>
""",
    unsafe_allow_html=True,
)

# ---------- HERO ----------
import base64 as _b64
_logo_b64 = _b64.b64encode(open("assets/drawsew-logo.png", "rb").read()).decode()
st.markdown(
    f"""
<div class="hero">
    <img src="data:image/png;base64,{_logo_b64}" alt="DrawSew logo"
         style="width:110px;height:110px;border-radius:24px;margin-bottom:14px;
                box-shadow:0 4px 16px rgba(0,0,0,0.25);background:#fff;" />
    <h1>Your logo, <span class="hl">stitch-ready</span> in 6&ndash;12 hours.</h1>
    <p>Professional embroidery digitizing in Wilcom &amp; Pulse. 800+ logos digitized. First sample free.</p>
    <div class="btnrow">
        <a class="abtn abtn-w" href="{MAILTO}">Get Free Sample</a>
        <a class="abtn abtn-o" href="{WHATSAPP_LINK}" target="_blank">WhatsApp Us</a>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# ---------- STATS ----------
c1, c2, c3, c4 = st.columns(4)
for col, n, l in [
    (c1, "800+", "Logos Digitized"),
    (c2, "2+", "Years Experience"),
    (c3, "6&ndash;12h", "Turnaround"),
    (c4, "100%", "Human Digitized"),
]:
    col.markdown(f'<div class="stat"><div class="n">{n}</div><div class="l">{l}</div></div>', unsafe_allow_html=True)

# ---------- SERVICES ----------
st.markdown('<h2 class="sec-title">Digitizing Services</h2>', unsafe_allow_html=True)
st.markdown('<p class="sec-sub">Every design hand-digitized for clean, distortion-free stitching.</p>', unsafe_allow_html=True)
s1, s2, s3, s4 = st.columns(4)
services = [
    ("🧢 Caps & 3D Puff", "Structured crowns, perfect puff elevation, clean small text."),
    ("🪡 Patches", "Merrowed edge, laser-cut precision, perfect registration."),
    ("👕 Workwear & Uniforms", "Left-chest logos, durable for industrial wash."),
    ("🧥 Jackets & Apparel", "Back designs, sleeves, full-front — distortion-free."),
]
for col, (t, d) in zip([s1, s2, s3, s4], services):
    col.markdown(f'<div class="card"><h3>{t}</h3><p>{d}</p></div>', unsafe_allow_html=True)

# ---------- FORMATS ----------
st.markdown('<h2 class="sec-title">One logo. Every machine format.</h2>', unsafe_allow_html=True)
st.markdown(
    '<p class="sec-sub">' + " ".join(f'<span class="fmt">{f}</span>' for f in
                                     ["DST", "PES", "EXP", "EMB", "JEF", "VP3"]) + "</p>",
    unsafe_allow_html=True,
)

# ---------- HOW IT WORKS ----------
st.markdown('<h2 class="sec-title">How It Works</h2>', unsafe_allow_html=True)
st.markdown('<p class="sec-sub">From logo to stitch file in three simple steps.</p>', unsafe_allow_html=True)
w1, w2, w3 = st.columns(3)
steps = [
    ("1", "Send your logo", "Any format works — JPG, PNG, PDF, even a photo."),
    ("2", "We digitize by hand", "Hand-built stitch paths in Wilcom & Pulse. Never auto-digitized."),
    ("3", "Get your file back", "Stitch-ready file delivered in 6–12 hours."),
]
for col, (n, t, d) in zip([w1, w2, w3], steps):
    col.markdown(f'<div class="step"><div class="num">{n}</div><h3>{t}</h3><p>{d}</p></div>', unsafe_allow_html=True)

# ---------- WHY DRAWSEW ----------
st.markdown('<h2 class="sec-title">Why DrawSew</h2>', unsafe_allow_html=True)
st.markdown(
    """
<div class="why"><h3>✋ Human digitizing, never auto-digitized</h3>
<p>Every file is built stitch-by-stitch by a specialist — no cheap auto-punch shortcuts.</p></div>
<div class="why"><h3>⚡ 6–12 hour turnaround</h3>
<p>Send your logo in the morning, sew it by evening. Rush jobs welcome.</p></div>
<div class="why"><h3>🎁 First sample free</h3>
<p>Judge our quality on your own machine before you pay a single rupee — no obligation.</p></div>
""",
    unsafe_allow_html=True,
)

# ---------- FAQ ----------
st.markdown('<h2 class="sec-title">FAQ</h2>', unsafe_allow_html=True)
faqs = [
    ("What is embroidery digitizing?",
     "Converting your logo into stitch data (a file like DST or PES) that an embroidery machine can sew."),
    ("Which formats do you deliver?",
     "DST, PES, EXP, EMB, JEF, VP3 — and others on request."),
    ("How fast is delivery?",
     "Standard turnaround is 6–12 hours. Tell us your deadline and we will meet it."),
    ("Is the first sample really free?",
     "Yes — completely free, no charge and no obligation. Send any logo and judge the quality yourself."),
]
for q, a in faqs:
    with st.expander(q):
        st.write(a)

# ---------- POSTS (40 free digitizing tips — full feed with images) ----------
import re
from pathlib import Path as _Path

@st.cache_data
def load_posts():
    text = _Path(__file__).parent.joinpath("posts.md").read_text(encoding="utf-8")
    parts = re.split(r"^## POST ", text, flags=re.M)
    posts = []
    for p in parts[1:]:
        lines = p.strip().split("\n")
        header = lines[0].strip()
        body = "\n".join(lines[1:]).strip()
        body = re.sub(r"^\*\*Image:\*\*.*$", "", body, flags=re.M).strip()
        body = re.sub(r"\n-{3,}\n?", "\n", body).strip()
        num = header.split("—")[0].strip()
        date = header.split("—", 1)[1].strip() if "—" in header else ""
        date = re.sub(r"\(published.*?\)", "", date).strip(" ,")
        posts.append({"num": num, "date": date, "body": body})
    return posts

@st.cache_data
def post_img_b64(num):
    p = _Path(__file__).parent.joinpath("assets", "posts", f"post-{int(num):02d}.jpg")
    if p.exists():
        return _b64.b64encode(p.read_bytes()).decode()
    return ""

st.markdown('<h2 class="sec-title">📝 Digitizing Tips — 40 Free Posts</h2>', unsafe_allow_html=True)
st.markdown('<p class="sec-sub">One practical embroidery tip every day — same posts we share on social media.</p>', unsafe_allow_html=True)

_posts = load_posts()
for _i in range(0, len(_posts), 2):
    _cols = st.columns(2)
    for _j, _col in enumerate(_cols):
        if _i + _j >= len(_posts):
            break
        _p = _posts[_i + _j]
        _img = post_img_b64(_p["num"])
        _img_html = (
            f'<img src="data:image/jpeg;base64,{_img}" alt="DrawSew post {_p["num"]}" '
            'style="width:100%;border-radius:12px 12px 0 0;display:block;" />'
            if _img else
            '<div style="background:linear-gradient(135deg,#0b6e4f,#1db386);color:#fff;'
            'text-align:center;padding:52px 10px;font-size:2.2rem;border-radius:12px 12px 0 0;">🧵</div>'
        )
        _body_html = _p["body"].replace("\n", "<br>")
        _col.markdown(
            f'<div class="card" style="padding:0;overflow:hidden;margin-bottom:18px;">'
            f"{_img_html}"
            f'<div style="padding:16px 18px;">'
            f'<p style="color:#0b6e4f;font-weight:700;font-size:0.85rem;margin:0 0 8px 0;">📅 {_p["date"]}</p>'
            f"<p>{_body_html}</p></div></div>",
            unsafe_allow_html=True,
        )

FB_PAGE = "https://www.facebook.com/profile.php?id=61594911263612"
IG_PAGE = "https://www.instagram.com/drawsew1/"
CALL_LINK = "tel:+923323167915"

# ---------- AI VOICE ASSISTANT (free, browser-based) ----------
st.markdown('<h2 class="sec-title">🎤 Talk to Our AI Assistant</h2>', unsafe_allow_html=True)
st.markdown('<p class="sec-sub">Tap the mic and ask about pricing, turnaround or file formats — Vicky answers instantly, no call charges.</p>', unsafe_allow_html=True)

VOICE_HTML = """
<div style="max-width:640px;margin:0 auto;background:#fff;border-radius:16px;
     box-shadow:0 4px 18px rgba(0,0,0,.08);padding:20px;font-family:sans-serif;">
  <div id="vlog" style="height:220px;overflow-y:auto;border:1px solid #eee;border-radius:10px;
       padding:12px;margin-bottom:14px;font-size:.92rem;line-height:1.5;background:#fafafa;"></div>
  <div style="display:flex;gap:10px;align-items:center;">
    <button id="vmic" style="flex:0 0 auto;background:#0b6e4f;color:#fff;border:none;border-radius:50%;
            width:64px;height:64px;font-size:1.7rem;cursor:pointer;">🎤</button>
    <input id="vtext" placeholder="or type your question…" style="flex:1;padding:12px;border:1px solid #ddd;
           border-radius:10px;font-size:.95rem;" />
    <button id="vsend" style="background:#0b6e4f;color:#fff;border:none;border-radius:10px;
            padding:12px 18px;font-size:.95rem;cursor:pointer;">Send</button>
  </div>
  <p id="vstatus" style="margin:10px 0 0;color:#0b6e4f;font-size:.85rem;min-height:1.2em;"></p>
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
    d.innerHTML = '<b style="color:#0b6e4f">' + who + ':</b> ' + text.replace(/</g,'&lt;');
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
        add('Vicky 🤖', a);
        status.textContent = '🔊 Vicky is speaking… (tap mic to interrupt)';
        speak(a);
        status.textContent = '';
        busy = false;
      })
      .catch(function(){
        add('Vicky 🤖', "Sorry, I'm having trouble right now. Please email drawsew1@gmail.com — we reply fast!");
        status.textContent = ''; busy = false;
      });
  }
  var SR = window.SpeechRecognition || window.webkitSpeechRecognition;
  var rec = null, listening = false;
  if(SR){
    rec = new SR(); rec.lang = 'en-US'; rec.interimResults = false; rec.maxAlternatives = 1;
    rec.onresult = function(e){
      var t = e.results[0][0].transcript;
      listening = false; mic.textContent = '🎤'; mic.style.background = '#0b6e4f';
      ask(t);
    };
    rec.onerror = function(){ listening = false; mic.textContent = '🎤'; mic.style.background = '#0b6e4f'; status.textContent = ''; };
    rec.onend = function(){ if(listening){ listening = false; mic.textContent = '🎤'; mic.style.background = '#0b6e4f'; status.textContent = ''; } };
  }
  mic.onclick = function(){
    if(!rec){ status.textContent = '⚠️ Voice not supported in this browser — please type instead.'; return; }
    if(listening){ rec.stop(); return; }
    try{ speechSynthesis.cancel(); }catch(e){}
    listening = true; mic.textContent = '⏹️'; mic.style.background = '#c0392b';
    status.textContent = '🎙️ Listening… speak now';
    try{ rec.start(); }catch(e){ listening = false; mic.textContent = '🎤'; mic.style.background = '#0b6e4f'; }
  };
  send.onclick = function(){ ask(txt.value.trim()); txt.value=''; };
  txt.addEventListener('keydown', function(e){ if(e.key === 'Enter'){ ask(txt.value.trim()); txt.value=''; } });
  add('Vicky 🤖', "Hi! I'm Vicky, DrawSew's AI assistant. Tap the mic and ask me anything about digitizing!");
})();
</script>
"""
components.html(VOICE_HTML, height=560)

# ---------- CONTACT ----------
st.markdown(
    f"""
<div class="contact">
    <h2>Get Your Free Sample</h2>
    <p>Send your logo — any format works — and get a stitch-ready file back in 6&ndash;12 hours.</p>
    <div class="btnrow">
        <a class="abtn abtn-w" href="{MAILTO}">{EMAIL}</a>
        <a class="abtn abtn-o" href="{WHATSAPP_LINK}" target="_blank">WhatsApp {WHATSAPP_DISPLAY}</a>
        <a class="abtn abtn-o" href="{CALL_LINK}">📞 Call {WHATSAPP_DISPLAY}</a>
    </div>
    <p style="margin:26px 0 12px 0;font-size:1rem;">Follow DrawSew</p>
    <div class="btnrow">
        <a class="abtn abtn-o" href="{FB_PAGE}" target="_blank" style="padding:10px 24px;font-size:0.95rem;">📘 Facebook</a>
        <a class="abtn abtn-o" href="{IG_PAGE}" target="_blank" style="padding:10px 24px;font-size:0.95rem;">📸 Instagram</a>
    </div>
</div>
<div class="footer">© 2026 DrawSew — Elite Draw Sew Digitizing · Vicky, Digitizing Specialist</div>
""",
    unsafe_allow_html=True,
)

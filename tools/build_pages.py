#!/usr/bin/env python3
"""
Sub-page generator for MIDAS CLINIC · INSPIRE.

Every page shares the same header / footer, so the pages are generated from
this one file. Edit the text below, then run from the repository root:

    python3 tools/build_pages.py

Each text is written as T(english, korean, chinese). English is the default
text in the HTML; Korean and Chinese are stored in data-ko / data-zh and
swapped in by js/main.js when the visitor changes language.
"""
import html
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def T(en, ko, zh):
    return (en, ko, zh)


def esc(s):
    return html.escape(s, quote=True)


def tx(tag, t, cls="", attrs=""):
    """Render a translatable element."""
    en, ko, zh = t
    c = f' class="{cls}"' if cls else ""
    return f'<{tag}{c}{attrs} data-ko="{esc(ko)}" data-zh="{esc(zh)}">{en}</{tag}>'


ARROW = '<svg><use href="#i-arrow"/></svg>'

# 세포 항목은 파나셀 홈페이지로 연결 (새 창)
PANACELL_URL = "https://panacell-website.pages.dev/"

NAV = [
    ("about", "about.html", T("About", "병원소개", "关于我们")),
    ("procedures", "procedures.html", T("Procedures", "진료안내", "诊疗项目")),
    ("global", "global-care.html", T("Global Care", "글로벌 케어", "国际关怀")),
    ("experience", "experience.html", T("Inspire Experience", "인스파이어 경험", "Inspire 体验")),
    ("media", "media.html", T("Media", "미디어", "媒体")),
    ("contact", "contact.html", T("Contact", "오시는 길", "联系我们")),
    ("cell", PANACELL_URL, T("Cell", "세포", "细胞")),
]
CONSULT = T("Consultation", "상담 예약", "预约咨询")
BOOK = T("Book a Consultation", "상담 예약하기", "预约咨询")
HOME = T("Home", "홈", "首页")


def nav_link(key, href, label, active=None):
    if href.startswith("http"):
        return tx("a", label, "ext", f' href="{href}" target="_blank" rel="noopener"')
    return tx("a", label, "active" if key == active else "", f' href="{href}"')


def header(active):
    links = "\n      ".join(nav_link(k, h, l, active) for k, h, l in NAV)
    drawer = "\n  ".join(nav_link(k, h, l) for k, h, l in NAV)
    return f'''<svg width="0" height="0" class="sr" aria-hidden="true">
  <symbol id="i-arrow" viewBox="0 0 20 12" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M0 6h18M13 1l5 5-5 5"/></symbol>
  <symbol id="i-chev" viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M1 3l4 4 4-4"/></symbol>
</svg>

<header class="header" id="header">
  <div class="header-in">
    <a href="index.html" class="logo" aria-label="Midas Clinic Inspire"><b>MIDAS CLINIC</b><small>INSPIRE</small></a>
    <nav class="gnb" aria-label="Main">
      {links}
    </nav>
    <div class="header-r">
      <div class="lang" id="lang">
        <button class="lang-btn" id="langBtn" aria-haspopup="true" aria-expanded="false"><span id="langLabel">EN</span><svg><use href="#i-chev"/></svg></button>
        <div class="lang-menu" role="menu">
          <button data-lang="en" role="menuitem">English</button>
          <button data-lang="ko" role="menuitem">한국어</button>
          <button data-lang="zh" role="menuitem">中文</button>
        </div>
      </div>
      {tx("a", CONSULT, "header-cta", ' href="contact.html"')}
      <button class="burger" id="burger" aria-label="Menu"><span></span><span></span></button>
    </div>
  </div>
</header>

<nav class="drawer" id="drawer" aria-label="Mobile">
  {drawer}
  <div class="drawer-foot">
    <div class="drawer-lang"><button data-lang="en">EN</button><button data-lang="ko">KR</button><button data-lang="zh">中文</button></div>
    <a class="drawer-tel" href="tel:+82322523210">+82 32 252 3210</a>
    <a class="btn" href="contact.html#form">{tx("span", BOOK)}{ARROW}</a>
  </div>
</nav>
'''


def footer():
    links = "\n        ".join(nav_link(k, h, l) for k, h, l in NAV)
    addr = T("Inspire Entertainment Resort<br>Incheon, Korea", "인스파이어 엔터테인먼트 리조트<br>인천, 대한민국",
             "Inspire Entertainment Resort<br>韩国 仁川")
    notice = T("※ Results vary by individual. All procedures carry risks such as bleeding, infection, swelling, asymmetry or scarring.",
               "※ 모든 수술 및 시술은 개인에 따라 결과가 다를 수 있으며 출혈·감염·부종·비대칭·흉터 등의 부작용이 발생할 수 있습니다.",
               "※ 手术效果因人而异，所有手术均可能出现出血、感染、肿胀、不对称或疤痕等副作用。")
    return f'''<footer class="footer">
  <div class="wrap">
    <div class="footer-grid">
      <a href="index.html" class="logo"><b>MIDAS CLINIC</b><small>INSPIRE</small></a>
      <nav class="footer-links" aria-label="Footer">
        {links}
      </nav>
      <div class="footer-addr">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M12 22s7-7.2 7-12.5A7 7 0 0 0 5 9.5C5 14.8 12 22 12 22z"/><circle cx="12" cy="9.5" r="2.5"/></svg>
        {tx("span", addr)}
      </div>
    </div>
    <div class="footer-bottom">
      <span>미다스의원 인스파이어리조트점 (구)선이고은 성형외과 · Formerly Beauty Line Plastic Surgery · 대표원장 최승호 · 사업자등록번호 617-66-00589<br>인천광역시 중구 공항문화로 127 인스파이어 엔터테인먼트 리조트 선타워 3층 · T. 032-252-3210 · F. 032-252-3211</span>
      {tx("span", notice)}
    </div>
  </div>
</footer>

<nav class="mobile-bar" aria-label="Quick actions">
  <a href="tel:+82322523210"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/></svg>{tx("span", T("Call", "전화", "致电"))}</a>
  <a href="contact.html#messengers"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M4 5h16v11H9l-5 4z"/></svg>{tx("span", T("Messenger", "메신저", "在线咨询"))}</a>
  <a class="primary" href="contact.html#form"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="4" y="5" width="16" height="15" rx="1"/><path d="M4 10h16M9 3v4M15 3v4"/></svg>{tx("span", CONSULT)}</a>
</nav>
<a class="to-top" href="#top" aria-label="Back to top"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 19V5M6 11l6-6 6 6"/></svg></a>
'''


SILK = '''<svg class="silk" viewBox="0 0 400 400" fill="none" aria-hidden="true" preserveAspectRatio="none">
    <defs><linearGradient id="silkG" x1="0" y1="1" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".55" stop-color="#fff" stop-opacity=".95"/><stop offset="1" stop-color="#dbe2ec" stop-opacity=".7"/></linearGradient></defs>
    <path d="M30 400 C 120 250, 250 150, 400 100 L400 400 Z" fill="url(#silkG)"/>
    <path d="M110 400 C 200 290, 300 220, 400 190" stroke="#fff" stroke-width="2"/>
  </svg>'''


def page_hero(crumb, kicker, title, lead, img=None):
    crumbs = f'<div class="crumbs"><a href="index.html" data-ko="홈" data-zh="首页">Home</a> / {tx("span", crumb)}</div>'
    body = f'''{crumbs}
      {tx("div", kicker, "kicker")}
      {tx("h1", title)}
      {tx("p", lead, "lead")}'''
    if img:
        return f'''<section class="page-hero with-img">
  <div class="wrap">
      {body}
  </div>
  <div class="media"><img src="{img}" alt="" fetchpriority="high"></div>
</section>'''
    return f'''<section class="page-hero">
  <div class="wrap">
      {body}
  </div>
  {SILK}
</section>'''


def cta_band(title=None, text=None, interest=None):
    title = title or T("Begin your <em>consultation</em>", "상담을 <em>시작하세요</em>", "开始您的<em>咨询</em>")
    text = text or T("By phone, online form, KakaoTalk, LINE, WhatsApp or WeChat.",
                     "전화, 온라인 상담, 카카오톡 · LINE · WhatsApp · WeChat으로 문의하실 수 있습니다.",
                     "可通过电话、在线表单、KakaoTalk、LINE、WhatsApp或微信咨询。")
    href = "contact.html" + (f"?interest={interest}#form" if interest is not None else "#form")
    return f'''<section class="cta-band">
  <div class="wrap">
    <div>{tx("h2", title)}{tx("p", text)}</div>
    <div class="btns">
      <a class="btn" href="{href}">{tx("span", BOOK)}{ARROW}</a>
      <a class="btn ghost" href="tel:+82322523210">+82 32 252 3210</a>
    </div>
  </div>
</section>'''


def page(filename, active, title, desc, body):
    en_title, ko_title, zh_title = title
    doc = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{en_title} — MIDAS CLINIC · INSPIRE</title>
<meta name="description" content="{esc(desc)}">
<meta property="og:title" content="{esc(en_title)} — MIDAS CLINIC · INSPIRE">
<meta property="og:image" content="images/hero-inspire.jpg">
<meta name="theme-color" content="#eef2f8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600&family=Jost:wght@300;400;500&family=Marcellus&family=Noto+Sans+KR:wght@300;400;500&family=Noto+Sans+SC:wght@300;400;500&family=Noto+Serif+KR:wght@400;500&family=Noto+Serif+SC:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
</head>
<body data-title-ko="{esc(ko_title)} — 미다스의원 인스파이어" data-title-zh="{esc(zh_title)} — MIDAS CLINIC · INSPIRE">

<a class="skip" href="#main">Skip to content</a>
{header(active)}
<main id="main">
{body}
</main>

{footer()}
<script src="js/main.js"></script>
</body>
</html>
'''
    with open(os.path.join(ROOT, filename), "w", encoding="utf-8") as f:
        f.write(doc)
    print("wrote", filename)


def sec_head(kicker, title, lead=None, center=False):
    lead_html = tx("p", lead, "lead reveal") if lead else ""
    return f'''<div class="sec-head{' center' if center else ''}">
      <div class="reveal">{tx("div", kicker, "kicker")}{tx("h2", title, "title")}</div>
      {lead_html}
    </div>'''


def checks(items):
    return '<ul class="checks reveal">' + "".join(tx("li", i) for i in items) + "</ul>"


def faq(items):
    out = '<div class="faq reveal">'
    for q, a in items:
        out += f"<details><summary>{tx('span', q)}</summary>{tx('p', a)}</details>"
    return out + "</div>"


def timeline(steps, four=False):
    out = f'<div class="timeline{" four" if four else ""}">'
    for i, (h, p) in enumerate(steps, 1):
        out += f'<div class="tl reveal"><div class="k">Step 0{i}</div>{tx("h4", h)}{tx("p", p)}</div>'
    return out + "</div>"


# =====================================================================
# Shared content
# =====================================================================
PROCESS = [
    (T("Consultation", "상담", "咨询"),
     T("Tell us your concerns by phone, online form or messenger. Photos help us prepare.",
       "전화·온라인·메신저로 고민을 알려주세요. 사진을 함께 보내주시면 상담 준비에 도움이 됩니다.",
       "通过电话、在线表单或即时通讯告诉我们您的需求，附上照片有助于我们提前准备。")),
    (T("Director's design", "원장 직접 상담", "院长亲自面诊"),
     T("The director examines your structure and explains realistic results, limits and recovery.",
       "대표원장이 직접 구조를 진단하고, 가능한 결과와 한계, 회복 과정을 설명드립니다.",
       "院长亲自诊断，如实说明可达到的效果、局限及恢复过程。")),
    (T("Surgery", "수술 · 시술", "手术"),
     T("After pre-operative checks, your procedure is performed with safety as the first priority.",
       "필요한 사전 검사를 거친 뒤, 안전을 최우선으로 진행합니다.",
       "完成术前检查后，以安全为第一原则进行手术。")),
    (T("Aftercare", "사후 관리", "术后管理"),
     T("We follow your recovery step by step until the result settles.",
       "결과가 자리 잡을 때까지 회복 단계별로 경과를 확인합니다.",
       "按恢复阶段跟进，直至效果稳定。")),
]

COMMON_FAQ = [
    (T("How long is the recovery?", "회복 기간은 얼마나 걸리나요?", "恢复期需要多久？"),
     T("It depends on the procedure, the method and each person's condition. We explain the expected recovery in detail during your consultation.",
       "수술 종류와 방법, 개인 상태에 따라 다릅니다. 상담 시 예상 회복 과정을 자세히 안내해 드립니다.",
       "因手术项目、方法及个人情况而异，面诊时会详细说明预计的恢复过程。")),
    (T("What kind of anesthesia is used?", "마취는 어떻게 하나요?", "采用何种麻醉？"),
     T("The anesthesia method is decided after reviewing the procedure and your health history, and explained to you in advance.",
       "수술 범위와 건강 상태를 확인한 뒤 마취 방법을 결정하며, 사전에 충분히 설명드립니다.",
       "根据手术范围及健康状况确定麻醉方式，并会提前向您充分说明。")),
    (T("Can I consult before visiting Korea?", "방문 전에 미리 상담할 수 있나요?", "来韩国之前可以先咨询吗？"),
     T("Yes. Send us your photos and questions via KakaoTalk, LINE, WhatsApp or WeChat for a preliminary consultation. Final planning is done after an in-person examination.",
       "네. 카카오톡·LINE·WhatsApp·WeChat으로 사진과 궁금한 점을 보내주시면 사전 상담이 가능합니다. 최종 계획은 내원 진찰 후 확정합니다.",
       "可以。通过KakaoTalk、LINE、WhatsApp或微信发送照片和问题即可进行预先咨询，最终方案需在面诊后确定。")),
]

RISK = T("※ Results and recovery vary by individual. Every surgery carries possible risks such as bleeding, infection, swelling, asymmetry or scarring. Please consult a specialist fully before deciding.",
         "※ 결과와 회복 기간은 개인에 따라 다를 수 있으며, 모든 수술에는 출혈·감염·부종·비대칭·흉터 등의 부작용이 발생할 수 있습니다. 충분한 상담 후 결정하시기 바랍니다.",
         "※ 效果及恢复期因人而异，所有手术都可能出现出血、感染、肿胀、不对称或疤痕等副作用，请在充分咨询后再做决定。")

# =====================================================================
# Procedure categories (used by procedures.html and each detail page)
# =====================================================================
CATS = [
    dict(slug="rhinoplasty", interest=0,
         icon='<path d="M17 4c-3 5-4 9-3 13 1 3 4 5 6 8-1 1-3 1-4 2"/><path d="M14 17c-1 2-3 3-5 3"/>',
         name=T("Rhinoplasty", "코성형", "鼻整形"),
         kicker=T("Signature · Nose", "시그니처 · 코", "招牌 · 鼻部"),
         title=T("The art of<br><em>the profile</em>", "라인과 호흡을<br>함께 설계하는 코", "兼顾线条与呼吸的<br>鼻整形"),
         lead=T("From structural reconstruction with rib cartilage to complex revisions — designed for both appearance and breathing.",
                "자가 늑연골을 이용한 구조적 재건부터 까다로운 재수술까지, 아름다움과 호흡 기능을 함께 설계합니다.",
                "从肋软骨结构重建到复杂的鼻修复，兼顾外形与呼吸功能。"),
         short=T("Structural rhinoplasty, septoplasty and revision surgery.", "늑연골 코성형, 비중격 교정, 코 재수술", "肋软骨隆鼻、鼻中隔矫正与鼻修复"),
         overview=T("The nose sits at the centre of the face and is also how we breathe. At Midas, rhinoplasty starts from the internal structure — cartilage support, septum and airway — so that the new line looks natural and stays stable over time.",
                    "코는 얼굴의 중심이자 숨을 쉬는 기관입니다. 미다스의원의 코성형은 겉모양이 아니라 연골 지지 구조와 비중격, 기도부터 살핍니다. 자연스러운 라인이 오래 안정적으로 유지되도록 설계합니다.",
                    "鼻子位于面部中心，也是呼吸器官。美达斯的鼻整形从软骨支撑、鼻中隔及气道等内部结构入手，使新的鼻型自然且长期稳定。"),
         items=[
             (T("Rib Cartilage Rhinoplasty", "늑연골(가슴연골) 코성형", "肋软骨隆鼻"),
              T("Your own rib cartilage is used to rebuild a strong framework — often chosen when septal cartilage is insufficient or for revision cases.",
                "자가 늑연골로 튼튼한 지지 구조를 만듭니다. 비중격 연골이 부족하거나 재수술이 필요한 경우 주로 고려합니다.",
                "使用自体肋软骨重建稳固的支撑结构，常用于鼻中隔软骨不足或修复手术。")),
             (T("Septoplasty", "비중격 만곡증 교정", "鼻中隔偏曲矫正"),
              T("Straightens a deviated septum to improve breathing, and can be combined with aesthetic rhinoplasty.",
                "휘어진 비중격을 바로잡아 호흡을 개선하며, 미용 코성형과 함께 진행할 수 있습니다.",
                "矫正偏曲的鼻中隔以改善呼吸，可与美容鼻整形同时进行。")),
             (T("Revision Rhinoplasty", "코 재수술", "鼻修复"),
              T("Corrects problems from previous surgery such as contracture, deviation or implant-related issues.",
                "이전 수술 후 생긴 구축, 휘어짐, 보형물 관련 문제 등을 교정합니다.",
                "矫正既往手术后出现的挛缩、歪斜或假体相关问题。")),
             (T("Male Rhinoplasty", "남자 코성형", "男士鼻整形"),
              T("A straighter, stronger line that suits male facial structure without looking overdone.",
                "남성의 골격과 인상에 어울리는 곧고 단단한 라인을 과하지 않게 만듭니다.",
                "打造符合男性骨骼与气质、挺拔而不夸张的鼻线。")),
         ],
         suits=[T("A low or flat nasal bridge, or an undefined tip", "콧대가 낮거나 코끝이 뭉툭한 경우", "鼻梁低平或鼻尖不够精致"),
                T("Breathing discomfort from a deviated septum", "비중격 만곡으로 코막힘·호흡 불편이 있는 경우", "因鼻中隔偏曲导致鼻塞或呼吸不畅"),
                T("Dissatisfaction or problems after previous nose surgery", "이전 코수술 결과가 불만족스럽거나 문제가 생긴 경우", "对既往鼻部手术不满意或出现问题"),
                T("Wanting a natural result that suits the whole face", "얼굴 전체와 어울리는 자연스러운 코를 원하는 경우", "希望鼻型与整体面部协调自然")]),
    dict(slug="eye", interest=1,
         icon='<path d="M3 16c4-6 9-8 13-8s9 2 13 8c-4 6-9 8-13 8S7 22 3 16z"/><circle cx="16" cy="16" r="4.5"/>',
         name=T("Eye Surgery", "눈성형", "眼部整形"),
         kicker=T("Face · Eyes", "얼굴 · 눈", "面部 · 眼部"),
         title=T("A clear,<br><em>effortless</em> gaze", "또렷하지만<br>편안한 눈매", "明亮而<br>自然的眼神"),
         lead=T("Eye design that considers eye-opening strength, skin thickness and the balance of the whole face.",
                "눈 뜨는 힘과 피부 두께, 얼굴 전체의 조화를 고려해 눈매를 디자인합니다.",
                "综合考虑睁眼力量、皮肤厚度与整体面部比例来设计眼型。"),
         short=T("Double eyelid, ptosis correction, canthoplasty and blepharoplasty.", "쌍꺼풀, 눈매교정, 트임, 상·하안검", "双眼皮、上睑下垂矫正、开眼角、眼睑整形"),
         overview=T("The eyes shape first impressions. Rather than a fixed design, we look at how your eyelids open, the thickness of the skin and fat, and the proportions of your face to create eyes that look clear yet natural.",
                    "눈은 첫인상을 좌우합니다. 정해진 디자인 대신 눈 뜨는 힘, 피부와 지방의 두께, 얼굴 비율을 살펴 또렷하면서도 자연스러운 눈매를 만듭니다.",
                    "眼睛决定第一印象。我们不套用固定模板，而是观察睁眼力量、皮肤与脂肪厚度及面部比例，打造明亮自然的眼型。"),
         items=[
             (T("Double Eyelid (Non-incision / Partial / Full incision)", "쌍꺼풀 (매몰법 · 부분절개 · 절개법)", "双眼皮（埋线 / 部分切开 / 全切开）"),
              T("The method is chosen according to skin thickness, fat and the line you want.",
                "피부 두께와 지방량, 원하는 라인에 따라 수술 방법을 선택합니다.",
                "根据皮肤厚度、脂肪量及期望的线条选择术式。")),
             (T("Ptosis Correction", "안검하수 (눈매교정)", "上睑下垂矫正"),
              T("Strengthens weak eye-opening muscles for a brighter, more alert look.",
                "눈 뜨는 근육의 힘을 보강해 또렷하고 시원한 눈매를 만듭니다.",
                "加强睁眼肌力，使眼神更明亮有神。")),
             (T("Epicanthoplasty / Lateral Canthoplasty", "앞트임 · 뒤트임", "开内眼角 / 开外眼角"),
              T("Fine-tunes the horizontal length and proportion of the eyes.",
                "눈의 가로 길이와 비율을 섬세하게 조정합니다.",
                "精细调整眼睛的横向长度与比例。")),
             (T("Upper / Lower Blepharoplasty", "상안검 · 하안검", "上眼睑 / 下眼睑整形"),
              T("Addresses sagging upper eyelids, under-eye fat and wrinkles.",
                "처진 윗눈꺼풀, 눈밑 지방과 주름을 개선합니다.",
                "改善上眼睑松弛、眼袋脂肪与细纹。")),
         ],
         suits=[T("Wanting a defined but natural double eyelid", "자연스러운 쌍꺼풀 라인을 원하는 경우", "希望拥有自然的双眼皮"),
                T("Eyes that look tired or sleepy", "눈이 졸려 보이거나 피곤해 보이는 경우", "眼睛显得疲惫或无神"),
                T("Sagging eyelids or under-eye bags with age", "나이가 들며 눈꺼풀이 처지거나 눈밑이 불룩한 경우", "随年龄出现眼睑松弛或眼袋")]),
    dict(slug="lifting", interest=2,
         icon='<path d="M8 27V9M16 27V7M24 27V9"/><path d="M5 12l3-3 3 3M13 10l3-3 3 3M21 12l3-3 3 3"/>',
         name=T("Lifting", "리프팅", "面部提升"),
         kicker=T("Signature · Anti-aging", "시그니처 · 안티에이징", "招牌 · 抗衰老"),
         title=T("Lift,<br><em>not change</em>", "얼굴은 그대로,<br>시간만 되돌리다", "不改变你，<br>只留住时间"),
         lead=T("SMAS-level lifting that restores a youthful contour while keeping your own expression.",
                "근막(SMAS)층부터 끌어올려, 본래의 인상은 지키면서 젊은 윤곽을 되찾습니다.",
                "从筋膜（SMAS）层提升，在保留本来神态的同时找回年轻轮廓。"),
         short=T("Face lift and SMAS lifting for the mid-face, brow and neck.", "안면거상, 중안면·눈썹하·목 SMAS 리프팅", "面部提升，中面部、眉下、颈部SMAS提升"),
         overview=T("Pulling only the skin can look tight and fade quickly. Our lifting works at the SMAS layer — the muscular-fascial layer beneath the skin — repositioning tissue for a natural result that lasts.",
                    "피부만 당기면 부자연스럽고 효과도 오래가기 어렵습니다. 미다스의원의 리프팅은 피부 아래 근막층(SMAS)부터 조직을 제자리로 끌어올려, 자연스럽고 오래 유지되는 결과를 지향합니다.",
                    "只拉紧皮肤容易显得僵硬，效果也难以持久。我们的提升从皮下筋膜层（SMAS）重新定位组织，追求自然而持久的效果。"),
         items=[
             (T("Face Lift", "안면거상", "面部提升"),
              T("Improves overall sagging and deep folds of the face at the SMAS level.",
                "얼굴 전반의 처짐과 깊은 주름을 근막층부터 개선합니다.",
                "从筋膜层改善面部整体松弛与深层皱纹。")),
             (T("Mid-face SMAS Lift", "중안면 SMAS 리프팅", "中面部SMAS提升"),
              T("Lifts the cheeks and nasolabial area for a fresher mid-face.",
                "볼과 팔자 부위를 끌어올려 중안면을 생기 있게 만듭니다.",
                "提升脸颊与法令纹区域，让中面部更显年轻。")),
             (T("Sub-brow / Neck SMAS Lift", "눈썹하 · 목 SMAS 리프팅", "眉下 / 颈部SMAS提升"),
              T("Refreshes heavy upper eyelids through a brow incision, or tightens the jawline and neck.",
                "눈썹 아래 절개로 처진 눈꺼풀을 개선하거나, 턱선과 목의 처짐을 정돈합니다.",
                "通过眉下切口改善上睑松弛，或紧致下颌线与颈部。")),
             (T("Cheek Lift · Forehead Lift", "볼 리프팅 · 포헤드 리프팅", "脸颊提升 · 额头提升"),
              T("Smooths sagging cheek lines, forehead wrinkles and drooping brows.",
                "처진 볼 라인, 이마 주름과 눈썹 처짐을 개선합니다.",
                "改善脸颊下垂、额头皱纹与眉毛下垂。")),
         ],
         suits=[T("Sagging jawline, cheeks or neck", "턱선·볼·목이 처진 경우", "下颌线、脸颊或颈部松弛"),
                T("Deep nasolabial folds", "팔자주름이 깊어진 경우", "法令纹加深"),
                T("Non-surgical lifting no longer gives enough effect", "시술형 리프팅만으로는 효과가 부족한 경우", "非手术提升效果已不明显"),
                T("Wanting to look refreshed, not different", "달라 보이기보다 생기 있어 보이길 원하는 경우", "希望看起来更年轻而非换脸")]),
    dict(slug="contouring", interest=3,
         icon='<path d="M16 4c-6 0-9 5-9 11 0 7 4 13 9 13s9-6 9-13c0-6-3-11-9-11z"/><path d="M13 22c2 1.3 4 1.3 6 0"/>',
         name=T("Facial Contouring", "윤곽 · 페이스", "轮廓整形"),
         kicker=T("Face · Contour", "얼굴 · 윤곽", "面部 · 轮廓"),
         title=T("Balance in<br><em>every dimension</em>", "입체감과 비율을<br>다듬는 얼굴", "立体与比例<br>兼具的面部"),
         lead=T("Volume where it is needed, refinement where balance is lost.",
                "필요한 곳은 채우고, 균형을 해치는 곳은 정돈합니다.",
                "需要的地方填充，失衡的地方修整。"),
         short=T("T-zone contouring, 3D fat grafting and gummy smile correction.", "T존 성형, 입체 지방이식, 잇몸 성형", "T区整形、立体脂肪移植、露龈笑矫正"),
         overview=T("Facial harmony comes from proportion and dimension. We assess the forehead, nose, cheeks and smile together to plan subtle changes that make the whole face look balanced.",
                    "얼굴의 조화는 비율과 입체감에서 나옵니다. 이마와 코, 볼, 미소까지 함께 살펴 얼굴 전체가 균형 있어 보이도록 섬세하게 계획합니다.",
                    "面部的和谐来自比例与立体感。我们综合评估额头、鼻子、脸颊与笑容，细致规划，使整体面部更加协调。"),
         items=[
             (T("T-zone Contouring", "T존 성형", "T区整形"),
              T("Refines the line connecting the forehead and nose for a more three-dimensional profile.",
                "이마와 코를 잇는 T존 라인을 입체적으로 다듬습니다.",
                "精修额头至鼻部的T区线条，使侧颜更立体。")),
             (T("3D Fat Grafting", "3차원 입체 지방이식", "3D立体脂肪移植"),
              T("Your own fat adds natural volume to hollow areas such as the forehead, temples or cheeks.",
                "자가 지방으로 이마·관자·볼 등 꺼진 부위에 자연스러운 볼륨을 더합니다.",
                "以自体脂肪为额头、太阳穴、脸颊等凹陷部位增加自然饱满度。")),
             (T("Gummy Smile Correction", "잇몸 성형", "露龈笑矫正"),
              T("Reduces excessive gum exposure when smiling for a more graceful smile.",
                "웃을 때 잇몸이 많이 드러나는 것을 개선해 단정한 미소를 만듭니다.",
                "改善笑时牙龈过度暴露，让笑容更优雅。")),
         ],
         suits=[T("A flat profile or hollow areas", "옆모습이 밋밋하거나 꺼진 부위가 있는 경우", "侧颜扁平或有凹陷部位"),
                T("Wanting volume with your own tissue", "자가 조직으로 볼륨을 원하는 경우", "希望用自体组织增加饱满度"),
                T("Self-conscious about gum exposure when smiling", "웃을 때 잇몸 노출이 신경 쓰이는 경우", "介意笑时露出牙龈")]),
    dict(slug="body", interest=4,
         icon='<path d="M11 4c1 5 0 8-2 11s-2 9 1 13M21 4c-1 5 0 8 2 11s2 9-1 13"/>',
         name=T("Body", "바디", "身体塑形"),
         kicker=T("Body", "바디", "身体"),
         title=T("Lines that<br><em>move with you</em>", "비율과 라인을<br>고려한 바디", "兼顾比例与线条的<br>身体塑形"),
         lead=T("Body contouring and hair restoration planned around your proportions and lifestyle.",
                "체형의 비율과 라이프스타일을 고려한 바디 디자인과 모발이식.",
                "根据身形比例与生活方式规划的身体塑形与植发。"),
         short=T("Liposuction, abdominoplasty, breast lift, stem cell breast surgery and hair transplant.", "지방흡입, 복부 성형, 유방 하수 교정, 줄기세포 유방 확대·재건, 모발이식", "吸脂、腹壁整形、乳房提升、干细胞丰胸与乳房重建、植发"),
         overview=T("Body procedures are planned with the director, a member of the American Society of Lipo-Suction Surgery and the American Society of Hair Restoration Surgery, who trained in breast surgery and reconstruction in the U.S. and Japan. The focus is on natural lines rather than volume alone.",
                    "미국지방흡입학회·미국모발이식학회 정회원이며 미국·일본에서 유방성형과 재건을 수련한 대표원장이 직접 상담합니다. 단순히 양을 바꾸는 것이 아니라 자연스러운 라인을 기준으로 계획합니다.",
                    "由美国吸脂学会及美国植发学会正式会员、曾在美国和日本进修乳房整形与重建的院长亲自面诊，不只追求体积变化，而以自然线条为标准进行规划。"),
         items=[
             (T("Liposuction", "지방흡입", "吸脂"),
              T("Refines fat layers area by area, with the overall body line in mind.",
                "부위별 지방층을 정밀하게 다듬어 전체 라인을 정돈합니다.",
                "分区域精细处理脂肪层，整体塑造身体线条。")),
             (T("Abdominoplasty", "복부 성형", "腹壁整形"),
              T("Tightens loose abdominal skin and fascia, for example after pregnancy or weight loss.",
                "출산이나 체중 감량 후 늘어진 복부 피부와 근막을 함께 정리합니다.",
                "收紧产后或减重后松弛的腹部皮肤与筋膜。")),
             (T("Breast Lift", "유방 하수 교정", "乳房提升"),
              T("Restores the position and shape of sagging breasts.",
                "처진 가슴의 위치와 형태를 바로잡습니다.",
                "恢复下垂乳房的位置与形态。")),
             (T("Stem Cell Breast Augmentation", "줄기세포 유방 확대술", "干细胞丰胸"),
              T("Breast augmentation with your own fat, grafted together with adipose-derived stem cells — natural volume and feel without implants.",
                "자가지방과 지방에서 얻은 줄기세포를 함께 이식하는 가슴 확대술. 보형물 없이 자연스러운 볼륨과 촉감을 추구합니다.",
                "将自体脂肪与脂肪来源干细胞一同移植的丰胸术，无需假体，追求自然的饱满度与手感。")),
             (T("Stem Cell Breast Reconstruction", "줄기세포 유방 재건술", "干细胞乳房重建"),
              T("Restores breast volume and shape after surgery, or corrects asymmetry and deformity, using your own fat and adipose-derived stem cells.",
                "유방 수술 후 또는 비대칭·변형으로 달라진 가슴의 볼륨과 형태를 자가지방·줄기세포로 재건합니다.",
                "以自体脂肪与脂肪来源干细胞，重建术后或因不对称、变形而改变的乳房体积与形态。")),
             (T("Hair Transplant", "모발이식", "植发"),
              T("Natural hairline and density designed for your face shape.",
                "얼굴형에 맞춘 자연스러운 헤어라인과 밀도를 디자인합니다.",
                "根据脸型设计自然的发际线与密度。")),
         ],
         suits=[T("Localised fat that does not respond to diet or exercise", "식단·운동으로 잘 빠지지 않는 부분 지방", "饮食或运动难以消除的局部脂肪"),
                T("Loose abdominal skin after pregnancy or weight loss", "출산·감량 후 늘어진 복부", "产后或减重后腹部松弛"),
                T("Wanting natural breast volume without implants, or reconstruction after breast surgery", "보형물 없이 자연스러운 가슴 볼륨을 원하거나, 유방 수술 후 재건이 필요한 경우", "希望不用假体获得自然丰满，或需要乳房术后重建"),
                T("Thinning hair or a receding hairline", "모발이 가늘어지거나 헤어라인이 후퇴한 경우", "头发稀疏或发际线后移")]),
    dict(slug="skin", interest=9,
         icon='<circle cx="16" cy="16" r="11"/><circle cx="16" cy="16" r="6"/>',
         name=T("Skin & Petit", "피부 · 쁘띠", "皮肤管理"),
         kicker=T("Skin", "피부", "皮肤"),
         title=T("Skin that<br><em>keeps the glow</em>", "결과를 오래<br>빛나게 하는 피부", "让美丽<br>持久焕发的肌肤"),
         lead=T("From pre- and post-surgery care to everyday skin concerns, tailored to your skin type.",
                "수술 전후 관리부터 일상의 피부 고민까지, 피부 타입에 맞춰 관리합니다.",
                "从术前术后护理到日常肌肤困扰，根据肤质量身定制。"),
         short=T("Botox, filler, skin renewal, PRP · Super PRP, pigment and acne care.", "보톡스·필러, 피부 재생, PRP·슈퍼 PRP, 색소·여드름", "肉毒素、玻尿酸、皮肤再生、PRP与超级PRP、色斑与痘痘"),
         overview=T("Good skin makes every result look better. We combine non-surgical treatments according to your skin type and condition, without unnecessary procedures.",
                    "좋은 피부는 모든 결과를 더 돋보이게 합니다. 피부 타입과 상태에 맞춰 필요한 시술만 조합합니다.",
                    "好的肌肤让一切效果更出色。我们根据肤质与状态，只组合真正需要的非手术项目。"),
         items=[
             (T("Botox · Filler", "보톡스 · 필러", "肉毒素 · 玻尿酸"),
              T("Softens expression lines and restores volume in a natural way.",
                "표정 주름을 완화하고 꺼진 볼륨을 자연스럽게 채웁니다.",
                "淡化表情纹，自然填充凹陷部位。")),
             (T("Deep Dermal Renewal · Skin Booster", "피부 심부 재생 · 물광주사", "深层皮肤再生 · 水光针"),
              T("Improves elasticity, texture and hydration from the deeper layers of the skin.",
                "피부 깊은 층부터 탄력과 결, 수분감을 개선합니다.",
                "从深层改善肌肤弹性、纹理与水润度。")),
             (T("Pores", "모공", "毛孔"),
              T("Targets enlarged pores and rough texture.",
                "넓어진 모공과 거친 피부결을 개선합니다.",
                "改善毛孔粗大与肤质粗糙。")),
             (T("PRP · PMRP", "PRP · PMRP", "PRP · PMRP"),
              T("Platelet-rich plasma concentrated from your own blood, applied to support skin regeneration, tone and elasticity.",
                "자신의 혈액에서 혈소판이 풍부한 혈장(PRP)을 농축해, 피부 재생과 톤·탄력 개선을 돕습니다.",
                "从自体血液中浓缩富含血小板的血浆（PRP），帮助肌肤再生，改善肤色与弹性。")),
             (T("Super PRP", "슈퍼 PRP", "超级PRP"),
              T("A higher-concentration PRP treatment for regeneration, texture and elasticity.",
                "PRP를 고농도로 농축해 피부 재생, 피부결, 탄력 개선에 활용합니다.",
                "将PRP高浓度浓缩，用于肌肤再生及改善肤质与弹性。")),
             (T("Pigment · Redness · Acne", "색소 · 홍조 · 여드름", "色斑 · 潮红 · 痘痘"),
              T("Customised treatment for melasma, freckles, facial redness, active acne and acne scars.",
                "기미·주근깨, 안면홍조, 여드름과 여드름흉터에 맞춘 치료를 제공합니다.",
                "针对黄褐斑、雀斑、面部潮红、痘痘及痘印的定制治疗。")),
         ],
         suits=[T("Fine lines and loss of volume", "잔주름과 볼륨 감소", "细纹与饱满度下降"),
                T("Dull, dehydrated or rough skin", "칙칙하고 건조하거나 거친 피부", "肌肤暗沉、干燥或粗糙"),
                T("Pigmentation, redness or acne concerns", "색소·홍조·여드름 고민", "色斑、潮红或痘痘困扰"),
                T("Care before or after surgery", "수술 전후 피부 관리", "术前术后肌肤护理")]),
]


BA_PREVIEW = {"rhinoplasty": ["case01", "case03", "case06", "case11"], "lifting": ["lift01", "lift03", "lift07", "lift08"], "eye": ["eye01", "eye03", "eye06", "eye08"],
              "body": ["breast01", "breast02", "breast04", "breast05"], "skin": ["skin01", "lip01", "chin01", "fore01"]}
BA_PREVIEW_CAT = {"rhinoplasty": "nose", "lifting": "lift", "eye": "eye", "body": "breast", "skin": "face"}


def detail_page(c):
    ba_section = "" if c["slug"] not in BA_PREVIEW else f'''<section class="section white">
  <div class="wrap">
    {sec_head(T("Before &amp; After", "전후 사진", "术前术后"), c["name"])}
    {ba_gallery(BA_PREVIEW[c["slug"]])}
    <a class="arrow-link reveal" href="results.html#{BA_PREVIEW_CAT[c["slug"]]}">{tx("span", T("View all cases", "전후 사례 모두 보기", "查看全部案例"))}{ARROW}</a>
  </div>
</section>'''
    others = "".join(tx("a", o["name"], "", f' href="{o["slug"]}.html"') for o in CATS if o["slug"] != c["slug"])
    items = "".join(
        f'<div class="detail reveal"><div class="n">{i:02d}</div>{tx("h3", n)}{tx("p", d)}</div>'
        for i, (n, d) in enumerate(c["items"], 1))
    body = f'''{page_hero(c["name"], c["kicker"], c["title"], c["lead"])}

<section class="section">
  <div class="wrap two-col">
    <div class="reveal">{tx("div", T("Overview", "개요", "概述"), "kicker")}{tx("h2", c["name"], "title")}</div>
    <div class="prose reveal">{tx("p", c["overview"])}</div>
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    {sec_head(T("Procedures", "진료 항목", "诊疗项目"), T("What we offer", "진료 항목", "项目介绍"))}
    <div class="detail-list">{items}</div>
  </div>
</section>

<section class="section white">
  <div class="wrap two-col">
    <div class="reveal">{tx("div", T("Is it for you?", "이런 분께", "适合人群"), "kicker")}{tx("h2", T("Who it may suit", "이런 분께 권합니다", "适合以下人群"), "title")}</div>
    {checks(c["suits"])}
  </div>
</section>

<section class="section">
  <div class="wrap">
    {sec_head(T("Your journey", "진료 과정", "诊疗流程"), T("From consultation<br>to recovery", "상담부터<br>회복까지", "从咨询<br>到恢复"))}
    {timeline(PROCESS, four=True)}
  </div>
</section>

{ba_section if c["slug"] in BA_PREVIEW else ""}
<section class="section alt">
  <div class="wrap">
    {sec_head(T("FAQ", "자주 묻는 질문", "常见问题"), T("Questions", "자주 묻는 질문", "常见问题"))}
    {faq(COMMON_FAQ)}
    {tx("div", RISK, "notice reveal")}
    <div class="reveal" style="margin-top:50px">{tx("div", T("Other procedures", "다른 진료 보기", "其他项目"), "kicker")}<div class="other-procs">{others}</div></div>
  </div>
</section>

{cta_band(interest=c["interest"])}'''
    page(f'{c["slug"]}.html', "procedures", c["name"],
         f'{c["name"][0]} at Midas Clinic, Inspire Resort Incheon. {c["short"][0]}', body)


# =====================================================================
# Pages
# =====================================================================
def about():
    values = [
        (T("Proven skill", "검증된 실력", "实力可信"),
         T("Surgery led by a director with years of experience and training at home and abroad.",
           "국내외 연수와 오랜 경험으로 검증된 대표원장이 직접 진료합니다.",
           "由在国内外进修、经验丰富的院长亲自诊疗。")),
        (T("Focused expertise", "분야별 전문성", "专科专精"),
         T("Deep experience in nose reconstruction, lifting and body contouring.",
           "코 재건, 리프팅, 바디 등 깊이 다뤄온 분야의 전문성을 갖추었습니다.",
           "在鼻重建、面部提升、身体塑形等领域积累了深厚经验。")),
        (T("A place to rest", "편안한 휴식 공간", "舒适的休憩空间"),
         T("A calm, private space inside the resort to consult and recover.",
           "리조트 안 조용하고 프라이빗한 공간에서 상담하고 회복합니다.",
           "在度假村内安静私密的空间中咨询与恢复。")),
        (T("Trust", "믿고 맡기는 병원", "值得托付"),
         T("Honest consultation — we recommend only what you truly need.",
           "꼭 필요한 수술만 정직하게 권하는, 믿고 맡길 수 있는 병원입니다.",
           "诚实咨询，只推荐您真正需要的项目。")),
        (T("Natural & individual", "자연스러움과 개성", "自然与个性"),
         T("Soft, natural lines that keep your own character.",
           "본래의 개성을 살린 부드럽고 자연스러운 라인을 추구합니다.",
           "追求保留个人特色的柔和自然线条。")),
        (T("Safety first", "안전 우선", "安全第一"),
         T("Careful checks, anesthesia management and step-by-step aftercare.",
           "정밀한 사전 검사와 마취 관리, 단계별 사후 관리로 안전을 지킵니다.",
           "通过细致的术前检查、麻醉管理和分阶段护理确保安全。")),
    ]
    cards = "".join(f'<div class="card reveal"><div class="num">0{i}</div>{tx("h3", h)}{tx("p", p)}</div>'
                    for i, (h, p) in enumerate(values, 1))
    cv = [
        (T("Position", "직책", "职务"), [
            T("Visiting Professor, The Catholic University of Korea College of Medicine", "가톨릭의대 외래교수", "天主教大学医学院 客座教授"),
            T("Medical Specialist", "전문의", "专科医生"),
            T("Academic Director, Korean aesthetic surgery society (대한미용외과학회)", "대한미용외과학회 학술이사", "大韩美容外科学会 学术理事")]),
        (T("Certification", "자격", "资格"), [
            T("IBCS-certified in Cosmetic Surgery (Europe)", "유럽 IBCS 미용외과 전문의", "欧洲IBCS美容外科专科医生")]),
        (T("Membership", "학회", "学会"), [
            T("American cosmetic surgery society", "미국미용외과학회 정회원", "美国美容外科学会 正式会员"),
            T("American Society of Lipo-Suction Surgery", "미국지방흡입학회 정회원", "美国吸脂学会 正式会员"),
            T("American Society of Hair Restoration Surgery", "미국모발이식학회 정회원", "美国植发学会 正式会员"),
            T("European aesthetic medicine society · Balkan aesthetic surgery society", "유럽미용의학학회 · 발칸미용외과학회 정회원", "欧洲美容医学学会 · 巴尔干美容外科学会 正式会员")]),
        (T("Training", "연수", "进修"), [
            T("Breast surgery & reconstruction — Northern Michigan and Indiana state universities, U.S.", "미국 노스미시간·인디애나 주립대학 — 유방성형 및 재건", "美国北密歇根、印第安纳州立大学 — 乳房整形与重建"),
            T("Breast & nipple reconstruction — Yokohama, Japan", "일본 요코하마 — 유방·유두 재건", "日本横滨 — 乳房与乳头重建"),
            T("Aesthetic surgery — Australia, the Philippines, Germany, Bulgaria", "호주 · 필리핀 · 독일 · 불가리아 — 미용성형 연수", "澳大利亚、菲律宾、德国、保加利亚 — 美容整形进修")]),
    ]
    cvh = "".join(f'<div>{tx("h4", h)}<ul>' + "".join(tx("li", i) for i in items) + "</ul></div>" for h, items in cv)
    body = f'''{page_hero(T("About", "병원소개", "关于我们"), T("About Midas", "미다스의원 소개", "关于美达斯"),
                T("Natural refinement,<br><em>lasting confidence</em>", "자연스러운 변화,<br>오래가는 자신감", "自然蜕变，<br>持久自信"),
                T("Personalized aesthetic care at Inspire Entertainment Resort, beside Incheon International Airport.",
                  "인천국제공항 곁 인스파이어 엔터테인먼트 리조트에서, 한 사람을 위한 맞춤 성형을 합니다.",
                  "在毗邻仁川国际机场的Inspire娱乐度假村，为每一位提供量身定制的美学诊疗。"),
                img="images/standard-portrait.jpg")}

<section class="section">
  <div class="wrap two-col">
    <div class="reveal">{tx("div", T("Our story", "우리의 이야기", "我们的故事"), "kicker")}{tx("h2", T("A new chapter,<br>the same philosophy", "새로운 이름,<br>변하지 않는 철학", "新的名字，<br>不变的理念"), "title")}</div>
    <div class="prose reveal">
      {tx("p", T("Midas Clinic Inspire Resort continues the practice formerly known as Beauty Line Plastic Surgery (선이고은 성형외과) — an honest clinic built on trustworthy treatment. With a new name and a new home inside Inspire Entertainment Resort, our approach stays the same.",
                 "미다스의원 인스파이어리조트점은 ‘정직한 병원, 신뢰가는 치료’를 지켜온 (구)선이고은 성형외과의 진료를 이어갑니다. 이름과 공간은 새로워졌지만, 진료에 대한 태도는 그대로입니다.",
                 "美达斯医院Inspire度假村店延续了以“诚实的医院、值得信赖的治疗”为宗旨的前身Beauty Line整形外科（선이고은）。名字与空间焕然一新，诊疗理念始终如一。"))}
      {tx("p", T("We do not design faces for trends. We study each person's structure and character, and change only what needs to change — so the result looks like you, only more refined.",
                 "유행을 따르는 얼굴을 만들지 않습니다. 한 사람의 골격과 인상을 살피고 꼭 필요한 부분만 바꿔, 더 다듬어진 '나'로 보이는 결과를 지향합니다.",
                 "我们不追逐潮流脸。我们研究每个人的骨骼与气质，只改变需要改变的部分，让结果看起来是更精致的你。"))}
    </div>
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    {sec_head(T("Our values", "진료 원칙", "诊疗原则"), T("Six commitments", "여섯 가지 약속", "六个承诺"),
              T("A clinic that creates the value of beauty — confident on the outside, at ease on the inside.",
                "아름다움의 가치를 만드는 병원. 겉모습의 자신감과 마음의 편안함을 함께 생각합니다.",
                "创造美之价值的医院——外在自信，内心安然。"))}
    <div class="cards">{cards}</div>
  </div>
</section>

<section class="director" id="director">
  <div class="director-card reveal">
    <span class="mono" aria-hidden="true">M</span>
    <img class="dir-photo" src="images/director.jpg" alt="" loading="lazy" onerror="this.remove()">
    {tx("div", T("Seungho Choi, M.D.", "최승호 대표원장", "Seungho Choi 代表院长"), "name")}
    <div class="role">Representative Director</div>
    {tx("blockquote", T("“Never settled on one method — every face deserves the safest, most refined answer.”",
                        "“한 가지 자격과 경험에 머무르지 않고, 더 아름답고 안전한 결과를 위해 매 순간 배우고 연구합니다.”",
                        "“不止于一种资格与经验，为了更美、更安全的结果，时刻学习与钻研。”"))}
  </div>
  <div class="split-body reveal">
    {tx("div", T("Our Director", "대표원장", "代表院长"), "kicker")}
    {tx("h2", T("Expertise<br>you can <em>trust</em>", "믿을 수 있는<br>전문성", "值得信赖的<br>专业"), "title")}
    {tx("p", T("Dr. Choi has never been satisfied with a single credential or a single line of study. He trained with breast surgery and reconstruction specialists in the United States and Japan and earned aesthetic surgery qualifications in several countries — always working to make surgery safer and more beautiful.",
               "최승호 대표원장은 한 가지 자격과 연구에 만족하지 않고 완벽을 추구해 왔습니다. 미국과 일본의 유방성형·재건 전문의에게 수련하고 여러 나라에서 미용성형 자격을 취득하며, 더 안전하고 더 아름다운 수술을 위해 노력하고 있습니다.",
               "崔院长从不满足于单一的资格或研究，始终追求完美。他曾在美国和日本师从乳房整形与重建专家，并在多个国家取得美容整形资格，致力于让手术更安全、更美丽。"), "lead")}
    <div class="cv-groups">{cvh}</div>
  </div>
</section>

{cta_band()}'''
    page("about.html", "about", T("About", "병원소개", "关于我们"),
         "About Midas Clinic Inspire — formerly 선이고은 Plastic Surgery. Director Choi Seung Ho.", body)


def procedures():
    cards = ""
    for c in CATS:
        lis = "".join(tx("li", n) for n, _ in c["items"])
        cards += (f'<a class="card reveal" href="{c["slug"]}.html"><svg class="ic" viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.1">{c["icon"]}</svg>'
                  f'{tx("h3", c["name"])}{tx("p", c["short"])}<ul>{lis}</ul>'
                  f'<span class="more">{tx("span", T("Learn more", "자세히 보기", "了解更多"))}{ARROW}</span></a>')
    body = f'''{page_hero(T("Procedures", "진료안내", "诊疗项目"), T("Procedures", "진료안내", "诊疗项目"),
                T("Tailored care for<br><em>your natural beauty</em>", "한 사람을 위한<br>맞춤 진료", "为您量身定制的<br>自然之美"),
                T("Face, body and skin — each plan starts from your own structure and lifestyle.",
                  "얼굴부터 바디, 피부까지. 모든 계획은 개인의 구조와 라이프스타일에서 시작합니다.",
                  "面部、身体与皮肤——每一个方案都从您的个人结构与生活方式出发。"))}

<section class="section">
  <div class="wrap">
    <div class="cards">{cards}</div>
    <a class="arrow-link reveal" href="results.html">{tx("span", T("Before &amp; after cases", "수술 전후 사례 보기", "术前术后案例"))}{ARROW}</a>
    {tx("div", RISK, "notice reveal")}
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    {sec_head(T("Your journey", "진료 과정", "诊疗流程"), T("From consultation<br>to recovery", "상담부터<br>회복까지", "从咨询<br>到恢复"))}
    {timeline(PROCESS, four=True)}
  </div>
</section>

{cta_band()}'''
    page("procedures.html", "procedures", T("Procedures", "진료안내", "诊疗项目"),
         "Rhinoplasty, eye surgery, lifting, facial contouring, body and skin care at Midas Clinic Inspire.", body)


def global_care():
    why = [
        ('<circle cx="16" cy="16" r="12"/><path d="M4 16h24M16 4c3.5 3.4 3.5 20.6 0 24M16 4c-3.5 3.4-3.5 20.6 0 24"/>',
         T("Multilingual channels", "다국어 상담 채널", "多语种咨询渠道"),
         T("Website in English, Korean and Chinese, with consultation by KakaoTalk, LINE, WhatsApp and WeChat.",
           "영어·한국어·중국어 홈페이지와 카카오톡·LINE·WhatsApp·WeChat 상담 채널을 운영합니다.",
           "提供英文、韩文、中文网站，并可通过KakaoTalk、LINE、WhatsApp、微信咨询。")),
        ('<path d="M3 19l4-1 4 3 15-9c2-1 3.5.5 2 2L13 24l-6 2-2-3"/><path d="M12 15l-5-4 2-1 9 2"/>',
         T("Near Incheon Airport", "인천국제공항 인근", "毗邻仁川机场"),
         T("Located inside Inspire Entertainment Resort near Incheon International Airport.",
           "인천국제공항 인근 인스파이어 엔터테인먼트 리조트 안에 있습니다.",
           "位于仁川国际机场附近的Inspire娱乐度假村内。")),
        ('<path d="M4 26V12l12-8 12 8v14"/><path d="M12 26v-8h8v8"/>',
         T("Stay & recover", "머물며 회복", "入住与恢复"),
         T("Recover comfortably while staying at the resort, with the clinic just steps away.",
           "리조트에 머물며 가까운 거리에서 편안하게 회복할 수 있습니다.",
           "可在度假村入住，就近舒适地恢复。")),
        ('<path d="M16 3l11 4v8c0 7-5 12-11 14C10 27 5 22 5 15V7z"/><path d="M11 16l4 4 7-8"/>',
         T("Private & discreet", "프라이빗 진료", "私密诊疗"),
         T("A private flow from consultation to recovery, away from other guests.",
           "상담부터 회복까지 다른 고객과 마주치지 않는 동선으로 진행합니다.",
           "从咨询到恢复全程私密动线，避免与其他顾客碰面。")),
    ]
    whyc = "".join(f'<div class="card reveal"><svg class="ic" viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.2">{i}</svg>{tx("h3", h)}{tx("p", p)}</div>'
                   for i, h, p in why)
    steps = [
        (T("Online consultation", "온라인 사전 상담", "线上预先咨询"),
         T("Send photos and your concerns by messenger or the online form.", "메신저나 온라인 상담으로 사진과 고민을 보내주세요.", "通过即时通讯或在线表单发送照片与需求。")),
        (T("Plan & schedule", "일정 계획", "制定行程"),
         T("We suggest a consultation date and an estimated stay based on your procedure.", "진료 항목에 맞춰 상담 날짜와 예상 체류 기간을 안내합니다.", "根据项目建议面诊日期与预计停留时间。")),
        (T("In-person consultation", "내원 상담", "到院面诊"),
         T("The director examines you in person and finalises the plan with you.", "대표원장이 직접 진찰하고 최종 계획을 함께 정합니다.", "院长亲自诊察，与您共同确定最终方案。")),
        (T("Surgery", "수술 · 시술", "手术"),
         T("Your procedure, performed with safety as the first priority.", "안전을 최우선으로 진행합니다.", "以安全为第一原则进行手术。")),
        (T("Recovery & follow-up", "회복 · 사후 관리", "恢复与随访"),
         T("Check-ups during your stay, and follow-up by messenger after you return home.", "체류 중 경과를 확인하고, 귀국 후에도 메신저로 경과를 확인합니다.", "停留期间复诊，回国后通过即时通讯继续随访。")),
    ]
    prepare = [T("Passport (identification)", "여권 등 신분증", "护照（身份证明）"),
               T("Medical history, current medications and allergies", "병력, 복용 중인 약, 알레르기 정보", "病史、正在服用的药物及过敏信息"),
               T("Records of any previous surgery", "이전 수술 기록 (해당 시)", "既往手术记录（如有）"),
               T("Clear front and side photos for pre-consultation", "사전 상담용 정면·측면 사진", "用于预先咨询的正面与侧面照片")]
    gfaq = [
        (T("How long should I stay in Korea?", "한국에 얼마나 머물러야 하나요?", "需要在韩国停留多久？"),
         T("It depends on the procedure and your recovery. We give you an estimate during the pre-consultation and confirm it after the in-person examination.",
           "수술 종류와 회복 상태에 따라 다릅니다. 사전 상담 때 예상 기간을 안내하고, 내원 진찰 후 확정합니다.",
           "取决于手术项目与恢复情况。预先咨询时会告知预计时间，面诊后确定。")),
        (T("Which languages can I consult in?", "어떤 언어로 상담할 수 있나요?", "可以用哪些语言咨询？"),
         T("Please contact us in English, Korean or Chinese. We will let you know the consultation and interpretation options available for your visit.",
           "영어·한국어·중국어로 문의해 주세요. 방문 일정에 맞춰 가능한 상담·통역 방법을 안내해 드립니다.",
           "欢迎用英文、韩文或中文联系我们，我们会根据您的行程告知可提供的咨询与翻译方式。")),
        (T("Can I get follow-up care after returning home?", "귀국 후에도 관리받을 수 있나요?", "回国后还能得到随访吗？"),
         T("Yes. You can send photos and questions by messenger, and we will guide you through your recovery.",
           "네. 메신저로 사진과 궁금한 점을 보내주시면 회복 과정을 안내해 드립니다.",
           "可以。通过即时通讯发送照片和问题，我们会指导您的恢复过程。")),
    ]
    body = f'''{page_hero(T("Global Care", "글로벌 케어", "国际关怀"), T("Global Care", "글로벌 케어", "国际关怀"),
                T("Fly in,<br><em>glow out</em>", "세계 어디서 오셔도,<br>편안하게", "无论从哪里来，<br>都安心舒适"),
                T("From your first message to follow-up at home — care designed for patients from abroad.",
                  "첫 메시지부터 귀국 후 관리까지, 해외 고객을 위해 설계한 진료 과정.",
                  "从第一条消息到回国后的随访，专为海外顾客设计的诊疗流程。"),
                img="images/hero-inspire.jpg")}

<section class="section">
  <div class="wrap">
    {sec_head(T("Why Midas", "왜 미다스인가", "为何选择美达斯"), T("Designed for<br>international patients", "해외 고객을 위한<br>진료 환경", "为海外顾客<br>打造的诊疗环境"))}
    <div class="cards four">{whyc}</div>
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    {sec_head(T("Your journey", "진료 과정", "诊疗流程"), T("Five steps,<br>one director", "다섯 단계,<br>한 명의 원장", "五个步骤，<br>一位院长"))}
    {timeline(steps)}
  </div>
</section>

<section class="section white">
  <div class="wrap two-col">
    <div class="reveal">{tx("div", T("Before you fly", "출국 전 준비", "出发前准备"), "kicker")}{tx("h2", T("What to prepare", "준비하실 것", "需要准备的物品"), "title")}</div>
    {checks(prepare)}
  </div>
</section>

<section class="section">
  <div class="wrap">
    {sec_head(T("Contact channels", "상담 채널", "咨询渠道"), T("Reach us<br>your way", "편한 방법으로<br>연락하세요", "选择您方便的<br>方式联系我们"),
              T("Scan a QR code with your phone to start a chat with our consultation team.",
                "휴대폰으로 QR 코드를 스캔하면 바로 상담 채팅을 시작할 수 있습니다.",
                "用手机扫描二维码，即可与我们的咨询团队开始聊天。"))}
    <div class="cards four">
      <div class="card qr-card reveal"><img src="images/qr-kakao.png" alt="KakaoTalk QR code" loading="lazy"><h3>KakaoTalk</h3>{tx("p", T("For guests in Korea", "국내 고객", "适合韩国境内顾客"))}</div>
      <div class="card qr-card reveal"><img src="images/qr-line.png" alt="LINE QR code" loading="lazy"><h3>LINE</h3>{tx("p", T("For guests from Japan, Taiwan and Thailand", "일본·대만·태국 고객", "适合日本、台湾、泰国顾客"))}</div>
      <div class="card qr-card reveal"><img src="images/qr-whatsapp.png" alt="WhatsApp QR code" loading="lazy"><h3>WhatsApp</h3>{tx("p", T("For guests worldwide", "해외 고객", "适合全球顾客"))}</div>
      <div class="card qr-card reveal"><img src="images/qr-wechat.png" alt="WeChat QR code" loading="lazy"><h3>WeChat</h3>{tx("p", T("For guests from China", "중국 고객", "适合中国顾客"))}</div>
    {tx("p", T("On your phone? Press and hold a QR code to save it, then scan it from the messenger app.", "휴대폰으로 보고 계신가요? QR 코드를 길게 눌러 저장한 뒤 메신저 앱에서 스캔해 주세요.", "正在用手机浏览？长按二维码保存后，在聊天应用中扫描即可。"), "qr-tip")}
    <div style="display:none"></div>
    </div>
    {tx("p", T("On a phone? Tap a QR code to enlarge it, then scan it from another device or save the image.", "휴대폰으로 보고 계신가요? QR 코드를 누르면 크게 보입니다. 다른 기기로 스캔하거나 이미지를 저장해 앱에서 불러오세요.", "正在用手机浏览？点击二维码可放大，用其他设备扫描或保存图片后在应用中识别。"), "qr-hint")}
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    {sec_head(T("FAQ", "자주 묻는 질문", "常见问题"), T("Questions", "자주 묻는 질문", "常见问题"))}
    {faq(gfaq)}
  </div>
</section>

{cta_band(T("Start your <em>global consultation</em>", "해외 상담을 <em>시작하세요</em>", "开始您的<em>海外咨询</em>"))}'''
    page("global-care.html", "global", T("Global Care", "글로벌 케어", "国际关怀"),
         "International patients at Midas Clinic Inspire, near Incheon International Airport. Consult via KakaoTalk, WhatsApp, WeChat.", body)


def experience():
    # Real facility categories from the clinic tour page. Put the clinic's own photos in images/ and set the path.
    spaces = [
        ("wide", "images/facility-lobby.jpg", T("Sun Tower Lobby", "선타워 로비", "Sun Tower 大堂"),
         T("A bright, green atrium welcomes you at Sun Tower, Inspire Resort.", "초록이 어우러진 선타워 로비에서 방문이 시작됩니다.", "绿意盎然的Sun Tower大堂迎接您的到来。")),
        ("wide", "images/facility-entrance.jpg", T("Clinic Entrance", "병원 입구", "医院入口"),
         T("A quiet, private entrance on the 3rd floor.", "3층의 조용하고 프라이빗한 입구.", "位于3层、安静私密的入口。")),
        ("", "images/facility-lounge.jpg", T("Lounge", "라운지", "休息室"),
         T("Relax before your consultation.", "상담 전 편안히 쉬는 공간.", "咨询前放松休息的空间。")),
        ("", "images/facility-consultation.jpg", T("Consultation Room", "상담실", "咨询室"),
         T("One-to-one consultation with the director.", "대표원장과 1:1로 상담합니다.", "与院长一对一咨询。")),
        ("", "images/facility-treatment.jpg", T("Treatment Room", "진료실", "诊疗室"),
         T("For examinations and non-surgical treatments.", "진찰과 시술을 위한 공간.", "用于检查与非手术治疗。")),
        ("wide", "images/facility-operating.jpg", T("Operating Room", "수술실", "手术室"),
         T("Equipped and prepared with safety as the first priority.", "안전을 최우선으로 갖춘 수술 공간.", "以安全为第一原则配备的手术空间。")),
        ("wide", "images/inspire-lounge.jpg", T("Stay at Inspire", "인스파이어에 머물기", "入住Inspire"),
         T("Recover at the resort, steps away from the clinic.", "병원 가까이 리조트에 머물며 회복할 수 있습니다.", "在毗邻诊所的度假村休养恢复。")),
    ]
    sp = ""
    for cls, img, h, p in spaces:
        media = f'<span>Photo</span><img src="{img}" alt="" loading="lazy" onerror="this.remove()">'
        sp += f'<div class="space-card {cls} reveal"><div class="ph">{media}</div><div class="body">{tx("h3", h)}{tx("p", p)}</div></div>'
    journey = [
        (T("Arrive", "도착", "抵达"), T("Arrive at Inspire, minutes from the airport.", "공항 가까운 인스파이어 리조트에 도착합니다.", "抵达毗邻机场的Inspire度假村。")),
        (T("Consult", "상담", "咨询"), T("Meet the director in a private room.", "프라이빗 상담실에서 대표원장을 만납니다.", "在私密咨询室与院长见面。")),
        (T("Procedure", "수술", "手术"), T("Your procedure, safely performed.", "안전하게 수술·시술을 진행합니다.", "安全进行手术。")),
        (T("Recover", "회복", "恢复"), T("Rest at the resort and return for check-ups.", "리조트에 머물며 회복하고 경과를 확인합니다.", "在度假村休养并按时复诊。")),
    ]
    body = f'''{page_hero(T("Inspire Experience", "인스파이어 경험", "Inspire 体验"), T("Inspire Experience", "인스파이어 경험", "Inspire 体验"),
                T("A refined<br><em>healing journey</em>", "세련된<br>회복의 여정", "精致的<br>恢复之旅"),
                T("From consultation to recovery, premium care in a vibrant, cosmopolitan setting at Inspire.",
                  "상담부터 회복까지, 인스파이어의 세련된 공간에서 프리미엄 진료를 경험하세요.",
                  "从咨询到恢复，在Inspire充满活力的都市空间中体验高端诊疗。"),
                img="images/facility-lobby.jpg")}

<section class="section">
  <div class="wrap two-col">
    <div class="reveal">{tx("div", T("The location", "위치", "位置"), "kicker")}{tx("h2", T("Sun Tower, 3F<br>Inspire Entertainment Resort", "인스파이어 엔터테인먼트 리조트<br>선타워 3층", "Inspire娱乐度假村<br>Sun Tower 3层"), "title")}</div>
    <div class="prose reveal">
      {tx("p", T("Midas Clinic is located on the 3rd floor of Sun Tower at Inspire Entertainment Resort in Incheon, close to Incheon International Airport.",
                 "미다스의원은 인천국제공항과 가까운 인스파이어 엔터테인먼트 리조트 선타워 3층에 있습니다.",
                 "美达斯医院位于靠近仁川国际机场的Inspire娱乐度假村Sun Tower 3层。"))}
      {tx("p", T("Visitors can combine their consultation and recovery with a stay at the resort — a private clinic inside a world of hospitality.",
                 "리조트에 머물며 상담과 회복을 함께할 수 있어, 바쁜 일정이나 해외에서 오시는 분들도 편안하게 진료받으실 수 있습니다.",
                 "顾客可以在度假村入住期间完成咨询与恢复，即使行程紧凑或来自海外，也能舒适就诊。"))}
    </div>
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    {sec_head(T("The space", "공간", "空间"), T("A private &amp; refined<br>healing space", "프라이빗하고<br>세련된 공간", "私密而精致的<br>疗愈空间"),
              T("Designed for comfort and discretion, with a private flow from arrival to recovery.",
                "도착부터 회복까지 다른 고객과 마주치지 않도록 설계했습니다.",
                "从抵达到恢复，全程私密动线设计。"))}
    <div class="space-grid">{sp}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    {sec_head(T("Your stay", "머무는 동안", "停留期间"), T("Stay, heal,<br><em>shine</em>", "머물고, 회복하고,<br>빛나다", "入住、恢复、<br>焕发光彩"))}
    {timeline(journey, four=True)}
  </div>
</section>

{cta_band(T("Plan your <em>visit</em>", "방문을 <em>계획하세요</em>", "规划您的<em>来访</em>"))}'''
    page("experience.html", "experience", T("Inspire Experience", "인스파이어 경험", "Inspire 体验"),
         "Midas Clinic at Sun Tower 3F, Inspire Entertainment Resort, Incheon. A private healing space near Incheon Airport.", body)


def contact():
    body = f'''{page_hero(T("Contact", "오시는 길", "联系我们"), T("Contact", "상담 · 오시는 길", "联系我们"),
                T("Begin your<br><em>consultation</em>", "상담을<br>시작하세요", "开始您的<br>咨询"),
                T("Call, message or leave a request — we will get back to you during clinic hours.",
                  "전화, 메신저, 온라인 신청 중 편한 방법으로 문의하세요. 진료시간 내 연락드립니다.",
                  "电话、即时通讯或在线申请均可，我们会在诊疗时间内与您联系。"))}

<section class="contact" style="padding-top:60px">
  <div class="wrap contact-grid">
    <div class="reveal">
      {tx("div", T("Clinic", "병원 정보", "医院信息"), "kicker")}
      <a class="tel" href="tel:+82322523210">+82 32 252 3210</a>
      <div class="tel-sub">032-252-3210 · FAX 032-252-3211 · drchoi119@gmail.com</div>
      <div class="status" id="status"><i></i><span id="statusText"></span></div>
      <dl class="info">
        <div class="info-row"><dt data-i18n="contact.address">Address</dt><dd data-i18n="contact.addressText">Sun Tower 3F, Inspire Entertainment Resort<br>127 Gonghang-munhwa-ro, Jung-gu, Incheon, Korea</dd></div>
        <div class="info-row"><dt data-i18n="contact.hours">Hours</dt><dd class="hours" id="hours"></dd></div>
        <div class="info-row"><dt data-i18n="contact.messenger">Messenger</dt><dd class="chips"><span>KakaoTalk</span><span>LINE</span><span>WhatsApp</span><span>WeChat</span></dd></div>
      </dl>
      <div class="qr-row" id="messengers">
        <figure class="qr"><img src="images/qr-kakao.png" alt="KakaoTalk QR" loading="lazy" onerror="this.parentNode.remove()"><figcaption>KakaoTalk</figcaption></figure>
        <figure class="qr"><img src="images/qr-line.png" alt="LINE QR" loading="lazy" onerror="this.parentNode.remove()"><figcaption>LINE</figcaption></figure>
        <figure class="qr"><img src="images/qr-whatsapp.png" alt="WhatsApp QR" loading="lazy" onerror="this.parentNode.remove()"><figcaption>WhatsApp</figcaption></figure>
        <figure class="qr"><img src="images/qr-wechat.png" alt="WeChat QR" loading="lazy" onerror="this.parentNode.remove()"><figcaption>WeChat</figcaption></figure>
      </div>
      {tx("p", T("On a phone? Tap a QR code to enlarge it, then scan it from another device or save the image.", "휴대폰으로 보고 계신가요? QR 코드를 누르면 크게 보입니다. 다른 기기로 스캔하거나 이미지를 저장해 앱에서 불러오세요.", "正在用手机浏览？点击二维码可放大，用其他设备扫描或保存图片后在应用中识别。"), "qr-hint")}
    </div>
    <form class="form reveal" id="form" novalidate>
      <h3 data-i18n="form.title">Online Consultation</h3>
      <p data-i18n="form.sub">We will contact you during clinic hours.</p>
      <div class="two">
        <div class="field"><label for="fName" data-i18n="form.name">Name</label><input id="fName" autocomplete="name" enterkeyhint="next"></div>
        <div class="field"><label for="fTel" data-i18n="form.phone">Phone / Messenger ID</label><input id="fTel" type="text" autocomplete="tel" enterkeyhint="next"></div>
      </div>
      <div class="two">
        <div class="field"><label for="fCat" data-i18n="form.interest">Interest</label><select id="fCat"></select></div>
        <div class="field"><label for="fLang" data-i18n="form.lang">Preferred Language</label><select id="fLang"><option>English</option><option>한국어</option><option>中文</option></select></div>
      </div>
      <div class="field"><label for="fMsg" data-i18n="form.msg">Message</label><textarea id="fMsg" rows="3"></textarea></div>
      <label class="agree"><input type="checkbox" id="fAgree"><span data-i18n="form.agree">I agree to the collection and use of my name and contact details for consultation purposes. (Required)</span></label>
      <button class="btn" type="submit"><span data-i18n="form.submit">Request Consultation</span>{ARROW}</button>
      <div class="form-msg" id="formMsg" role="status"></div>
    </form>
  </div>
</section>

<section class="section white">
  <div class="wrap">
    {sec_head(T("Location", "위치", "位置"), T("Finding us", "찾아오시는 길", "如何到达"),
              T("Inspire Entertainment Resort, Sun Tower 3F — near Incheon International Airport. For transport details, please call us.",
                "인스파이어 엔터테인먼트 리조트 선타워 3층, 인천국제공항 인근입니다. 교통편은 전화로 안내해 드립니다.",
                "Inspire娱乐度假村 Sun Tower 3层，靠近仁川国际机场。交通方式请致电咨询。"))}
    <div class="map reveal"><iframe title="Map" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
      src="https://www.google.com/maps?q=%EC%9D%B8%EC%8A%A4%ED%8C%8C%EC%9D%B4%EC%96%B4+%EC%97%94%ED%84%B0%ED%85%8C%EC%9D%B8%EB%A8%BC%ED%8A%B8+%EB%A6%AC%EC%A1%B0%ED%8A%B8&output=embed"></iframe></div>
    <div class="map-links reveal">
      <a href="https://map.naver.com/p/search/%EC%9D%B8%EC%8A%A4%ED%8C%8C%EC%9D%B4%EC%96%B4%20%EC%97%94%ED%84%B0%ED%85%8C%EC%9D%B8%EB%A8%BC%ED%8A%B8%20%EB%A6%AC%EC%A1%B0%ED%8A%B8" target="_blank" rel="noopener">Naver Map</a>
      <a href="https://map.kakao.com/?q=%EC%9D%B8%EC%8A%A4%ED%8C%8C%EC%9D%B4%EC%96%B4%20%EC%97%94%ED%84%B0%ED%85%8C%EC%9D%B8%EB%A8%BC%ED%8A%B8%20%EB%A6%AC%EC%A1%B0%ED%8A%B8" target="_blank" rel="noopener">Kakao Map</a>
      <a href="https://www.google.com/maps/search/?api=1&amp;query=Inspire+Entertainment+Resort+Incheon" target="_blank" rel="noopener">Google Maps</a>
    </div>
  </div>
</section>'''
    page("contact.html", "contact", T("Contact", "오시는 길", "联系我们"),
         "Contact Midas Clinic Inspire: +82 32 252 3210. Sun Tower 3F, Inspire Entertainment Resort, Incheon.", body)


# =====================================================================
# Media (기사 · 동영상)
#   VIDEOS: ("YouTube 영상 ID", T(제목), "YYYY-MM-DD")
#           예) https://www.youtube.com/watch?v=AbCdEf12345  →  "AbCdEf12345"
#   PRESS:  (T(기사 제목), "매체명", "YYYY-MM-DD", "기사 URL")
# =====================================================================
VIDEOS = [
    # 기존 홈페이지 동영상 게시판(총 14편) 순서 · 제목 기준. 새 영상은 맨 위에 추가
    ("2ECnLkCL7Z4", T("Mid-face SMAS lifting", "중안면 스마스 리프팅", "中面部SMAS提升"), ""),
    ("rHHxLysGtLw", T("Rhinoplasty using Rib Cartilage", "가슴연골을 이용한 코성형수술", "肋软骨隆鼻手术"), ""),
    ("jXXz-rf2PZo", T("Autologous cartilage rhinoplasty", "자가연골 코성형", "自体软骨隆鼻"), ""),
    ("QEXCBkwSdHI", T("Natural youthful-face surgery", "동안수술", "童颜手术"), ""),
    ("E5QL126AQPA", T("Making a beautiful nose · Doctor Life", "예쁜코 만들기 · 닥터라이프", "打造美鼻 · Doctor Life"), ""),
    ("v1Zx3usdkug", T("Nose reconstruction using rib cartilage", "가슴연골을 이용한 코 재건술", "肋软骨鼻重建"), ""),
    ("K4JvVd5wjCk", T("Congenital and acquired nose reconstruction", "선천성 및 후천성 코재건술", "先天性与后天性鼻重建"), ""),
    ("mddvpham3hg", T("Autologous rib cartilage in nose reconstruction", "코재건술에 사용되는 (자가)가슴연골", "鼻重建中使用的自体肋软骨"), ""),
    ("yCliYaUxtCM", T("Materials for nose reconstruction: rib cartilage", "코재건술에 사용되는 재료들 – 가슴연골", "鼻重建材料：肋软骨"), ""),
    ("nm3iPItbjEU", T("The ideal nose — who is a candidate for nose reconstruction?", "이상적인 코의 모양, 과연 어떤 사람들이 코재건술 수술대상인가?", "理想的鼻型——哪些人适合鼻重建？"), ""),
    ("KonXhnkdf80", T("What is nose reconstruction? · TV Doctor", "코재건술이란 무엇인가 · TV닥터", "什么是鼻重建？· TV医生"), ""),
    ("GwVnHXa72_U", T("Rhinoplasty using Rib Cartilage", "가슴연골을 이용한 코성형", "肋软骨隆鼻"), ""),
    ("yM99I7L0YEA", T("Rib Cartilage Rhinoplasty", "가슴연골 코수술", "肋软骨隆鼻手术"), ""),
    ("8lM00noyg0g", T("23rd World Miss University contestants visit the clinic", "제23회 월드미스유니버시티 참가자 내원", "第23届世界大学小姐参赛者到访"), ""),
]
PRESS = [
]


def media():
    if VIDEOS:
        vids = '<div class="video-grid">' + "".join(
            f'''<figure class="video reveal"><button class="yt" data-id="{vid}" aria-label="Play">
  <img src="https://i.ytimg.com/vi/{vid}/hqdefault.jpg" alt="" loading="lazy" onerror="this.style.visibility='hidden'"><span class="play"></span></button>
  <figcaption>{tx("span", title)}<small>{date}</small></figcaption></figure>'''
            for vid, title, date in VIDEOS) + "</div>"
    else:
        vids = tx("p", T("Videos are being prepared.", "영상을 준비하고 있습니다.", "视频正在准备中。"), "empty reveal")
    if PRESS:
        press = '<div class="press-list">' + "".join(
            f'''<a class="press reveal" href="{url}" target="_blank" rel="noopener"><span class="date">{date}</span>
  {tx("span", title, "ttl")}<span class="outlet">{outlet}</span>{ARROW}</a>'''
            for title, outlet, date, url in PRESS) + "</div>"
    else:
        press = tx("p", T("Articles are being prepared.", "기사를 준비하고 있습니다.", "报道正在准备中。"), "empty reveal")
    body = f'''{page_hero(T("Media", "미디어", "媒体"), T("Media", "미디어", "媒体"),
                T("Midas in<br><em>the media</em>", "미디어 속<br>미다스", "媒体中的<br>美达斯"),
                T("Videos and press coverage of Midas Clinic and Dr. Seungho Choi.",
                  "미다스의원과 최승호 대표원장의 영상과 언론 보도입니다.",
                  "美达斯医院与崔承浩院长的视频与媒体报道。"))}

<section class="section" id="videos">
  <div class="wrap">
    {sec_head(T("Videos", "동영상", "视频"), T("Watch", "영상으로 보기", "观看视频"))}
    {vids}
  </div>
</section>

<section class="section alt" id="press">
  <div class="wrap">
    {sec_head(T("Press", "언론 보도", "媒体报道"), T("In the news", "언론 보도", "新闻报道"))}
    {press}
  </div>
</section>

{cta_band()}'''
    page("media.html", "media", T("Media", "미디어", "媒体"),
         "Videos and press coverage of Midas Clinic Inspire and Dr. Seungho Choi.", body)


# =====================================================================
# Before & After (코성형 전후 사례) — images/results/caseNN-before.jpg / -after.jpg
# =====================================================================
NOSE_CAP = T("Rhinoplasty", "코성형", "鼻整形")
# (파일 접두어, 분야, 설명)
RESULTS = [(f"case{n:02d}", "nose", T("Rhinoplasty · side view", "코성형 · 측면", "鼻整形 · 侧面") if n == 18 else NOSE_CAP) for n in range(1, 19)] + [
    ("lift01", "lift", T("Lower eyelid + mid-face SMAS lift · 2 weeks after (swelling remains)", "하안검 + 중안면 SMAS 리프팅 · 수술 후 2주 (붓기 남아 있음)", "下眼睑 + 中面部SMAS提升 · 术后2周（仍有肿胀）")),
    ("lift02", "lift", T("Mid-face SMAS lift · long-term: surgery at 40, photo 8 years later", "중안면 SMAS 리프팅 · 장기 경과: 40세 수술, 8년 후 사진", "中面部SMAS提升 · 长期效果：40岁手术，8年后照片")),
    ("lift03", "lift", T("Mid-face SMAS lift · 1 week after", "중안면 SMAS 리프팅 · 수술 후 1주", "中面部SMAS提升 · 术后1周")),
    ("lift04", "lift", T("Lower eyelid + mid-face SMAS lift · 2 weeks after", "하안검 + 중안면 SMAS 리프팅 · 수술 후 2주", "下眼睑 + 中面部SMAS提升 · 术后2周")),
    ("lift05", "lift", T("Same patient, oblique view · 2 weeks after", "같은 환자 측면 · 수술 후 2주", "同一患者侧面 · 术后2周")),
    ("lift06", "lift", T("Forehead lift · 1 month after (incision line marked)", "포헤드(이마) 리프팅 · 수술 후 1개월 (봉합선 표시)", "额头提升 · 术后1个月（标注缝合线）")),
    ("lift07", "lift", T("Neck SMAS lift · jaw and neck line, side view", "목 SMAS 리프팅 · 턱·목 라인 측면", "颈部SMAS提升 · 下颌与颈部线条侧面")),
    ("lift08", "lift", T("Face lift · jowl and jawline, oblique view", "안면거상 · 턱선·볼 처짐, 사선 측면", "面部提升 · 下颌线与脸颊下垂，斜侧面")),
] + [(f"eye{n:02d}", "eye", T("Ptosis correction", "안검하수 (눈매교정)", "上睑下垂矫正") if n == 6 else T("Eye surgery", "눈성형", "眼部整形")) for n in range(1, 9)] + [
    ("breast01", "breast", T("Stem-cell breast augmentation · reconstruction · side view", "줄기세포 가슴확대·재건 · 측면", "干细胞丰胸·乳房重建 · 侧面")),
    ("breast02", "breast", T("Stem-cell breast augmentation · reconstruction · side view", "줄기세포 가슴확대·재건 · 측면", "干细胞丰胸·乳房重建 · 侧面")),
    ("breast03", "breast", T("Stem-cell breast augmentation · reconstruction · front view", "줄기세포 가슴확대·재건 · 정면", "干细胞丰胸·乳房重建 · 正面")),
    ("breast04", "breast", T("Stem-cell breast augmentation · reconstruction · front view", "줄기세포 가슴확대·재건 · 정면", "干细胞丰胸·乳房重建 · 正面")),
    ("breast05", "breast", T("Stem-cell breast augmentation · reconstruction · oblique view", "줄기세포 가슴확대·재건 · 사선 측면", "干细胞丰胸·乳房重建 · 斜侧面")),
    ("skin01", "face", T("Nasolabial fold filler", "팔자주름 필러", "法令纹填充")),
    ("lip01", "face", T("Cheek filler", "볼 필러", "面颊填充")),
    ("chin01", "face", T("Chin filler · side view", "턱 필러 · 측면", "下巴填充 · 侧面")),
    ("fore01", "face", T("Hair transplant · hairline", "모발이식 · 헤어라인", "植发 · 发际线")),
]
BA_CATS = [("all", T("All", "전체", "全部")), ("nose", T("Nose", "코성형", "鼻整形")), ("eye", T("Eye", "눈성형", "眼部整形")), ("lift", T("Lifting", "리프팅", "面部提升")),
           ("breast", T("Breast", "가슴", "胸部")), ("face", T("Filler · Hair", "필러 · 모발이식", "填充 · 植发"))]
# 사진 모양: 기본은 720x619, 아래 항목은 정사각형 / 원형
BA_SQUARE = {"breast01": 640, "breast02": 640, "breast03": 600, "breast04": 600, "breast05": 600, "fore01": 640}
BA_ROUND = {"skin01": 480, "lip01": 480, "chin01": 480}
BA_NOTICE = T("These photos are of actual patients, shared with consent. Results differ from person to person and are not a guarantee of outcome. All surgery carries possible risks such as bleeding, infection, swelling, asymmetry and scarring.",
              "아래 사진은 동의를 받은 실제 환자의 사례입니다. 수술 결과는 개인에 따라 다르며, 같은 결과를 보장하지 않습니다. 모든 수술에는 출혈·감염·부종·비대칭·흉터 등의 부작용이 발생할 수 있습니다.",
              "以下照片为经本人同意的真实患者案例。手术效果因人而异，不代表能获得相同效果。所有手术均可能出现出血、感染、肿胀、不对称或疤痕等副作用。")


def ba_card(key, cat, cap, idx):
    size = BA_SQUARE.get(key) or BA_ROUND.get(key)
    wh = (960, 240) if cat == "eye" else (size, size) if size else (720, 619)
    shape = " wide" if cat == "eye" else " round" if key in BA_ROUND else ""
    return f'''<figure class="ba reveal{shape}" data-cat="{cat}">
  <div class="ba-frame" style="--pos:50%;aspect-ratio:{wh[0]}/{wh[1]}">
    <img class="ba-after" src="images/results/{key}-after.jpg" alt="Case {idx:02d} after" loading="lazy" width="{wh[0]}" height="{wh[1]}">
    <img class="ba-before" src="images/results/{key}-before.jpg" alt="Case {idx:02d} before" loading="lazy" width="{wh[0]}" height="{wh[1]}">
    <span class="ba-tag l">Before</span><span class="ba-tag r">After</span>
    <span class="ba-handle" aria-hidden="true"></span>
    <input class="ba-range" type="range" min="0" max="100" value="50" aria-label="Compare before and after">
  </div>
  <figcaption><b>Case {idx:02d}</b>{tx("span", cap)}</figcaption>
</figure>'''


def ba_gallery(keys=None, filters=False):
    items = [(i, k, c, cap) for i, (k, c, cap) in enumerate(RESULTS, 1) if keys is None or k in keys]
    cards = "".join(ba_card(k, c, cap, i) for i, k, c, cap in items)
    chips = ""
    if filters:
        chips = '<div class="ba-filter" role="tablist">' + "".join(
            f'<button type="button" class="chip{" on" if key == "all" else ""}" data-f="{key}">{tx("span", label)}<small>{len(RESULTS) if key == "all" else sum(1 for r in RESULTS if r[1] == key)}</small></button>'
            for key, label in BA_CATS) + "</div>"
    return f'''{chips}<div class="ba-wrap" data-ba-gate>
    <div class="ba-grid">{cards}</div>
    <div class="ba-gate">
      <div class="ba-gate-box">
        {tx("div", T("Before &amp; After", "전후 사진", "术前术后"), "kicker")}
        {tx("p", BA_NOTICE)}
        <button type="button" class="btn ba-open">{tx("span", T("I understand — view photos", "확인했습니다 · 사진 보기", "我已了解 · 查看照片"))}</button>
      </div>
    </div>
  </div>'''


def results():
    body = f'''{page_hero(T("Before &amp; After", "전후 사진", "术前术后"), T("Before &amp; After", "전후 사진", "术前术后"),
                T("Case<br><em>gallery</em>", "수술<br>전후 사례", "手术<br>案例"),
                T("Nose, eye, lifting, breast, filler and hair transplant cases. Drag the line on each photo to compare before and after.",
                  "코성형·눈성형·리프팅·가슴·필러·모발이식 전후 사진입니다. 사진 가운데 선을 좌우로 움직여 비교해 보세요.",
                  "鼻整形、眼部整形、面部提升、胸部、填充与植发案例。左右拖动照片中间的线对比术前术后。"))}

<section class="section">
  <div class="wrap">
    {ba_gallery(filters=True)}
    {tx("div", BA_NOTICE, "notice reveal")}
  </div>
</section>

{cta_band(interest=0)}'''
    page("results.html", "procedures", T("Before &amp; After", "전후 사진", "术前术后"),
         "Before and after case gallery — nose, eye, lifting, breast, filler and hair transplant — Midas Clinic Inspire.", body)


if __name__ == "__main__":
    media()
    results()
    about()
    procedures()
    for c in CATS:
        detail_page(c)
    global_care()
    experience()
    contact()

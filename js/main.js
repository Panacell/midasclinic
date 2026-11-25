/* =========================================================
   MIDAS CLINIC · INSPIRE — main.js
   - i18n (EN / KO / ZH)
   - header, drawer, language menu
   - hero slider, procedures tabs/accordion
   - opening status, reveal, consultation form
   ========================================================= */
(function () {
  'use strict';

  /* ---------------------------------------------------------
     1. Translations
     --------------------------------------------------------- */
  var I18N = {
    en: {
      'nav.about': 'About', 'nav.procedures': 'Procedures', 'nav.global': 'Global Care',
      'nav.experience': 'Inspire Experience', 'nav.contact': 'Contact', 'nav.media': 'Media', 'nav.cell': 'Cell',
      'cta.consult': 'Consultation', 'cta.book': 'Book a Consultation', 'cta.explore': 'Explore Procedures', 'cta.call': 'Call',

      'hero1.kicker': 'Premium Plastic Surgery',
      'hero1.title': 'A Global Aesthetic<br>Destination at Inspire',
      'hero1.text': 'World-class plastic surgery in Korea,<br>with seamless travel and exceptional care.',
      'hero2.kicker': 'Signature Rhinoplasty',
      'hero2.title': 'The Art of<br>the Profile',
      'hero2.text': 'From rib-cartilage reconstruction to revision,<br>designed for both line and breath.',
      'hero3.kicker': 'Lifting · Anti-aging',
      'hero3.title': 'Lift, Not Change',
      'hero3.text': 'SMAS-level lifting that restores,<br>never replaces, who you are.',

      'std.kicker': 'The Midas Standard',
      'std.title': 'Natural Refinement,<br>Lasting Confidence',
      'std.text': 'Personalized aesthetic care by a Korean specialist, for results that are naturally beautiful and uniquely you.',
      'std.link': 'Our Philosophy',

      'f1.title': 'Global Care', 'f1.text': 'Multilingual consultation<br>and international coordination',
      'f2.title': 'Easy Travel', 'f2.text': 'Convenient access at<br>Incheon Inspire',
      'f3.title': 'Premium &amp; Private', 'f3.text': 'Discreet, comfortable care<br>in a world-class setting',

      'exp.kicker': 'Inspire Experience',
      'exp.title': 'A Refined<br>Healing Journey',
      'exp.text': 'From consultation to recovery, experience premium care in a vibrant, cosmopolitan environment at Inspire.',
      'exp.link': 'Explore the Experience',

      'proc.kicker': 'Procedures', 'proc.title': 'Tailored Care for<br>Your Natural Beauty',
      'tab.face': 'Face', 'tab.body': 'Body', 'tab.skin': 'Skin',

      'dir.kicker': 'Our Director', 'dir.title': 'Expertise<br>You Can <em>Trust</em>',
      'dir.name': 'Seungho Choi, M.D.', 'dir.role': 'Representative Director',
      'dir.quote': '“Never settled on one method — every face deserves the safest, most refined answer.”',

      'contact.kicker': 'Contact', 'contact.title': 'Begin Your<br><em>Consultation</em>',
      'contact.address': 'Address', 'contact.hours': 'Hours', 'contact.messenger': 'Messenger',
      'contact.addressText': 'Sun Tower 3F, Inspire Entertainment Resort<br>127 Gonghang-munhwa-ro, Jung-gu, Incheon, Korea',

      'form.title': 'Online Consultation', 'form.sub': 'We will contact you during clinic hours.',
      'form.name': 'Name', 'form.phone': 'Phone / Messenger ID', 'form.interest': 'Interest',
      'form.lang': 'Preferred Language', 'form.msg': 'Message',
      'form.agree': 'I agree to the collection and use of my name and contact details for consultation purposes. (Required)',
      'form.submit': 'Request Consultation',
      'form.errFields': 'Please enter your name and phone or messenger ID.',
      'form.errAgree': 'Please agree to the privacy terms.',
      'form.notReady': 'Online booking is being prepared. Please call <b>+82 32 252 3210</b> or message us on KakaoTalk, LINE, WhatsApp or WeChat.',
      'form.ok': 'Thank you. We will contact you during clinic hours.',
      'form.fail': 'Sending failed. Please call <b>+82 32 252 3210</b>.',

      'footer.addr': 'Inspire Entertainment Resort<br>Incheon, Korea',
      'footer.notice': '※ Results vary by individual. All procedures carry risks such as bleeding, infection, swelling, asymmetry or scarring.',

      'hours.wk': 'Mon–Fri', 'hours.sat': 'Saturday', 'hours.lunch': 'Lunch',
      'status.open': 'Open now · until ', 'status.lunch': 'Lunch break · back at 13:00', 'status.closed': 'Closed now'
    },

    ko: {
      'nav.about': '병원소개', 'nav.procedures': '진료안내', 'nav.global': '글로벌 케어',
      'nav.experience': '인스파이어 경험', 'nav.contact': '오시는 길', 'nav.media': '미디어', 'nav.cell': '세포',
      'cta.consult': '상담 예약', 'cta.book': '상담 예약하기', 'cta.explore': '진료 안내 보기', 'cta.call': '전화',

      'hero1.kicker': 'Premium Plastic Surgery',
      'hero1.title': '인스파이어에서 만나는<br>글로벌 에스테틱',
      'hero1.text': '세계 어디에서 오셔도 편안하게.<br>인천국제공항 곁, 프리미엄 맞춤 성형.',
      'hero2.kicker': 'Signature Rhinoplasty',
      'hero2.title': '라인과 호흡을<br>함께 설계하는 코',
      'hero2.text': '늑연골 구조 재건부터 코 재수술까지,<br>아름다움과 기능을 함께 완성합니다.',
      'hero3.kicker': 'Lifting · Anti-aging',
      'hero3.title': '얼굴은 그대로,<br>시간만 되돌리다',
      'hero3.text': '근막(SMAS)층부터 끌어올리는<br>자연스러운 리프팅.',

      'std.kicker': 'The Midas Standard',
      'std.title': '자연스러운 변화,<br>오래가는 자신감',
      'std.text': '유행이 아닌 한 사람의 골격과 인상을 존중합니다. (구)선이고은 성형외과의 철학을 이어, 꼭 필요한 수술만 정직하게 권합니다.',
      'std.link': '진료 철학',

      'f1.title': '글로벌 케어', 'f1.text': '다국어 상담 채널과<br>해외 고객 일정 조율',
      'f2.title': '편리한 접근성', 'f2.text': '인천국제공항 인근<br>인스파이어 리조트',
      'f3.title': '프리미엄 · 프라이빗', 'f3.text': '다른 고객과 마주치지 않는<br>프라이빗한 진료 동선',

      'exp.kicker': 'Inspire Experience',
      'exp.title': '세련된<br>회복의 여정',
      'exp.text': '상담부터 회복까지, 인스파이어 엔터테인먼트 리조트 선타워 3층에서 편안하고 세련된 진료를 경험하세요.',
      'exp.link': '방문 안내',

      'proc.kicker': 'Procedures', 'proc.title': '한 사람을 위한<br>맞춤 진료',
      'tab.face': '얼굴', 'tab.body': '바디', 'tab.skin': '피부',

      'dir.kicker': 'Our Director', 'dir.title': '믿을 수 있는<br><em>전문성</em>',
      'dir.name': '최승호 대표원장', 'dir.role': 'Representative Director',
      'dir.quote': '“한 가지 자격과 경험에 머무르지 않고, 더 아름답고 안전한 결과를 위해 매 순간 배우고 연구합니다.”',

      'contact.kicker': 'Contact', 'contact.title': '상담을<br><em>시작하세요</em>',
      'contact.address': '주소', 'contact.hours': '진료시간', 'contact.messenger': '메신저',
      'contact.addressText': '인천광역시 중구 공항문화로 127<br>인스파이어 엔터테인먼트 리조트 선타워 3층',

      'form.title': '온라인 상담 신청', 'form.sub': '남겨주신 연락처로 진료시간 내 연락드립니다.',
      'form.name': '성함', 'form.phone': '연락처 / 메신저 ID', 'form.interest': '관심 분야',
      'form.lang': '상담 언어', 'form.msg': '문의 내용',
      'form.agree': '[필수] 상담을 위한 개인정보(성함, 연락처) 수집·이용에 동의합니다. 수집된 정보는 상담 목적으로만 사용됩니다.',
      'form.submit': '상담 신청하기',
      'form.errFields': '성함과 연락처를 입력해 주세요.',
      'form.errAgree': '개인정보 수집·이용에 동의해 주세요.',
      'form.notReady': '온라인 접수는 준비 중입니다. 전화 <b>032-252-3210</b> 또는 카카오톡으로 문의해 주세요.',
      'form.ok': '상담 신청이 접수되었습니다. 진료시간 내 연락드리겠습니다.',
      'form.fail': '전송에 실패했습니다. 전화 <b>032-252-3210</b>으로 문의해 주세요.',

      'footer.addr': '인스파이어 엔터테인먼트 리조트<br>인천, 대한민국',
      'footer.notice': '※ 모든 수술 및 시술은 개인에 따라 결과가 다를 수 있으며 출혈·감염·부종·비대칭·흉터 등의 부작용이 발생할 수 있습니다.',

      'hours.wk': '평일', 'hours.sat': '토요일', 'hours.lunch': '점심',
      'status.open': '진료 중 · ', 'status.lunch': '점심시간 · 13:00 진료 재개', 'status.closed': '진료 종료'
    },

    zh: {
      'nav.about': '关于我们', 'nav.procedures': '诊疗项目', 'nav.global': '国际关怀',
      'nav.experience': 'Inspire 体验', 'nav.contact': '联系我们', 'nav.media': '媒体', 'nav.cell': '细胞',
      'cta.consult': '预约咨询', 'cta.book': '预约咨询', 'cta.explore': '查看诊疗项目', 'cta.call': '致电',

      'hero1.kicker': 'Premium Plastic Surgery',
      'hero1.title': 'Inspire<br>全球美学目的地',
      'hero1.text': '韩国高端整形外科，<br>便捷出行，悉心照护。',
      'hero2.kicker': 'Signature Rhinoplasty',
      'hero2.title': '兼顾线条与呼吸的<br>鼻整形',
      'hero2.text': '从肋软骨结构重建到鼻修复，<br>美观与功能兼得。',
      'hero3.kicker': 'Lifting · Anti-aging',
      'hero3.title': '不改变你，<br>只留住时间',
      'hero3.text': '从筋膜（SMAS）层提升的<br>自然拉皮。',

      'std.kicker': 'The Midas Standard',
      'std.title': '自然蜕变，<br>持久自信',
      'std.text': '尊重每个人的骨骼与气质，而非追逐潮流。延续前身整形外科的理念，只诚实推荐真正需要的手术。',
      'std.link': '我们的理念',

      'f1.title': '国际关怀', 'f1.text': '多语种咨询渠道<br>海外行程协调',
      'f2.title': '交通便利', 'f2.text': '毗邻仁川国际机场<br>Inspire 度假村',
      'f3.title': '高端 · 私密', 'f3.text': '私密动线<br>舒适安心的诊疗环境',

      'exp.kicker': 'Inspire Experience',
      'exp.title': '精致的<br>恢复之旅',
      'exp.text': '从咨询到恢复，在 Inspire 娱乐度假村 Sun Tower 3层，体验舒适而精致的高端诊疗。',
      'exp.link': '来访指南',

      'proc.kicker': 'Procedures', 'proc.title': '为您量身定制的<br>自然之美',
      'tab.face': '面部', 'tab.body': '身体', 'tab.skin': '皮肤',

      'dir.kicker': 'Our Director', 'dir.title': '值得信赖的<br><em>专业</em>',
      'dir.name': 'Seungho Choi 代表院长', 'dir.role': 'Representative Director',
      'dir.quote': '“不止于一种资格与经验，为了更美、更安全的结果，时刻学习与钻研。”',

      'contact.kicker': 'Contact', 'contact.title': '开始您的<br><em>咨询</em>',
      'contact.address': '地址', 'contact.hours': '诊疗时间', 'contact.messenger': '即时通讯',
      'contact.addressText': '韩国仁川广域市中区机场文化路127<br>Inspire Entertainment Resort Sun Tower 3层',

      'form.title': '在线咨询', 'form.sub': '我们将在诊疗时间内与您联系。',
      'form.name': '姓名', 'form.phone': '电话 / 即时通讯ID', 'form.interest': '咨询项目',
      'form.lang': '咨询语言', 'form.msg': '咨询内容',
      'form.agree': '【必选】同意为咨询目的收集和使用本人姓名及联系方式。',
      'form.submit': '提交咨询',
      'form.errFields': '请输入姓名和联系方式。',
      'form.errAgree': '请同意个人信息收集与使用。',
      'form.notReady': '在线预约正在准备中。请致电 <b>+82 32 252 3210</b>，或通过微信、LINE、WhatsApp、KakaoTalk联系我们。',
      'form.ok': '咨询申请已提交，我们将在诊疗时间内与您联系。',
      'form.fail': '发送失败，请致电 <b>+82 32 252 3210</b>。',

      'footer.addr': 'Inspire Entertainment Resort<br>韩国 仁川',
      'footer.notice': '※ 手术效果因人而异，所有手术均可能出现出血、感染、肿胀、不对称或疤痕等副作用。',

      'hours.wk': '周一至周五', 'hours.sat': '周六', 'hours.lunch': '午休',
      'status.open': '营业中 · 至 ', 'status.lunch': '午休中 · 13:00恢复', 'status.closed': '已休诊'
    }
  };

  /* Procedures (Face / Body / Skin) — name and sub-items per language */
  var PROCEDURES = {
    face: [
      { icon: 'nose', en: ['Rhinoplasty', ['Rib Cartilage Rhinoplasty', 'Septoplasty', 'Revision Rhinoplasty', 'Male Rhinoplasty']],
        ko: ['코성형 · 코 재건', ['늑연골(가슴연골) 코성형', '비중격 만곡증 교정', '코 재수술', '남자 코성형']],
        zh: ['鼻整形 · 鼻重建', ['肋软骨隆鼻', '鼻中隔偏曲矫正', '鼻修复', '男士鼻整形']] },
      { icon: 'eye', en: ['Eye Surgery', ['Double Eyelid (Non-incision / Partial / Full incision)', 'Ptosis Correction', 'Epicanthoplasty / Lateral Canthoplasty', 'Upper / Lower Blepharoplasty']],
        ko: ['눈성형', ['매몰법 · 부분절개 · 절개법', '안검하수 (눈매교정)', '앞트임 · 뒤트임', '상안검 · 하안검']],
        zh: ['眼部整形', ['埋线 · 部分切开 · 全切开双眼皮', '上睑下垂矫正', '开内眼角 · 开外眼角', '上眼睑 · 下眼睑整形']] },
      { icon: 'lift', en: ['Lifting', ['Face Lift', 'Mid-face SMAS Lift', 'Sub-brow / Neck SMAS Lift', 'Cheek Lift · Forehead Lift']],
        ko: ['리프팅', ['안면거상', '중안면 SMAS 리프팅', '눈썹하 · 목 SMAS 리프팅', '볼 리프팅 · 포헤드 리프팅']],
        zh: ['提升', ['面部提升', '中面部SMAS提升', '眉下 · 颈部SMAS提升', '脸颊提升 · 额头提升']] },
      { icon: 'face', en: ['Facial Contouring', ['T-zone Contouring', '3D Fat Grafting', 'Gummy Smile Correction']],
        ko: ['윤곽 · 페이스', ['T존 성형', '3차원 입체 지방이식', '잇몸 성형']],
        zh: ['轮廓整形', ['T区整形', '3D立体脂肪移植', '露龈笑矫正']] }
    ],
    body: [
      { icon: 'body', en: ['Liposuction', ['Area-specific Liposuction']], ko: ['지방흡입', ['부위별 지방흡입']], zh: ['吸脂', ['局部吸脂']] },
      { icon: 'abdomen', en: ['Abdominoplasty', ['Tummy Tuck']], ko: ['복부 성형', ['늘어진 복부 피부 · 근막 정리']], zh: ['腹部整形', ['腹壁成形']] },
      { icon: 'breast', en: ['Breast Lift', ['Breast Ptosis Correction']], ko: ['유방 하수 교정', ['처진 가슴의 위치 · 형태 교정']], zh: ['乳房提升', ['乳房下垂矫正']] },
      { icon: 'breast', en: ['Stem Cell Breast Surgery', ['Stem Cell Breast Augmentation', 'Stem Cell Breast Reconstruction']], ko: ['줄기세포 유방 성형', ['줄기세포 유방 확대술', '줄기세포 유방 재건술']], zh: ['干细胞乳房整形', ['干细胞丰胸', '干细胞乳房重建']] },
      { icon: 'hair', en: ['Hair Transplant', ['Hairline & Density Design']], ko: ['모발이식', ['헤어라인 · 밀도 디자인']], zh: ['植发', ['发际线与密度设计']] }
    ],
    skin: [
      { icon: 'spark', en: ['Botox · Filler', ['Wrinkle Botox', 'Volume Filler']], ko: ['보톡스 · 필러', ['주름 보톡스', '볼륨 필러']], zh: ['肉毒素 · 玻尿酸', ['除皱肉毒素', '填充玻尿酸']] },
      { icon: 'ring', en: ['Skin Renewal', ['Deep Dermal Renewal', 'Pore Care', 'Skin Booster']], ko: ['피부 재생', ['피부 심부 재생', '모공', '물광주사']], zh: ['皮肤再生', ['深层皮肤再生', '毛孔管理', '水光针']] },
      { icon: 'spark', en: ['PRP · Super PRP', ['PRP · PMRP', 'Super PRP']], ko: ['PRP · 슈퍼 PRP', ['PRP · PMRP', '슈퍼 PRP']], zh: ['PRP · 超级PRP', ['PRP · PMRP', '超级PRP']] },
      { icon: 'dots', en: ['Pigment · Acne', ['Melasma · Freckles · Redness', 'Acne · Acne Scars']], ko: ['색소 · 여드름', ['기미 · 주근깨 · 안면홍조', '여드름 · 여드름흉터']], zh: ['色斑 · 痘痘', ['黄褐斑 · 雀斑 · 面部潮红', '痘痘 · 痘印']] }
    ]
  };
  var PROC_IMG = { face: 'images/standard-portrait.jpg', body: 'images/inspire-lounge.jpg', skin: 'images/standard-portrait.jpg' };

  var ICONS = {
    nose: '<path d="M17 4c-3 5-4 9-3 13 1 3 4 5 6 8-1 1-3 1-4 2"/><path d="M14 17c-1 2-3 3-5 3"/>',
    eye: '<path d="M3 16c4-6 9-8 13-8s9 2 13 8c-4 6-9 8-13 8S7 22 3 16z"/><circle cx="16" cy="16" r="4.5"/>',
    lift: '<path d="M8 27V9M16 27V7M24 27V9"/><path d="M5 12l3-3 3 3M13 10l3-3 3 3M21 12l3-3 3 3"/>',
    face: '<path d="M16 4c-6 0-9 5-9 11 0 7 4 13 9 13s9-6 9-13c0-6-3-11-9-11z"/><path d="M13 22c2 1.3 4 1.3 6 0"/>',
    body: '<path d="M11 4c1 5 0 8-2 11s-2 9 1 13M21 4c-1 5 0 8 2 11s2 9-1 13"/>',
    abdomen: '<rect x="9" y="5" width="14" height="22" rx="7"/><path d="M12 17h8"/>',
    breast: '<path d="M4 12c3 9 9 9 12 2 3 7 9 7 12-2"/>',
    hair: '<path d="M7 21c0-9 4-14 9-14s9 5 9 14"/><path d="M10 13c1-2 2-3 3-3M16 9v4M22 13c-1-2-2-3-3-3"/>',
    spark: '<path d="M16 4l3 8 8 1-6 5 2 9-7-5-7 5 2-9-6-5 8-1z"/>',
    ring: '<circle cx="16" cy="16" r="11"/><circle cx="16" cy="16" r="6"/>',
    dots: '<circle cx="16" cy="16" r="12"/><circle cx="11" cy="13" r="1.6"/><circle cx="20" cy="11" r="1.2"/><circle cx="18" cy="20" r="2"/>'
  };

  var CREDS = {
    en: ['Visiting Professor, The Catholic University of Korea College of Medicine · Medical Specialist',
         'Academic Director, Korean aesthetic surgery society (대한미용외과학회)',
         'IBCS-certified in Cosmetic Surgery (Europe)',
         'Member, American Society of Lipo-Suction Surgery · American Society of Hair Restoration Surgery · American cosmetic surgery society',
         'Member, European aesthetic medicine society · Balkan aesthetic surgery society',
         'Breast surgery & reconstruction training in the U.S. and Japan; aesthetic surgery training in Australia, the Philippines, Germany and Bulgaria'],
    ko: ['가톨릭의대 외래교수, 전문의', '대한미용외과학회 학술이사', '유럽 IBCS 미용외과 전문의',
         '미국미용외과학회 · 미국지방흡입학회 · 미국모발이식학회 정회원', '유럽미용의학학회 · 발칸미용외과학회 정회원',
         '미국 노스미시간·인디애나 주립대학, 일본 요코하마 유방성형·재건 연수 / 호주·필리핀·독일·불가리아 미용성형 연수'],
    zh: ['天主教大学医学院 客座教授、专科医生', '大韩美容外科学会 学术理事', '欧洲IBCS美容外科专科医生',
         '美国美容外科学会 · 美国吸脂学会 · 美国植发学会 正式会员', '欧洲美容医学学会 · 巴尔干美容外科学会 正式会员',
         '于美国、日本进修乳房整形与重建；于澳大利亚、菲律宾、德国、保加利亚进修美容整形']
  };

  var LANG_LABEL = { en: 'EN', ko: 'KR', zh: '中文' };
  var HTML_LANG = { en: 'en', ko: 'ko', zh: 'zh' };
  var current = 'en';

  function t(key) { return (I18N[current] && I18N[current][key]) || I18N.en[key] || ''; }

  /* ---------------------------------------------------------
     2. Render dynamic parts
     --------------------------------------------------------- */
  var procWrap = document.getElementById('procLists');
  var procImg = document.getElementById('procImg');
  var activeTab = 'face';

  function renderProcedures() {
    if (!procWrap) return;
    var html = '';
    Object.keys(PROCEDURES).forEach(function (tab) {
      html += '<div class="proc-list' + (tab === activeTab ? ' on' : '') + '" data-tab="' + tab + '">';
      PROCEDURES[tab].forEach(function (p, i) {
        var d = p[current] || p.en;
        html += '<div class="proc-item' + (i === 0 ? ' open' : '') + '">' +
          '<button type="button" aria-expanded="' + (i === 0) + '">' +
          '<svg class="ic" viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.1">' + ICONS[p.icon] + '</svg>' +
          '<span class="nm">' + d[0] + '</span>' +
          '<svg class="ar"><use href="#i-arrow"/></svg></button>' +
          '<div class="sub"><ul>' + d[1].map(function (s) { return '<li>' + s + '</li>'; }).join('') + '</ul></div></div>';
      });
      html += '</div>';
    });
    procWrap.innerHTML = html;
    procWrap.querySelectorAll('.proc-item > button').forEach(function (b) {
      b.addEventListener('click', function () {
        var item = b.parentNode, wasOpen = item.classList.contains('open');
        item.parentNode.querySelectorAll('.proc-item').forEach(function (x) {
          x.classList.remove('open'); x.firstElementChild.setAttribute('aria-expanded', 'false');
        });
        if (!wasOpen) { item.classList.add('open'); b.setAttribute('aria-expanded', 'true'); }
      });
    });
  }

  function renderCreds() {
    var el = document.getElementById('creds'); if (!el) return;
    el.innerHTML = (CREDS[current] || CREDS.en).map(function (c) { return '<li>' + c + '</li>'; }).join('');
  }

  function renderInterestOptions() {
    var sel = document.getElementById('fCat'); if (!sel) return;
    var keep = sel.selectedIndex;
    var opts = [];
    PROCEDURES.face.concat(PROCEDURES.body, PROCEDURES.skin).forEach(function (p) { opts.push((p[current] || p.en)[0]); });
    opts.push(current === 'ko' ? '기타' : current === 'zh' ? '其他' : 'Other');
    sel.innerHTML = opts.map(function (o) { return '<option>' + o + '</option>'; }).join('');
    if (keep > -1) sel.selectedIndex = keep;
    var q = (location.search.match(/[?&]interest=(\d+)/) || [])[1];
    if (q && keep < 1) sel.selectedIndex = +q;
  }

  function renderHours() {
    var el = document.getElementById('hours'); if (!el) { tick(); return; }
    el.innerHTML =
      '<span data-d="wk">' + t('hours.wk') + '</span><span data-d="wk">10:00 – 18:30</span>' +
      '<span data-d="sat">' + t('hours.sat') + '</span><span data-d="sat">10:00 – 16:00</span>' +
      '<span>' + t('hours.lunch') + '</span><span>12:00 – 13:00</span>';
    tick();
  }

  function setLang(lang) {
    if (!I18N[lang]) lang = 'en';
    current = lang;
    document.documentElement.lang = HTML_LANG[lang];
    document.querySelectorAll('[data-i18n]').forEach(function (el) {
      var v = t(el.getAttribute('data-i18n'));
      if (v) el.innerHTML = v;
    });
    /* sub pages: inline translations — English is the default text, data-ko / data-zh hold the others */
    document.querySelectorAll('[data-ko],[data-zh]').forEach(function (el) {
      if (el.dataset.en === undefined) el.dataset.en = el.innerHTML;
      el.innerHTML = lang === 'en' ? el.dataset.en : (el.getAttribute('data-' + lang) || el.dataset.en);
    });
    document.querySelectorAll('[data-ph-ko]').forEach(function (el) {
      if (el.dataset.phEn === undefined) el.dataset.phEn = el.getAttribute('placeholder') || '';
      el.setAttribute('placeholder', lang === 'en' ? el.dataset.phEn : (el.getAttribute('data-ph-' + lang) || el.dataset.phEn));
    });
    if (document.body.dataset.titleKo) {
      if (!document.body.dataset.titleEn) document.body.dataset.titleEn = document.title;
      document.title = lang === 'en' ? document.body.dataset.titleEn : (document.body.getAttribute('data-title-' + lang) || document.body.dataset.titleEn);
    }
    document.getElementById('langLabel').textContent = LANG_LABEL[lang];
    document.querySelectorAll('[data-lang]').forEach(function (b) { b.classList.toggle('on', b.dataset.lang === lang); });
    renderProcedures(); renderCreds(); renderInterestOptions(); renderHours();
    try { localStorage.setItem('midas-lang', lang); } catch (e) {}
  }

  /* ---------------------------------------------------------
     3. Header / drawer / language menu / quick bar / back-to-top
     --------------------------------------------------------- */
  var header = document.getElementById('header');
  var mbar = document.querySelector('.mobile-bar'), toTop = document.querySelector('.to-top');
  var lastY = window.scrollY, ticking = false;
  function onScroll() {
    var y = window.scrollY, down = y > lastY + 4, up = y < lastY - 4;
    header.classList.toggle('solid', y > 40);
    if (!document.body.classList.contains('lock')) {
      if (down && y > 220) header.classList.add('hide');
      else if (up || y < 220) header.classList.remove('hide');
    }
    if (toTop) toTop.classList.toggle('show', y > window.innerHeight * 1.2);
    if (Math.abs(y - lastY) > 4) lastY = y;
    ticking = false;
  }
  window.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
  onScroll();
  if (toTop) toTop.addEventListener('click', function (e) { e.preventDefault(); window.scrollTo({ top: 0, behavior: 'smooth' }); });

  /* hide the quick bar while typing in the form (keyboard open) */
  if (mbar) {
    document.addEventListener('focusin', function (e) { if (e.target.matches('input,select,textarea')) mbar.classList.add('hide'); });
    document.addEventListener('focusout', function () { mbar.classList.remove('hide'); });
  }

  var burger = document.getElementById('burger'), drawer = document.getElementById('drawer');
  function setDrawer(open) {
    drawer.classList.toggle('open', open); burger.classList.toggle('x', open);
    header.classList.toggle('menu-open', open); header.classList.remove('hide');
    document.body.classList.toggle('lock', open);
    burger.setAttribute('aria-expanded', open);
  }
  burger.addEventListener('click', function () { setDrawer(!drawer.classList.contains('open')); });
  drawer.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', function () { setDrawer(false); }); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { setDrawer(false); closeLightbox(); } });
  window.addEventListener('resize', function () { if (window.innerWidth > 1100 && drawer.classList.contains('open')) setDrawer(false); });
  var here = location.pathname.split('/').pop() || 'index.html';
  drawer.querySelectorAll('a[href]').forEach(function (a) { if (a.getAttribute('href') === here) a.classList.add('active'); });

  /* mobile home: the contact form is replaced by a short CTA block */
  document.querySelectorAll('a[href="#contact"]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      var m = document.getElementById('contact-m');
      if (m && getComputedStyle(m).display !== 'none') { e.preventDefault(); m.scrollIntoView({ behavior: 'smooth' }); }
    });
  });

  /* Before & After: compare slider + consent gate */
  document.querySelectorAll('.ba-frame').forEach(function (f) {
    var r = f.querySelector('.ba-range');
    function set(v) { f.style.setProperty('--pos', v + '%'); }
    r.addEventListener('input', function () { set(r.value); });
    /* also follow a drag that starts anywhere on the photo */
    f.addEventListener('pointerdown', function (e) {
      if (e.pointerType === 'mouse' && e.button !== 0) return;
      var rect = f.getBoundingClientRect();
      function move(ev) { var v = Math.max(0, Math.min(100, (ev.clientX - rect.left) / rect.width * 100)); r.value = v; set(v); }
      move(e);
      if (e.pointerType === 'mouse') {
        var up = function () { window.removeEventListener('pointermove', move); window.removeEventListener('pointerup', up); };
        window.addEventListener('pointermove', move); window.addEventListener('pointerup', up);
      }
    });
  });
  var chipsBa = [].slice.call(document.querySelectorAll('.ba-filter .chip'));
  function baFilter(f) {
    chipsBa.forEach(function (c) { c.classList.toggle('on', c.dataset.f === f); });
    document.querySelectorAll('.ba[data-cat]').forEach(function (b) { b.classList.toggle('hide', f !== 'all' && b.dataset.cat !== f); });
  }
  chipsBa.forEach(function (c) { c.addEventListener('click', function () { baFilter(c.dataset.f); }); });
  if (chipsBa.length && /^#(nose|eye|lift)$/.test(location.hash)) baFilter(location.hash.slice(1));
  var baOk = false;
  try { baOk = sessionStorage.getItem('midas-ba-ok') === '1'; } catch (e) {}
  document.querySelectorAll('[data-ba-gate]').forEach(function (w) {
    if (!baOk) w.classList.add('gated');
    var b = w.querySelector('.ba-open');
    if (b) b.addEventListener('click', function () {
      document.querySelectorAll('[data-ba-gate]').forEach(function (x) { x.classList.remove('gated'); });
      try { sessionStorage.setItem('midas-ba-ok', '1'); } catch (e) {}
    });
  });

  /* QR codes: tap / click to enlarge */
  var lb = null;
  function closeLightbox() { if (lb) lb.classList.remove('open'); document.body.classList.remove('lock'); }
  document.querySelectorAll('.qr img, .qr-card img').forEach(function (img) {
    img.addEventListener('click', function () {
      if (!lb) {
        lb = document.createElement('div'); lb.className = 'lightbox'; lb.setAttribute('role', 'dialog');
        lb.innerHTML = '<button type="button" aria-label="Close">×</button><img alt=""><p></p>';
        lb.addEventListener('click', function (e) { if (e.target === lb || e.target.tagName === 'BUTTON') closeLightbox(); });
        document.body.appendChild(lb);
      }
      lb.querySelector('img').src = img.src;
      var cap = img.closest('.qr, .qr-card').querySelector('figcaption, h3');
      lb.querySelector('p').textContent = cap ? cap.textContent : '';
      lb.classList.add('open'); document.body.classList.add('lock');
    });
  });

  var langBox = document.getElementById('lang'), langBtn = document.getElementById('langBtn');
  langBtn.addEventListener('click', function (e) {
    e.stopPropagation();
    var open = langBox.classList.toggle('open');
    langBtn.setAttribute('aria-expanded', open);
  });
  document.addEventListener('click', function () { langBox.classList.remove('open'); langBtn.setAttribute('aria-expanded', 'false'); });
  document.querySelectorAll('[data-lang]').forEach(function (b) { b.addEventListener('click', function () { setLang(b.dataset.lang); }); });

  /* ---------------------------------------------------------
     4. Hero slider
     --------------------------------------------------------- */
  var slides = [].slice.call(document.querySelectorAll('.hero-slide'));
  if (slides.length > 1) (function () {
  var dots = [].slice.call(document.querySelectorAll('#heroDots button'));
  var idx = 0, timer;
  function go(n) {
    idx = (n + slides.length) % slides.length;
    slides.forEach(function (s, i) { s.classList.toggle('on', i === idx); });
    dots.forEach(function (d, i) { d.classList.toggle('on', i === idx); });
    clearTimeout(timer); timer = setTimeout(function () { go(idx + 1); }, 6500);
  }
  dots.forEach(function (d, i) { d.addEventListener('click', function () { go(i); }); });
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!reduce) timer = setTimeout(function () { go(1); }, 6500);
  document.addEventListener('visibilitychange', function () { if (document.hidden) clearTimeout(timer); else if (!reduce) go(idx); });
  var hero = document.querySelector('.hero'), sx = 0, sy = 0;
  if (hero) {
    hero.addEventListener('touchstart', function (e) { sx = e.touches[0].clientX; sy = e.touches[0].clientY; }, { passive: true });
    hero.addEventListener('touchend', function (e) {
      var dx = e.changedTouches[0].clientX - sx, dy = e.changedTouches[0].clientY - sy;
      if (Math.abs(dx) > 50 && Math.abs(dx) > Math.abs(dy) * 1.5) go(idx + (dx < 0 ? 1 : -1));
    }, { passive: true });
  }
  })();

  /* ---------------------------------------------------------
     5. Procedure tabs
     --------------------------------------------------------- */
  var tabs = [].slice.call(document.querySelectorAll('.tab'));
  if (procImg)
  tabs.forEach(function (tab) {
    tab.addEventListener('click', function () {
      activeTab = tab.dataset.tab;
      tabs.forEach(function (x) { x.classList.toggle('on', x === tab); });
      procWrap.querySelectorAll('.proc-list').forEach(function (l) { l.classList.toggle('on', l.dataset.tab === activeTab); });
      if (procImg.getAttribute('src') !== PROC_IMG[activeTab]) procImg.src = PROC_IMG[activeTab];
    });
  });

  /* ---------------------------------------------------------
     6. Opening status (KST)
     --------------------------------------------------------- */
  function tick() {
    if (!document.getElementById('status')) return;
    var d = new Date(Date.now() + 9 * 3600e3), day = d.getUTCDay(), m = d.getUTCHours() * 60 + d.getUTCMinutes();
    var wk = day >= 1 && day <= 5, sat = day === 6, end = wk ? 1110 : sat ? 960 : 0, open = false, label = t('status.closed');
    if ((wk || sat) && m >= 600 && m < end) {
      if (m >= 720 && m < 780) label = t('status.lunch');
      else { open = true; label = t('status.open') + (wk ? '18:30' : '16:00'); }
    }
    document.getElementById('status').classList.toggle('open', open);
    document.getElementById('statusText').textContent = label;
    document.querySelectorAll('#hours [data-d]').forEach(function (s) {
      s.classList.toggle('today', (s.dataset.d === 'wk' && wk) || (s.dataset.d === 'sat' && sat));
    });
  }
  setInterval(tick, 30000);

  /* YouTube: load the player only when clicked */
  document.querySelectorAll('.yt[data-id]').forEach(function (b) {
    b.addEventListener('click', function () {
      var f = document.createElement('iframe');
      f.src = 'https://www.youtube-nocookie.com/embed/' + b.dataset.id + '?autoplay=1&rel=0';
      f.allow = 'autoplay; encrypted-media; picture-in-picture'; f.allowFullscreen = true; f.title = 'Video';
      b.replaceWith(f);
    });
  });

  /* ---------------------------------------------------------
     7. Reveal on scroll
     --------------------------------------------------------- */
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { threshold: 0.12 });
    document.querySelectorAll('.reveal').forEach(function (el) { io.observe(el); });
  } else {
    document.querySelectorAll('.reveal').forEach(function (el) { el.classList.add('in'); });
  }

  /* ---------------------------------------------------------
     8. Consultation form
        접수 서버(또는 Formspree 등 폼 서비스) 주소를 ENDPOINT 에 넣으면 실제 전송됩니다.
     --------------------------------------------------------- */
  var ENDPOINT = '';
  var form = document.getElementById('form'), msg = document.getElementById('formMsg');
  if (form) form.addEventListener('submit', function (e) {
    e.preventDefault();
    msg.style.display = 'block';
    var name = document.getElementById('fName').value.trim(), tel = document.getElementById('fTel').value.trim();
    document.querySelectorAll('#form .field').forEach(function (f) { f.classList.remove('err'); });
    if (!name || !tel) {
      msg.innerHTML = t('form.errFields');
      var bad = !name ? 'fName' : 'fTel'; var el = document.getElementById(bad);
      el.parentNode.classList.add('err'); el.focus(); return;
    }
    if (!document.getElementById('fAgree').checked) { msg.innerHTML = t('form.errAgree'); return; }
    if (!ENDPOINT) { msg.innerHTML = t('form.notReady'); return; }
    fetch(ENDPOINT, {
      method: 'POST', headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
      body: JSON.stringify({ name: name, contact: tel, interest: document.getElementById('fCat').value,
        language: document.getElementById('fLang').value, message: document.getElementById('fMsg').value, site_lang: current })
    }).then(function (r) { if (!r.ok) throw new Error(); msg.innerHTML = t('form.ok'); form.reset(); })
      .catch(function () { msg.innerHTML = t('form.fail'); });
  });

  /* ---------------------------------------------------------
     9. Init language: saved → browser → EN
     --------------------------------------------------------- */
  var saved = null;
  try { saved = localStorage.getItem('midas-lang'); } catch (e) {}
  var nav = (navigator.language || 'en').toLowerCase();
  setLang(saved || (nav.indexOf('ko') === 0 ? 'ko' : nav.indexOf('zh') === 0 ? 'zh' : 'en'));
})();

# MIDAS CLINIC · INSPIRE — 홈페이지

미다스의원 인스파이어리조트점 (구 선이고은 성형외과) 공식 홈페이지 소스입니다.
디자인 시안(“A Global Aesthetic Destination at Inspire”)을 기준으로 구현했습니다.

## 폴더 구조
```
index.html              홈
about.html              병원소개 · 대표원장
procedures.html         진료안내 (전체)
rhinoplasty.html        코성형          ┐
eye.html                눈성형          │
lifting.html            리프팅          │ 시술별 상세 페이지
contouring.html         윤곽 · 페이스    │
body.html               바디            │
skin.html               피부 · 쁘띠      ┘
global-care.html        해외 고객 안내
experience.html         인스파이어 공간 · 위치
contact.html            상담 신청 · 오시는 길 · 지도
css/style.css           스타일 (색·서체 변수는 파일 상단 :root)
js/main.js              다국어(EN/KR/中文), 메뉴, 슬라이더, 진료 탭, 진료 상태, 상담 폼
images/                 사진 (현재는 시안에서 잘라낸 임시 이미지)
tools/build_pages.py    서브 페이지 생성 스크립트
```
빌드 과정이 없는 정적 사이트입니다. 아무 정적 호스팅(GitHub Pages 등)에 그대로 올리면 됩니다.

## 수정 방법
- **서브 페이지 문구 / 번역**: `tools/build_pages.py`에서 `T("영어", "한국어", "中文")` 형태로 수정한 뒤 `python3 tools/build_pages.py` 실행 (헤더·푸터도 이 파일에서 한 번에 바뀜)
- **홈 문구**: `js/main.js`의 `I18N`
- **문구 / 번역**: `js/main.js`의 `I18N` (en / ko / zh)
- **시술 목록**: `js/main.js`의 `PROCEDURES`
- **원장 경력**: `js/main.js`의 `CREDS`
- **색상·서체**: `css/style.css` 상단 `:root`
- **사진 교체**: `images/` 폴더의 같은 파일명으로 덮어쓰기
  - `hero-inspire.jpg` (권장 2400px 이상 가로), `standard-portrait.jpg`, `inspire-lounge.jpg`

## 오픈 전 확인할 것
1. **사진**: 지금 이미지는 시안 파일에서 잘라 확대한 임시본이라 해상도가 낮습니다. 원본 고해상도 파일(그리고 모델·건물 사진의 사용 권리)이 있는지 확인 후 교체해 주세요.
2. **상담 폼**: `js/main.js`의 `ENDPOINT`에 접수 주소(예: Formspree, 자체 서버)를 넣어야 실제 전송됩니다. 비어 있으면 전화/메신저 안내가 표시됩니다.
3. **진료시간**: 기존 사이트에 평일 19:00과 18:30이 섞여 있어 18:30으로 넣었습니다.
4. **원장 경력 영문·중문 표기**: 학회 공식 영문명이 확인되지 않은 항목은 일반 명칭으로 적어 두었습니다. 공식 명칭으로 확인해 주세요.
5. **의료광고**: “World-class” 같은 최상급 표현은 의료광고 심의에서 문제될 수 있습니다. 게시 전 심의 대상 여부를 확인해 주세요. 전후 사진은 넣지 않았습니다.
6. **메신저 링크**: 카카오톡 채널·WhatsApp·WeChat 주소를 받으면 연결합니다.

## 기존 사이트와의 관계
- **세포 메뉴**: 새 사이트에서는 메뉴의 `Cell / 세포` 항목이 파나셀 홈페이지(https://panacellbio.com/ko/)로 새 창 연결됩니다. 주소는 `tools/build_pages.py`의 `PANACELL_URL`과 `index.html`에서 바꿀 수 있습니다.
- **줄기세포 유방 확대술·재건술**: 바디(`body.html`)에 포함
- **PRP(PMRP)·슈퍼 PRP**: 피부(`skin.html`)에 포함
- **기사·동영상**: `media.html`. 목록은 `tools/build_pages.py`의 `VIDEOS`, `PRESS`에 추가한 뒤 `python3 tools/build_pages.py` 실행

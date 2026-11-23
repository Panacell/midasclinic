# MIDAS CLINIC · INSPIRE — 홈페이지

미다스의원 인스파이어리조트점 (구 선이고은 성형외과) 공식 홈페이지 소스입니다.
디자인 시안(“A Global Aesthetic Destination at Inspire”)을 기준으로 구현했습니다.

## 폴더 구조
```
index.html          페이지 마크업
css/style.css       스타일 (색·서체 변수는 파일 상단 :root)
js/main.js          다국어(EN/KR/中文), 메뉴, 슬라이더, 진료 탭, 진료 상태, 상담 폼
images/             사진 (현재는 시안에서 잘라낸 임시 이미지)
```
빌드 과정이 없는 정적 사이트입니다. `index.html`을 브라우저로 열거나, 아무 정적 호스팅(GitHub Pages, Netlify, Vercel 등)에 올리면 됩니다.

## 섹션
1. Header — 로고, 메뉴, 언어 선택(EN/KR/中文), Consultation 버튼
2. Hero — 3장 슬라이드 (글로벌 데스티네이션 / 코성형 / 리프팅)
3. The Midas Standard — 인물 사진 + 철학
4. Global Care · Easy Travel · Premium & Private — 3가지 강점
5. Inspire Experience — 라운지 사진 + 회복 여정
6. Procedures — Face / Body / Skin 탭, 펼쳐지는 시술 목록
7. Director — 최승호 대표원장 경력
8. Contact — 연락처, 진료시간(실시간 진료 상태), 상담 신청 폼
9. Footer — 사업자 정보, 부작용 고지

## 수정 방법
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

## 기존 사이트에서 제외한 내용
세포 메뉴 전체(세포연구, 암 유전자·중금속·DNA·면역 검사 등), 줄기세포 유방 확대·재건, PRP·PMRP, BL Stem 팜플렛 링크.

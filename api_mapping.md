# digitalnow.co.kr API 매핑 정보
BASE: https://digitalnow.co.kr/reserve/pensionInfo/thebgyeong/{n}

## n=4 업체정보 (result: 단일 객체)
- BUSI_NM: "더비경프라이빗풀빌라"
- USER_TEL1: "010-9429-7070"
- BUSI_NO: "512-08-54757"
- BUSI_PRE_NM: "이성철"
- NEW_USER_ADDR: "경상북도 예천군 풍양면 덕암로 1123-33"
- USER_ACCO: "국민은행 98-676-02-3348 이성철"
- CHECK_IN: "16", CHECK_OUT: "12"

## n=5 요금표 (result: 배열)
- ROOM_CODE, TYPE_NM (객실명), ADLT_BASE_PERS, ADLT_MAX_PERS
- P01_WEEK_PRCE, P01_FRD_PRCE, P01_SAT_PRCE, P01_SUN_PRCE (시즌1)
- P02~P06 (시즌2~6, 0이면 미사용)
- 예: 숲 P01: 평일520000, 금570000, 토620000, 일520000

## n=8 객실상세 (result: 배열, 12개)
- TYPE_NM: 한글 객실명 (숲/아침/달/하늘/별/노을/이슬/풀잎/구름/바람/강/초원)
- TYPE_NM_EN: 영문명
- ROOM_EXTN: 평수 (30평)
- ROOM_TYPE: 객실 특징 설명 (쉼표 구분)
- FLHT_ROOM_CNT: 거실수, BED_ROOM_CNT: 침실수, TOLT_CNT: 화장실수
- ADLT_BASE_PERS, ADLT_MAX_PERS, KIDS_MAX_PERS, INFT_MAX_PERS
- ADLT_EXCS_PRCE: 추가인원 요금 (30000)
- INTERIOR: 기본 시설 목록
- ETC_DETL: 객실 상세 설명 (HTML 포함)
- SORT_NO: 정렬번호 (1~12)
- BED_INFO: JSON 배열 [{QUEEN_CNT:"1",...}]
- TYPE_NAME: 타입명 (풀빌라/스파빌라/프라이빗 빌라)
- ASSIST_CONTENT: 추가 안내
- TYPE_DESC: 영문 타입명
- USE_YN: N (모두 N이지만 표시함)

## n=9 스페셜 (result: 배열, 8개)
- TITLE_KR: 한글명
- TITLE_EN: 영문명
- CONTENT: HTML 본문
- CONTENT1~4: 추가 내용
- IMAGE_URL: 비어있음 (이미지는 별도 경로)
- IMAGE_COUNT: 이미지 수
- ORDER_NUM: 정렬번호

## n=12 퍼실리티 (result: 배열, 4개)
- 동일 구조 (TITLE_KR, TITLE_EN, CONTENT, ORDER_NUM, IMAGE_URL)

## n=15 객실 타입 (result: 배열, 3개)
- IDX: 100637/100638/100639
- TYPE_NAME: 풀빌라/스파빌라/프라이빗 빌라
- TYPE_DESC: Poolvilla/Spa Villa/Private Villa
- TYPE_CONTENT: Poolvilla/Luxury Poolvilla/Private Villa

## 이미지 경로 규칙 (기존 하드코딩 기준)
- 객실: http://gonylab11.speedgabia.com/thebgyeong/room/{SORT_NO}/{img_idx}.jpg
- 스페셜: http://gonylab11.speedgabia.com/thebgyeong/special/{ORDER_NUM}/{img_idx}.jpg
- 타입 대표: room/1/1.jpg(풀빌라), room/6/1.jpg(스파빌라), room/9/1.jpg(프라이빗)

## 타입별 객실 매핑 (TYPE_NAME 기준)
- 풀빌라: SORT_NO 1~5 (숲/아침/달/하늘/별)
- 스파빌라: SORT_NO 6~8 (노을/이슬/풀잎)
- 프라이빗 빌라: SORT_NO 9~12 (구름/바람/강/초원)

## 타입 로고 파일
- 풀빌라: logo_pool_villa.png
- 스파빌라: logo_spa_villa.png
- 프라이빗 빌라: logo_private_villa.png

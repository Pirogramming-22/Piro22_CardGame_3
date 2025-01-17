# 숫자 카드 대결 게임

## 📌 프로젝트 소개
숫자 카드(1~10) 중 무작위로 제공된 5장의 카드에서 1장을 선택해 다른 유저와 대결하는 웹 게임입니다.

랜덤한 게임 룰로 승패가 결정됩니다.   
승자는 카드 숫자만큼 점수를 얻고, 패자는 숫자만큼 점수를 잃습니다.   
랭킹 시스템을 통해 점수 순위를 확인할 수 있습니다.  

## 🛠️ 기술 스택
- **Backend:** Django  
- **Frontend:** HTML, CSS, JavaScript  
- **협업 도구:** GitHub, Notion, Figma  

## 🔥 주요 기능
1. **회원가입/로그인**
   - 일반 로그인 (Django 기본 인증)
   - 소셜 로그인 (Naver)

2. **게임 진행**
   - 카드 선택 및 상대방 도전
   - 결과에 따른 점수 변동

3. **랭킹 시스템**
   - 유저별 누적 점수 랭킹

4. **게임 관리**
   - 진행한 게임 내역 확인 및 삭제

## 📋 역할 분담 및 회의 계획
프로젝트의 역할 분담, 회의 계획 및 프로젝트 설계는 Notion에서 확인할 수 있습니다.  
**Notion 링크:** [Piro22_CardGame_3](https://www.notion.so/Piro22_CardGame_3-17dba5296cf980d190f3feea58520e2b?pvs=4)

## 🎨 디자인
프로젝트의 디자인은 Figma를 통해 진행되었습니다.  
**Figma 링크:** [Piro22_CardGame_3](https://www.figma.com/design/L6GtIDSITqP5cYUvThW5wk/Piro22_CardGame_3?node-id=0-1&t=sjXjOawUbrcCdvyx-1)

## 🚀 패키지 설치
```bash
pip install django
pip install django-allauth
pip install requests

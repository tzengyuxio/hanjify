# HANJIFY — 영어 한자화 도구

[English](README.md) | [繁體中文](README.zh-TW.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md)

**HANJIFY**는 영어 텍스트를 한자 표기로 변환하는 도구입니다 — 로마자 표기의 역방향 버전입니다.

🔗 **데모 사이트:** [hanjify.tzengyuxio.me](https://hanjify.tzengyuxio.me)

## 기능 소개

영어 텍스트를 입력하면 HANJIFY가 알려진 단어를 대응하는 한자로 치환하고, 루비 텍스트로 원문을 표시합니다:

```
입력: The little prince lived on a small planet.
출력: 其 小 王子 活於 上 一 小 行星。
     (한자 위에 작은 글씨로 원래 영어를 표시)
```

## 주요 기능

- **실시간 변환** — 약 4,800개의 영한 대조 사전 내장
- **루비 표시** — 한자 위의 영어 원문 표시/숨기기 전환 가능
- **다국어 UI** — 영어, 번체 중국어, 간체 중국어, 일본어 지원
- **스크린샷 내보내기** — 변환 결과를 PNG 이미지로 저장 (워터마크 포함)
- **예시 텍스트** — 내장 샘플로 바로 체험 가능

## 작동 원리

1. 각 영어 단어를 사전(`wordlist.js`)에서 검색
2. 대응하는 한자가 있으면 `<ruby>` 태그로 치환
3. 찾을 수 없으면 일반적인 접미사(s, ed, ing 등)를 제거 후 재검색
4. 대응할 수 없는 단어는 그대로 표시

## 변환 사양

변환 규칙은 [`docs/spec.md`](docs/spec.md)에 정의되어 있습니다 — 본 도구의 single source of truth이며, 기능어 대응, 형태소 규칙, 자형 채택, 충돌 회피, 경계 사례를 포함합니다. 본 웹 도구와 [Claude Code `hanjify` skill](https://github.com/tzengyuxio/skills/tree/main/hanjify) 모두 같은 사양을 구현합니다.

## 로컬 실행

```bash
# 아무 정적 파일 서버나 사용
python3 -m http.server 8000
# http://localhost:8000 열기
```

빌드 도구 불필요, 패키지 의존성 없음 — 순수 정적 HTML/CSS/JS입니다.

## 데이터 파이프라인

사전 데이터는 Python 스크립트로 관리합니다:

| 스크립트 | 용도 |
|---------|------|
| `simple.py` | Wikipedia/Wiktionary에서 단어 목록 가져오기 |
| `process_words.py` | DeepL API로 일괄 번역 |
| `extract.py` | CSV를 `wordlist.js`로 변환 |

사전 재생성:
```bash
python3 extract.py
```

## 기술 스택

- 순수 HTML / CSS / JavaScript (프레임워크 없음)
- Python 데이터 처리 스크립트
- GitHub Pages 호스팅
- dom-to-image 스크린샷 생성

## 라이선스

MIT 라이선스 — 자세한 내용은 [LICENSE](LICENSE) 참조.

## 저자

[Tzeng Yuxio](https://github.com/tzengyuxio)

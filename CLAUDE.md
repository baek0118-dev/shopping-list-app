# 🧪 VibeCoding Study-06 프로젝트

## 프로젝트 개요
- **목적**: Claude Code 스킬 개발 및 학습
- **작업 디렉토리**: C:\Users\J.C.BAEK\Desktop\VibeCoding\study-06

## 스킬 정의

### /review
**코드 자동 리뷰 스킬**

코드를 Claude API를 통해 종합적으로 분석하고 개선 제안을 제공합니다.

**사용법:**
```
/review <file-path> [--focus <area1> <area2>] [--interactive] [--save]
```

**옵션:**
- `--focus` - 분석 영역 지정 (quality, security, performance, maintainability, design)
- `--interactive` - 대화형 모드 활성화 (추가 질문 가능)
- `--save` - 결과를 파일로 저장

**예시:**
```
/review src/app.py
/review src/api.ts --focus security performance
/review main.py --interactive --save
```

**분석 항목:**
1. **코드 품질** - 가독성, 명명 규칙, 함수 크기와 책임
2. **보안** - 취약점, 입력 검증, 의존성 관리
3. **성능** - 알고리즘 복잡도, 병목 지점, 최적화 기회
4. **유지보수성** - 테스트 가능성, 에러 처리, 문서화
5. **설계** - SOLID 원칙, 디자인 패턴, 구조

**구현 세부사항:**
- Python 스크립트: `code_reviewer.py`
- PowerShell 래퍼: `review.ps1`
- 사용 설명서: `CODE_REVIEW_README.md`
- 빠른 시작: `QUICK_START.md`
- 테스트 샘플: `sample_code.py`

---

## 프로젝트 상태

### ✅ 완료된 작업
- [x] 코드 리뷰 Python 스크립트 개발
- [x] PowerShell 래퍼 생성
- [x] 상세 사용설명서 작성
- [x] 빠른 시작 가이드 제공
- [x] 테스트용 샘플 코드 작성

### 🚀 스킬 활성화 방법

#### 필수 설정 (처음 한 번만)
```powershell
# 1. 필수 패키지 설치
pip install anthropic

# 2. 환경변수 설정
$env:ANTHROPIC_API_KEY = "sk-ant-xxxxxxxxxxxxx"
```

#### 사용
```powershell
# 방법 1: Python 직접 실행
python code_reviewer.py <file-path> [옵션]

# 방법 2: PowerShell 래퍼 (권장)
.\review.ps1 <file-path> [옵션]

# 방법 3: Claude Code 스킬 (이 CLAUDE.md 정의 사용)
/review <file-path> [옵션]
```

---

## 주요 기능

### 🎯 분석 심도
- **적응형 사고 (Adaptive Thinking)** - Opus 4.7의 advanced thinking 활용
- **다언어 지원** - 20+ 프로그래밍 언어 및 마크업 언어
- **구조화된 피드백** - 심각도(높음/중간/낮음) 표시
- **종합 평점** - 1-10 점수 체계

### 💬 대화형 기능
리뷰 후 추가 질문 가능:
- 특정 부분에 대한 상세 설명 요청
- 개선 방법에 대한 구체적 조언
- 코드 패턴 및 베스트 프랙티스 학습

### 📁 결과 저장
마크다운 형식으로 리뷰 결과를 저장하여 팀과 공유 가능

---

## 지원 언어

**프로그래밍 언어:**
Python, JavaScript, TypeScript, JSX, TSX, Java, Go, Rust, C++, C, C#, Ruby, PHP, Shell

**마크업 및 설정:**
SQL, HTML, CSS, JSON, YAML

---

## 기술 스택

- **언어**: Python 3
- **API**: Anthropic Claude API (Opus 4.7)
- **기능**: Adaptive Thinking, Advanced Analysis
- **래퍼**: PowerShell (Windows) / Bash (Unix)

---

## 참고 문서

| 파일 | 목적 |
|------|------|
| `code_reviewer.py` | 메인 리뷰 엔진 |
| `review.ps1` | PowerShell 래퍼 |
| `CODE_REVIEW_README.md` | 상세 사용설명서 |
| `QUICK_START.md` | 5분 빠른 시작 가이드 |
| `sample_code.py` | 테스트용 샘플 코드 |

---

## 다음 단계

1. **초기 설정**
   ```powershell
   pip install anthropic
   $env:ANTHROPIC_API_KEY = "your-api-key"
   ```

2. **테스트 실행**
   ```powershell
   python code_reviewer.py sample_code.py
   ```

3. **자신의 코드 리뷰**
   ```powershell
   .\review.ps1 your_code.py --interactive --save
   ```

---

## 주의사항

⚠️ **민감한 데이터 주의**
- 비밀번호, API 키, 개인 정보를 포함한 코드는 리뷰하지 마세요
- 코드가 API를 통해 전송됩니다

⚠️ **파일 크기**
- 매우 큰 파일 (1MB+)는 처리 시간이 오래 걸릴 수 있습니다
- 필요 시 파일을 분할하여 리뷰하세요

---

**최종 업데이트**: 2026-05-04

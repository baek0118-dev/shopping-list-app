# 🚀 코드 리뷰 도구 - 빠른 시작

## 1단계: 필수 패키지 설치

```powershell
pip install anthropic
```

## 2단계: API 키 설정

### 방법 A: 환경변수 설정 (권장)

**PowerShell:**
```powershell
$env:ANTHROPIC_API_KEY = "sk-ant-xxxxxxxxxxxxx"
```

**CMD:**
```cmd
set ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxx
```

### 방법 B: .env 파일 생성

프로젝트 루트에 `.env` 파일 생성:
```
ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxx
```

## 3단계: 코드 리뷰 실행

### 샘플 코드로 테스트

```powershell
python code_reviewer.py sample_code.py
```

또는 PowerShell 래퍼 사용:
```powershell
.\review.ps1 sample_code.py
```

## 4단계: 옵션 활용

### 보안에 집중한 리뷰
```powershell
python code_reviewer.py sample_code.py --focus security
```

### 대화형 모드 (추가 질문 가능)
```powershell
python code_reviewer.py sample_code.py --interactive
```

### 결과를 파일로 저장
```powershell
python code_reviewer.py sample_code.py --save
```

### 모든 옵션 사용
```powershell
python code_reviewer.py sample_code.py --focus security performance --interactive --save
```

## 문제 해결

### ❌ "No module named 'anthropic'"
```powershell
pip install anthropic
```

### ❌ "ANTHROPIC_API_KEY is not set"
1. Anthropic 계정 생성: https://console.anthropic.com
2. API 키 발급 후 환경변수 설정
3. PowerShell 재시작

### ❌ FileNotFoundError
파일 경로가 정확한지 확인하세요:
```powershell
# ❌ 잘못된 예
.\review.ps1 app.py

# ✅ 올바른 예
python code_reviewer.py .\sample_code.py
python code_reviewer.py C:\Users\...\app.py
```

## 주요 기능

### 📋 리뷰 항목
- **코드 품질**: 가독성, 명명 규칙, 함수 크기
- **보안**: 취약점, 입력 검증, 의존성
- **성능**: 알고리즘 복잡도, 병목 지점
- **유지보수성**: 테스트 가능성, 에러 처리, 문서화
- **설계**: SOLID 원칙, 디자인 패턴

### 💬 대화형 기능
리뷰 후 추가 질문:
```
🤔 질문: 이 부분의 시간 복잡도를 개선할 방법이 있을까요?
🤔 질문: 어떤 디자인 패턴을 적용하면 좋을까요?
🤔 질문: 더 보안이 좋은 방법이 있나요?
```

### 📁 다양한 언어 지원
Python, JavaScript, TypeScript, Java, Go, Rust, C++, C#, Ruby, PHP, SQL, HTML, CSS 등

## 다음 단계

- 📖 자세한 사용법: [CODE_REVIEW_README.md](CODE_REVIEW_README.md)
- 🔍 자신의 코드로 테스트해보세요
- 💡 `--focus` 옵션으로 특정 영역에 집중해보세요
- 💾 `--save` 옵션으로 결과를 저장하고 팀과 공유하세요

## 유용한 팁

### Tip 1: 여러 파일 한 번에 리뷰
```powershell
Get-ChildItem -Filter "*.py" | ForEach-Object {
    python code_reviewer.py $_.FullName --save
}
```

### Tip 2: 특정 영역에 집중
```powershell
# 보안 문제만 확인
python code_reviewer.py app.py --focus security

# 성능 최적화 제안
python code_reviewer.py app.py --focus performance

# 코드 품질 개선
python code_reviewer.py app.py --focus quality
```

### Tip 3: 결과 저장 후 검토
```powershell
python code_reviewer.py app.py --save
# app_review.md 파일이 생성됩니다
```

---

**준비 완료! 이제 코드 리뷰를 시작하세요.** ✨

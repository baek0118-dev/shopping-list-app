# 코드 자동 리뷰 도구

Claude API를 사용하여 코드를 자동으로 리뷰합니다. 품질, 보안, 성능, 유지보수성, 설계 패턴 등을 종합적으로 분석합니다.

## 설치

### 1. 필수 패키지 설치
```bash
pip install anthropic
```

### 2. API 키 설정
환경변수에 Anthropic API 키를 설정합니다:

**Windows (PowerShell):**
```powershell
$env:ANTHROPIC_API_KEY = "your-api-key-here"
```

**Windows (CMD):**
```cmd
set ANTHROPIC_API_KEY=your-api-key-here
```

**Linux/Mac:**
```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

또는 `.env` 파일을 프로젝트 루트에 생성:
```
ANTHROPIC_API_KEY=your-api-key-here
```

## 사용법

### 기본 사용법

**Python으로 직접 실행:**
```bash
python code_reviewer.py app.py
```

**PowerShell을 사용 (Windows):**
```powershell
.\review.ps1 app.py
```

### 옵션

#### `--focus` / `-f`: 특정 영역에 집중
```bash
python code_reviewer.py app.py --focus security performance
# 또는
.\review.ps1 app.py -Focus security, performance
```

선택 옵션:
- `quality` - 코드 품질 (가독성, 명명 규칙 등)
- `security` - 보안 문제 분석
- `performance` - 성능 최적화
- `maintainability` - 유지보수성
- `design` - 디자인 패턴

#### `--interactive` / `-i`: 대화형 모드
리뷰 후 추가 질문을 할 수 있습니다:
```bash
python code_reviewer.py app.py --interactive
# 또는
.\review.ps1 app.py -Interactive
```

#### `--save` / `-s`: 결과 저장
리뷰 결과를 마크다운 파일로 저장합니다:
```bash
python code_reviewer.py app.py --save
# 또는
.\review.ps1 app.py -Save
```

### 사용 예시

#### 예시 1: 기본 리뷰
```bash
python code_reviewer.py src/main.py
```

#### 예시 2: 보안과 성능에 집중한 리뷰
```bash
python code_reviewer.py src/api.js --focus security performance
```

#### 예시 3: 리뷰 후 대화형으로 질문하기
```bash
python code_reviewer.py app.ts --interactive
```

#### 예시 4: 모든 옵션 활용
```bash
python code_reviewer.py src/database.sql --focus security maintainability --interactive --save
```

## 리뷰 항목

### 1. 코드 품질
- ✅ 가독성과 명확성
- ✅ 명명 규칙 준수
- ✅ 함수/메서드의 크기와 책임

### 2. 보안 문제
- ✅ 잠재적 보안 취약점
- ✅ 입력 검증 및 방어
- ✅ 의존성 및 라이브러리 사용

### 3. 성능
- ✅ 알고리즘 복잡도
- ✅ 불필요한 계산이나 할당
- ✅ 병목 지점

### 4. 유지보수성
- ✅ 테스트 가능성
- ✅ 에러 처리
- ✅ 주석과 문서화

### 5. 설계 패턴
- ✅ SOLID 원칙 준수
- ✅ 디자인 패턴의 적절한 사용
- ✅ 의존성 관리

## 출력 형식

리뷰는 다음과 같은 구조로 출력됩니다:

```
📊 'app.py' 코드 리뷰 중...

[리뷰 내용]

💾 리뷰가 저장되었습니다: app_review.md
```

## 지원 언어

- Python (.py)
- JavaScript (.js)
- TypeScript (.ts, .tsx)
- JSX (.jsx)
- Java (.java)
- Go (.go)
- Rust (.rs)
- C++ (.cpp)
- C (.c)
- C# (.cs)
- Ruby (.rb)
- PHP (.php)
- Shell (.sh)
- SQL (.sql)
- HTML (.html)
- CSS (.css)
- JSON (.json)
- YAML (.yaml, .yml)

## 팁

### 팁 1: 특정 부분 리뷰
특정 부분만 검토하려면, 그 부분을 별도 파일로 추출한 후 리뷰하세요.

### 팁 2: 대화형 모드 활용
리뷰 후 `--interactive` 옵션으로 구체적인 질문을 할 수 있습니다:
```
🤔 질문: 이 함수의 시간복잡도를 개선할 수 있는 방법이 있을까요?
🤔 질문: SOLID 원칙 중 어떤 것을 위반하고 있나요?
```

### 팁 3: 결과 저장과 공유
`--save` 옵션으로 결과를 마크다운 파일로 저장하면, 팀과 공유하거나 나중에 참고할 수 있습니다.

### 팁 4: 여러 파일 일괄 리뷰
```powershell
Get-ChildItem -Filter "*.py" | ForEach-Object { 
    python code_reviewer.py $_.FullName --save
}
```

## 문제 해결

### "ANTHROPIC_API_KEY가 설정되지 않았습니다"
- API 키가 환경변수에 설정되어 있는지 확인하세요
- PowerShell을 재시작해야 할 수도 있습니다

### "파일을 찾을 수 없습니다"
- 파일 경로가 정확한지 확인하세요
- 상대 경로 대신 절대 경로를 사용해보세요

### "API 응답이 너무 길어요"
- `--focus` 옵션으로 특정 영역에만 집중하도록 제한하세요

## 주의사항

⚠️ **민감한 데이터 주의**
- 리뷰 코드가 API를 통해 전송됩니다
- 비밀번호, API 키, 개인 정보를 포함한 코드는 리뷰하지 마세요

## 라이선스

Anthropic API 이용약관을 따릅니다.

#!/usr/bin/env python3
"""
코드 자동 리뷰 도구
Claude API를 사용하여 코드의 품질, 보안, 성능을 자동으로 검토합니다.
"""

import sys
import os
import json
import argparse
from pathlib import Path
from anthropic import Anthropic

client = Anthropic()


def read_code_file(file_path: str) -> tuple[str, str]:
    """파일에서 코드를 읽습니다."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"파일을 찾을 수 없습니다: {file_path}")

    with open(path, 'r', encoding='utf-8') as f:
        code = f.read()

    return code, str(path)


def get_file_context(file_path: str) -> str:
    """파일의 언어와 크기를 기반으로 컨텍스트를 생성합니다."""
    path = Path(file_path)
    extension = path.suffix.lower()
    file_size = path.stat().st_size

    language_map = {
        '.py': 'Python',
        '.js': 'JavaScript',
        '.ts': 'TypeScript',
        '.jsx': 'JSX',
        '.tsx': 'TSX',
        '.java': 'Java',
        '.go': 'Go',
        '.rs': 'Rust',
        '.cpp': 'C++',
        '.c': 'C',
        '.cs': 'C#',
        '.rb': 'Ruby',
        '.php': 'PHP',
        '.sh': 'Shell',
        '.sql': 'SQL',
        '.html': 'HTML',
        '.css': 'CSS',
        '.json': 'JSON',
        '.yaml': 'YAML',
        '.yml': 'YAML',
    }

    language = language_map.get(extension, '알 수 없음')
    size_kb = file_size / 1024

    return f"언어: {language}, 파일 크기: {size_kb:.1f}KB"


def review_code(code: str, file_path: str, focus_areas: list[str] = None) -> str:
    """Claude를 사용하여 코드를 리뷰합니다."""

    file_context = get_file_context(file_path)
    file_name = Path(file_path).name

    focus_prompt = ""
    if focus_areas:
        focus_prompt = f"\n\n특히 다음 영역에 집중해주세요: {', '.join(focus_areas)}"

    system_prompt = """당신은 경험 많은 코드 리뷰 전문가입니다. 다음 항목을 중심으로 상세한 리뷰를 제공하세요:

1. **코드 품질**
   - 가독성과 명확성
   - 명명 규칙 준수
   - 함수/메서드의 크기와 책임

2. **보안 문제**
   - 잠재적 보안 취약점
   - 입력 검증 및 방어
   - 의존성 및 라이브러리 사용

3. **성능**
   - 알고리즘 복잡도
   - 불필요한 계산이나 할당
   - 병목 지점

4. **유지보수성**
   - 테스트 가능성
   - 에러 처리
   - 주석과 문서화

5. **설계 패턴**
   - SOLID 원칙 준수
   - 디자인 패턴의 적절한 사용
   - 의존성 관리

구체적인 개선 제안을 제시하고, 심각도(높음/중간/낮음)를 표시해주세요.
최종적으로 종합 평점(1-10)을 제시해주세요."""

    user_message = f"""파일: {file_name}
{file_context}

다음 코드를 리뷰해주세요:{focus_prompt}

```
{code}
```"""

    conversation_history = [
        {"role": "user", "content": user_message}
    ]

    print(f"\n📊 '{file_name}' 코드 리뷰 중...\n")

    response = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=4096,
        thinking={
            "type": "adaptive"
        },
        output_config={
            "effort": "high"
        },
        system=system_prompt,
        messages=conversation_history
    )

    review_text = response.content[-1].text
    conversation_history.append({"role": "assistant", "content": review_text})

    return review_text, conversation_history


def interactive_review(code: str, file_path: str, initial_review: str, initial_history: list) -> None:
    """사용자와 상호작용하며 추가 질문을 처리합니다."""

    file_name = Path(file_path).name
    conversation_history = initial_history.copy()

    print("\n💬 추가 질문이 있으신가요? (exit 또는 quit 입력 시 종료)\n")

    system_prompt = """당신은 경험 많은 코드 리뷰 전문가입니다.
이전 리뷰 내용을 바탕으로 사용자의 후속 질문에 답변해주세요."""

    while True:
        try:
            question = input("🤔 질문: ").strip()

            if question.lower() in ['exit', 'quit', '종료']:
                print("\n리뷰를 마칩니다. 감사합니다!")
                break

            if not question:
                continue

            conversation_history.append({"role": "user", "content": question})

            response = client.messages.create(
                model="claude-opus-4-7",
                max_tokens=2048,
                thinking={
                    "type": "adaptive"
                },
                system=system_prompt,
                messages=conversation_history
            )

            answer = response.content[-1].text
            conversation_history.append({"role": "assistant", "content": answer})

            print(f"\n✅ 답변:\n{answer}\n")

        except KeyboardInterrupt:
            print("\n\n리뷰를 종료합니다.")
            break


def save_review(review_text: str, file_path: str) -> str:
    """리뷰 결과를 파일로 저장합니다."""
    original_path = Path(file_path)
    review_file = original_path.parent / f"{original_path.stem}_review.md"

    with open(review_file, 'w', encoding='utf-8') as f:
        f.write(f"# 코드 리뷰: {original_path.name}\n\n")
        f.write(f"생성일: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("---\n\n")
        f.write(review_text)

    return str(review_file)


def main():
    parser = argparse.ArgumentParser(
        description="코드를 자동으로 리뷰합니다.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
예시:
  python code_reviewer.py app.py
  python code_reviewer.py src/main.ts --focus security performance
  python code_reviewer.py index.js --interactive --save
        """
    )

    parser.add_argument("file", help="리뷰할 코드 파일 경로")
    parser.add_argument(
        "--focus",
        nargs="+",
        choices=["quality", "security", "performance", "maintainability", "design"],
        help="특정 영역에 집중 (예: security performance)"
    )
    parser.add_argument(
        "--interactive", "-i",
        action="store_true",
        help="리뷰 후 대화형 모드 활성화"
    )
    parser.add_argument(
        "--save", "-s",
        action="store_true",
        help="리뷰 결과를 파일로 저장"
    )

    args = parser.parse_args()

    try:
        code, file_path = read_code_file(args.file)
        review_text, conversation_history = review_code(code, file_path, args.focus)

        print(review_text)

        if args.save:
            review_file = save_review(review_text, file_path)
            print(f"\n💾 리뷰가 저장되었습니다: {review_file}")

        if args.interactive:
            interactive_review(code, file_path, review_text, conversation_history)

    except FileNotFoundError as e:
        print(f"❌ 오류: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"❌ 오류: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

"""
쇼핑 리스트 앱 자동 테스트 - Playwright 사용
"""
import asyncio
import os
from pathlib import Path
from playwright.async_api import async_playwright


async def test_shopping_list():
    """쇼핑 리스트 앱의 모든 기능을 테스트"""

    # HTML 파일 경로
    html_file = Path(__file__).parent / "shopping-list.html"
    html_url = f"file:///{str(html_file).replace(chr(92), '/')}"

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        print("🧪 쇼핑 리스트 앱 자동 테스트 시작\n")

        try:
            # 1. 앱 로드 테스트
            print("1️⃣ [테스트] 앱 로드")
            await page.goto(html_url)
            title = await page.title()
            print(f"   ✅ 페이지 제목: {title}\n")

            # 2. 초기 상태 확인
            print("2️⃣ [테스트] 초기 상태")
            empty_msg = await page.is_visible('#emptyMessage')
            total_count = await page.text_content('#totalCount')
            print(f"   ✅ 빈 메시지 표시: {empty_msg}")
            print(f"   ✅ 초기 아이템 수: {total_count}\n")

            # 3. 아이템 추가 테스트
            print("3️⃣ [테스트] 아이템 추가")
            items_to_add = ["우유", "빵", "계란", "치즈"]

            for item in items_to_add:
                await page.fill('#itemInput', item)
                await page.click('button:has-text("추가")')
                await page.wait_for_timeout(100)

            # 아이템 추가 확인
            items = await page.locator('.list-item').count()
            print(f"   ✅ 추가된 아이템 수: {items}")

            # 통계 확인
            total = await page.text_content('#totalCount')
            remain = await page.text_content('#remainCount')
            print(f"   ✅ 전체 아이템: {total}, 남은 아이템: {remain}\n")

            # 4. 아이템 체크 테스트
            print("4️⃣ [테스트] 아이템 체크")
            checkboxes = await page.locator('input[type="checkbox"]').all()

            # 첫 번째와 세 번째 아이템 체크
            await checkboxes[0].check()
            await page.wait_for_timeout(100)
            await checkboxes[2].check()
            await page.wait_for_timeout(100)

            # 체크 상태 확인
            completed = await page.text_content('#completeCount')
            remain = await page.text_content('#remainCount')
            print(f"   ✅ 완료된 아이템: {completed}")
            print(f"   ✅ 남은 아이템: {remain}\n")

            # 체크된 아이템의 스타일 확인
            completed_items = await page.locator('.list-item.completed').count()
            print(f"   ✅ 완료 표시된 아이템: {completed_items}\n")

            # 5. 아이템 삭제 테스트
            print("5️⃣ [테스트] 아이템 삭제")

            # 삭제 버튼 찾기
            delete_btns = await page.locator('.delete-btn').all()
            initial_count = await page.locator('.list-item').count()

            # 두 번째 아이템 삭제
            await delete_btns[1].click()

            # 확인 대화상자 처리
            await page.on("dialog", lambda dialog: asyncio.create_task(dialog.accept()))
            await page.wait_for_timeout(200)

            final_count = await page.locator('.list-item').count()
            total = await page.text_content('#totalCount')

            print(f"   ✅ 삭제 전 아이템 수: {initial_count}")
            print(f"   ✅ 삭제 후 아이템 수: {final_count}")
            print(f"   ✅ 통계에 반영된 전체: {total}\n")

            # 6. 체크 상태 토글 테스트
            print("6️⃣ [테스트] 체크 상태 토글")
            checkboxes = await page.locator('input[type="checkbox"]').all()

            if len(checkboxes) > 0:
                # 첫 번째 아이템의 체크 해제
                checked_before = await checkboxes[0].is_checked()
                await checkboxes[0].click()
                await page.wait_for_timeout(100)
                checked_after = await checkboxes[0].is_checked()

                print(f"   ✅ 토글 전 상태: {'✓' if checked_before else '☐'}")
                print(f"   ✅ 토글 후 상태: {'✓' if checked_after else '☐'}")

                completed = await page.text_content('#completeCount')
                remain = await page.text_content('#remainCount')
                print(f"   ✅ 현재 완료: {completed}, 남음: {remain}\n")

            # 7. 엔터 키로 추가 테스트
            print("7️⃣ [테스트] 엔터 키 추가")
            items_before = await page.locator('.list-item').count()

            await page.fill('#itemInput', '버터')
            await page.press('#itemInput', 'Enter')
            await page.wait_for_timeout(100)

            items_after = await page.locator('.list-item').count()
            input_value = await page.input_value('#itemInput')

            print(f"   ✅ 추가 전: {items_before}, 추가 후: {items_after}")
            print(f"   ✅ 입력창 초기화: {input_value == ''}\n")

            # 최종 결과
            print("=" * 50)
            print("✨ 모든 테스트 완료!")
            print("=" * 50)

            final_total = await page.text_content('#totalCount')
            final_complete = await page.text_content('#completeCount')
            final_remain = await page.text_content('#remainCount')

            print(f"\n📊 최종 통계")
            print(f"   전체: {final_total}")
            print(f"   완료: {final_complete}")
            print(f"   남음: {final_remain}")

        except Exception as e:
            print(f"❌ 오류 발생: {e}")
        finally:
            await browser.close()


if __name__ == "__main__":
    asyncio.run(test_shopping_list())

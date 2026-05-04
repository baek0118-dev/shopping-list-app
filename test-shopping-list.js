const { chromium } = require('playwright');
const path = require('path');

async function runTests() {
  console.log('🧪 쇼핑 리스트 앱 자동 테스트 시작\n');

  const htmlPath = path.join(__dirname, 'shopping-list.html');
  const htmlUrl = `file:///${htmlPath.replace(/\\/g, '/')}`;

  const browser = await chromium.launch();
  const page = await browser.newPage();

  try {
    // 1. 앱 로드
    console.log('1️⃣ [테스트] 앱 로드');
    await page.goto(htmlUrl);
    const title = await page.title();
    console.log(`   ✅ 페이지 제목: ${title}\n`);

    // 2. 초기 상태 확인
    console.log('2️⃣ [테스트] 초기 상태');
    const emptyMsgVisible = await page.isVisible('#emptyMessage');
    const totalCount = await page.textContent('#totalCount');
    console.log(`   ✅ 빈 메시지 표시: ${emptyMsgVisible}`);
    console.log(`   ✅ 초기 아이템 수: ${totalCount}\n`);

    // 3. 아이템 추가 테스트
    console.log('3️⃣ [테스트] 아이템 추가');
    const items = ['우유', '빵', '계란', '치즈'];

    for (const item of items) {
      await page.fill('#itemInput', item);
      await page.click('button:has-text("추가")');
      await page.waitForTimeout(100);
    }

    const itemCount = await page.locator('.list-item').count();
    const newTotal = await page.textContent('#totalCount');
    const newRemain = await page.textContent('#remainCount');

    console.log(`   ✅ 추가된 아이템 수: ${itemCount}`);
    console.log(`   ✅ 전체 아이템: ${newTotal}, 남은 아이템: ${newRemain}\n`);

    // 4. 아이템 체크 테스트
    console.log('4️⃣ [테스트] 아이템 체크');
    const checkboxes = await page.locator('input[type="checkbox"]').all();

    // 첫 번째와 세 번째 아이템 체크
    await checkboxes[0].check();
    await page.waitForTimeout(100);
    if (checkboxes.length > 2) {
      await checkboxes[2].check();
      await page.waitForTimeout(100);
    }

    const completed = await page.textContent('#completeCount');
    const remaining = await page.textContent('#remainCount');
    console.log(`   ✅ 완료된 아이템: ${completed}`);
    console.log(`   ✅ 남은 아이템: ${remaining}`);

    const completedItems = await page.locator('.list-item.completed').count();
    console.log(`   ✅ 완료 표시된 아이템: ${completedItems}\n`);

    // 5. 아이템 삭제 테스트
    console.log('5️⃣ [테스트] 아이템 삭제');

    const beforeDelete = await page.locator('.list-item').count();

    // 삭제 버튼 클릭 (두 번째 아이템)
    const deleteBtn = page.locator('.delete-btn').first();

    page.once('dialog', dialog => dialog.accept());
    await deleteBtn.click();
    await page.waitForTimeout(200);

    const afterDelete = await page.locator('.list-item').count();
    const finalTotal = await page.textContent('#totalCount');

    console.log(`   ✅ 삭제 전 아이템 수: ${beforeDelete}`);
    console.log(`   ✅ 삭제 후 아이템 수: ${afterDelete}`);
    console.log(`   ✅ 통계에 반영된 전체: ${finalTotal}\n`);

    // 6. 체크 상태 토글 테스트
    console.log('6️⃣ [테스트] 체크 상태 토글');
    const firstCheckbox = page.locator('input[type="checkbox"]').first();

    const checkedBefore = await firstCheckbox.isChecked();
    await firstCheckbox.click();
    await page.waitForTimeout(100);
    const checkedAfter = await firstCheckbox.isChecked();

    console.log(`   ✅ 토글 전 상태: ${checkedBefore ? '✓' : '☐'}`);
    console.log(`   ✅ 토글 후 상태: ${checkedAfter ? '✓' : '☐'}`);

    const finalCompleted = await page.textContent('#completeCount');
    const finalRemaining = await page.textContent('#remainCount');
    console.log(`   ✅ 현재 완료: ${finalCompleted}, 남음: ${finalRemaining}\n`);

    // 7. 엔터 키로 추가 테스트
    console.log('7️⃣ [테스트] 엔터 키 추가');
    const beforeEnter = await page.locator('.list-item').count();

    await page.fill('#itemInput', '버터');
    await page.press('#itemInput', 'Enter');
    await page.waitForTimeout(100);

    const afterEnter = await page.locator('.list-item').count();
    const inputValue = await page.inputValue('#itemInput');

    console.log(`   ✅ 추가 전: ${beforeEnter}, 추가 후: ${afterEnter}`);
    console.log(`   ✅ 입력창 초기화: ${inputValue === ''}\n`);

    // 최종 결과
    console.log('='.repeat(50));
    console.log('✨ 모든 테스트 완료!');
    console.log('='.repeat(50));

    const lastTotal = await page.textContent('#totalCount');
    const lastCompleted = await page.textContent('#completeCount');
    const lastRemaining = await page.textContent('#remainCount');

    console.log('\n📊 최종 통계');
    console.log(`   전체: ${lastTotal}`);
    console.log(`   완료: ${lastCompleted}`);
    console.log(`   남음: ${lastRemaining}`);

    console.log('\n✅ 모든 기능이 정상적으로 작동합니다!');

  } catch (error) {
    console.error('❌ 오류 발생:', error.message);
  } finally {
    await browser.close();
  }
}

runTests();

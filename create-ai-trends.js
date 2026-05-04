const PptxGenJS = require('pptxgenjs');

const prs = new PptxGenJS();

// 색상 팔레트 - AI 주제에 맞는 현대적인 색상
const colors = {
  darkBlue: '1E3A8A',      // 진한 파란색
  lightBlue: '3B82F6',     // 밝은 파란색
  purple: '8B5CF6',        // 보라색
  pink: 'EC4899',          // 분홍색
  white: 'FFFFFF',
  darkGray: '1F2937',
  lightGray: 'F3F4F6'
};

// 슬라이드 생성 - 1개
const slide = prs.addSlide();
slide.background = { color: colors.darkBlue };

// 제목 - 상단
slide.addText('2026 AI 기술 트랜드', {
  x: 0.5,
  y: 0.4,
  w: 9,
  h: 0.8,
  fontSize: 44,
  bold: true,
  color: colors.white,
  fontFace: 'Arial',
  align: 'left'
});

// 구분선
slide.addShape(prs.ShapeType.rect, {
  x: 0.5,
  y: 1.3,
  w: 1.2,
  h: 0.08,
  fill: { color: colors.pink },
  line: { type: 'none' }
});

// 5가지 주요 트랜드 - 컬럼 레이아웃
const trends = [
  {
    title: '🤖 멀티모달 AI',
    desc: '텍스트·이미지·음성·영상을 통합 처리하는 AI 모델 확산',
    color: colors.lightBlue
  },
  {
    title: '⚡ 에지 AI',
    desc: '클라우드 없이 기기에서 직접 AI 실행하는 기술',
    color: colors.purple
  },
  {
    title: '🧠 추론 AI',
    desc: '복잡한 문제를 단계별로 해결하는 고도의 사고형 AI',
    color: colors.pink
  },
  {
    title: '🔒 AI 보안',
    desc: '데이터 개인정보보호와 모델 방어 기술 강화',
    color: colors.lightBlue
  },
  {
    title: '💰 AI 효율화',
    desc: '더 적은 비용과 자원으로 고성능 달성',
    color: colors.purple
  }
];

const startY = 2.0;
const cardHeight = 1.0;
const cardSpacing = 0.15;
const cardWidth = 8.5;

trends.forEach((trend, idx) => {
  const yPos = startY + (idx * (cardHeight + cardSpacing));

  // 카드 배경
  slide.addShape(prs.ShapeType.rect, {
    x: 0.5,
    y: yPos,
    w: cardWidth,
    h: cardHeight,
    fill: { color: trend.color },
    line: { type: 'none' },
    shadow: {
      type: 'outer',
      blur: 8,
      opacity: 0.3,
      angle: 45,
      color: '000000'
    }
  });

  // 제목 텍스트
  slide.addText(trend.title, {
    x: 0.8,
    y: yPos + 0.1,
    w: cardWidth - 0.6,
    h: 0.35,
    fontSize: 16,
    bold: true,
    color: colors.white,
    fontFace: 'Arial',
    align: 'left'
  });

  // 설명 텍스트
  slide.addText(trend.desc, {
    x: 0.8,
    y: yPos + 0.45,
    w: cardWidth - 0.6,
    h: 0.45,
    fontSize: 12,
    color: colors.white,
    fontFace: 'Arial',
    align: 'left'
  });
});

// 하단 요약
slide.addShape(prs.ShapeType.rect, {
  x: 0.5,
  y: 8.6,
  w: 8.5,
  h: 0.7,
  fill: { color: colors.lightGray },
  line: { type: 'none' }
});

slide.addText('💡 핵심: AI는 더 스마트하고, 더 빠르고, 더 안전하게 진화하고 있습니다.', {
  x: 0.7,
  y: 8.7,
  w: 8.1,
  h: 0.5,
  fontSize: 13,
  bold: true,
  color: colors.darkBlue,
  fontFace: 'Arial',
  align: 'left'
});

// 파일 저장
const outputPath = 'AI_Trends_2026.pptx';
prs.writeFile({ fileName: outputPath });

console.log(`✅ PPTX 생성 완료: ${outputPath}`);

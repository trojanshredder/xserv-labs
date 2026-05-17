const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1440, height: 1400 } });
  await p.goto('http://localhost:8765/blog/', { waitUntil: 'networkidle' });
  await p.waitForTimeout(1500);
  await p.screenshot({ path: '_audit_blog_final.png' });
  console.log('ok');
  await b.close();
})();

const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1440, height: 600 } });
  await p.goto('http://localhost:8765/blog/', { waitUntil: 'networkidle' });
  await p.waitForTimeout(1500);
  const nav = await p.$('header.site-header');
  if (nav) await nav.screenshot({ path: '_audit_blog_nav.png' });
  await p.screenshot({ path: '_audit_blog_top.png' });
  await b.close();
  console.log('ok');
})();

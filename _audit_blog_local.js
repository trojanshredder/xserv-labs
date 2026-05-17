const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1440, height: 700 } });
  const file = 'file://' + path.resolve(__dirname, 'blog/index.html').replace(/\\/g, '/');
  await page.goto(file, { waitUntil: 'networkidle' });
  await page.waitForTimeout(1500);
  await page.screenshot({ path: '_audit_blog_local_top.png' });
  // Crop just the nav
  const nav = await page.$('header.site-header');
  if (nav) await nav.screenshot({ path: '_audit_blog_nav.png' });
  await browser.close();
  console.log('ok');
})();

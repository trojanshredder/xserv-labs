const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  await page.goto('https://xservlabs.com/blog/?nocache=' + Date.now(), { waitUntil: 'networkidle' });
  await page.waitForTimeout(1800);
  await page.screenshot({ path: '_audit_blog_top.png' });

  // Logo crop
  const logo = await page.$('.logo');
  if (logo) await logo.screenshot({ path: '_audit_blog_logo.png' });

  // Also check a blog post
  await page.goto('https://xservlabs.com/blog/cost-to-build-erp-in-india/?nocache=' + Date.now(), { waitUntil: 'networkidle' });
  await page.waitForTimeout(1500);
  await page.screenshot({ path: '_audit_blogpost_top.png' });
  console.log('ok');
  await browser.close();
})();

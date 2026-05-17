// Quick screenshot tool for auditing the live site
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 });
  const page = await ctx.newPage();

  const url = process.argv[2] || 'https://xservlabs.com/';
  const out = process.argv[3] || '_audit_full.png';

  await page.goto(url, { waitUntil: 'networkidle', timeout: 30000 });
  // Allow extra time for animations / lazy loaded content
  await page.waitForTimeout(2000);

  await page.screenshot({ path: out, fullPage: true });
  console.log(`Saved ${out}`);
  await browser.close();
})();

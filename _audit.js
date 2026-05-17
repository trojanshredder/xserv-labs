const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  const file = 'file://' + path.resolve(__dirname, 'index.html').replace(/\\/g, '/');
  await page.goto(file, { waitUntil: 'networkidle' });
  await page.waitForTimeout(1500);
  await page.screenshot({ path: '_audit_after_top.png' });

  await page.evaluate(() => document.querySelector('#services').scrollIntoView());
  await page.waitForTimeout(800);
  await page.screenshot({ path: '_audit_after_services.png' });

  await page.evaluate(() => document.querySelector('#industries').scrollIntoView());
  await page.waitForTimeout(800);
  await page.screenshot({ path: '_audit_after_industries.png' });

  // Also screenshot the deep-nav section specifically
  const sdn = await page.$$('.service-deep-nav');
  for (let i = 0; i < sdn.length; i++) {
    await sdn[i].scrollIntoViewIfNeeded();
    await page.waitForTimeout(500);
    await sdn[i].screenshot({ path: `_audit_sdn_${i}.png` });
  }
  await browser.close();
  console.log('ok');
})();

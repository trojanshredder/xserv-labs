// Audit the live site at 3 key viewports — catch anything that looks off.
const { chromium } = require('playwright');

(async () => {
  const b = await chromium.launch();
  const targets = [
    ['https://xservlabs.com/', '_aud_home', 1440, 900],
    ['https://xservlabs.com/blog/', '_aud_blog', 1440, 700],
    ['https://xservlabs.com/services/erp-software-development/', '_aud_svc', 1440, 700],
    ['https://xservlabs.com/', '_aud_home_mobile', 390, 844],
  ];
  for (const [url, name, w, h] of targets) {
    const p = await b.newPage({ viewport: { width: w, height: h } });
    await p.goto(url + '?t=' + Date.now(), { waitUntil: 'networkidle' });
    await p.waitForTimeout(1800);
    await p.screenshot({ path: `${name}.png` });
    console.log(`${name}.png saved`);
    await p.close();
  }
  await b.close();
})();

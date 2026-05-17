const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1440, height: 800 } });
  for (const [url, name] of [
    ['http://localhost:8765/about/', '_new_about'],
    ['http://localhost:8765/contact/', '_new_contact'],
    ['http://localhost:8765/products/traxium/vs-loginext/', '_new_vs'],
  ]) {
    await p.goto(url, { waitUntil: 'networkidle' });
    await p.waitForTimeout(1200);
    await p.screenshot({ path: `${name}.png` });
    console.log(`${name}.png saved`);
  }
  await b.close();
})();

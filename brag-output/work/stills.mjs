import { chromium } from 'playwright';
import path from 'path';
const times = process.argv.slice(2).map(Number);
const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
await p.goto('file://' + path.resolve('composition.html'));
await p.evaluate(() => window.ready);
for (const t of times) {
  await p.evaluate(t => window.render(t), t);
  await p.screenshot({ path: `still-${t.toFixed(2)}.jpg`, type: 'jpeg', quality: 70 });
}
await b.close();

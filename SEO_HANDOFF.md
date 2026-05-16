# SEO Handoff — XServ Labs

This is the short, actionable list of what's already done on-page, what *you* (a human) need to do next, and what should ship in the coming weeks. A senior SEO strategist agent is producing a deeper plan separately — this file is the operational checklist.

---

## ✅ Phase 1 — Done in this commit (technical foundation)

- **Meta tags**: title, description, keywords, author, robots, theme-color, geo (Hyderabad lat/long), canonical
- **Open Graph + Twitter Cards**: full set, ready for LinkedIn / X / WhatsApp previews
- **JSON-LD structured data**: Organization, LocalBusiness, WebSite (with SearchAction), ProfessionalService with OfferCatalog (all 9 services), SoftwareApplication entries for Traxium & Praxate, FAQPage
- **H1 moved into static HTML** (was being injected by JS — bad for crawlers)
- **Semantic landmarks**: `<header>`, `<main>`, `<footer>`, `aria-label`s on nav
- **`rel="noopener"` added** to all `target="_blank"` links (security + minor perf)
- **Praxate footer link**: upgraded from `http://` to `https://`
- **`robots.txt`** + **`sitemap.xml`** created
- **404.html** rewritten — branded, no auto-redirect (auto-redirects from 404 hurt SEO)
- **`site.webmanifest`** + **`favicon.svg`** created
- **Performance**: preconnect to unpkg + cdnjs, `defer` on Spline + Lottie

---

## 🔴 You need to do these **right now** (won't take long)

### 1. Generate raster favicons & OG image
SVG favicon is in place but you need PNG fallbacks. Use [realfavicongenerator.net](https://realfavicongenerator.net) — upload `favicon.svg`, download the package, drop these files in the project root:

- `favicon-16.png` (16×16)
- `favicon-32.png` (32×32)
- `favicon-192.png` (192×192)
- `favicon-512.png` (512×512)
- `favicon-512-maskable.png` (512×512, with safe-area padding)
- `apple-touch-icon.png` (180×180)
- `logo.png` (512×512, used in JSON-LD Organization)

### 2. Create the OG image — **most important social asset**
- File: `og-image.png` in project root
- Size: **1200×630 px** exactly
- Design: dark background (#0A0A0A), the XServ Labs logomark + "Software for the industries that move the world" + tag line. Use the orange (#F97316) accent.
- Tools: Figma, Canva (`Open Graph` template), or [og-image.vercel.app](https://og-image.vercel.app/)
- Test once live: [opengraph.xyz](https://www.opengraph.xyz/) and LinkedIn Post Inspector.

### 3. Update social URLs in JSON-LD
In [index.html](index.html), find the `sameAs` block (around the Organization schema) and replace the placeholders with your **real** profile URLs:

```
"https://www.linkedin.com/company/xservlabs",
"https://github.com/xservlabs",
"https://x.com/xservlabs"
```

If a profile doesn't exist yet, **create it** (LinkedIn Company Page especially — major SEO trust signal).

---

## 🟡 You need to do these **this week** (off-page foundation)

### 4. Google Search Console
1. Go to [search.google.com/search-console](https://search.google.com/search-console).
2. Add property → Domain: `xservlabs.com` (preferred) or URL prefix `https://xservlabs.com/`.
3. Verify via DNS TXT record (domain) or HTML meta tag (URL prefix — paste it into [index.html](index.html) head).
4. Once verified: **Sitemaps** → submit `https://xservlabs.com/sitemap.xml`.
5. Request indexing for the homepage via the URL Inspection tool.

### 5. Bing Webmaster Tools
- [bing.com/webmasters](https://www.bing.com/webmasters). Easiest path: import from GSC after step 4.
- Submit the sitemap there too.

### 6. Google Business Profile (huge for "near me" + Hyderabad queries)
- [business.google.com](https://business.google.com).
- Category: "Software company" (primary) + "Website designer", "Computer consultant" (secondary).
- Add real photos of your office + team. **Crucial** — listings with 10+ photos get ~35% more clicks.
- Get the first 10 reviews from existing clients within 30 days. Ask via WhatsApp with a direct review link.

### 7. Analytics
- Install **Google Analytics 4** + **Microsoft Clarity** (free heatmaps & session replay). Drop the tags right before `</head>`.

### 8. Submit to high-authority directories
Priority order (do this week):
1. **Clutch.co** — software company directory; high DR; clients can leave reviews
2. **GoodFirms** — similar to Clutch
3. **DesignRush** — premium B2B agency directory
4. **Crunchbase** — company profile
5. **G2** + **Capterra** — list Traxium & Praxate
6. **LinkedIn Company Page**
7. **IndiaMART** + **Sulekha** (India-specific)
8. **TheManifest**

---

## 🟢 Next 30 days (content + structure)

The single-page architecture caps your ranking ceiling. You need **dedicated pages** so each can target a distinct keyword cluster. Priority order:

1. `/services/custom-software-development/`
2. `/services/ai-and-machine-learning/`
3. `/services/erp-development/`
4. `/services/mobile-app-development/`
5. `/products/traxium/` (case study + landing)
6. `/products/praxate/`
7. `/industries/logistics/`
8. `/industries/manufacturing/`
9. `/blog/` with 4–6 cornerstone articles

The strategist agent's output (delivered separately in this session) will include exact keyword targets, titles, and word counts for each.

---

## 📊 Track these from day one

| Metric | Tool | Target by Day 90 |
|---|---|---|
| Branded keyword position ("XServ Labs") | GSC | #1 |
| Indexed pages | GSC | All shipped pages indexed within 7 days |
| Total organic clicks/mo | GSC | 500+ |
| Backlinks (referring domains) | Ahrefs Webmaster Tools (free) | 25+ |
| Google Business Profile actions | GBP dashboard | 50+ direction/call clicks/mo |
| Core Web Vitals — LCP, INP, CLS | PageSpeed Insights | All "Good" |

---

## ⚠️ Don't do these (common mistakes)

- ❌ Don't buy backlinks from Fiverr / cheap SEO packages. Penalty risk is real.
- ❌ Don't keyword-stuff. The homepage copy is good — keep it natural.
- ❌ Don't redirect 404s with `<meta refresh>` (we already removed this).
- ❌ Don't change the canonical URL or move the site without 301 redirects in place.
- ❌ Don't use AI to mass-generate blog content. Google's helpful-content system penalizes it. Use AI to *assist* a human writer, not replace one.

---

## Files changed in this commit
- `index.html` — full SEO head, JSON-LD, semantic landmarks, static H1
- `404.html` — rebuilt
- `robots.txt` — new
- `sitemap.xml` — new
- `site.webmanifest` — new
- `favicon.svg` — new
- `SEO_HANDOFF.md` — this file

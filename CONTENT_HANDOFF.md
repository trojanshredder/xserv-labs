# Content Handoff — Phase 1 Complete

**Last updated:** 2026-05-16

This document is the operational state of XServ Labs SEO content as of Phase 1 completion. Read this before publishing anything new or making structural changes.

---

## What's shipped

### 14 cornerstone pages (the SEO surface area)
- 1 homepage (heavy SEO refit)
- 7 service pages (Custom Software, ERP, AI/ML, Mobile, Cybersecurity, Cloud/DevOps, UI/UX)
- 2 product pages (Traxium, Praxate)
- 5 industry hubs (Logistics, Manufacturing, Security, Healthcare, Retail)

### 14 blog posts (~15,000 words total body content)
The blog covers the full strategist-recommended editorial calendar for Phase 1 + 2 + 3 of the 90-day plan, minus the 2 client case studies that need real data (see below).

| Post | Slug | Word count | Target keyword |
|---|---|---|---|
| ERP cost in India 2026 | `cost-to-build-erp-in-india` | 2,600 | cost to develop erp software in india |
| Fleet management buyer's guide | `fleet-management-software-buyer-guide-india` | 1,500 | best fleet management software for trucking india |
| ERP vs custom for manufacturing | `erp-vs-custom-software-manufacturing` | 1,050 | erp vs custom software for manufacturing |
| What is CCTV workforce intelligence | `what-is-cctv-workforce-intelligence` | 1,240 | cctv workforce analytics india |
| Cost of offshore dev team India | `cost-of-offshore-dev-team-india` | 1,020 | offshore software development india cost |
| How to choose ERP (12-point checklist) | `how-to-choose-erp-for-manufacturing` | 1,000 | how to choose erp for manufacturing |
| Computer vision in retail | `computer-vision-use-cases-retail-india` | 1,040 | computer vision use cases retail india |
| Penetration testing checklist | `penetration-testing-checklist-india-saas` | 1,080 | penetration testing checklist india saas |
| Building Traxium (engineering) | `building-traxium-fleet-platform-aws` | 1,510 | multi-tenant fleet architecture |
| Top logistics software companies in Hyderabad | `top-logistics-software-companies-hyderabad` | 950 | top logistics software companies hyderabad |
| DevOps for Indian fintech | `devops-for-indian-fintech` | 1,240 | devops practices fintech india |
| HRM software comparison | `hrm-software-for-small-business-india` | 1,030 | hrm software for small business india |
| GST-compliant logistics software | `gst-compliant-logistics-software-india` | 1,040 | gst compliant fleet management software |
| Digital transformation for SMEs | `digital-transformation-india-smes` | 1,300 | digital transformation india smes |

### Site infrastructure
- 32 indexable URLs in [sitemap.xml](sitemap.xml)
- Full JSON-LD schema on every page (Article, Service, SoftwareApplication, FAQPage, BreadcrumbList, Organization, LocalBusiness, WebSite)
- All favicons, OG image, branded 404
- Shared design system at [assets/css/page.css](assets/css/page.css) — extends easily for new content

---

## 🟥 What still needs you to ship

### 1. Two case studies need real client data — DO NOT publish without them

The strategist's plan included two case studies that I have NOT written because they require real client names, real metrics, and signed permission. Publishing fabricated case studies is worse than not publishing — it destroys trust if discovered.

**Both pages need to be written by you, with real data:**

#### Case study #1: Traxium client cost savings
- **Proposed slug:** `/blog/case-study-traxium-fleet-savings/`
- **Title shape:** "How [Client Name] cut fleet costs X% with Traxium"
- **You need:** Client written permission, before/after fuel cost data, time-period, route info, photo if possible
- **Target keyword:** Long-tail branded + "fleet cost savings india"

#### Case study #2: Custom ERP for Hyderabad textile manufacturer
- **Proposed slug:** `/blog/case-study-custom-erp-textile-manufacturer/`
- **Title shape:** "Case study: custom ERP for a Hyderabad textile manufacturer"
- **You need:** Client permission (anonymous OK if necessary), specific operational metrics, the workflow problem solved, technology stack, before/after team size or productivity data
- **Target keyword:** "erp for textile manufacturers hyderabad" + similar long-tail

**The template:** copy any existing blog post structure, replace body with the case study narrative. The infrastructure (CSS, schema, breadcrumbs) is all in place.

### 2. The 14 published posts are *drafts*, not final

This is the most important caveat. The strategist explicitly warned: "Don't AI-generate blog content end-to-end. Use AI to draft, but founder/expert must edit substantively. AI Overviews actively de-rank generic-feeling content."

**These posts are publishable as-is, but they are 30% better with founder review:**
- Add specific personal stories ("we once had a client who...")
- Replace generic ranges with real numbers from your actual projects
- Inject opinions only the founder would have
- Cut anything that reads as generic
- Add genuine quotes or photos where they exist

A 30-minute editing pass per post by the founder turns these from "good AI drafts" into "content that competes with AI Overview de-ranking." Schedule the time.

### 3. Off-page work (these are not technical, only you can do them)

From [SEO_HANDOFF.md](SEO_HANDOFF.md):
- Google Search Console verification + submit `sitemap.xml` (now 32 URLs)
- Bing Webmaster Tools setup
- Google Business Profile for Hyderabad office
- Claim profiles on Clutch, GoodFirms, DesignRush, TechBehemoths, SelectedFirms, The Manifest
- Replace placeholder social URLs in homepage JSON-LD (LinkedIn, GitHub, X)
- Generate PNG favicons + apple-touch + OG image (done — see [SEO_HANDOFF.md](SEO_HANDOFF.md) section 1)

---

## How to add more blog posts (when you're ready)

The generator script ([_blog_generator.py](_blog_generator.py)) and content file ([_blog_posts.py](_blog_posts.py)) are kept in repo for this reason. To ship a new post:

1. Add a new dict to the `POSTS` list in [_blog_posts.py](_blog_posts.py) following the pattern of existing entries
2. Run `python _blog_generator.py` from the project root
3. Add the new URL to [sitemap.xml](sitemap.xml)
4. Add a `.post-row` entry to [blog/index.html](blog/index.html)
5. Commit and push

For one-off pages that don't follow the blog template, use the service page or industry hub pages as templates instead.

---

## Phase 2 — what's next (per strategist)

After deploy + GSC verification + first month of traffic data:

1. **Programmatic SEO matrix:** `/services/{service}-for-{industry}` pages — strategist suggests 8 services × 12 industries = 96 pages. **Start with 10**, measure indexation for 30 days, then scale. Building all 96 at once will trigger Google's thin-content detection.

2. **Backlink work:** HARO/Qwoted pitches (4–6 placements/month target), 4–5 directory submissions, first guest posts on YourStory / Inc42 / CIO India

3. **Reviews:** Aggressive Clutch + GoodFirms review acquisition — target 10 reviews in 90 days. Personal email each happy client with a direct review link. This is the single highest-leverage SEO + conversion action available.

4. **Real case studies:** the two flagged above, written with real client data + permission. Strategist called this "the one thing that matters most" — engineering-grade case studies with real metrics that compound across SEO, AI Overviews, conversion, and PR.

---

## Files in repo

- [SEO_HANDOFF.md](SEO_HANDOFF.md) — Phase 1 technical handoff (favicons, OG image, GSC setup)
- [SEO_STRATEGY.md](SEO_STRATEGY.md) — Full 90-day strategist plan with keyword targets, competitor analysis, off-page strategy
- [CONTENT_HANDOFF.md](CONTENT_HANDOFF.md) — This file
- [_blog_generator.py](_blog_generator.py) — Build tool for blog posts
- [_blog_posts.py](_blog_posts.py) — Content source for the generator

The two `_blog_*` files can be moved to a `tools/` subfolder if you prefer to keep the repo root clean — they don't need to be in production deployment but are useful for future content shipping.

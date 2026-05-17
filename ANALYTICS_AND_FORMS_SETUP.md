# Analytics &amp; Contact Form — Setup Guide

Total time: **~20 minutes**. After this, you'll have analytics on all 44 pages and a working contact form, with no further code changes.

---

## Part 1: Activate analytics (10 minutes)

You only edit **one file**: [assets/js/analytics.js](assets/js/analytics.js).

The script is already injected into every page on the site. The placeholders are inert — until you replace them, nothing fires, nothing is tracked, no external calls.

### Step 1: Google Analytics 4 (free, takes 5 min)

1. Go to **https://analytics.google.com**
2. Sign in with your Google account → Click "Start measuring"
3. Account name: `XServ Labs` → Next
4. Property name: `xservlabs.com` → Time zone: India → Currency: INR → Next
5. Business info → answer roughly → Create
6. Choose a platform: **Web**
7. Website URL: `https://xservlabs.com` → Stream name: `xservlabs.com` → Create stream
8. **Copy the Measurement ID** (looks like `G-ABC1234567`)

### Step 2: Microsoft Clarity (free heatmaps + session replay, takes 3 min)

1. Go to **https://clarity.microsoft.com**
2. Sign in with Google / Microsoft / LinkedIn → "Add new project"
3. Project name: `XServ Labs` → Website URL: `https://xservlabs.com` → Category: `Technology / Software` → Create
4. Settings → Setup → **Copy the Project ID** (10-character alphanumeric)

### Step 3: Paste both IDs into the analytics file

Open [assets/js/analytics.js](assets/js/analytics.js) and find these two lines near the top:

```javascript
var GA4_MEASUREMENT_ID = 'REPLACE_WITH_GA4_ID';      // e.g. 'G-ABC1234567'
var CLARITY_PROJECT_ID = 'REPLACE_WITH_CLARITY_ID';  // e.g. 'abc1234567'
```

Replace both. Save. Commit + push:

```bash
git add assets/js/analytics.js
git commit -m "Activate GA4 and Microsoft Clarity"
git push
```

Within 60 seconds, every page on the site is tracked.

### What you'll see

- **GA4** → real-time visitor count within minutes. After 24h: traffic sources, page views, conversion events (we already track WhatsApp clicks, phone clicks, form submits)
- **Clarity** → session replay videos of real visitors within 30 minutes. Heatmaps after 100+ sessions.

---

## Part 2: Activate the contact form (10 minutes)

The contact form on [/contact/](contact/) is built and styled. Right now if a visitor submits it, the form falls back to opening their email client (mailto) — so it never breaks. But you want real form submissions to your inbox. We use **Formspree** (free for up to 50 submissions/month, paid above).

### Step 1: Sign up for Formspree

1. Go to **https://formspree.io** → Click "Get started"
2. Sign up with your email → Verify
3. Create a new form → Name: `XServ Labs Contact` → Email: where you want submissions to land (e.g. `hello@xservlabs.com`)
4. **Copy the form endpoint** — looks like `https://formspree.io/f/xabc1234`. You only need the part after `/f/` (the form ID, like `xabc1234`).

### Step 2: Paste the form ID

Open [contact/index.html](contact/index.html) and find this line:

```html
action="https://formspree.io/f/REPLACE_WITH_FORMSPREE_FORM_ID"
```

Replace `REPLACE_WITH_FORMSPREE_FORM_ID` with your form ID (e.g. `xabc1234`). Save, commit, push:

```bash
git add contact/index.html
git commit -m "Activate Formspree contact form"
git push
```

Test it by submitting the form on [https://xservlabs.com/contact/](https://xservlabs.com/contact/).

### How Formspree handles spam

- **Honeypot field** built into the form — most bots are blocked automatically
- Formspree's own spam filter on top
- You can add reCAPTCHA in Formspree settings if needed

### Upgrading later

If you exceed 50 submissions/month, Formspree's paid plan is $10/month. Or migrate to:
- **Web3Forms** (free unlimited) — simpler, less polished dashboard
- **Netlify Forms** (free with Netlify hosting, paid above) — would require migrating off GitHub Pages
- Your own backend if you want full control

---

## Part 3: Verify Google Search Console (5 minutes — separate from above but should be done same day)

GSC is what lets you actually see Google indexing data, search rankings, and click-through rates.

1. Go to **https://search.google.com/search-console**
2. Add property → **Domain** → `xservlabs.com`
3. Choose verification method: **DNS TXT record** (most reliable)
4. Copy the TXT record value Google gives you
5. Log into your DNS provider (wherever you bought the domain — GoDaddy, Cloudflare, Namecheap, etc.)
6. Add a new TXT record at the root (`@`) with the value Google gave you
7. Back in GSC, click "Verify". Wait up to 60 minutes if it doesn't verify immediately.
8. Once verified: **Sitemaps** in left nav → submit `https://xservlabs.com/sitemap.xml`

### Same for Bing Webmaster Tools

After GSC is verified:
1. Go to **https://www.bing.com/webmasters**
2. Sign in → "Import from Google Search Console" (easiest path)
3. Submit the same sitemap

---

## What you can ignore (for now)

- **Tag Manager (GTM)** — only useful if you'll add many tracking tools. GA4 + Clarity direct is fine for now.
- **Cookie consent banner** — required by GDPR and DPDP Act for EU/India PII collection. GA4 by default doesn't collect PII (we set `anonymize_ip: true`), so you're in a safer position. But for full DPDP/GDPR compliance, add a consent banner (Cookiebot, OneTrust, or a simple custom one) before you start running paid ads to EU/UK.
- **Facebook Pixel / LinkedIn Insight Tag** — only needed if you're running paid ads on those platforms.

---

## TL;DR

**Three things to do today:**
1. Get GA4 + Clarity IDs → paste into `assets/js/analytics.js`
2. Get Formspree ID → paste into `contact/index.html`
3. Verify GSC + Bing → submit sitemap

**Total time: ~20 minutes.**

After that, you have a fully measured, conversion-ready site that's discoverable by every major search engine. The rest is content + backlinks + reviews — covered in [OUTREACH_TEMPLATES.md](OUTREACH_TEMPLATES.md).

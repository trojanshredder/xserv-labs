#!/usr/bin/env python3
"""
Programmatic SEO page generator — /services/{service}-for-{industry}/
Used to ship industry-specific service landing pages efficiently.
After all pages are generated, this file can be deleted.
"""
import os, json
ROOT = os.path.dirname(os.path.abspath(__file__))

WHATSAPP_SVG = '''<svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.498 14.382c-.301-.15-1.767-.867-2.04-.966-.273-.101-.473-.15-.673.15-.197.295-.771.964-.944 1.162-.175.195-.349.21-.646.075-.3-.15-1.263-.465-2.403-1.485-.888-.795-1.484-1.77-1.66-2.07-.174-.3-.019-.465.13-.615.136-.135.301-.345.451-.523.146-.181.194-.301.297-.496.1-.21.049-.375-.025-.524-.075-.15-.672-1.62-.922-2.205-.24-.585-.487-.51-.672-.51-.172-.015-.371-.015-.571-.015-.2 0-.523.074-.797.359-.273.3-1.045 1.02-1.045 2.475s1.07 2.865 1.219 3.075c.149.195 2.105 3.195 5.1 4.485.714.3 1.27.48 1.704.629.714.227 1.365.195 1.88.121.574-.091 1.767-.721 2.016-1.426.255-.705.255-1.29.18-1.425-.074-.135-.27-.21-.57-.345m-5.446 7.443h-.016c-1.77 0-3.524-.48-5.055-1.38l-.36-.214-3.75.975 1.005-3.645-.239-.375a9.869 9.869 0 0 1-1.516-5.26c.002-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.885-9.885 9.885M20.52 3.449C18.24 1.245 15.24 0 12.045 0 5.463 0 .104 5.334.101 11.893c0 2.096.549 4.14 1.595 5.945L0 24l6.335-1.652a12.062 12.062 0 0 0 5.71 1.447h.006c6.585 0 11.946-5.336 11.949-11.896 0-3.176-1.24-6.165-3.495-8.411"/></svg>'''


def build_page(p):
    slug = p["slug"]
    canonical = f"https://xservlabs.com/services/{slug}/"
    og_img = "https://xservlabs.com/og-image.png"

    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Service",
                "name": p["service_name"],
                "serviceType": p["service_type"],
                "provider": {
                    "@type": "Organization",
                    "name": "XServ Labs",
                    "url": "https://xservlabs.com/",
                    "logo": "https://xservlabs.com/logo.png",
                    "address": {"@type": "PostalAddress", "addressLocality": "Hyderabad", "addressRegion": "Telangana", "addressCountry": "IN"}
                },
                "areaServed": {"@type": "Country", "name": "India"},
                "description": p["description"],
                "url": canonical
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://xservlabs.com/"},
                    {"@type": "ListItem", "position": 2, "name": "Services", "item": "https://xservlabs.com/#services"},
                    {"@type": "ListItem", "position": 3, "name": p["crumb"], "item": canonical}
                ]
            }
        ]
    }
    if p.get("faq"):
        schema["@graph"].append({
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
                for q, a in p["faq"]
            ]
        })

    related_html = ""
    for r in p["related"]:
        related_html += f'''    <a href="{r["href"]}"><div class="ttl">{r["ttl"]}</div><div class="desc">{r["desc"]}</div></a>\n'''

    chips_html = ""
    for chip in p.get("chips", []):
        chips_html += f'    <span class="chip">{chip}</span>\n'

    pain_points = ""
    for pp in p["pain_points"]:
        pain_points += f"      <li>{pp}</li>\n"

    capabilities = ""
    for cap_title, cap_desc in p["capabilities"]:
        capabilities += f'''    <div class="feat-card">
      <div class="ic"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg></div>
      <h3>{cap_title}</h3>
      <p>{cap_desc}</p>
    </div>
'''

    wa_link = p.get("cta_wa", f"https://wa.me/918897599624?text=Hi%2C%20I%27d%20like%20to%20discuss%20{p['slug']}.")

    schema_str = json.dumps(schema, indent=2, ensure_ascii=False)

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>{p["title"]} — XServ Labs</title>
<meta name="description" content="{p["description"]}">
<meta name="keywords" content="{p["keywords"]}">
<meta name="author" content="XServ Labs">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<meta name="theme-color" content="#0A0A0A">
<link rel="canonical" href="{canonical}">

<meta property="og:type" content="article">
<meta property="og:site_name" content="XServ Labs">
<meta property="og:title" content="{p["title"]}">
<meta property="og:description" content="{p["description"]}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_img}">
<meta property="og:locale" content="en_IN">

<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{p["title"]}">
<meta name="twitter:description" content="{p["description"]}">
<meta name="twitter:image" content="{og_img}">

<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Instrument+Serif:ital@0;1&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/page.css">
<script src="/assets/js/analytics.js" defer></script>

<script type="application/ld+json">
{schema_str}
</script>
</head>
<body>

<header class="site-header" role="banner">
  <nav class="nav" aria-label="Primary">
    <a href="/" class="logo" aria-label="XServ Labs — home">
      <div class="logo-mark" aria-hidden="true">
        <div class="orbit orbit-1"><div class="orbit-dot od-1"></div></div>
        <div class="orbit orbit-2"><div class="orbit-dot od-2"></div></div>
        <div class="orbit orbit-3"><div class="orbit-dot od-3"></div></div>
        <span class="logo-x">X</span>
      </div>
      <span class="logo-text">XServ Labs</span>
    </a>
    <ul class="nav-links">
      <li><a href="/about/">About</a></li>
      <li><a href="/#services">Services</a></li>
      <li><a href="/#products">Products</a></li>
      <li><a href="/#industries">Industries</a></li>
      <li><a href="/blog/">Blog</a></li>
      <li class="nav-cta-li"><a href="/contact/" class="nav-cta">Get in Touch</a></li>
    </ul>
  </nav>
</header>

<main id="main">

<nav class="crumbs" aria-label="Breadcrumb">
  <a href="/">Home</a><span class="sep">/</span><a href="/#services">Services</a><span class="sep">/</span><span class="cur">{p["crumb"]}</span>
</nav>

<section class="page-hero">
  <div class="eyebrow">{p["eyebrow"]}</div>
  <h1>{p["h1"]}</h1>
  <p class="lede">{p["lede"]}</p>
  <div class="hero-cta">
    <a href="{wa_link}" class="btn btn-primary" target="_blank" rel="noopener">{p["cta1"]}</a>
    <a href="{p["cta2_href"]}" class="btn btn-ghost">{p["cta2"]}</a>
  </div>
</section>

<div class="trust-strip">
  <div class="item"><div class="num">{p["stat1_num"]}</div><div class="lbl">{p["stat1_lbl"]}</div></div>
  <div class="item"><div class="num">{p["stat2_num"]}</div><div class="lbl">{p["stat2_lbl"]}</div></div>
  <div class="item"><div class="num">{p["stat3_num"]}</div><div class="lbl">{p["stat3_lbl"]}</div></div>
  <div class="item"><div class="num">{p["stat4_num"]}</div><div class="lbl">{p["stat4_lbl"]}</div></div>
</div>

<section class="section">
  <div class="label">{p["why_label"]}</div>
  <h2>{p["why_h2"]}</h2>
  <p class="intro">{p["why_intro"]}</p>
  <ul class="check-list">
{pain_points}  </ul>
</section>

<section class="section" style="border-top: 1px solid var(--border);">
  <div class="label">What we build</div>
  <h2>{p["what_h2"]}</h2>
  <p class="intro">{p["what_intro"]}</p>

  <div class="feat-grid">
{capabilities}  </div>
</section>

<section class="section">
  <div class="label">{p["approach_label"]}</div>
  <h2>{p["approach_h2"]}</h2>
  <div class="two-col">
    <div>
      <h3>{p["approach_left_h3"]}</h3>
      <p>{p["approach_left_p"]}</p>
    </div>
    <div>
      <h3>{p["approach_right_h3"]}</h3>
      <p>{p["approach_right_p"]}</p>
    </div>
  </div>
</section>

{('<section class="section" style="border-top: 1px solid var(--border);"><div class="label">Where it fits</div><h2>' + p.get("chips_h2", "Sub-sectors we have shipped for.") + '</h2><div class="chips">' + chips_html + '</div></section>') if p.get("chips") else ""}

<section class="section" style="border-top: 1px solid var(--border);">
  <div class="label">Common questions</div>
  <h2>Direct answers.</h2>
  <div class="faq">
{''.join(f'    <details><summary>{q}</summary><p>{a}</p></details>' + chr(10) for q, a in p["faq"])}  </div>
</section>

<div class="cta-block">
  <h2>{p["final_cta_h2"]}</h2>
  <p>{p["final_cta_p"]}</p>
  <div class="cta-actions">
    <a href="{wa_link}" class="btn btn-primary" target="_blank" rel="noopener">WhatsApp us</a>
    <a href="tel:+918897599624" class="btn btn-ghost">Call +91 88975 99624</a>
  </div>
</div>

<section class="related">
  <h3>Related</h3>
  <div class="grid">
{related_html.rstrip()}
  </div>
</section>

</main>

<footer class="site-footer" role="contentinfo">
  <div>&copy; 2026 XServ Labs · Hyderabad, India</div>
  <nav class="foot-links" aria-label="Footer">
    <a href="/">Home</a><a href="/#services">Services</a><a href="/#products">Products</a><a href="/blog/">Blog</a>
    <a href="/privacy-policy/">Privacy</a><a href="/terms-of-service/">Terms</a><a href="https://wa.me/918897599624" target="_blank" rel="noopener">WhatsApp</a><a href="tel:+918897599624">Call</a>
  </nav>
</footer>

<a href="{wa_link}" class="wa-float" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">
  {WHATSAPP_SVG}
</a>

</body>
</html>
'''


def write_page(p):
    out_dir = os.path.join(ROOT, "services", p["slug"])
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(build_page(p))
    return out_path


if __name__ == "__main__":
    from _prog_pages import PAGES
    for p in PAGES:
        path = write_page(p)
        print(f"wrote {path}  ({os.path.getsize(path):,} bytes)")

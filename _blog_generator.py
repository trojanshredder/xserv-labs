#!/usr/bin/env python3
"""
Internal blog generator — used to ship Phase 1 cornerstone content efficiently.
Each post supplies meta + body markdown-like blocks; this wraps them in the
standard XServ Labs article template with schema, breadcrumbs, byline, CTA.

After generation, this file can be deleted — it's a one-time scaffolding tool.
"""
import os, json, html as html_lib

ROOT = os.path.dirname(os.path.abspath(__file__))

WHATSAPP_SVG = '''<svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.498 14.382c-.301-.15-1.767-.867-2.04-.966-.273-.101-.473-.15-.673.15-.197.295-.771.964-.944 1.162-.175.195-.349.21-.646.075-.3-.15-1.263-.465-2.403-1.485-.888-.795-1.484-1.77-1.66-2.07-.174-.3-.019-.465.13-.615.136-.135.301-.345.451-.523.146-.181.194-.301.297-.496.1-.21.049-.375-.025-.524-.075-.15-.672-1.62-.922-2.205-.24-.585-.487-.51-.672-.51-.172-.015-.371-.015-.571-.015-.2 0-.523.074-.797.359-.273.3-1.045 1.02-1.045 2.475s1.07 2.865 1.219 3.075c.149.195 2.105 3.195 5.1 4.485.714.3 1.27.48 1.704.629.714.227 1.365.195 1.88.121.574-.091 1.767-.721 2.016-1.426.255-.705.255-1.29.18-1.425-.074-.135-.27-.21-.57-.345m-5.446 7.443h-.016c-1.77 0-3.524-.48-5.055-1.38l-.36-.214-3.75.975 1.005-3.645-.239-.375a9.869 9.869 0 0 1-1.516-5.26c.002-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.885-9.885 9.885M20.52 3.449C18.24 1.245 15.24 0 12.045 0 5.463 0 .104 5.334.101 11.893c0 2.096.549 4.14 1.595 5.945L0 24l6.335-1.652a12.062 12.062 0 0 0 5.71 1.447h.006c6.585 0 11.946-5.336 11.949-11.896 0-3.176-1.24-6.165-3.495-8.411"/></svg>'''


def build_article(p):
    """Render a full HTML article page from a dict `p`."""
    faq_jsonld = ""
    if p.get("faq"):
        faq_items = []
        for q, a in p["faq"]:
            faq_items.append({
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a}
            })
        faq_jsonld = ",\n    " + json.dumps({
            "@type": "FAQPage",
            "mainEntity": faq_items
        }, indent=2, ensure_ascii=False).replace("\n", "\n    ")

    related_html = ""
    for r in p["related"]:
        related_html += f'''        <a href="{r["href"]}"><div class="ttl">{r["ttl"]}</div><div class="desc">{r["desc"]}</div></a>\n'''

    slug = p["slug"]
    canonical = f"https://xservlabs.com/blog/{slug}/"
    og_img = "https://xservlabs.com/og-image.png"
    wa_link = f'https://wa.me/918897599624?text=Hi%20XServ%2C%20I%27d%20like%20to%20discuss%20a%20project.'

    body_html = p["body_html"].strip()

    article_jsonld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Article",
                "@id": f"{canonical}#article",
                "headline": p["title_plain"],
                "description": p["description"],
                "image": og_img,
                "datePublished": "2026-05-16T10:00:00+05:30",
                "dateModified": "2026-05-16T10:00:00+05:30",
                "author": {"@type": "Organization", "name": "XServ Labs", "url": "https://xservlabs.com/"},
                "publisher": {
                    "@type": "Organization",
                    "name": "XServ Labs",
                    "logo": {"@type": "ImageObject", "url": "https://xservlabs.com/logo.png"}
                },
                "mainEntityOfPage": canonical,
                "articleSection": p["tag"],
                "keywords": p["keywords_array"],
                "wordCount": p.get("word_count", 2000)
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://xservlabs.com/"},
                    {"@type": "ListItem", "position": 2, "name": "Blog", "item": "https://xservlabs.com/blog/"},
                    {"@type": "ListItem", "position": 3, "name": p["crumb"], "item": canonical}
                ]
            }
        ]
    }
    if p.get("faq"):
        article_jsonld["@graph"].append({
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
                for q, a in p["faq"]
            ]
        })

    schema_str = json.dumps(article_jsonld, indent=2, ensure_ascii=False)

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
<meta property="article:published_time" content="2026-05-16T10:00:00+05:30">
<meta property="article:modified_time" content="2026-05-16T10:00:00+05:30">
<meta property="article:author" content="XServ Labs">
<meta property="article:section" content="{p["tag"]}">

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
      <li><a href="/blog/">Blog</a></li>
      <li class="nav-cta-li"><a href="/contact/" class="nav-cta">Get in Touch</a></li>
    </ul>
  </nav>
</header>

<main id="main">

<nav class="crumbs" aria-label="Breadcrumb">
  <a href="/">Home</a><span class="sep">/</span><a href="/blog/">Blog</a><span class="sep">/</span><span class="cur">{p["crumb"]}</span>
</nav>

<article class="article-wrap">
  <header class="article-header">
    <div class="article-meta-top">
      <span class="tag">{p["tag"]}</span>
      <span>16 May 2026</span>
      <span>&middot;</span>
      <span>{p.get("read_time", "10 min read")}</span>
    </div>
    <h1>{p["h1"]}</h1>
    <p class="lede">{p["lede"]}</p>
    <div class="article-byline">
      <div class="avatar">X</div>
      <div>
        <strong>XServ Labs Engineering</strong>
        <span class="sep">·</span>
        Hyderabad, India
      </div>
    </div>
  </header>

  <div class="article-body">

{body_html}

  </div>

  <footer class="article-footer">
    <div class="article-cta-card">
      <h3>{p["cta_heading"]}</h3>
      <p>{p["cta_body"]}</p>
      <div style="display:flex; gap:12px; flex-wrap:wrap;">
        <a href="{p.get("cta_wa", wa_link)}" class="btn btn-primary" target="_blank" rel="noopener">WhatsApp us</a>
        <a href="tel:+918897599624" class="btn btn-ghost">Call +91 88975 99624</a>
      </div>
    </div>

    <h3 style="font-size:13px; letter-spacing:1.6px; text-transform:uppercase; color:var(--text-muted); margin-bottom:18px;">Read next</h3>
    <div class="related" style="padding:0; border:0;">
      <div class="grid">
{related_html.rstrip()}
      </div>
    </div>
  </footer>
</article>

</main>

<footer class="site-footer" role="contentinfo">
  <div>&copy; 2026 XServ Labs · Hyderabad, India</div>
  <nav class="foot-links" aria-label="Footer">
    <a href="/">Home</a><a href="/#services">Services</a><a href="/#products">Products</a><a href="/blog/">Blog</a>
    <a href="https://wa.me/918897599624" target="_blank" rel="noopener">WhatsApp</a><a href="tel:+918897599624">Call</a>
  </nav>
</footer>

<a href="{p.get("cta_wa", wa_link)}" class="wa-float" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">
  {WHATSAPP_SVG}
</a>

</body>
</html>
'''


def write_post(p):
    out_dir = os.path.join(ROOT, "blog", p["slug"])
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(build_article(p))
    return out_path


if __name__ == "__main__":
    # Posts are defined in companion file _blog_posts.py
    from _blog_posts import POSTS
    for p in POSTS:
        path = write_post(p)
        print(f"wrote {path}  ({os.path.getsize(path):,} bytes)")

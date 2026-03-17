# XServ Labs — GitHub Pages Deployment Guide

## Files in this package

```
xserv-labs-site/
├── index.html                      ← Main website
├── 404.html                        ← Redirect for unknown pages
├── CNAME                           ← Custom domain (edit this!)
├── README.md                       ← Repo description
├── xserv-labs-logo-animated.svg    ← Animated logo (web)
├── xserv-labs-logo-static.svg      ← Static logo (print)
├── xserv-labs-logo-white.svg       ← White version (dark bg)
├── xserv-labs-logo-mono.svg        ← Monochrome version
└── xserv-labs-icon-animated.svg    ← Icon mark only
```

---

## Step 1: Create a GitHub repository

1. Go to https://github.com/new
2. Name it: `xserv-labs` (or `xservlabs.github.io` if you want the default GitHub Pages URL)
3. Set it to **Public**
4. Do NOT initialize with README (we have our own)
5. Click **Create repository**

---

## Step 2: Push these files to GitHub

Open your terminal and run:

```bash
cd xserv-labs-site

git init
git add .
git commit -m "Initial commit — XServ Labs website"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/xserv-labs.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your actual GitHub username.

---

## Step 3: Enable GitHub Pages

1. Go to your repo on GitHub
2. Click **Settings** (top tab)
3. Scroll to **Pages** in the left sidebar
4. Under "Source", select:
   - Branch: `main`
   - Folder: `/ (root)`
5. Click **Save**
6. Wait 1-2 minutes — your site will be live at:
   `https://YOUR_USERNAME.github.io/xserv-labs/`

---

## Step 4: Connect your custom domain

### A. Edit the CNAME file

Open the `CNAME` file and replace `xservlabs.com` with your actual domain:

```
yourdomain.com
```

Commit and push the change.

### B. Add DNS records at your domain registrar

Go to your domain registrar (GoDaddy, Namecheap, Cloudflare, etc.) and add these DNS records:

**For apex domain (yourdomain.com):**

| Type | Name | Value                    |
|------|------|--------------------------|
| A    | @    | 185.199.108.153          |
| A    | @    | 185.199.109.153          |
| A    | @    | 185.199.110.153          |
| A    | @    | 185.199.111.153          |

**For www subdomain:**

| Type  | Name | Value                              |
|-------|------|------------------------------------|
| CNAME | www  | YOUR_USERNAME.github.io            |

### C. Verify in GitHub

1. Go to **Settings → Pages** in your repo
2. Under "Custom domain", type your domain and click **Save**
3. Check the box **Enforce HTTPS** (wait for the certificate — takes ~15 min)
4. DNS propagation can take up to 24-48 hours, but usually works in 10-30 minutes

---

## Step 5: Verify it's live

Visit your domain in a browser. You should see the XServ Labs site with the animated Portal Vortex logo.

Test these:
- [ ] Logo animates in nav bar
- [ ] Large logo animates in hero
- [ ] All section links scroll smoothly
- [ ] "Try Traxium Free" opens traxium.in
- [ ] Contact form displays correctly
- [ ] Mobile responsive works
- [ ] HTTPS padlock shows in browser

---

## Updating the site

Any time you edit files:

```bash
git add .
git commit -m "Update: description of changes"
git push
```

GitHub Pages auto-deploys in ~60 seconds.

---

## Troubleshooting

**Site shows 404:**
- Make sure the file is named `index.html` (not `Index.html`)
- Check Settings → Pages → Source is set to `main` branch

**Custom domain not working:**
- Verify DNS records are correct (use https://dnschecker.org)
- Make sure CNAME file has your domain with no extra spaces
- Wait 30 min for DNS propagation

**No HTTPS:**
- Remove and re-add the custom domain in Settings → Pages
- Wait 15 minutes for the SSL certificate

---

That's it! Your XServ Labs site is now live.

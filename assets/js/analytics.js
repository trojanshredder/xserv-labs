/* ═══════════════════════════════════════════════════════════════════
   XServ Labs — Analytics loader
   ═══════════════════════════════════════════════════════════════════
   ONE-FILE CONTROL for all site-wide analytics.

   To activate:
     1. Replace the placeholders below with your real IDs.
     2. Commit + push. Analytics goes live on all 43 pages.

   Free tools (no credit card needed):
     - Google Analytics 4:  analytics.google.com  →  Admin →  Data Streams →  Web →  copy "Measurement ID" (G-XXXXXXXXXX)
     - Microsoft Clarity:   clarity.microsoft.com →  Settings →  Setup →  copy "Project ID" (10-character alphanumeric)

   Until you replace the placeholders, nothing fires — no calls to Google/Microsoft, no privacy concerns, no broken tracking data.
   ═══════════════════════════════════════════════════════════════════ */

(function () {
  'use strict';

  // ── EDIT THESE TWO VALUES TO ACTIVATE ──
  var GA4_MEASUREMENT_ID = 'REPLACE_WITH_GA4_ID';   // e.g. 'G-ABC1234567'
  var CLARITY_PROJECT_ID = 'REPLACE_WITH_CLARITY_ID'; // e.g. 'abc1234567'
  // ────────────────────────────────────────

  var isPlaceholder = function (val) {
    return !val || /^REPLACE_WITH_/.test(val);
  };

  // ── Google Analytics 4 (gtag.js) ──
  if (!isPlaceholder(GA4_MEASUREMENT_ID)) {
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(GA4_MEASUREMENT_ID);
    document.head.appendChild(s);
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag('js', new Date());
    window.gtag('config', GA4_MEASUREMENT_ID, {
      // Honour user privacy by default — anonymise IP, no ad personalization
      anonymize_ip: true,
      allow_ad_personalization_signals: false,
      send_page_view: true
    });

    // Track key conversion events (WhatsApp click, phone click, contact form submit)
    document.addEventListener('click', function (ev) {
      var t = ev.target.closest('a');
      if (!t) return;
      var href = t.getAttribute('href') || '';
      if (/^https?:\/\/wa\.me\//.test(href)) {
        window.gtag('event', 'whatsapp_click', { event_category: 'engagement', event_label: t.textContent.trim().slice(0, 60) });
      } else if (/^tel:/.test(href)) {
        window.gtag('event', 'phone_click', { event_category: 'engagement', event_label: href });
      } else if (/^mailto:/.test(href)) {
        window.gtag('event', 'email_click', { event_category: 'engagement', event_label: href });
      }
    });

    // Track contact form submissions
    document.addEventListener('submit', function (ev) {
      var f = ev.target;
      if (f && f.matches('form[data-track-form]')) {
        window.gtag('event', 'form_submit', { event_category: 'conversion', event_label: f.getAttribute('data-track-form') || 'unknown' });
      }
    });
  }

  // ── Microsoft Clarity (free heatmaps + session replay) ──
  if (!isPlaceholder(CLARITY_PROJECT_ID)) {
    (function (c, l, a, r, i, t, y) {
      c[a] = c[a] || function () { (c[a].q = c[a].q || []).push(arguments); };
      t = l.createElement(r); t.async = 1; t.src = 'https://www.clarity.ms/tag/' + i;
      y = l.getElementsByTagName(r)[0]; y.parentNode.insertBefore(t, y);
    })(window, document, 'clarity', 'script', CLARITY_PROJECT_ID);
  }
})();

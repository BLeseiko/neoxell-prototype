#!/usr/bin/env python3
"""
Replaces the @media (min-width: 900px) block in index6.html
with a proper 12-column CSS Grid layout matching Figma node 302:10620.
"""
import re, sys

FILE = "index6.html"

with open(FILE, "r", encoding="utf-8") as f:
    content = f.read()

OLD_START = "  /* =========================\n     DESKTOP RESPONSIVE\n     @media (min-width: 900px)\n  ========================= */\n  @media (min-width: 900px) {"
OLD_END   = "    .footer-links { gap: 24px; }\n  }"

start_idx = content.find(OLD_START)
end_idx   = content.find(OLD_END, start_idx)

if start_idx == -1:
    sys.exit("ERROR: could not find start marker")
if end_idx == -1:
    sys.exit("ERROR: could not find end marker")

end_idx += len(OLD_END)  # include the closing brace

NEW_BLOCK = """  /* =========================
     DESKTOP RESPONSIVE
     @media (min-width: 900px)
  ========================= */
  @media (min-width: 900px) {
    body { max-width: none; }

    /* ============================================================
       12-COLUMN GRID SYSTEM
       Canvas: 1440px | Side padding: 20px | Gap: 20px
       Padded col-unit: (1440-40-220)/12 = 98.33px | span 6 = 690px
       Full-bleed col-unit: 120px
    ============================================================ */

    /* ---- NAV ---- */
    #main-nav {
      display: grid;
      grid-template-columns: auto 1fr auto;
      padding: 0 20px;
      align-items: center;
    }
    .nav-links {
      display: flex; gap: 32px; align-items: center; justify-content: center;
    }
    .nav-links a {
      font-family: 'Karla', sans-serif; font-size: 14px; font-weight: 400;
      letter-spacing: .5px; text-decoration: none; white-space: nowrap;
    }
    nav:not(.scrolled) .nav-links a { color: #fff; }
    nav.scrolled .nav-links a { color: var(--text-dark); }
    .burger { display: none; }
    .btn-book-nav {
      opacity: 1 !important; pointer-events: auto !important;
      transform: scale(1) !important;
    }
    nav:not(.scrolled) .btn-book-nav {
      background: rgba(255,255,255,.15);
      border: 1px solid rgba(255,255,255,.5);
      color: #fff;
    }
    nav:not(.scrolled) .btn-book-nav:hover { background: rgba(255,255,255,.3); }

    /* ---- HERO — full-bleed: 472px cream panel / 968px image ---- */
    #hero {
      min-height: 603px; height: 603px;
      display: flex; flex-direction: row;
      padding: 0; align-items: stretch;
    }
    .hero-video { display: none; }
    .hero-bg { display: none; }
    .hero-content {
      flex: 0 0 472px; width: 472px;
      padding: 168px 40px 60px;
      background: var(--cream);
      position: relative; z-index: 2;
      justify-content: flex-start;
      text-align: left; align-items: flex-start;
    }
    .hero-eyebrow { color: var(--text-mid); }
    .hero-title { color: var(--dark-green); font-size: 64px; line-height: 1.05; }
    .hero-title em { color: #b39462; }
    .hero-sub { color: var(--text-mid); }
    .hero-ctas { flex-direction: row; gap: 12px; }
    .btn-primary { width: 200px; }
    .btn-outline { color: var(--dark-green); border-color: var(--dark-green); width: 200px; }
    .hero-image-desktop {
      flex: 1; height: 100%;
      background: url('Index6Assets/hero-desktop.jpg') center/cover no-repeat;
      background-color: #d0c8bc;
    }

    /* ---- SERVICES — 12-col grid (padded): 4 equal cards ---- */
    #services { padding: 40px 20px; }
    .services-grid { grid-template-columns: repeat(4, 1fr); }
    .svc-card { border-right: 1px solid var(--cream3); border-bottom: none; padding-bottom: 24px; }
    .svc-card:last-child { border-right: none; }

    /* ---- CONCERNS — 12-col grid (padded): col 1-6 text / col 7-12 image ---- */
    #concerns {
      display: grid;
      grid-template-columns: repeat(12, 1fr);
      column-gap: 20px;
      padding: 0 20px;
      min-height: 432px;
      overflow: hidden;
    }
    .concerns-left-col {
      grid-column: 1 / 7;
      padding: 80px 0;
      display: flex; flex-direction: column; justify-content: center;
    }
    .skin-concern-img {
      grid-column: 7 / 13;
      width: 100% !important; height: 100% !important;
      min-height: 432px;
      object-fit: cover; margin: 0 !important; border-radius: 0;
    }
    .concerns-grid { grid-template-columns: repeat(2, 1fr); }

    /* ---- LASER — 12-col grid (padded): col 1-6 text / col 7-12 stats ---- */
    #laser {
      display: grid;
      grid-template-columns: repeat(12, 1fr);
      column-gap: 20px;
      padding: 80px 20px;
      align-items: start;
    }
    .laser-left-col {
      grid-column: 1 / 7;
      display: flex; flex-direction: column; gap: 16px;
    }
    .laser-stats-grid {
      grid-column: 7 / 13;
      margin-top: 0;
      grid-template-columns: repeat(2, 1fr);
    }

    /* ---- BEFORE/AFTER — 12-col grid (full-bleed): col 1-4 left / col 5-12 cards ---- */
    #before-after {
      display: grid;
      grid-template-columns: repeat(12, 1fr);
      column-gap: 0;
      padding: 0;
      align-items: stretch;
    }
    .ba-left-col {
      grid-column: 1 / 5;
      padding: 80px 40px 80px 20px;
      display: flex; flex-direction: column; justify-content: center;
      background: var(--cream2);
    }
    .ba-right-col {
      grid-column: 5 / 13;
      padding: 40px 20px 40px 40px;
      display: flex; flex-direction: column; justify-content: center; gap: 16px;
      overflow: hidden;
    }
    #before-after .ba-scroll-track { overflow-x: auto; }

    /* ---- TREATMENTS — 12-col grid (full-bleed): col 1-4 left / col 5-12 list ---- */
    #treatments {
      display: grid;
      grid-template-columns: repeat(12, 1fr);
      column-gap: 0;
      padding: 0;
      align-items: stretch;
    }
    .treatments-left-col {
      grid-column: 1 / 5;
      padding: 80px 40px 80px 20px;
      display: flex; flex-direction: column; justify-content: center;
      background: var(--green-bg);
    }
    .treatment-list {
      grid-column: 5 / 13;
      padding: 60px 20px 60px 40px;
      display: flex; flex-direction: column; justify-content: center;
    }

    /* ---- FIRST VISIT — 12-col grid (full-bleed): col 1-8 image / col 9-12 content ---- */
    #first-visit {
      display: grid;
      grid-template-columns: repeat(12, 1fr);
      column-gap: 0;
      padding: 0;
      align-items: stretch;
      min-height: 824px;
    }
    .fv-image-area { grid-column: 1 / 9; }
    .fv-content {
      grid-column: 9 / 13;
      padding: 80px 20px 80px 40px;
      overflow-y: auto;
    }

    /* ---- REVIEWS ---- */
    #reviews { padding: 80px 20px; }
    .reviews-header { flex-direction: row; justify-content: space-between; align-items: flex-end; }
    .reviews-track { display: flex; flex-direction: row; gap: 20px; overflow-x: auto; padding-bottom: 8px; }
    .review-card { flex: 0 0 300px; }
    .review-ig-card { flex: 0 0 220px; }

    /* ---- TEAM ---- */
    #team { padding: 80px 20px; }
    .team-cards { display: flex; flex-direction: row; gap: 24px; }
    .team-card-group { flex: 1; }
    .team-specialist-card { flex: 0 0 353px; }

    /* ---- PARTNERS ---- */
    #partners { display: flex; flex-direction: row; align-items: center; padding: 32px 20px; gap: 40px; }
    .partners-label { white-space: nowrap; }
    .partners-logos { flex-wrap: nowrap; gap: 40px; }

    /* ---- MORE REASONS — 12-col grid (padded): col 1-5 header / col 6-12 cards ---- */
    #more-reasons {
      display: grid;
      grid-template-columns: repeat(12, 1fr);
      column-gap: 20px;
      padding: 80px 20px;
      align-items: start;
    }
    .reasons-header { grid-column: 1 / 6; }
    .reasons-scroll {
      grid-column: 6 / 13;
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;
      overflow: visible;
    }
    .reasons-offer-card { min-width: unset; width: 100%; }

    /* ---- CTA ---- */
    #cta { padding: 100px 20px; }
    .cta-text { align-items: flex-start; text-align: left; }
    .cta-actions { align-items: flex-start; }
    .btn-cta { width: auto; padding: 0 40px; }
    .cta-address { text-align: left; }

    /* ---- FOOTER ---- */
    footer { padding: 60px 20px; }
    .footer-links { gap: 24px; }
  }"""

new_content = content[:start_idx] + NEW_BLOCK + content[end_idx:]

with open(FILE, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"Done. Replaced {end_idx - start_idx} chars with {len(NEW_BLOCK)} chars.")
print(f"New file length: {len(new_content)} chars.")

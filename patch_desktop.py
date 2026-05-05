import re

with open('index6.html', 'r', encoding='utf-8') as f:
    content = f.read()

original_len = len(content)

# ============================================================
# 1. Add desktop nav links
# ============================================================
needle = '</a>\n    <div class="nav-right">'
replacement = '</a>\n    <div class="nav-links">\n      <a href="#services">Services</a>\n      <a href="#laser">Laser</a>\n      <a href="#treatments">Treatments</a>\n      <a href="#more-reasons">Offers</a>\n      <a href="#reviews">Reviews</a>\n      <a href="#cta">Contact</a>\n    </div>\n    <div class="nav-right">'
assert needle in content, "NAV NEEDLE NOT FOUND"
content = content.replace(needle, replacement, 1)
print("1. Nav links added")

# ============================================================
# 2. Concerns: wrap text in .concerns-left-col
# ============================================================
needle = '<section id="concerns">\n  <span class="eyebrow reveal">SKIN SOLUTIONS</span>'
replacement = '<section id="concerns">\n  <div class="concerns-left-col">\n  <span class="eyebrow reveal">SKIN SOLUTIONS</span>'
assert needle in content, "CONCERNS OPEN NOT FOUND"
content = content.replace(needle, replacement, 1)

# Close concerns-left-col before image
# The img tag appears after the concerns grid closing div
old_img_marker = '  </div>\n</section>\n\n<section id="laser">'
# Instead target more specifically
needle2 = '  <img class="skin-concern-img reveal" src="data:image/png'
replacement2 = '  </div>\n  <img class="skin-concern-img reveal" src="data:image/png'
assert needle2 in content, "CONCERNS IMG NOT FOUND"
content = content.replace(needle2, replacement2, 1)
print("2. Concerns wrapped")

# ============================================================
# 3. Laser: wrap text in .laser-left-col
# ============================================================
needle = '<section id="laser">\n  <span class="eyebrow reveal">LASER HAIR REMOVAL</span>'
replacement = '<section id="laser">\n  <div class="laser-left-col">\n  <span class="eyebrow reveal">LASER HAIR REMOVAL</span>'
assert needle in content, "LASER OPEN NOT FOUND"
content = content.replace(needle, replacement, 1)

needle = 'worldwide.</p>\n  <div class="laser-stats-grid reveal">'
replacement = 'worldwide.</p>\n  </div>\n  <div class="laser-stats-grid reveal">'
assert needle in content, "LASER SPLIT NOT FOUND"
content = content.replace(needle, replacement, 1)
print("3. Laser wrapped")

# ============================================================
# 4. Before/After: wrap in 2-col
# ============================================================
needle = '<section id="before-after">\n  <span class="eyebrow reveal">REAL RESULTS</span>'
replacement = '<section id="before-after">\n  <div class="ba-left-col">\n  <span class="eyebrow reveal">REAL RESULTS</span>'
assert needle in content, "BA OPEN NOT FOUND"
content = content.replace(needle, replacement, 1)

# Close ba-left-col and open ba-right-col before ba-scroll-track
needle = '  <div class="ba-scroll-track reveal">'
replacement = '  </div>\n  <div class="ba-right-col">\n  <div class="ba-scroll-track reveal">'
assert needle in content, "BA TRACK NOT FOUND"
content = content.replace(needle, replacement, 1)

# Close ba-right-col at end of section
needle_ba_end = 'ba-ig-link reveal">See more on Instagram \u2192</a>\n</section>'
replacement_ba_end = 'ba-ig-link reveal">See more on Instagram \u2192</a>\n  </div>\n</section>'
assert needle_ba_end in content, "BA END NOT FOUND"
content = content.replace(needle_ba_end, replacement_ba_end, 1)
print("4. Before/After wrapped")

# ============================================================
# 5. Treatments: wrap in 2-col
# ============================================================
needle = '<section id="treatments">\n  <span class="eyebrow reveal">TREATMENTS</span>'
replacement = '<section id="treatments">\n  <div class="treatments-left-col">\n  <span class="eyebrow reveal">TREATMENTS</span>'
assert needle in content, "TREATMENTS OPEN NOT FOUND"
content = content.replace(needle, replacement, 1)

needle = "your skin's needs.</p>\n  <div class=\"treatment-list reveal\">"
replacement = "your skin's needs.</p>\n  </div>\n  <div class=\"treatment-list reveal\">"
assert needle in content, "TREATMENTS SPLIT NOT FOUND"
content = content.replace(needle, replacement, 1)
print("5. Treatments wrapped")

# ============================================================
# 6. Hero: add desktop image div
# ============================================================
# Find hero-content div closing before section close
# Hero section ends: </div>\n  </div>\n</section>\n\n\n\n<section id="services"
hero_end_needle = '    </div>\n  </div>\n</section>\n\n\n\n<section id="services"'
hero_end_replacement = '    </div>\n  </div>\n  <div class="hero-image-desktop"></div>\n</section>\n\n\n\n<section id="services"'
assert hero_end_needle in content, "HERO END NOT FOUND: " + repr(content[content.find('id="services"')-100:content.find('id="services"')])
content = content.replace(hero_end_needle, hero_end_replacement, 1)
print("6. Hero image div added")

# ============================================================
# 7. Append desktop CSS before </style>
# ============================================================
desktop_css = """
  /* =========================
     DESKTOP RESPONSIVE
     @media (min-width: 900px)
  ========================= */
  @media (min-width: 900px) {
    body { max-width: none; }

    /* NAV */
    #main-nav { padding: 0 40px; }
    .nav-links { display: flex; gap: 32px; align-items: center; }
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

    /* HERO */
    #hero {
      min-height: 603px; height: 603px;
      flex-direction: row;
      padding: 0; justify-content: flex-start; align-items: stretch;
    }
    .hero-video { display: none; }
    .hero-bg { display: none; }
    .hero-content {
      width: 472px; flex-shrink: 0;
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

    /* SERVICES */
    #services { padding: 40px; }
    .services-grid { grid-template-columns: repeat(4, 1fr); }
    .svc-card { border-right: 1px solid var(--cream3); border-bottom: none; padding-bottom: 24px; }
    .svc-card:last-child { border-right: none; }

    /* CONCERNS */
    #concerns { display: flex; flex-direction: row; padding: 0; overflow: hidden; min-height: 500px; }
    .concerns-left-col {
      flex: 0 0 50%; padding: 80px 60px;
      display: flex; flex-direction: column; justify-content: center;
    }
    .skin-concern-img { flex: 0 0 50%; width: 50% !important; min-height: 500px; object-fit: cover; margin: 0 !important; border-radius: 0; order: 2; }
    .concerns-grid { grid-template-columns: repeat(2, 1fr); }

    /* LASER */
    #laser { display: flex; flex-direction: row; padding: 80px 60px; gap: 60px; align-items: flex-start; }
    .laser-left-col { flex: 0 0 45%; display: flex; flex-direction: column; gap: 16px; }
    .laser-stats-grid { flex: 1; margin-top: 0; grid-template-columns: repeat(2, 1fr); }

    /* BEFORE/AFTER */
    #before-after { display: flex; flex-direction: row; padding: 0; align-items: stretch; }
    .ba-left-col {
      flex: 0 0 400px; padding: 80px 60px;
      display: flex; flex-direction: column; justify-content: center;
      background: var(--cream2);
    }
    .ba-right-col {
      flex: 1; padding: 40px; overflow: hidden;
      display: flex; flex-direction: column; justify-content: center; gap: 16px;
    }
    #before-after .ba-scroll-track { overflow-x: auto; }

    /* TREATMENTS */
    #treatments { display: flex; flex-direction: row; padding: 0; align-items: stretch; }
    .treatments-left-col {
      flex: 0 0 380px; padding: 80px 60px;
      display: flex; flex-direction: column; justify-content: center;
      background: var(--green-bg);
    }
    .treatment-list { flex: 1; padding: 40px 60px; display: flex; flex-direction: column; justify-content: center; }

    /* FIRST VISIT */
    #first-visit { display: flex; flex-direction: row-reverse; padding: 0; align-items: stretch; min-height: 600px; }
    .fv-image-area { flex: 0 0 55%; }
    .fv-content { flex: 0 0 45%; padding: 80px 60px; overflow-y: auto; }

    /* REVIEWS */
    #reviews { padding: 80px 40px; }
    .reviews-header { flex-direction: row; justify-content: space-between; align-items: flex-end; }
    .reviews-track { display: flex; flex-direction: row; gap: 20px; overflow-x: auto; padding-bottom: 8px; }
    .review-card { flex: 0 0 300px; }
    .review-ig-card { flex: 0 0 220px; }

    /* TEAM */
    #team { padding: 80px 40px; }
    .team-cards { display: flex; flex-direction: row; gap: 24px; }
    .team-card-group { flex: 1; }
    .team-specialist-card { flex: 0 0 353px; }

    /* PARTNERS */
    #partners { display: flex; flex-direction: row; align-items: center; padding: 32px 40px; gap: 40px; }
    .partners-label { white-space: nowrap; }
    .partners-logos { flex-wrap: nowrap; gap: 40px; }

    /* MORE REASONS */
    #more-reasons { display: flex; flex-direction: row; padding: 80px 40px; gap: 60px; align-items: flex-start; }
    .reasons-header { flex: 0 0 440px; }
    .reasons-scroll {
      flex: 1; display: grid; grid-template-columns: repeat(3, 1fr);
      gap: 20px; overflow: visible;
    }
    .reasons-offer-card { min-width: unset; width: 100%; }

    /* CTA */
    #cta { padding: 100px 40px; }
    .cta-text { align-items: flex-start; text-align: left; }
    .cta-actions { align-items: flex-start; }
    .btn-cta { width: auto; padding: 0 40px; }
    .cta-address { text-align: left; }

    /* FOOTER */
    footer { padding: 60px 40px; }
    .footer-links { gap: 24px; }
  }
"""

assert '</style>' in content, "</style> NOT FOUND"
content = content.replace('</style>', desktop_css + '</style>', 1)
print("7. Desktop CSS appended")

with open('index6.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Done. File size: {len(content)} chars (was {original_len})")

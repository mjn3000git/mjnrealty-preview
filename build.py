#!/usr/bin/env python3
"""Build the navy broker homepage (preview: Matthew J. Nothdurft, no business name). Usage: build.py preview|live OUTDIR"""
import sys, pathlib
mode, out = sys.argv[1], pathlib.Path(sys.argv[2])
assert mode in ("preview", "live")
P = mode == "preview"
DESC = "Matthew J. Nothdurft, Licensed Real Estate Broker. Real estate, seasonal rentals, and property management in the Adirondack region of New York."
TITLE = "Matthew J. Nothdurft, Licensed Real Estate Broker | Adirondack Real Estate and Property Management"
FH = "https://dos.ny.gov/fair-housing-notice"
DHR = "https://dhr.ny.gov/final-regulations-regarding-notice-tenants-rights-reasonable-accommodation"
LIVE = "https://mjnrealty.com/"
BROKER = "Matthew J. Nothdurft, Licensed Real Estate Broker"
if P:
    # Preview is Matthew's personal broker site: no business name anywhere.
    TITLE = f"{BROKER} | Adirondack Real Estate and Property Management"
    DESC = f"{BROKER}. Real estate, seasonal rentals, and property management in the Adirondack region of New York."

head_extra = ('<meta name="robots" content="noindex,nofollow">\n' if P else f'''<link rel="canonical" href="{LIVE}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{BROKER}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="{DESC}">
<meta property="og:url" content="{LIVE}">
<meta property="og:image" content="{LIVE}images/hero-schroon-lake-drone-DJI_0012.jpg">
<meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"RealEstateAgent","name":"{BROKER}","url":"{LIVE}","description":"{DESC}","telephone":"+1-518-868-6689","image":"{LIVE}images/hero-schroon-lake-drone-DJI_0012.jpg","address":{{"@type":"PostalAddress","streetAddress":"8 Triphammer Road","addressLocality":"Queensbury","addressRegion":"NY","postalCode":"12804","addressCountry":"US"}},"founder":{{"@type":"Person","name":"Matthew J. Nothdurft","jobTitle":"Licensed Real Estate Broker"}},"areaServed":[{{"@type":"Place","name":"Lake George, NY"}},{{"@type":"Place","name":"Schroon Lake, NY"}},{{"@type":"Place","name":"Queensbury, NY"}},{{"@type":"Place","name":"Glens Falls, NY"}},{{"@type":"Place","name":"Adirondacks, NY"}}]}}
</script>
''')
LIC_NAV = '<a href="license.html">License</a>' if P else ''
PKG_NAV = '<a href="packages.html">Packages</a>' if P else ''
LIC_FOOT = '<p><a href="license.html">License record (NYS Department of State)</a></p>' if P else ''
preview_bar = (f'<div class="preview-bar" role="note">Preview, not live. The live site is <a href="{LIVE}">mjnrealty.com</a></div>\n' if P else "")

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{TITLE}</title>
<meta name="description" content="{DESC}">
{head_extra}<link rel="icon" href="images/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,600;0,700;1,400;1,500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/navy.css">
</head>
<body id="top">
<a class="skip" href="#main">Skip to content</a>
{preview_bar}<div class="fh-bar"><a href="{FH}" target="_blank" rel="noopener">Fair Housing Notice (NYS Human Rights Law)</a></div>
<header class="hero">
  <div class="site-nav-row">
    <a class="brand" href="#top" aria-label="Matthew Nothdurft, home"><span class="mono" aria-hidden="true">MJN</span><span class="brand-name">Matthew Nothdurft</span></a>
    <button class="nav-toggle" aria-controls="site-nav" aria-expanded="false"><span class="sr">Menu</span><span class="bars"></span></button>
    <nav class="site-nav" id="site-nav" aria-label="Main"><a href="#about">About</a><a href="#services">Services</a><a href="#properties">Properties</a><a href="#areas">Areas</a><a href="#contact">Contact</a>{PKG_NAV}{LIC_NAV}<a class="callbtn" href="tel:+15188686689">Call 518-868-6689</a></nav>
  </div>
  <div class="wm" aria-hidden="true">MJN</div>
  <div class="hero-copy">
    <h1>Matthew<br>Nothdurft</h1>
    <p class="lic">Licensed Real Estate Broker</p>
    <p class="adk">Adirondack living</p>
    <div class="rule"></div>
    <div class="btns"><a class="btn gold" href="#properties">View Properties</a><a class="btn ghost" href="tel:+15188686689">Call 518-868-6689</a></div>
  </div>
  <div class="photo-credit">Schroon Lake from above, drone photo by Matthew Nothdurft</div>
</header>
<main id="main">

<section id="properties" class="properties">
  <div class="wrap">
  <p class="eyebrow">Featured property</p>
  <h2>Adirondack homes</h2>
  <article class="featured">
    <div class="ph" role="img" aria-label="The Hayes House"><div class="tag">Family-owned property</div></div>
    <div class="fc">
      <h3>The Hayes House</h3>
      <p class="addr">Schroon Lake, New York</p>
      <p class="desc">Family-owned property.</p>
      <p class="facts">4 bedrooms &middot; 3 baths &middot; Sleeps 8</p>
      <div class="inset" role="img" aria-label="Wooded path at the Hayes House"></div>
      <a class="more" href="https://41hayes.com" target="_blank" rel="noopener">Visit 41hayes.com &rarr;</a>
    </div>
  </article>
  </div>
</section>

<section class="services" id="services">
  <div class="wrap">
  <p class="eyebrow">Services</p>
  <h2>What we do</h2>
  <div class="svc-wrap">
    <ul class="svc-list">
      <li class="svc"><span class="n">01</span><div><h3>Seasonal and vacation rentals</h3><p>Weekly and full-season rentals across the Adirondacks. We handle the details, from marketing and reservations to guest communication and cleaning, so owners can stay hands-off.</p></div></li>
      <li class="svc"><span class="n">02</span><div><h3>Vacation home purchases</h3><p>Help finding the right second home or getaway. We look past the price at location, upkeep, rental potential, and long-term fit.</p></div></li>
      <li class="svc"><span class="n">03</span><div><h3>Property management</h3><p>Care for homes while owners are away, including regular home watch visits, seasonal opening and closing, and checks after storms.</p></div></li>
      <li class="svc"><span class="n">04</span><div><h3>Free rental income evaluation</h3><p>A free, no-obligation estimate of what a home could earn as a seasonal rental, for owners and for buyers.</p></div></li>
      <li class="svc"><span class="n">05</span><div><h3>List and sell your home</h3><p>Thinking of selling? We present your Adirondack home to the right buyers, with a market analysis to start.</p></div></li>
    </ul>
    <div class="pics">
      <div class="pic" style="background-image:url(images/hayes-lake-shoreline-mountains.jpg)"><span>Schroon Lake</span></div>
      <div class="pic" style="background-image:url(images/aerial-DJI_0670.jpg)"><span>Queensbury from above</span></div>
    </div>
  </div>
  </div>
</section>

<section id="about" class="about">
  <div class="wrap about-grid">
    <figure class="about-photo"><img src="images/matthew-nothdurft.jpg" alt="Matthew Nothdurft" width="671" height="894" loading="lazy"><figcaption>Matthew J. Nothdurft<br><span>Licensed Real Estate Broker</span></figcaption></figure>
    <div class="about-text"><p class="eyebrow">About Matthew</p><h2>Local roots, hands-on care.</h2>
      <p>Born in the Adirondacks and raised on its lakes and trails, Matthew Nothdurft is a licensed real estate broker with a deep love for the region he calls home.</p>
      <p>We offer full-service property management and real estate services covering the Lake George and Schroon Lake regions of New York.</p>
      <p>What sets us apart is a hands-on, personal approach. From routine check-ins to coordinating repairs with the right contractors and vendors, we treat every property like our own.</p>
      <p>Beyond the work itself, Matthew is a local resource for the area. PADI scuba certified and an e-bike enthusiast, he knows the Adirondacks inside and out and is glad to point you toward the best of what the region has to offer.</p>
    </div>
  </div>
</section>

<section id="areas" class="areas">
  <div class="wrap"><p class="eyebrow">Areas served</p><h2>The Adirondack region of New York</h2>
  <ul class="area-list">
    <li class="area"><h3>Lake George</h3><p>Lakeside homes, seasonal cottages, and year-round properties around the lake and its villages.</p></li>
    <li class="area"><h3>Schroon Lake</h3><p>Quiet shoreline, mountain views, and classic Adirondack camps in the Schroon Lake area.</p></li>
    <li class="area"><h3>Queensbury</h3><p>Year-round living close to Glens Falls, with easy access to the lakes and the Northway.</p></li>
    <li class="area"><h3>The greater Adirondacks</h3><p>Woods, lakes, and small towns across the Adirondack region of New York.</p></li>
  </ul></div>
</section>

<section id="contact" class="contact">
  <div class="wrap"><p class="eyebrow">Contact</p><h2>Let's talk</h2><div class="contact-grid">
  <div class="contact-info">
    <p class="contact-lead">Questions about buying, selling, renting, or caring for an Adirondack home? Call Matthew Nothdurft directly.</p>
    <p class="contact-phone"><span>Office</span><a href="tel:+15188686689">518-868-6689</a></p>
    <p class="contact-region"><span>Based in</span>The Adirondack region of New York</p>
  </div>
  <!-- Contact form: Formspree free plan. Set FORMSPREE_ID in js/main.js to turn it on. While it is empty the form stays hidden and disabled. -->
  <form id="contact-form" class="contact-form" method="POST" hidden>
    <fieldset disabled>
      <label>Name<input name="name" type="text" autocomplete="name" required></label>
      <label>Email<input name="email" type="email" autocomplete="email" required></label>
      <label>Phone (optional)<input name="phone" type="tel" autocomplete="tel"></label>
      <label>How can we help?<textarea name="message" rows="5" required></textarea></label>
      <input type="text" name="_gotcha" style="display:none" tabindex="-1" autocomplete="off">
      <button type="submit">Send message</button>
      <p class="form-status" id="form-status" role="status" tabindex="-1"></p>
    </fieldset>
  </form>
  </div></div>
</section>
</main>

<footer>
  <div class="wrap footer-inner">
    <span class="mono" aria-hidden="true">MJN</span>
    <div>
      <p class="lic-name">Matthew J. Nothdurft, Licensed Real Estate Broker</p>
      <p>8 Triphammer Road, Queensbury, NY 12804 | Office: <a href="tel:+15188686689">518-868-6689</a></p>
      <p>Licensed by the New York State Department of State, Division of Licensing Services.</p>
      <p>NYS Housing and Anti-Discrimination Notice (Fair Housing Notice): <a href="{FH}" target="_blank" rel="noopener">{FH}</a></p>
      <p>Tenants' Rights to Reasonable Accommodations for Persons with Disabilities (NYS Division of Human Rights notice): <a href="{DHR}" target="_blank" rel="noopener">dhr.ny.gov</a></p>
      <p>Equal Housing Opportunity.</p>
      {LIC_FOOT}
      <p class="copy">&copy; <span data-year>2026</span> {BROKER}. All rights reserved.</p>
    </div>
    <div class="eho" aria-label="Equal Housing Opportunity"><svg width="34" height="34" viewBox="0 0 34 34" fill="none" stroke="#c9a24a" stroke-width="2.2" aria-hidden="true"><path d="M4 16 17 5l13 11"/><path d="M8 13v16h18V13"/><path d="M12.5 18.5h9M12.5 23h9"/></svg></div>
  </div>
</footer>
<script src="js/main.js"></script>
</body>
</html>
'''
if P:
    # Preview-only homepage edits: merged bio, 41 Hayes nav item, featured card links to hayes.html.
    def _rep(s, old, new):
        assert s.count(old) == 1, old
        return s.replace(old, new)
    ABOUT_OLD = html[html.index('<p class="eyebrow">About Matthew</p>'):html.index('</div>', html.index('<div class="about-text">'))]
    ABOUT_NEW = ('<p class="eyebrow">About Matthew</p><h2>Local roots, hands-on care.</h2>\n'
                 '      <p>Born in the Adirondacks and raised on its lakes and trails, Matthew Nothdurft is a licensed real estate broker with a deep love for the region he calls home. '
                 'He covers the Lake George and Schroon Lake regions of New York.</p>\n'
                 '      <p>What sets him apart is a hands-on, personal approach. From routine check-ins to coordinating repairs with the right contractors and vendors, he treats every property like his own.</p>\n    ')
    html = _rep(html, ABOUT_OLD, ABOUT_NEW)
    html = _rep(html, '<a href="#properties">Properties</a>', '<a href="#properties">Properties</a><a href="hayes.html">41 Hayes</a>')
    html = _rep(html, '<div class="tag">Family-owned property</div>', '<div class="tag">Showcase property</div>')
    html = _rep(html, '<p class="desc">Family-owned property.</p>', '<p class="desc">A family home, cared for like one. Seasonal rental coming soon.</p>')
    html = _rep(html, '<a class="more" href="https://41hayes.com" target="_blank" rel="noopener">Visit 41hayes.com &rarr;</a>',
                '<a class="more" href="hayes.html">See 41 Hayes Road &rarr;</a>')
assert "\u2014" not in html and "\u2013" not in html
assert "mjn real" not in html.lower()
for bad in ("lakefront", "dock", "lake access", "boating", "boater"):
    assert bad not in html.lower(), bad
(out / "index.html").write_text(html)
print("wrote", out / "index.html", mode)

if P:
    a = html.index("<header class=\"hero\">"); b = html.index("<main id=\"main\">")
    top = html[:a].replace(f"<title>{TITLE}</title>", "<title>License record | Matthew J. Nothdurft, Licensed Real Estate Broker</title>")
    top = top.replace('<body id="top">', '<body id="top" class="sub">')
    nav = html[a:b]
    nav = nav[nav.index('<div class="site-nav-row">'):nav.index('<div class="wm"')]
    for k in ("about","services","properties","areas","contact"):
        nav = nav.replace(f'href="#{k}"', f'href="index.html#{k}"')
    nav = nav.replace('href="#top"', 'href="index.html"')
    foot = html[html.index("</main>"):]
    NS = "Not shown in the public record"
    EA = "https://appext20.dos.ny.gov/nydos/searchByLicNumber.do"
    OD = "https://data.ny.gov/resource/9twf-9yig.json?$q=Nothdurft"
    OH = "https://dos.ny.gov/administrative-hearings"
    rows = [
        ("Name", "MATTHEW J NOTHDURFT"),
        ("License type", "Individual Broker"),
        ("License number", "10351205006"),
        ("Status", "Current"),
        ("Issue date", f'<em>{NS}</em>'),
        ("Expiration date", "January 22, 2028"),
        ("Business name", "NOTHDURFT MATTHEW J"),
        ("Business address", "8 Triphammer Road, Queensbury, NY 12804 (Warren County)"),
        ("Principal office", "License 10991209577, 8 Triphammer Road, Queensbury, NY 12804"),
        ("Phone", f'<em>{NS}</em>'),
        ("Disciplinary actions", f'<em>{NS}</em>. A search of the DOS Office of Administrative Hearings decisions and consent orders for "Nothdurft" returned no results on Nov 1, 2026.'),
    ]
    trs = "\n".join(f'      <tr><th scope="row">{k}</th><td>{v}</td></tr>' for k, v in rows)
    page = top + f"""<header class="subhead">
  {nav}</header>
<main id="main">
<section class="license">
  <div class="wrap lic-wrap">
    <p class="eyebrow">License record</p>
    <h2>NYS real estate broker license</h2>
    <p class="lic-intro">As shown in the New York State Department of State public license records.</p>
    <table class="lic-table">
{trs}
    </table>
    <p class="lic-src"><strong>Sources:</strong> NYS Department of State eAccessNY Public License Search, license number 10351205006: <a href="{EA}" target="_blank" rel="noopener">appext20.dos.ny.gov</a>. Open NY Active Real Estate Brokers dataset: <a href="{OD}" target="_blank" rel="noopener">data.ny.gov</a>. DOS administrative hearing decisions and consent orders search: <a href="{OH}" target="_blank" rel="noopener">dos.ny.gov/administrative-hearings</a>.</p>
    <p class="lic-ver">Verified on Nov 1, 2026</p>
  </div>
</section>
""" + foot
    assert "\u2014" not in page and "\u2013" not in page
    (out / "license.html").write_text(page)
    print("wrote", out / "license.html")

if P:
    # List-ready packages page (preview only). No license.html links on this page.
    a = html.index("<header class=\"hero\">"); b = html.index("<main id=\"main\">")
    top = html[:a].replace(f"<title>{TITLE}</title>", "<title>List-ready packages | Matthew J. Nothdurft, Licensed Real Estate Broker</title>")
    top = top.replace(f'content="{DESC}"', 'content="List-ready packages: pre-listing repairs and drone media from Adirondack Craftworks, offered separately from real estate brokerage by Matthew J. Nothdurft, Licensed Real Estate Broker."')
    top = top.replace('<body id="top">', '<body id="top" class="sub">')
    nav = html[a:b]
    nav = nav[nav.index('<div class="site-nav-row">'):nav.index('<div class="wm"')]
    for k in ("about","services","properties","areas","contact"):
        nav = nav.replace(f'href="#{k}"', f'href="index.html#{k}"')
    nav = nav.replace('href="#top"', 'href="index.html"').replace(LIC_NAV, "")
    nav = nav.replace('<a href="packages.html">', '<a href="packages.html" aria-current="page">')
    foot = html[html.index("</main>"):].replace("      " + LIC_FOOT + "\n", "")
    SOON = "Coming soon, pending FAA Part 107 certification"
    pk = [
      ("Punch List", "$940", None, "For homes that need a light touch before photos.", [
        "Walk-through and punch list",
        "Up to 8 hours of repair work",
        "1 haul-away load"], None),
      ("Show Ready", "$1,460", "$1,755", "For homes that need visible fixes before showings.", [
        "Walk-through and punch list",
        "Up to 16 hours of repair work",
        "1 haul-away load"], "Drone media"),
      ("Market Ready", "$2,725", "$3,220", "For homes that need repair and refresh work before going on the market.", [
        "Walk-through and punch list",
        "About 32 hours of repair and refresh work",
        "2 haul-away loads"], "Drone stills and video"),
    ]
    cards = ""
    for i, (name, price, dprice, lead, items, drone) in enumerate(pk, 1):
        li = "".join(f'<li><span>{x}</span></li>' for x in items)
        if drone:
            li += f'<li class="soon"><span>{drone}</span><b>{SOON}</b></li>'
        withd = f'      <p class="pkg-note">{dprice} with {drone.lower()} once available.</p>\n' if dprice else ""
        cards += (f'    <article class="pkg"><p class="pkg-n">0{i}</p><h3>{name}</h3><p class="pkg-lead">{lead}</p>\n'
                  f'      <ul class="pkg-items">{li}</ul>\n'
                  f'      <p class="pkg-total"><span>Adirondack Craftworks package price{" now" if dprice else ""}</span><b>{price}</b></p>\n'
                  + withd +
                  f'      <p class="pkg-note">Materials and sales tax extra.</p>\n'
                  f'      <p class="pkg-note">Does not include listing your home. Brokerage is a separate service. See below.</p>\n'
                  f'    </article>\n')
    page = top + f"""<header class="subhead">
  {nav}</header>
<main id="main">
<section class="pkgs">
  <div class="wrap pkg-wrap">
    <p class="eyebrow">List-ready packages</p>
    <h2>Get your home ready to list</h2>
    <p class="lic-intro">Bundles of pre-listing repairs and drone media from Adirondack Craftworks, for owners getting ready to sell. Listing with Matthew J. Nothdurft, Licensed Real Estate Broker, is a separate service. </p>
    <p class="pkg-alc">These packages are a starting point. Every item can be added, removed or adjusted a la carte to fit your property.</p>
    <p class="pkg-flag">Proposed pricing, not final. Materials and sales tax extra.</p>
    <h3 class="pkg-sec">Adirondack Craftworks services</h3>
    <p class="pkg-sub">Pre-listing repairs and media. These are home services, not real estate services. Adirondack Craftworks does not offer licensed plumbing or electrical work.</p>
    <div class="pkg-grid">
{cards}    </div>
    <div class="addon">
      <p class="eyebrow">Optional add-on</p>
      <p class="addon-row"><span>Home watch while listed (Basic home watch rate)</span><b>$149 a month</b></p>
      <p class="pkg-note">Adirondack Craftworks service. Proposed pricing, not final.</p>
    </div>
  </div>
</section>
<section class="broker" id="brokerage">
  <div class="wrap pkg-wrap">
    <p class="eyebrow">Real estate brokerage</p>
    <!-- LEGAL REVIEW: no assumed business name filed with DOS; broker name only -->
    <h2>Listing with Matthew J. Nothdurft, Licensed Real Estate Broker</h2>
    <div class="broker-box">
      <p class="broker-fee"><span>Broker commission</span><b>Negotiable</b></p>
      <ul class="broker-list">
        <li>Real estate brokerage services are provided by Matthew J. Nothdurft, Licensed Real Estate Broker.</li>
        <li>Listing your home is a separate service, with its own written listing agreement and its own commission. The commission is never part of any Adirondack Craftworks package or service price.</li>
        <li>Commissions are not set by law. The commission is fully negotiable between you and the broker.</li>
        <li>Listing with Matthew J. Nothdurft, Licensed Real Estate Broker, is not conditional on buying any Adirondack Craftworks services. You are free to use any contractor or photographer you choose.</li>
        <li>Buying a package does not require you to list with Matthew J. Nothdurft, Licensed Real Estate Broker.</li>
      </ul>
      <p class="disclose"><strong>Disclosure:</strong> Matthew Nothdurft owns Adirondack Craftworks and profits from the services it sells.</p>
      <p class="broker-cta"><a class="btn gold" href="tel:+15188686689">Call 518-868-6689</a></p>
    </div>
  </div>
</section>
""" + foot
    assert "\u2014" not in page and "\u2013" not in page
    for bad in ("lakefront", "dock", "lake access", "boat", "license.html", "family-owned", "mj and"):
        assert bad not in page.lower(), bad
    (out / "packages.html").write_text(page)
    print("wrote", out / "packages.html")

if P:
    # 41 Hayes Road page (preview only). Facts reused from 41hayes.com: 4 bedrooms, 3 baths, sleeps 8;
    # 41 Hayes Road, Schroon Lake, NY 12870; near I-87; day trips to Lake George and Lake Placid; prepared with care before every arrival.
    PV = "https://mjn3000git.github.io/mjnrealty-preview/"
    HT = "41 Hayes Road | A family home for the season in Schroon Lake, NY"
    HD = "Seasonal and long-term rental in Schroon Lake, New York. 4 bedrooms, 3 baths, sleeps 8. Bookings not open yet. Coming soon to VRBO."
    a = html.index("<header class=\"hero\">"); b = html.index("<main id=\"main\">")
    top = html[:a].replace(f"<title>{TITLE}</title>", f"<title>{HT}</title>")
    top = top.replace(f'content="{DESC}"', f'content="{HD}"')
    og = (f'<meta property="og:type" content="website">\n<meta property="og:site_name" content="{BROKER}">\n'
          f'<meta property="og:title" content="{HT}">\n<meta property="og:description" content="{HD}">\n'
          f'<meta property="og:url" content="{PV}hayes.html">\n<meta property="og:image" content="{PV}images/hayes-front-of-house.jpg">\n'
          f'<meta property="og:image:alt" content="The front of the house at 41 Hayes Road, Schroon Lake, New York">\n'
          f'<meta name="twitter:card" content="summary_large_image">\n<meta name="twitter:title" content="{HT}">\n'
          f'<meta name="twitter:description" content="{HD}">\n<meta name="twitter:image" content="{PV}images/hayes-front-of-house.jpg">\n')
    top = top.replace('<meta name="robots" content="noindex,nofollow">\n', '<meta name="robots" content="noindex,nofollow">\n' + og)
    top = top.replace('<body id="top">', '<body id="top" class="sub">')
    nav = html[a:b]
    nav = nav[nav.index('<div class="site-nav-row">'):nav.index('<div class="wm"')]
    for k in ("about","services","properties","areas","contact"):
        nav = nav.replace(f'href="#{k}"', f'href="index.html#{k}"')
    nav = nav.replace('href="#top"', 'href="index.html"').replace(LIC_NAV, "")
    nav = nav.replace('<a href="hayes.html">', '<a href="hayes.html" aria-current="page">')
    foot = html[html.index("</main>"):].replace("      " + LIC_FOOT + "\n", "")
    page = top + f"""<header class="hayes-hero">
  {nav}<div class="hayes-copy">
    <p class="eyebrow">Showcase property &middot; Schroon Lake, New York</p>
    <h1>A family home in the Adirondacks, ready for your season</h1>
    <p class="hayes-sub">41 Hayes Road &middot; Seasonal and long-term rental</p>
    <div class="btns"><a class="btn gold" href="#availability">Get notified when dates open</a></div>
  </div>
</header>
<main id="main">
<section class="hayes-intro">
  <div class="wrap hayes-grid">
    <div>
      <p class="eyebrow">The Hayes House</p>
      <h2>Cared for like a family home</h2>
      <p class="hayes-lead">41 Hayes Road is a showcase property and seasonal rental in Schroon Lake, New York. It is Matthew's family home, so it gets the care a family home deserves, and the house is prepared with care before every arrival.</p>
      <ul class="hl">
        <li>4 bedrooms &middot; 3 baths &middot; sleeps 8</li>
        <li>Schroon Lake, New York, near the water, in the heart of the Adirondacks</li>
        <li>Minutes from I-87, the Adirondack Northway</li>
        <li>Day trips to Lake George and Lake Placid</li>
        <li>Seasonal and long-term stays</li>
      </ul>
      <p class="garage"><strong>Please note:</strong> The large garage behind the house is private storage and is not part of the rental.</p>
    </div>
    <figure class="hayes-main"><img src="images/hayes-front-of-house.jpg" alt="The front of the house at 41 Hayes Road" loading="lazy"><figcaption>41 Hayes Road</figcaption></figure>
  </div>
</section>
<section class="hayes-gallery" aria-label="Photos">
  <div class="wrap gal">
    <figure><img src="images/hayes-lake-path.jpg" alt="A wooded path at the Hayes House" loading="lazy"><figcaption>The path through the trees</figcaption></figure>
    <figure><img src="images/hayes-lake-shoreline-mountains.jpg" alt="Schroon Lake and the mountains nearby" loading="lazy"><figcaption>Schroon Lake and the mountains nearby</figcaption></figure>
  </div>
</section>
<section class="hayes-avail" id="availability">
  <div class="wrap avail-box">
    <p class="eyebrow">Availability</p>
    <h2>Bookings not open yet. Dates are currently blocked.</h2>
    <p class="vrbo">Coming soon to VRBO.</p>
    <p>Want first word when dates open? Call or send a message and we will let you know.</p>
    <div class="btns"><a class="btn gold" href="tel:+15188686689">Get notified when dates open: call 518-868-6689</a><a class="btn ghost" href="index.html#contact">Send a message</a></div>
  </div>
</section>
""" + foot
    assert "\u2014" not in page and "\u2013" not in page
    for bad in ("lakefront", "dock", "lake access", "boat", "state farm", "short-term", "short term", "license.html"):
        assert bad not in page.lower(), bad
    (out / "hayes.html").write_text(page)
    print("wrote", out / "hayes.html")

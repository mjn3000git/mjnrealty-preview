# Generates the MJN Realty preview pages from one shared header and footer.
HEAD='''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="robots" content="noindex, nofollow">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500&amp;family=Inter:wght@400;500;600&amp;display=swap">
  <link rel="stylesheet" href="css/style.css">
  <link rel="icon" href="images/favicon.svg" type="image/svg+xml">
  <script src="js/main.js" defer></script>
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>
  <div class="draft-banner" role="note">Preview only &middot; not the live site</div>
  <header class="site-header">
    <div class="wrap header-inner">
      <a href="index.html" class="logo" aria-label="MJN Realty home">
        <span class="logo-mark mjn" aria-hidden="true"><span>MJN</span></span>
        <span><span class="logo-name">MJN Realty</span><span class="logo-sub">Adirondacks, New York</span></span>
      </a>
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">Menu</button>
      <nav class="site-nav" id="site-nav" aria-label="Main">
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="properties.html">Properties</a></li>
          <li><a href="about.html">About</a></li>
          <li><a href="contact.html" class="nav-cta">Contact</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <main id="main">
'''
FOOT='''  </main>

  <footer class="site-footer">
    <svg class="ridge" viewBox="0 0 1200 60" preserveAspectRatio="none" aria-hidden="true" focusable="false"><path d="M0 50 L110 32 L190 42 L320 14 L430 38 L540 24 L650 44 L780 10 L900 36 L1010 22 L1120 40 L1200 30" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>
    <div class="wrap footer-grid">
      <div>
        <div class="footer-brand"><span class="logo-mark mjn" aria-hidden="true"><span>MJN</span></span><span class="logo-name">MJN Realty</span></div>
        <p>Adirondack property in the Lake George and Schroon Lake region of New York.</p>
      </div>
      <div>
        <p><strong>Contact</strong><br>
        <span class="ph">Email, phone, and mailing address to be added</span></p>
      </div>
      <div>
        <p><a href="properties.html">Properties</a><br>
        <a href="https://41hayes.com">The Hayes House</a><br>
        <a href="about.html">About</a><br>
        <a href="contact.html">Contact</a></p>
      </div>
    </div>
    <p class="wrap small">&copy; <span data-year>2026</span> MJN Realty. All rights reserved.</p>
  </footer>
</body>
</html>
'''
CTA='''    <section class="cta-band">
      <div class="wrap">
        <h2>Let&rsquo;s talk</h2>
        <p>Questions about a property or the region? Reach out to MJN Realty directly.</p>
        <div class="btn-row"><a class="btn" href="contact.html">Get in touch</a></div>
      </div>
    </section>
'''
HAYES='''<div class="property">
          <figure><img src="images/hayes-house-800.jpg" srcset="images/hayes-house-800.jpg 800w, images/hayes-house.jpg 1400w" sizes="(max-width: 760px) 100vw, 620px" alt="The Hayes House: a white single-story home with blue shutters and a blue front door on a wide lawn under tall pines and early fall color" loading="lazy" width="1400" height="1050"></figure>
          <div class="body">
            <p class="eyebrow">Seasonal rental</p>
            <h3>The Hayes House</h3>
            <p class="meta">Schroon Lake, New York</p>
            <p>A private Adirondack retreat in Schroon Lake, kept for family, friends, and select guests by invitation. Stays are seasonal and arranged directly, never through a booking platform.</p>
            <p>Bedrooms: 4 &middot; Baths: 3 &middot; Sleeps: 8</p>
            <div class="btn-row"><a class="btn" href="https://41hayes.com">Visit 41hayes.com</a></div>
          </div>
        </div>'''
pages={}
pages['index.html']=('MJN Realty | Adirondack Property, New York','MJN Realty, Adirondack property in the Lake George and Schroon Lake region of New York. Founded by Matthew Nothdurft.','''    <section class="hero mjn">
      <div class="wrap hero-grid">
      <figure class="hero-photo"><img src="images/schroon-lake-800.jpg" srcset="images/schroon-lake-800.jpg 800w, images/schroon-lake.jpg 1600w" sizes="(max-width: 860px) 100vw, 680px" alt="Schroon Lake on a clear fall day, with wooded Adirondack hills in autumn color across the water" width="1600" height="1200" fetchpriority="high"></figure>
      <div class="hero-panel">
        <p class="eyebrow">Adirondacks &middot; New York</p>
        <h1>MJN Realty</h1>
        <p class="tagline">Adirondack property, kept with care.</p>
        <p>Adirondack property in the Lake George and Schroon Lake region of New York, founded by Matthew Nothdurft, licensed real estate broker.</p>
        <div class="btn-row">
          <a class="btn" href="properties.html">View properties</a>
          <a class="btn secondary" href="contact.html">Contact</a>
        </div>
      </div>
      </div>
    </section>
    <ul class="region-strip" aria-label="Region"><li>Adirondacks</li><li>Lake George</li><li>Schroon Lake</li><li>Queensbury</li></ul>

    <section class="section">
      <div class="wrap">
        <h2>About MJN Realty</h2>
        <p class="lead">MJN Realty was founded by Matthew Nothdurft in the Adirondack region of New York. We are a service that specializes in seasonal and rental properties as well as property management in the Adirondack region.</p>
      </div>
    </section>

    <section class="section alt">
      <div class="wrap">
        <h2>What we do</h2>
        <div class="grid five">
          <div class="card steel"><span class="num">01</span><h3>Seasonal and vacation rentals</h3><p>Weekly and full-season rentals across the Adirondacks. We handle the details, from marketing and reservations to guest communication and cleaning, so owners can stay hands-off.</p></div>
          <div class="card wood"><span class="num">02</span><h3>Vacation home purchases</h3><p>Help finding the right second home or getaway. We look past the price at location, upkeep, rental potential, and long-term fit.</p></div>
          <div class="card"><span class="num">03</span><h3>Property management</h3><p>Care for homes while owners are away, including regular home watch visits, seasonal opening and closing, and checks after storms.</p></div>
          <div class="card steel"><span class="num">04</span><h3>Free rental income evaluation</h3><p>A free, no-obligation estimate of what a home could earn as a seasonal rental, for owners and for buyers.</p></div>
          <div class="card wood"><span class="num">05</span><h3>List and sell your home</h3><p>Thinking of selling? We present your Adirondack home to the right buyers, with a market analysis to start.</p></div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap">
        <h2>Featured property</h2>
        '''+HAYES+'''
      </div>
    </section>

    <section class="section alt">
      <div class="wrap">
        <h2>The region</h2>
        <p class="lead">Lakes, mountains, and quiet woods, from Lake George north to Schroon Lake.</p>
        <div class="gallery three">
          <figure><img src="images/fall-shallows-800.jpg" srcset="images/fall-shallows-800.jpg 800w, images/fall-shallows.jpg 1600w" sizes="(max-width: 600px) 100vw, 360px" alt="Fallen oak and maple leaves in clear, shallow lake water" loading="lazy" width="1600" height="1200"><figcaption>Fall on the water</figcaption></figure>
          <figure><img src="images/wooded-path-800.jpg" srcset="images/wooded-path-800.jpg 600w, images/wooded-path.jpg 1050w" sizes="(max-width: 600px) 100vw, 360px" alt="A sandy path through tall pines and early fall foliage on a sunny day" loading="lazy" width="1050" height="1400"><figcaption>Adirondack woods</figcaption></figure>
          <figure><img src="images/leaves-in-lake-800.jpg" srcset="images/leaves-in-lake-800.jpg 800w, images/leaves-in-lake.jpg 1600w" sizes="(max-width: 600px) 100vw, 360px" alt="Orange and brown autumn leaves resting on pebbles under clear lake water" loading="lazy" width="1600" height="1200"><figcaption>Autumn leaves in the lake</figcaption></figure>
        </div>
      </div>
    </section>
'''+CTA)
pages['properties.html']=('Properties | MJN Realty','Properties from MJN Realty in the Adirondacks of New York, including the Hayes House, a seasonal rental in Schroon Lake.','''    <section class="page-hero">
      <div class="wrap">
        <p class="eyebrow">MJN Realty</p>
        <h1>Properties</h1>
        <p>Adirondack property from MJN Realty.</p>
      </div>
    </section>

    <section class="section">
      <div class="wrap">
        <h2>The Hayes House</h2>
        '''+HAYES+'''
      </div>
    </section>

    <section class="section alt">
      <div class="wrap">
        <h2>Other properties</h2>
        <p><span class="ph">Any other property Matthew wants listed here, with his own description and photos. Leave this section out if there are none to show.</span></p>
      </div>
    </section>
'''+CTA)
pages['about.html']=('About | MJN Realty','About MJN Realty and its founder, Matthew Nothdurft.','''    <section class="page-hero">
      <div class="wrap">
        <p class="eyebrow">MJN Realty</p>
        <h1>About</h1>
        <p>MJN Realty was founded by Matthew Nothdurft.</p>
      </div>
    </section>

    <section class="section">
      <div class="wrap split">
        <div>
          <h2>Matthew Nothdurft</h2>
          <p class="eyebrow">Founder &amp; CEO</p>
          <p>Matthew Nothdurft is the founder and CEO of MJN Realty.</p>
          <p>Born in the Adirondacks and raised on its lakes and trails, Matthew Nothdurft leads MJN Realty with a deep love for the region he calls home.</p>
        </div>
        <figure class="portrait-photo"><img src="images/matthew-nothdurft.jpg" alt="Matthew Nothdurft" width="671" height="894" loading="lazy"></figure>
      </div>
    </section>

    <section class="section alt">
      <div class="wrap">
        <h2>The company</h2>
        <p class="lead">MJN Realty is a full-service property management and real estate company covering the Lake George and Schroon Lake regions of New York, including Hayes House at Schroon Lake.</p>
        <p>What sets us apart is a hands-on, personal approach. From routine check-ins to coordinating repairs with the right contractors and vendors, we treat every property like our own. Beyond the work itself, Matthew is a local resource for the area. PADI scuba certified, boater's licensed, and an e-bike enthusiast, he knows the Adirondacks inside and out and is glad to point you toward the best of what the region has to offer.</p>
        <figure class="feature-photo"><img src="images/schroon-lake-800.jpg" srcset="images/schroon-lake-800.jpg 800w, images/schroon-lake.jpg 1600w" sizes="(max-width: 1100px) 100vw, 1100px" alt="Schroon Lake on a clear fall day, with wooded hills across the water" loading="lazy" width="1600" height="1200"><figcaption>Schroon Lake, New York</figcaption></figure>
      </div>
    </section>
'''+CTA)
pages['contact.html']=('Contact | MJN Realty','How to reach MJN Realty.','''    <section class="page-hero">
      <div class="wrap">
        <p class="eyebrow">MJN Realty</p>
        <h1>Contact</h1>
        <p>Questions about a property or the region are welcome.</p>
      </div>
    </section>

    <section class="section">
      <div class="wrap split">
        <div>
          <h2>Get in touch</h2>
          <ul class="contact-list">
            <li><strong>Email</strong><span class="ph">Business email to be added</span></li>
            <li><strong>Phone</strong><span class="ph">Business phone to be added</span></li>
            <li><strong>Mailing address</strong><span class="ph">Mailing address, if Matthew wants one shown</span></li>
          </ul>
          <p>For stays at the Hayes House, see <a href="https://41hayes.com">41hayes.com</a>.</p>
        </div>
        <form class="inquiry" id="contact-form" novalidate>
          <p class="form-note">This form is a preview and is not connected. Nothing you type here is sent.</p>
          <fieldset disabled>
            <div class="form-row">
              <div><label for="name">Name</label><input id="name" name="name" autocomplete="name"></div>
              <div><label for="email">Email</label><input id="email" name="email" type="email" autocomplete="email"></div>
            </div>
            <div><label for="message">Message</label><textarea id="message" name="message" rows="5"></textarea></div>
            <div><button class="btn" type="submit">Send message</button></div>
          </fieldset>
          <p id="form-status" tabindex="-1" aria-live="polite"></p>
        </form>
      </div>
    </section>
''')
for f,(t,d,body) in pages.items():
    open(f,'w').write(HEAD.format(title=t,desc=d)+body+FOOT)

# Sun Mountain — Brand Site

A 9-page static brand site built from the Figma designs. Plain HTML / CSS / JS — no build step, no dependencies, deploys anywhere.

## Run it locally

```bash
# from this folder
python3 -m http.server 8080
# or
npx serve .
```

Then open http://localhost:8080

## File map

```
SITE BUILD/
├── index.html         Home
├── brand.html         Our Brand
├── logo.html          Our Logo
├── color.html         Color
├── typography.html    Typography
├── grid.html          Grid & Layouts
├── photography.html   Photography
├── application.html   Application
├── downloads.html     Downloads
├── css/
│   ├── tokens.css     Design tokens (colors, type, spacing) — single source of truth
│   ├── base.css       Reset, web-fonts, base typography
│   ├── components.css Nav, footer, buttons, cards
│   └── pages.css      Per-page section styles
├── js/main.js         Active-nav highlighting, mobile menu toggle, year stamp
├── assets/
│   ├── logos/         Logos used inline in the chrome (nav, footer, hero)
│   ├── svg/           Brand illustrations (color mod, layout examples, etc.)
│   ├── img/           PNG mockups (web, ooh, magazine, app, social, products)
│   ├── fonts/         (drop licensed font files here)
│   └── downloads/     User-facing downloadable assets
│       ├── logos-svg/   34 SVG logo files
│       ├── logos-png/   32 4x PNG logo files
│       ├── logos-eps/   31 EPS print logo files
│       ├── logos-all.zip      9.2 MB — all formats
│       ├── logos-svg-only.zip 71 KB
│       ├── logos-png-only.zip 988 KB
│       └── logos-eps-only.zip 8.2 MB
└── _partials/         Reference nav.html / footer.html (markup is also inlined per page)
```

## Design tokens

Edit `css/tokens.css` to change colors, type, or spacing — every page picks the changes up.

| Token | Value |
|---|---|
| `--c-mountain-green` | `#113027` |
| `--c-deep-blue` | `#121B35` |
| `--c-scratch-black` | `#1C1C1C` |
| `--c-sand` | `#EFEBDF` |
| `--c-sun-yellow` | `#E9CB7D` |
| `--c-white` | `#FFFFFF` |

## Fonts

The site loads **Bricolage Grotesque** from Google Fonts automatically. The other three families are licensed and need files dropped into `assets/fonts/`:

| Family | Files expected |
|---|---|
| Freight Display Compressed | `FreightDispCmp-BoldItalic.woff2` and `.woff` |
| Bicyclette | `Bicyclette-Bold.woff2/.woff`, `Bicyclette-Light.woff2/.woff` |
| Avenir | `Avenir-Roman.woff2`, `Avenir-Light.woff2`, `Avenir-Book.woff2` |

If you have a different filename or weight set, edit the `@font-face` blocks at the top of `css/base.css`. Until those files are present, the site uses high-quality system fallbacks (Playfair Display in italic for the display, Inter / system sans for everything else).

## To finish

A few things to drop in to complete the site:

1. **Hero photo** — drop your golf-course hero shot in `assets/img/hero.jpg`, then in `index.html` find the comment in the `.home-hero__photo` block and uncomment the `<img>` tag. Until then the gradient placeholder renders.
2. **Brand guidelines PDF** — drop your assembled PDF as `assets/downloads/Sun-Mountain-Brand-Guidelines.pdf`. The "Download Full Guidelines" buttons across the site are already wired to it.
3. **Photography library** — the photography page uses CSS placeholder tiles where the gallery photos go. To swap them in, replace each `<div class="placeholder-photo">…</div>` inside a `.media-card` with `<img src="assets/img/photo-name.jpg" alt="…" />`.
4. **Color palette `.ase`** — drop `assets/downloads/sun-mountain-palette.ase` to enable the palette download on the Color page.
5. **Templates** — the Templates section on the Downloads page expects files in `assets/downloads/templates/`. Update the links once the files are in.

## Hosting

The site is fully static. Deploy anywhere:
- **Vercel / Netlify / Cloudflare Pages** — drag this folder into a new project, no config needed.
- **S3 + CloudFront** — upload everything and set `index.html` as default.
- **GitHub Pages** — push the contents of this folder to a repo's `main` branch.

## Editing tips

Each page inlines the nav and footer markup so the site stays static-deployable. If you change the nav (e.g. add a page), find this block in every `*.html` file and update it:

```html
<div class="site-nav__items" id="site-nav-items">
  <a class="site-nav__item" href="brand.html" data-page="brand.html">Brand</a>
  …
</div>
```

The `data-page` attribute is what `js/main.js` uses to highlight the current page.

## Browser support

Modern Chrome, Safari, Firefox, Edge. CSS uses CSS variables, grid, flexbox, and `backdrop-filter`. No transpilation required.

#!/usr/bin/env python3
"""Générateur du site 2 m² : produit des pages HTML statiques optimisées pour le référencement.
Ajouter un guide = ajouter une entrée dans content.py (GUIDES), puis relancer : python3 build.py
"""
import html, json, os, shutil, datetime
from urllib.parse import quote_plus
from content import SITE, PRODUCTS, GUIDES

OUT = os.path.join(os.path.dirname(__file__), "public")
SRC = os.path.join(os.path.dirname(__file__), "src")
TODAY = datetime.date.today().isoformat()
e = html.escape


def aff(query):
    return f"https://www.amazon.fr/s?k={quote_plus(query)}&tag={SITE['amazon_tag']}"


def url(path):
    return SITE["base_url"].rstrip("/") + "/" + path.lstrip("/")


FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..900&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">')


def head(title, desc, path, jsonld, og_type="website"):
    full_title = title if title.startswith(SITE["name"]) else f"{title} | {SITE['name']}"
    ld = "".join(f'<script type="application/ld+json">{json.dumps(j, ensure_ascii=False)}</script>' for j in jsonld)
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(full_title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url(path)}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{e(SITE['name'])}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url(path)}">
<meta property="og:image" content="{url('og.png')}">
<meta property="og:locale" content="fr_FR">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#1d4ed8">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
{FONTS}
<link rel="stylesheet" href="style.css">
{ld}
</head>
<body>"""


NAV = [("index.html", "Accueil"), ("index.html#calcul", "Calculer mon espace"), ("index.html#guides", "Guides"), ("a-propos.html", "À propos")]


def header(current):
    links = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h == current else ""}>{t}</a>' for h, t in NAV)
    return f"""<header class="top"><div class="wrap">
<a class="brand" href="index.html"><span class="brand-mark">2&nbsp;m<sup>2</sup></span><span><strong>{e(SITE['tagline'])}</strong><small>Matériel · plans · programmes</small></span></a>
<nav aria-label="Navigation principale">{links}</nav>
</div></header>
<div class="disclose"><div class="wrap">Liens affiliés : si tu achètes via nos liens, on touche une petite commission, sans surcoût pour toi. Ça finance le site.</div></div>"""


def footer():
    guides = "".join(f'<li><a href="{g["slug"]}.html">{e(g["short"])}</a></li>' for g in GUIDES)
    return f"""<footer><div class="wrap">
<div><span class="brand-mark">2&nbsp;m<sup>2</sup></span><p>{e(SITE['description'])}</p>
<p>En tant que Partenaire Amazon, nous réalisons un bénéfice sur les achats remplissant les conditions requises.</p></div>
<div><h3>Guides</h3><ul>{guides}</ul></div>
<div><h3>Le site</h3><ul><li><a href="a-propos.html">À propos et méthode</a></li><li><a href="mentions-legales.html">Mentions légales</a></li><li><a href="mentions-legales.html#affiliation">Liens affiliés</a></li></ul>
<p>Conseils généraux, qui ne remplacent pas l'avis d'un professionnel de santé.</p></div>
</div></footer>
</body></html>"""


def footprint_svg(w, d, size=64):
    """Emprise au sol dessinée à l'échelle, façon plan coté."""
    if not w or not d:
        return (f'<svg width="{size}" height="{size}" viewBox="0 0 64 64" aria-hidden="true">'
                f'<rect x="4" y="4" width="56" height="56" fill="none" stroke="var(--line)" stroke-dasharray="3 3"/>'
                f'<text x="32" y="36" text-anchor="middle" font-size="9" fill="var(--blue)" font-family="var(--mono)">0 m²</text></svg>')
    m = max(w, d)
    rw, rd = 52 * w / m, 52 * d / m
    x, y = (64 - rw) / 2, (64 - rd) / 2
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 64 64" aria-hidden="true">'
            f'<rect x="{x:.1f}" y="{y:.1f}" width="{rw:.1f}" height="{rd:.1f}" fill="var(--blue-soft)" stroke="var(--blue)" stroke-width="1.5"/></svg>')


def product_card(i, p):
    area = f"≈ {p['w']} × {p['d']} cm au sol" if p["w"] else "0 cm² au sol"
    return f"""<article class="card">
<div class="num"><span>RÉF. {i:02d}</span><b>{e(p['level'])}</b></div>
<h3>{e(p['name'])}</h3>
<p>{e(p['why'])}</p>
<div>
<div class="foot">{footprint_svg(p['w'], p['d'])}<span class="mono">{area}<br>{e(p['storage'])}</span></div>
<p style="margin-top:12px"><a class="go" href="{aff(p['query'])}" rel="sponsored nofollow noopener" target="_blank">Voir les modèles →</a>{' · <a href="' + p['guide'] + '.html">Notre guide</a>' if p.get('guide') else ''}</p>
</div>
</article>"""


HERO_PLAN = """<svg viewBox="0 0 420 300" role="img" aria-label="Plan coté d'un coin d'entraînement de 2 mètres sur 1 mètre : tapis, haltères, kettlebell, élastiques">
<rect class="draw" x="40" y="40" width="340" height="170" fill="none" stroke="var(--ink)" stroke-width="2.5"/>
<rect class="draw d2" x="60" y="60" width="311" height="104" fill="var(--blue-soft)" stroke="var(--blue)" stroke-width="1.5"/>
<text x="215" y="117" text-anchor="middle" font-size="12" fill="var(--blue)">TAPIS 183 × 61</text>
<rect class="draw d3" x="60" y="174" width="68" height="28" fill="none" stroke="var(--orange)" stroke-width="2"/>
<text x="94" y="192" text-anchor="middle" font-size="10" fill="var(--orange)">HALTÈRES</text>
<circle class="draw d4" cx="160" cy="188" r="15" fill="none" stroke="var(--orange)" stroke-width="2"/>
<text x="160" y="192" text-anchor="middle" font-size="9" fill="var(--orange)">KB</text>
<rect class="draw d5" x="190" y="176" width="44" height="26" fill="none" stroke="var(--orange)" stroke-width="2"/>
<text x="212" y="193" text-anchor="middle" font-size="9" fill="var(--orange)">ÉLAST.</text>
<line x1="40" y1="245" x2="380" y2="245" stroke="var(--ink)"/><line x1="40" y1="238" x2="40" y2="252" stroke="var(--ink)"/><line x1="380" y1="238" x2="380" y2="252" stroke="var(--ink)"/>
<text x="210" y="268" text-anchor="middle" font-size="13" fill="var(--ink)">200 cm</text>
<line x1="400" y1="40" x2="400" y2="210" stroke="var(--ink)"/><line x1="393" y1="40" x2="407" y2="40" stroke="var(--ink)"/><line x1="393" y1="210" x2="407" y2="210" stroke="var(--ink)"/>
<text x="412" y="130" font-size="13" fill="var(--ink)" transform="rotate(90 412 130)" text-anchor="middle">100 cm</text>
<text x="40" y="28" font-size="11" fill="var(--muted)">ÉCH. 1:10 · SALON / CHAMBRE / COULOIR</text>
</svg>"""


CALC = """<div class="calc">
<div class="controls">
<div><label for="w">Largeur dispo <span class="val" id="wv">200 cm</span></label><input type="range" id="w" min="80" max="400" step="10" value="200"></div>
<div><label for="d">Profondeur dispo <span class="val" id="dv">120 cm</span></label><input type="range" id="d" min="60" max="400" step="10" value="120"></div>
<div><label for="h">Hauteur sous plafond <span class="val" id="hv">250 cm</span></label><input type="range" id="h" min="200" max="300" step="5" value="250"></div>
<p class="mono" style="margin:0;color:var(--muted)">Mesure l'espace libre au sol, meubles déplacés. Les emprises sont des moyennes.</p>
</div>
<div class="result">
<div class="verdict" id="verdict"></div>
<svg class="canvas" id="room" viewBox="0 0 420 260" role="img" aria-label="Plan de ton espace à l'échelle"></svg>
<ul id="fits"></ul>
</div>
</div>
<script>
(() => {
  const items = [
    {id:"tapis", n:"Tapis de sol", w:183, d:61, need:[190,70], q:"tapis de sol fitness épais"},
    {id:"elast", n:"Élastiques de résistance", w:30, d:20, need:[150,80], q:"élastiques de résistance musculation lot"},
    {id:"barre", n:"Barre de traction de porte", w:0, d:0, need:[0,0], q:"barre de traction porte sans perçage"},
    {id:"halt", n:"Haltères réglables", w:45, d:40, need:[180,100], q:"haltères réglables"},
    {id:"kb", n:"Kettlebell", w:22, d:22, need:[180,150], q:"kettlebell fonte"},
    {id:"corde", n:"Corde à sauter", w:0, d:0, need:[200,120], h:240, q:"corde à sauter roulements"},
    {id:"banc", n:"Banc pliable", w:125, d:50, need:[200,140], q:"banc de musculation pliable"}
  ];
  const TAG = "__TAG__";
  const $ = id => document.getElementById(id);
  const fits = (it, W, D, H) => {
    const [a,b] = it.need; if (it.h && H < it.h) return false;
    return (W >= a && D >= b) || (D >= a && W >= b);
  };
  function render() {
    const W = +$("w").value, D = +$("d").value, H = +$("h").value;
    $("wv").textContent = W + " cm"; $("dv").textContent = D + " cm"; $("hv").textContent = H + " cm";
    const ok = items.filter(it => fits(it, W, D, H));
    const m2 = (W * D / 10000).toLocaleString("fr-FR", {maximumFractionDigits: 1});
    const level = ok.length >= 7 ? "le kit complet" : ok.length >= 5 ? "le kit 2 m²" : ok.length >= 3 ? "le kit mini" : "le kit de poche";
    $("verdict").innerHTML = `${m2} m² : tu peux installer <span>${level}</span>, ${ok.length} équipements sur ${items.length}.`;
    $("fits").innerHTML = items.map(it => {
      const y = fits(it, W, D, H);
      const why = !y ? (it.h && H < it.h ? "plafond trop bas" : `il faut ${it.need[0]} × ${it.need[1]} cm`) : (it.w ? `${it.w} × ${it.d} cm au sol` : "0 cm² au sol");
      return `<li class="${y ? "" : "no"}">${y ? "✓" : "✕"} <a href="https://www.amazon.fr/s?k=${encodeURIComponent(it.q)}&tag=${TAG}" rel="sponsored nofollow noopener" target="_blank">${it.n}</a> <span class="mono">${why}</span></li>`;
    }).join("");
    const s = Math.min(380 / W, 220 / D), rw = W * s, rd = D * s, x0 = (420 - rw) / 2, y0 = (260 - rd) / 2;
    let svg = `<rect x="${x0}" y="${y0}" width="${rw}" height="${rd}" fill="none" stroke="var(--ink)" stroke-width="2"/>`;
    svg += `<text x="${x0 + rw/2}" y="${y0 - 6}" text-anchor="middle" font-size="11" fill="var(--ink)" font-family="var(--mono)">${W} cm</text>`;
    let cx = x0 + 8, cy = y0 + 8;
    const horiz = W >= D;
    if (ok.find(i => i.id === "tapis")) {
      const tw = (horiz ? 183 : 61) * s, td = (horiz ? 61 : 183) * s;
      svg += `<rect x="${cx}" y="${cy}" width="${tw}" height="${td}" fill="var(--blue-soft)" stroke="var(--blue)"/><text x="${cx + tw/2}" y="${cy + td/2 + 4}" text-anchor="middle" font-size="10" fill="var(--blue)" font-family="var(--mono)">TAPIS</text>`;
      if (horiz) cy += td + 8; else cx += tw + 8;
    }
    ok.filter(i => i.w && i.id !== "tapis").forEach(it => {
      const iw = it.w * s, id = it.d * s;
      if (horiz && cx + iw > x0 + rw) { cx = x0 + 8; cy += id + 8; }
      if (!horiz && cy + id > y0 + rd) { cy = y0 + 8; cx += iw + 8; }
      svg += `<rect x="${cx}" y="${cy}" width="${iw}" height="${id}" fill="none" stroke="var(--orange)" stroke-width="1.5"/>`;
      if (iw > 34) svg += `<text x="${cx + iw/2}" y="${cy + id/2 + 3}" text-anchor="middle" font-size="8" fill="var(--orange)" font-family="var(--mono)">${it.n.split(" ")[0].toUpperCase()}</text>`;
      if (horiz) cx += iw + 8; else cy += id + 8;
    });
    $("room").innerHTML = svg;
  }
  ["w","d","h"].forEach(id => $(id).addEventListener("input", render));
  render();
})();
</script>"""


def org_ld():
    return {"@context": "https://schema.org", "@type": "WebSite", "name": SITE["name"], "url": url(""),
            "description": SITE["description"], "inLanguage": "fr-FR"}


def build_index():
    cards = "".join(product_card(i + 1, p) for i, p in enumerate(PRODUCTS))
    guides = "".join(f'<a class="guide" href="{g["slug"]}.html"><span class="mono">GUIDE · {e(g["kicker"])}</span><h3>{e(g["title"])}</h3><p>{e(g["desc"])}</p></a>' for g in GUIDES)
    itemlist = {"@context": "https://schema.org", "@type": "ItemList", "name": "Le kit pour s'entraîner dans 2 m²",
                "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": p["name"]} for i, p in enumerate(PRODUCTS)]}
    page = head(f"{SITE['name']} : la salle de sport qui tient dans 2 m²",
                "Tout pour s'entraîner chez soi dans un petit espace : calcule ce qui tient chez toi, choisis le bon matériel et suis un programme simple.",
                "", [org_ld(), itemlist])
    page += header("index.html")
    page += f"""<main>
<div class="wrap hero">
<div>
<span class="kicker">Plan n° 01 · Salle de sport d'appartement</span>
<h1>La salle de sport qui tient dans <span class="o">2&nbsp;m²</span>.</h1>
<p class="lead">On mesure, on dessine, on choisit. Tout le matériel pour t'entraîner chez toi, avec la place exacte que chaque objet prend au sol.</p>
<div class="actions"><a class="btn" href="#calcul">Calculer mon espace →</a><a class="btn ghost" href="#kit">Voir le kit</a></div>
</div>
<div class="plan"><span class="tag">FIG. 1 · LE KIT 2 m²</span>{HERO_PLAN}</div>
</div>

<section class="section" id="calcul"><div class="wrap">
<div class="section-head"><span class="ref">§ 01 · CALCUL</span><div><h2>Qu'est-ce qui tient chez toi ?</h2><p>Règle la taille de ton espace libre. Le plan se redessine à l'échelle et te dit quel matériel rentre, et ce qu'il te faudrait pour le reste.</p></div></div>
{CALC.replace("__TAG__", SITE['amazon_tag'])}
</div></section>

<section class="section" id="kit"><div class="wrap">
<div class="section-head"><span class="ref">§ 02 · KIT</span><div><h2>Le kit, pièce par pièce</h2><p>Chaque fiche indique l'emprise au sol, où le ranger, et pour quel niveau. Commence par les deux premières : tu peux déjà travailler tout le corps.</p></div></div>
<div class="kit">{cards}</div>
</div></section>

<section class="section" id="guides"><div class="wrap">
<div class="section-head"><span class="ref">§ 03 · GUIDES</span><div><h2>Les guides pour bien choisir</h2><p>Ce qu'on regarde vraiment avant d'acheter, et les erreurs à éviter.</p></div></div>
<div class="guides">{guides}</div>
</div></section>
</main>"""
    page += footer()
    return page


def build_guide(g):
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage",
              "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in g["faq"]]}
    art_ld = {"@context": "https://schema.org", "@type": "Article", "headline": g["title"], "description": g["desc"],
              "datePublished": g["date"], "dateModified": TODAY, "inLanguage": "fr-FR",
              "author": {"@type": "Organization", "name": SITE["name"]}, "publisher": {"@type": "Organization", "name": SITE["name"]},
              "image": url("og.png"), "mainEntityOfPage": url(g["slug"] + ".html")}
    crumb_ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Accueil", "item": url("")},
        {"@type": "ListItem", "position": 2, "name": g["short"], "item": url(g["slug"] + ".html")}]}
    body = g["body"].replace("{{TAG}}", SITE["amazon_tag"])
    for key, q in g.get("links", {}).items():
        body = body.replace("{{" + key + "}}", aff(q))
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in g["faq"])
    others = "".join(f'<li><a href="{o["slug"]}.html">{e(o["short"])}</a></li>' for o in GUIDES if o["slug"] != g["slug"])
    toc = "".join(f"<li>{e(t)}</li>" for t in g["toc"])
    page = head(g["title"], g["desc"], g["slug"] + ".html", [art_ld, faq_ld, crumb_ld], "article")
    page += header("")
    page += f"""<main class="wrap">
<div class="crumbs"><a href="index.html">Accueil</a> / {e(g['short'])}</div>
<header class="article-head">
<span class="mono" style="color:var(--blue)">GUIDE · {e(g['kicker'])}</span>
<h1>{e(g['title'])}</h1>
<p class="lead">{e(g['desc'])}</p>
<p class="meta">Mis à jour le {datetime.date.today().strftime('%d/%m/%Y')} · {g['minutes']} min de lecture</p>
</header>
<div class="article-body">
<article class="prose">{body}
<h2 id="faq">Questions fréquentes</h2><div class="faq">{faq}</div>
</article>
<aside class="aside">
<div class="box"><h3>Dans ce guide</h3><ol>{toc}</ol></div>
<div class="box"><h3>Combien de place as-tu ?</h3><p style="margin:0 0 10px;font-size:15px;color:var(--muted)">Le calculateur dessine ton espace et te dit ce qui rentre.</p><a class="btn" href="index.html#calcul">Calculer →</a></div>
<div class="box"><h3>Autres guides</h3><ul style="margin:0;padding-left:18px;font-size:15px">{others}</ul></div>
</aside>
</div>
</main>"""
    page += footer()
    return page


def build_simple(slug, title, desc, inner):
    page = head(title, desc, slug + ".html", [org_ld()])
    page += header(slug + ".html")
    page += f'<main class="wrap"><header class="article-head"><h1>{e(title)}</h1></header><div class="prose" style="padding:32px 0 64px">{inner}</div></main>'
    page += footer()
    return page


ABOUT = """<p><strong>2 m²</strong> part d'une idée simple : la plupart des gens n'ont ni la place ni le budget pour une salle de sport à la maison. Ils ont un bout de salon, de chambre ou de couloir. C'est suffisant, à condition de bien choisir.</p>
<h2>Notre méthode</h2>
<p>Pour chaque équipement, on regarde trois choses : l'utilité (combien d'exercices il permet), l'emprise au sol (la place réellement occupée, en centimètres) et le rangement (où il va quand on ne s'en sert pas).</p>
<p>On explique les critères de choix pour que tu puisses comparer toi-même les modèles. On n'invente ni tests, ni avis, ni notes. Quand on donne des mesures, ce sont des moyennes à vérifier sur la fiche du produit.</p>
<h2>Comment le site est financé</h2>
<p>Certains liens sont des liens affiliés, notamment vers Amazon. Si tu achètes après avoir cliqué, on touche une petite commission. Le prix reste le même pour toi. Ça ne change pas nos conseils : on recommande aussi du matériel qui ne coûte presque rien, comme les élastiques.</p>"""

LEGAL = """<p><em>À compléter avant la mise en ligne officielle.</em></p>
<h2>Éditeur du site</h2><p>Nom et prénom ou raison sociale, statut (micro-entreprise), numéro SIRET, adresse, adresse e-mail de contact.</p>
<h2>Hébergeur</h2><p>Nom, adresse et contact de l'hébergeur du site.</p>
<h2 id="affiliation">Liens affiliés</h2><p>Ce site participe au Programme Partenaires d'Amazon EU, un programme d'affiliation conçu pour permettre à des sites de percevoir une rémunération grâce à la création de liens vers Amazon.fr. En tant que Partenaire Amazon, nous réalisons un bénéfice sur les achats remplissant les conditions requises.</p>
<h2>Données personnelles</h2><p>Ce site ne dépose pas de cookie de mesure d'audience à ce jour. Les sites marchands vers lesquels mènent nos liens ont leur propre politique de confidentialité.</p>
<h2>Santé</h2><p>Les contenus sont des conseils généraux sur l'entraînement. Ils ne remplacent pas l'avis d'un médecin ou d'un professionnel de santé. En cas de douleur, de blessure ou de problème de santé, demande un avis médical avant de commencer.</p>"""


def build():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    pages = {"index.html": build_index()}
    for g in GUIDES:
        pages[g["slug"] + ".html"] = build_guide(g)
    pages["a-propos.html"] = build_simple("a-propos", "À propos de 2 m²", "Qui on est, comment on choisit le matériel et comment le site est financé.", ABOUT)
    pages["mentions-legales.html"] = build_simple("mentions-legales", "Mentions légales", "Mentions légales, liens affiliés et données personnelles du site 2 m².", LEGAL)
    for name, content in pages.items():
        with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
            f.write(content)
    for name in ("style.css", "favicon.svg", "og.png"):
        if os.path.exists(os.path.join(SRC, name)):
            shutil.copy(os.path.join(SRC, name), OUT)
    sitemap = "".join(f"<url><loc>{url('' if n == 'index.html' else n)}</loc><lastmod>{TODAY}</lastmod></url>"
                      for n in pages if n != "mentions-legales.html")
    with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{sitemap}</urlset>')
    with open(os.path.join(OUT, "robots.txt"), "w") as f:
        f.write(f"User-agent: *\nAllow: /\nSitemap: {url('sitemap.xml')}\n")
    print("OK :", ", ".join(sorted(os.listdir(OUT))))


if __name__ == "__main__":
    build()

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
         '<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600..800&family=Nunito+Sans:wght@400;600;700;800&display=swap" rel="stylesheet">')


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


NAV = [("index.html", "Accueil"), ("index.html#commencer", "Par où commencer"), ("index.html#materiel", "Le matériel"), ("index.html#guides", "Les guides")]


def header(current):
    links = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h == current else ""}>{t}</a>' for h, t in NAV)
    return f"""<header class="top"><div class="wrap">
<a class="brand" href="index.html"><span class="brand-mark">2m²</span><strong>{e(SITE['tagline'])}</strong></a>
<nav aria-label="Navigation principale">{links}</nav>
</div></header>
<div class="disclose">Certains liens sont affiliés : si tu achètes via ces liens, on touche une petite commission. Ça ne change pas le prix pour toi.</div>"""


def footer():
    guides = "".join(f'<li><a href="{g["slug"]}.html">{e(g["short"])}</a></li>' for g in GUIDES)
    return f"""<footer><div class="wrap">
<div><span class="brand-mark">2m²</span><p>{e(SITE['description'])}</p>
<p>En tant que Partenaire Amazon, nous réalisons un bénéfice sur les achats remplissant les conditions requises.</p></div>
<div><h3>Guides</h3><ul>{guides}</ul></div>
<div><h3>Le site</h3><ul><li><a href="a-propos.html">À propos et méthode</a></li><li><a href="mentions-legales.html">Mentions légales</a></li><li><a href="mentions-legales.html#affiliation">Liens affiliés</a></li></ul>
<p>Conseils généraux, qui ne remplacent pas l'avis d'un professionnel de santé.</p></div>
</div></footer>
</body></html>"""


ICONS = {
    "tapis": '<rect x="10" y="30" width="78" height="26" rx="4"/><ellipse cx="88" cy="43" rx="10" ry="13"/><ellipse cx="88" cy="43" rx="4" ry="6"/>',
    "elastiques": '<ellipse cx="38" cy="43" rx="26" ry="16"/><ellipse cx="62" cy="43" rx="26" ry="16"/>',
    "halteres": '<rect x="12" y="26" width="12" height="34" rx="3"/><rect x="24" y="31" width="8" height="24" rx="2"/><line x1="32" y1="43" x2="68" y2="43" stroke-width="6"/><rect x="68" y="31" width="8" height="24" rx="2"/><rect x="76" y="26" width="12" height="34" rx="3"/>',
    "barre": '<path d="M22 80 V16 H78 V80"/><line x1="12" y1="24" x2="88" y2="24" stroke-width="6"/><rect x="34" y="18" width="8" height="12" rx="2"/><rect x="58" y="18" width="8" height="12" rx="2"/>',
    "kettlebell": '<path d="M36 34 C36 14 64 14 64 34"/><circle cx="50" cy="55" r="22"/>',
    "corde": '<rect x="14" y="14" width="10" height="24" rx="5"/><rect x="76" y="14" width="10" height="24" rx="5"/><path d="M19 38 C19 90 81 90 81 38"/>',
    "rouleau": '<rect x="18" y="32" width="64" height="24" rx="4"/><ellipse cx="18" cy="44" rx="6" ry="12"/><line x1="34" y1="32" x2="34" y2="56"/><line x1="50" y1="32" x2="50" y2="56"/><line x1="66" y1="32" x2="66" y2="56"/>',
    "banc": '<rect x="12" y="34" width="76" height="12" rx="4"/><line x1="24" y1="46" x2="24" y2="72"/><line x1="76" y1="46" x2="76" y2="72"/><line x1="16" y1="72" x2="32" y2="72"/><line x1="68" y1="72" x2="84" y2="72"/>',
}


def icon(name, size=88):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 100 86" fill="none" stroke="currentColor" stroke-width="4" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')


BUDGET = {"€": "Petit budget", "€€": "Budget moyen", "€€€": "Gros budget"}


def product_card(i, p):
    tier = p["tier"]
    badge = f'<span class="badge{" alt" if tier != "Essentiel" else ""}">{e(tier)}</span>'
    guide = f'<a class="guide-link" href="{p["guide"]}.html">Comment bien le choisir</a>' if p.get("guide") else ""
    mate = next(x for x in PRODUCTS if x["icon"] == p["pair"])
    return f"""<article class="card{' start' if tier == 'Essentiel' else ''}" id="p-{p['icon']}">{badge}
<div class="art">{icon(p['icon'])}</div>
<h3>{e(p['name'])}</h3>
<p>{e(p['why'])}</p>
<div class="facts"><span><b>Place :</b> {e(p['compare'])}</span><span><b>Rangement :</b> {e(p['storage'].lower())}</span><span><b>Prix :</b> {BUDGET[p['budget']].lower()}</span></div>
<a class="btn go" href="{aff(p['query'])}" rel="sponsored nofollow noopener" target="_blank">Voir les prix</a>
<p class="pair">Va bien avec : <a href="{aff(mate['query'])}" rel="sponsored nofollow noopener" target="_blank">{e(mate['name'].lower())}</a></p>
{guide}
</article>"""


KITS = [
    ("Kit débutant", "Pour démarrer cette semaine", "Tout le corps, 3 fois par semaine.", ["tapis", "elastiques", "halteres"], "€"),
    ("Kit progression", "Après 1 ou 2 mois", "Le kit débutant, plus de quoi muscler le dos et faire du cardio.", ["tapis", "elastiques", "halteres", "barre", "kettlebell", "corde"], "€€"),
    ("Kit complet", "Ta vraie salle à la maison", "Tout le matériel, plus le banc et la récupération.", ["tapis", "elastiques", "halteres", "barre", "kettlebell", "corde", "rouleau", "banc"], "€€€"),
]


def kits_html():
    out = []
    for i, (name, when, what, ids, budget) in enumerate(KITS):
        items = "".join(f'<li><a href="{aff(p["query"])}" rel="sponsored nofollow noopener" target="_blank">{e(p["name"])}</a></li>'
                        for p in PRODUCTS if p["icon"] in ids)
        out.append(f"""<div class="kitcard{' best' if i == 1 else ''}">{'<span class="badge">Notre conseil</span>' if i == 1 else ''}
<span class="when">{e(when)}</span><h3>{e(name)}</h3><p>{e(what)}</p>
<ul>{items}</ul><span class="budget">{BUDGET[budget]}</span></div>""")
    return '<div class="kits">' + "".join(out) + "</div>"


HERO_ART = """<figure class="hero-art" style="margin:0">
<svg viewBox="0 0 440 300" role="img" aria-label="Un coin sport de 2 mètres sur 1 mètre avec un tapis, des haltères, des élastiques et un kettlebell">
<rect x="20" y="40" width="400" height="200" rx="18" fill="var(--blue-soft)"/>
<rect x="50" y="70" width="250" height="84" rx="10" fill="var(--blue)" opacity=".85"/>
<text x="175" y="118" text-anchor="middle" font-size="20" font-weight="800" fill="#fff" font-family="var(--display)">Ton tapis</text>
<g fill="none" stroke="var(--orange)" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">
<rect x="70" y="175" width="12" height="36" rx="3"/><line x1="82" y1="193" x2="122" y2="193" stroke-width="7"/><rect x="122" y="175" width="12" height="36" rx="3"/>
<path d="M176 182 C176 166 200 166 200 182"/><circle cx="188" cy="198" r="16"/>
<ellipse cx="250" cy="194" rx="22" ry="13"/><ellipse cx="268" cy="194" rx="22" ry="13"/>
</g>
<g fill="none" stroke="var(--ink)" stroke-width="3" stroke-linecap="round"><path d="M330 220 V60 H400 V220"/><line x1="320" y1="72" x2="410" y2="72" stroke-width="6"/></g>
<text x="365" y="250" text-anchor="middle" font-size="14" fill="var(--muted)" font-family="var(--body)">ta porte</text>
<text x="220" y="28" text-anchor="middle" font-size="18" font-weight="800" fill="var(--ink)" font-family="var(--display)">2 mètres</text>
<text x="220" y="285" text-anchor="middle" font-size="15" fill="var(--muted)" font-family="var(--body)">La place d'un tapis de couloir suffit.</text>
</svg>
<figcaption>Tout ton matériel tient ici. Et se range en 2 minutes.</figcaption>
</figure>"""


CALC = """<div class="calc">
<div class="presets" role="group" aria-label="Choisis ton espace">
<button class="preset" data-w="200" data-d="100" aria-pressed="true"><span class="ico" aria-hidden="true">🛏</span><span><b>Un coin de chambre</b><small>environ 2 m × 1 m</small></span></button>
<button class="preset" data-w="250" data-d="150" aria-pressed="false"><span class="ico" aria-hidden="true">🛋</span><span><b>Un bout de salon</b><small>environ 2,5 m × 1,5 m</small></span></button>
<button class="preset" data-w="300" data-d="100" aria-pressed="false"><span class="ico" aria-hidden="true">🚪</span><span><b>Un couloir</b><small>environ 3 m × 1 m</small></span></button>
<button class="preset" data-w="300" data-d="250" aria-pressed="false"><span class="ico" aria-hidden="true">🏠</span><span><b>Une petite pièce libre</b><small>environ 3 m × 2,5 m</small></span></button>
<details class="custom"><summary>Je préfère mesurer moi-même</summary>
<label for="w">Longueur libre <span class="val" id="wv"></span></label><input type="range" id="w" min="80" max="400" step="10" value="200">
<label for="d">Largeur libre <span class="val" id="dv"></span></label><input type="range" id="d" min="60" max="400" step="10" value="100">
</details>
</div>
<div class="result" aria-live="polite">
<div class="verdict" id="verdict"></div>
<svg id="room" viewBox="0 0 420 220" role="img" aria-label="Ton espace dessiné avec le matériel qui rentre"></svg>
<ul id="fits"></ul>
</div>
</div>
<script>
(() => {
  const items = [
    {id:"tapis", n:"Un tapis de sol", w:183, d:61, need:[190,70], q:"tapis de sol fitness épais"},
    {id:"elast", n:"Des élastiques", w:30, d:20, need:[150,80], q:"élastiques de résistance musculation lot"},
    {id:"halt", n:"Des haltères réglables", w:45, d:40, need:[180,90], q:"haltères réglables"},
    {id:"barre", n:"Une barre de traction (sur une porte)", w:0, d:0, need:[0,0], q:"barre de traction porte sans perçage"},
    {id:"kb", n:"Un kettlebell", w:22, d:22, need:[180,140], q:"kettlebell fonte"},
    {id:"corde", n:"Une corde à sauter", w:0, d:0, need:[200,120], q:"corde à sauter roulements"},
    {id:"banc", n:"Un banc pliable", w:125, d:50, need:[200,140], q:"banc de musculation pliable"}
  ];
  const TAG = "__TAG__";
  const $ = id => document.getElementById(id);
  const fits = (it, W, D) => { const [a,b] = it.need; return (W >= a && D >= b) || (D >= a && W >= b); };
  const m = v => (v / 100).toLocaleString("fr-FR") + " m";
  function render(W, D) {
    $("w").value = W; $("d").value = D; $("wv").textContent = m(W); $("dv").textContent = m(D);
    const ok = items.filter(it => fits(it, W, D));
    const msg = ok.length === items.length ? "Parfait : <span>tout le matériel rentre</span> !" :
                ok.length >= 4 ? `Bonne nouvelle : <span>${ok.length} équipements sur ${items.length}</span> rentrent chez toi.` :
                `C'est un peu juste, mais <span>${ok.length} équipements</span> rentrent déjà.`;
    $("verdict").innerHTML = msg;
    $("fits").innerHTML = items.map(it => fits(it, W, D)
      ? `<li><span class="yes" aria-hidden="true">✓</span><a href="https://www.amazon.fr/s?k=${encodeURIComponent(it.q)}&tag=${TAG}" rel="sponsored nofollow noopener" target="_blank">${it.n}</a></li>`
      : `<li class="no"><span aria-hidden="true">✕</span>${it.n} <small>(il faut un peu plus de place)</small></li>`).join("");
    const s = Math.min(380 / W, 170 / D), rw = W * s, rd = D * s, x0 = (420 - rw) / 2, y0 = 30;
    let svg = `<rect x="${x0}" y="${y0}" width="${rw}" height="${rd}" rx="10" fill="var(--blue-soft)" stroke="var(--blue)" stroke-width="2"/>`;
    svg += `<text x="210" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="var(--muted)" font-family="var(--body)">Ton espace : ${m(W)} × ${m(D)}</text>`;
    let cx = x0 + 10, cy = y0 + 10; const horiz = W >= D;
    if (ok.find(i => i.id === "tapis")) {
      const tw = (horiz ? 183 : 61) * s, td = (horiz ? 61 : 183) * s;
      svg += `<rect x="${cx}" y="${cy}" width="${tw}" height="${td}" rx="6" fill="var(--blue)" opacity=".85"/><text x="${cx + tw/2}" y="${cy + td/2 + 5}" text-anchor="middle" font-size="13" font-weight="800" fill="#fff" font-family="var(--body)">Tapis</text>`;
      if (horiz) cy += td + 10; else cx += tw + 10;
    }
    ok.filter(i => i.w && i.id !== "tapis").forEach(it => {
      const iw = it.w * s, id = it.d * s;
      if (horiz && cx + iw > x0 + rw) { cx = x0 + 10; cy += id + 10; }
      if (!horiz && cy + id > y0 + rd) { cy = y0 + 10; cx += iw + 10; }
      svg += `<rect x="${cx}" y="${cy}" width="${iw}" height="${id}" rx="5" fill="var(--orange)" opacity=".85"/>`;
      if (horiz) cx += iw + 10; else cy += id + 10;
    });
    $("room").innerHTML = svg;
  }
  document.querySelectorAll(".preset").forEach(b => b.addEventListener("click", () => {
    document.querySelectorAll(".preset").forEach(x => x.setAttribute("aria-pressed", x === b));
    render(+b.dataset.w, +b.dataset.d);
  }));
  ["w","d"].forEach(id => $(id).addEventListener("input", () => {
    document.querySelectorAll(".preset").forEach(x => x.setAttribute("aria-pressed", "false"));
    render(+$("w").value, +$("d").value);
  }));
  render(200, 100);
})();
</script>"""


HOME_FAQ = [
    ("Je n'ai jamais fait de sport. Je peux commencer à la maison ?", "Oui, c'est même l'endroit idéal pour débuter : pas de regard des autres, pas de trajet, et tu vas à ton rythme. Commence par 2 ou 3 séances courtes par semaine."),
    ("Combien ça coûte pour s'équiper ?", "Pour commencer, un tapis et un lot d'élastiques suffisent : c'est un petit budget. Les haltères réglables viennent ensuite, quand tu as pris l'habitude."),
    ("J'ai très peu de place, c'est possible ?", "Oui. Un espace de 2 mètres sur 1 mètre suffit, et tout le matériel du début se range sous un lit ou dans un tiroir."),
    ("Combien de temps par séance ?", "30 à 40 minutes suffisent, trois fois par semaine. Mieux vaut des séances courtes et régulières que longues et rares."),
]

def org_ld():
    return {"@context": "https://schema.org", "@type": "WebSite", "name": SITE["name"], "url": url(""),
            "description": SITE["description"], "inLanguage": "fr-FR"}


def build_index():
    cards = "".join(product_card(i + 1, p) for i, p in enumerate(PRODUCTS))
    guides = "".join(f'<a class="guide" href="{g["slug"]}.html"><span class="tag">{e(g["kicker"])}</span><h3>{e(g["title"])}</h3><p>{e(g["desc"])}</p></a>' for g in GUIDES)
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in HOME_FAQ)
    itemlist = {"@context": "https://schema.org", "@type": "ItemList", "name": "Le matériel pour s'entraîner chez soi",
                "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": p["name"]} for i, p in enumerate(PRODUCTS)]}
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage",
              "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in HOME_FAQ]}
    page = head(f"{SITE['name']} : faire du sport à la maison, même dans un petit espace",
                "Tu veux te mettre au sport à la maison ? Découvre ce qui tient chez toi, le matériel simple pour débuter et un programme facile à suivre.",
                "", [org_ld(), itemlist, faq_ld])
    page += header("index.html")
    page += f"""<main>
<div class="wrap hero">
<div>
<span class="pill">Fait pour les débutants</span>
<h1>Le sport à la maison, <span class="o">même dans 2&nbsp;m²</span>.</h1>
<p class="lead">Pas besoin d'une salle de sport ni d'une grande pièce. On t'aide à choisir le bon matériel pour commencer, sans te tromper.</p>
<div class="actions"><a class="btn" href="#commencer">Je commence ici</a><a class="btn ghost" href="#materiel">Voir le matériel</a></div>
<div class="reassure"><span>Sans abonnement</span><span>Petit budget</span><span>Tout se range</span></div>
</div>
{HERO_ART}
</div>

<section class="section alt" id="commencer"><div class="wrap">
<div class="section-head"><span class="step">Par où commencer ?</span><h2>3 étapes, c'est tout</h2><p>Pas de jargon. Suis les étapes dans l'ordre, et ton coin sport grandit avec toi.</p></div>
<div class="steps">
<a class="stepcard" href="#espace"><span class="n">1</span><h3>Regarde la place que tu as</h3><p>Choisis ta pièce : on te montre ce qui rentre chez toi.</p><span class="more">Voir ma place →</span></a>
<a class="stepcard" href="#materiel"><span class="n">2</span><h3>Commence avec les essentiels</h3><p>Un tapis, des élastiques, des haltères pour démarrer. Puis complète au fil de tes progrès.</p><span class="more">Voir le matériel →</span></a>
<a class="stepcard" href="programme-musculation-maison-debutant.html"><span class="n">3</span><h3>Suis un programme simple</h3><p>3 séances de 40 minutes par semaine, expliquées pas à pas.</p><span class="more">Voir le programme →</span></a>
</div>
</div></section>

<section class="section" id="espace"><div class="wrap">
<div class="section-head"><span class="step">Étape 1</span><h2>Qu'est-ce qui rentre chez toi ?</h2><p>Clique sur l'endroit où tu veux t'entraîner. On dessine ton espace avec le matériel qui rentre.</p></div>
{CALC.replace("__TAG__", SITE['amazon_tag'])}
</div></section>

<section class="section alt" id="materiel"><div class="wrap">
<div class="section-head"><span class="step">Étape 2</span><h2>Le matériel, expliqué simplement</h2><p>Commence par les essentiels. Ensuite, chaque nouvel objet débloque de nouveaux exercices et te fait progresser plus vite.</p></div>
{kits_html()}
<h3 class="subhead">Chaque objet en détail</h3>
<div class="kit">{cards}</div>
</div></section>

<section class="section" id="guides"><div class="wrap">
<div class="section-head"><span class="step">Pour aller plus loin</span><h2>Nos guides</h2><p>Pour bien choisir ton matériel et t'entraîner sans te blesser.</p></div>
<div class="guides">{guides}</div>
</div></section>

<section class="section alt" id="questions"><div class="wrap">
<div class="section-head"><span class="step">Tu te poses la question ?</span><h2>Les questions des débutants</h2></div>
<div class="faq" style="max-width:780px">{faq}</div>
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
    used = " ".join(g.get("links", {}).values())
    picks = [p for p in PRODUCTS if p["query"] not in used and p.get("guide") != g["slug"]][:3]
    upsell = "".join(f'<div class="buy"><div><strong>{e(p["name"])}</strong><span>{e(p["why"])}</span></div><a class="btn" href="{aff(p["query"])}" rel="sponsored nofollow noopener" target="_blank">Voir les prix</a></div>' for p in picks)
    page = head(g["title"], g["desc"], g["slug"] + ".html", [art_ld, faq_ld, crumb_ld], "article")
    page += header("")
    page += f"""<main class="wrap">
<div class="crumbs"><a href="index.html">Accueil</a> / {e(g['short'])}</div>
<header class="article-head">
<span class="tag">{e(g['kicker'])}</span>
<h1>{e(g['title'])}</h1>
<p class="lead">{e(g['desc'])}</p>
<p class="meta">Mis à jour le {datetime.date.today().strftime('%d/%m/%Y')} · {g['minutes']} min de lecture</p>
</header>
<div class="article-body">
<article class="prose">{body}
<h2>Complète ton coin sport</h2>
<p>Ces objets vont bien avec ce que tu viens de lire, et ajoutent de nouveaux exercices.</p>
{upsell}
<h2 id="faq">Questions fréquentes</h2><div class="faq">{faq}</div>
</article>
<aside class="aside">
<div class="box"><h3>Dans ce guide</h3><ol>{toc}</ol></div>
<div class="box"><h3>Tu débutes ?</h3><p style="margin:0 0 12px;font-size:16px;color:var(--muted)">Regarde ce qui rentre chez toi en un clic.</p><a class="btn" href="index.html#espace">Voir ma place</a></div>
<div class="box"><h3>Autres guides</h3><ul>{others}</ul></div>
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

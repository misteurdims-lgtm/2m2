#!/usr/bin/env python3
"""Générateur du site 2 m² : produit des pages HTML statiques optimisées pour le référencement.
Ajouter un guide = ajouter une entrée dans content.py (GUIDES), puis relancer : python3 build.py
"""
import html, json, os, shutil, datetime
from urllib.parse import quote_plus
from content import SITE, PRODUCTS, GUIDES
from iso import scene

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "docs")
SRC = os.path.join(os.path.dirname(__file__), "src")
TODAY = datetime.date.today().isoformat()
import hashlib
CSS_V = hashlib.md5(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "src", "style.css"), "rb").read()).hexdigest()[:8]
e = html.escape


def aff(query):
    return f"https://www.amazon.fr/s?k={quote_plus(query)}&tag={SITE['amazon_tag']}"


def link(p):
    """Lien vers le modèle choisi (fiche produit Amazon), sinon vers une recherche."""
    if p.get("asin"):
        return f"https://www.amazon.fr/dp/{p['asin']}?tag={SITE['amazon_tag']}"
    return aff(p["query"])


def url(path):
    return SITE["base_url"].rstrip("/") + "/" + path.lstrip("/")


def _analytics():
    code = SITE.get("goatcounter")
    if not code:
        return ""
    return (f'<script data-goatcounter="https://{code}.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>'
            '<script>document.addEventListener("click", e => { const a = e.target.closest("a[rel~=sponsored]"); '
            'if (a && window.goatcounter && goatcounter.count) goatcounter.count({path: "clic-" + (a.textContent || "").trim().slice(0, 40), title: location.pathname, event: true}); });</script>')


ANALYTICS = _analytics()


FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Anton&family=Instrument+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">')


GV = (f'<meta name="google-site-verification" content="{SITE["google_verif"]}">' if SITE.get("google_verif") else "") + (f'<meta name="msvalidate.01" content="{SITE["bing_verif"]}">' if SITE.get("bing_verif") else "")


def head(title, desc, path, jsonld, og_type="website", seo_title=None):
    title_tag = seo_title or title
    full_title = title_tag if title_tag.startswith(SITE["name"]) else f"{title_tag} | {SITE['name']}"
    ld = "".join(f'<script type="application/ld+json">{json.dumps(j, ensure_ascii=False)}</script>' for j in jsonld)
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(full_title)}</title>
<meta name="description" content="{e(desc)}">{GV}
<link rel="canonical" href="{url(path)}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{e(SITE['name'])}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url(path)}">
<meta property="og:image" content="{url('og.png')}">
<meta property="og:locale" content="fr_FR">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0c0d10">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
{FONTS}
<link rel="stylesheet" href="style.css?v={CSS_V}">
{ANALYTICS}
{ld}
</head>
<body>
<a class="skip" href="#contenu">Aller au contenu</a>"""


SEASON = r"""<div class="season" id="season" hidden></div>
<script>
(() => {
  const d = new Date(), m = d.getMonth() + 1, day = d.getDate(), el = document.getElementById("season");
  let msg = "";
  if (m === 11 && day <= 30) msg = "Black Friday le 27 novembre : c'est souvent le meilleur moment de l'année pour s'équiper. <a href='index.html#quiz'>Trouve ton kit avant →</a>";
  else if (m === 12 && day <= 24) msg = "Une idée cadeau qui sert vraiment : un kit pour faire du sport à la maison. <a href='index.html#materiel'>Voir les kits →</a>";
  else if ((m === 12 && day >= 26) || m === 1) msg = "Nouvelle année, bonne résolution : commence le sport chez toi, sans abonnement. <a href='index.html#quiz'>Trouve ton kit →</a>";
  else if (m === 9) msg = "C'est la rentrée : le bon moment pour (re)prendre le sport à la maison. <a href='index.html#quiz'>Trouve ton kit →</a>";
  if (msg) { el.innerHTML = msg; el.hidden = false; }
})();
</script>"""


NAV = [("index.html", "Accueil"), ("index.html#quiz", "Mon kit"), ("index.html#materiel", "Matériel"), ("index.html#guides", "Guides")]


DISCLOSE = '<p class="disclose">Liens affiliés : si tu achètes via nos liens, on touche une petite commission, sans surcoût pour toi. <a href="mentions-legales.html#affiliation">En savoir plus</a></p>'


def header(current):
    links = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h == current else ""}>{t}</a>' for h, t in NAV)
    return f"""<header class="top"><div class="wrap">
<a class="brand" href="index.html"><span class="brand-mark">2M<span class="sq">²</span></span><strong>{e(SITE['tagline'])}</strong></a>
<nav aria-label="Navigation principale">{links}</nav>
</div></header>
{SEASON}
<a class="sticky-cta" id="sticky" href="index.html#quiz">Trouver mon kit en 30 secondes</a>
<script>(() => {{ const s = document.getElementById("sticky"); const f = () => s.classList.toggle("show", scrollY > 700); addEventListener("scroll", f, {{passive: true}}); f(); }})();</script>
"""


def footer():
    guides = "".join(f'<li><a href="{g["slug"]}.html">{e(g["short"])}</a></li>' for g in GUIDES)
    return f"""<footer><div class="wrap">
<div><span class="brand-mark">2M<span class="sq">²</span></span><p>{e(SITE['description'])}</p>
<p>En tant que Partenaire Amazon, nous réalisons un bénéfice sur les achats remplissant les conditions requises.</p></div>
<div><h3>Guides</h3><ul>{guides}</ul></div>
<div><h3>Le site</h3><ul><li><a href="a-propos.html">Qui sommes-nous ?</a></li><li><a href="mentions-legales.html">Mentions légales</a></li><li><a href="mentions-legales.html#affiliation">Liens affiliés</a></li></ul>
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
    "pot": '<rect x="28" y="24" width="44" height="50" rx="8"/><rect x="32" y="12" width="36" height="12" rx="3"/><line x1="36" y1="44" x2="64" y2="44"/><line x1="36" y1="54" x2="56" y2="54"/>',
    "shaker": '<path d="M32 26 L36 78 H64 L68 26 Z"/><rect x="30" y="16" width="40" height="10" rx="3"/><line x1="46" y1="8" x2="54" y2="8"/><line x1="50" y1="8" x2="50" y2="16"/>',
    "banc": '<rect x="12" y="34" width="76" height="12" rx="4"/><line x1="24" y1="46" x2="24" y2="72"/><line x1="76" y1="46" x2="76" y2="72"/><line x1="16" y1="72" x2="32" y2="72"/><line x1="68" y1="72" x2="84" y2="72"/>',
}


def icon(name, size=88):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 100 86" fill="none" stroke="currentColor" stroke-width="4" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')


GICON = {"salle-de-sport-petit-appartement": "tapis", "halteres-reglables": "halteres", "barre-traction-sans-percer": "barre",
         "elastiques-musculation": "elastiques", "programme-musculation-maison-debutant": "kettlebell", "creatine-proteines-complements": "pot"}


BUDGET = {"€": "Petit budget", "€€": "Budget moyen", "€€€": "Gros budget"}


def product_card(i, p):
    tier = p["tier"]
    kind = "start" if tier == "Essentiel" else "nut" if tier.startswith("Nutrition") else ""
    badge = f'<span class="badge{" nut" if kind == "nut" else " alt" if not kind else ""}">{e(tier)}</span>'
    guide = f'<a class="guide-link" href="{p["guide"]}.html">Comment bien le choisir</a>' if p.get("guide") else ""
    mate = next(x for x in PRODUCTS if x["icon"] == p["pair"])
    return f"""<article class="card {kind}" id="p-{p['icon']}">{badge}
<div class="art">{icon(p['icon'])}</div>
<h3>{e(p['name'])}</h3>
<p>{e(p['why'])}</p>
<div class="facts"><span><b>Place :</b> {e(p['compare'])}</span><span><b>Rangement :</b> {e(p['storage'].lower())}</span><span><b>Prix :</b> {BUDGET[p['budget']].lower()}</span>{f'<span class="pick"><b>Notre choix :</b> {e(p["pick"])} · <a href="{aff(p["query"])}" rel="sponsored nofollow noopener" target="_blank">autres modèles</a></span>' if p.get("pick") else ""}</div>
<a class="btn go" href="{link(p)}" rel="sponsored nofollow noopener" target="_blank">Voir le prix du jour</a>
<p class="pair">Va bien avec : <a href="{link(mate)}" rel="sponsored nofollow noopener" target="_blank">{e(mate['name'].lower())}</a></p>
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
        items = "".join(f'<li><a href="{link(p)}" rel="sponsored nofollow noopener" target="_blank">{e(p["name"])}</a></li>'
                        for p in PRODUCTS if p["icon"] in ids)
        out.append(f"""<div class="kitcard{' best' if i == 1 else ''}">{'<span class="badge">Notre conseil</span>' if i == 1 else ''}
<span class="when">{e(when)}</span><h3>{e(name)}</h3><p>{e(what)}</p>
<ul>{items}</ul><span class="budget">{BUDGET[budget]}</span></div>""")
    return '<div class="kits">' + "".join(out) + "</div>"


TICK = "".join(f"<span>{w}</span><em>✦</em>" for w in ["Sans abonnement", "Dès un petit budget", "Tout se range", "Pour débutants", "À ton rythme", "Sans trajet"])


def hero_art():
    return f"""<div class="stage">{scene()}
<div class="chip c1"><b>2&nbsp;m²</b>suffisent</div>
<div class="chip c2">✓ Tout se range en 2 min</div>
</div>"""


CALC = """<div class="calc">
<div class="presets" role="group" aria-label="Choisis ton espace">
<button type="button" class="preset" data-w="200" data-d="100" aria-pressed="true"><span class="ico" aria-hidden="true">🛏</span><span><b>Un coin de chambre</b><small>environ 2 m × 1 m</small></span></button>
<button type="button" class="preset" data-w="250" data-d="150" aria-pressed="false"><span class="ico" aria-hidden="true">🛋</span><span><b>Un bout de salon</b><small>environ 2,5 m × 1,5 m</small></span></button>
<button type="button" class="preset" data-w="300" data-d="100" aria-pressed="false"><span class="ico" aria-hidden="true">🚪</span><span><b>Un couloir</b><small>environ 3 m × 1 m</small></span></button>
<button type="button" class="preset" data-w="300" data-d="250" aria-pressed="false"><span class="ico" aria-hidden="true">🏠</span><span><b>Une petite pièce libre</b><small>environ 3 m × 2,5 m</small></span></button>
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
  const TAG = "__TAG__", URLS = __URLS__;
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
      ? `<li><span class="yes" aria-hidden="true">✓</span><a href="${URLS[it.id]}" rel="sponsored nofollow noopener" target="_blank">${it.n}</a></li>`
      : `<li class="no"><span aria-hidden="true">✕</span>${it.n} <small>(il faut un peu plus de place)</small></li>`).join("");
    const s = Math.min(380 / W, 170 / D), rw = W * s, rd = D * s, x0 = (420 - rw) / 2, y0 = 30;
    let svg = `<defs><clipPath id="roomclip"><rect x="${x0}" y="${y0}" width="${rw}" height="${rd}" rx="10"/></clipPath></defs><rect x="${x0}" y="${y0}" width="${rw}" height="${rd}" rx="10" fill="var(--blue-soft)" stroke="var(--blue)" stroke-width="2"/><g clip-path="url(#roomclip)">`;
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
    $("room").innerHTML = svg + "</g>";
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


QUIZ = """<div class="quiz" id="quizbox">
<div class="questions"><p class="qprog" id="qprog">0 / 3 réponses</p>
<div class="q" data-q="goal"><h3><span>1.</span>Ton objectif ?</h3><div class="opts">
<button type="button" aria-pressed="false" data-v="forme">Me remettre en forme</button><button type="button" aria-pressed="false" data-v="muscle">Me muscler</button><button type="button" aria-pressed="false" data-v="poids">Perdre du poids</button></div></div>
<div class="q" data-q="space"><h3><span>2.</span>Ta place ?</h3><div class="opts">
<button type="button" aria-pressed="false" data-v="petit">Un petit coin</button><button type="button" aria-pressed="false" data-v="moyen">Un bout de pièce</button><button type="button" aria-pressed="false" data-v="grand">Une pièce libre</button></div></div>
<div class="q" data-q="budget"><h3><span>3.</span>Ton budget pour démarrer ?</h3><div class="opts">
<button type="button" aria-pressed="false" data-v="1">Le plus petit possible</button><button type="button" aria-pressed="false" data-v="2">Raisonnable</button><button type="button" aria-pressed="false" data-v="3">Je veux bien m'équiper</button></div></div>
</div>
<div class="answer-slot"><div class="placeholder" id="ph"><b>Ton kit<br>apparaît ici.</b>Réponds aux 3 questions. Ça prend 30 secondes.</div><div class="answer" id="answer" hidden></div></div>
</div>
<script>
(() => {
  const P = __PRODUCTS__, TAG = "__TAG__", pick = {};
  const box = document.getElementById("quizbox"), out = document.getElementById("answer");
  box.querySelectorAll(".q").forEach(q => q.querySelectorAll("button").forEach(b => b.addEventListener("click", () => {
    q.querySelectorAll("button").forEach(x => x.setAttribute("aria-pressed", x === b));
    pick[q.dataset.q] = b.dataset.v; document.getElementById("qprog").textContent = Object.keys(pick).length + " / 3 réponses"; show();
  })));
  function show() {
    if (!(pick.goal && pick.space && pick.budget)) return;
    let ids = ["tapis", "elastiques"];
    if (+pick.budget >= 2 || pick.goal === "muscle") ids.push("halteres");
    if (pick.goal === "poids") ids.push("corde", "kettlebell");
    if (pick.goal === "muscle") ids.push("barre");
    if (pick.goal === "forme") ids.push("rouleau");
    if (+pick.budget === 3) ids.push("barre", "kettlebell", "rouleau");
    if (+pick.budget === 3 && pick.space === "grand") ids.push("banc");
    if (pick.space === "petit") ids = ids.filter(i => i !== "banc");
    if (pick.goal === "muscle") ids.push("pot", "shaker");
    ids = [...new Set(ids)];
    const names = {forme: "te remettre en forme", muscle: "te muscler", poids: "perdre du poids"};
    out.innerHTML = `<h3>Ton kit pour ${names[pick.goal]} : ${ids.length} objets</h3>
      <p>Dans l'ordre où les acheter. Les prix changent souvent : compare-les sur la page du vendeur.</p>
      <ol>${ids.map(id => { const p = P.find(x => x.icon === id); return `<li><span><b>${p.name}</b><small>${p.why}</small></span><a class="btn" href="${p.url}" rel="sponsored nofollow noopener" target="_blank">Voir le prix</a></li>`; }).join("")}</ol>
      <p class="next"><button type="button" class="reset" id="reset">Recommencer</button> Ensuite : <a href="programme-musculation-maison-debutant.html">ton programme de 3 séances par semaine →</a></p>${pick.goal === "muscle" ? '<p class="small">Compléments : réservés aux adultes en bonne santé. <a href="creatine-proteines-complements.html">Ce qu&apos;en disent les experts →</a></p>' : ""}`;
    out.hidden = false; document.getElementById("ph").hidden = true;
    document.getElementById("reset").addEventListener("click", () => { for (const k in pick) delete pick[k]; box.querySelectorAll(".opts button").forEach(x => x.setAttribute("aria-pressed", "false")); out.hidden = true; document.getElementById("ph").hidden = false; document.getElementById("qprog").textContent = "0 / 3 réponses"; }); out.scrollIntoView({behavior: matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth", block: "nearest"});
  }
})();
</script>"""


OBJECTIONS = [
    ("« Je n'ai pas la place »", "Un coin de 2 m sur 1 m suffit, et tout se range sous un lit ou dans un tiroir. Le calculateur plus bas te le montre en un clic."),
    ("« Je n'ai pas le temps »", "Pas de trajet, pas de vestiaire : 30 à 40 minutes chez toi, quand tu veux, même tard le soir ou pendant la sieste des enfants."),
    ("« Je vais abandonner »", "Le matériel à la vue de tous est un rappel quotidien. Et un programme simple, déjà prêt, évite de se demander quoi faire."),
]


HOME_FAQ = [
    ("Je n'ai jamais fait de sport. Je peux commencer à la maison ?", "Oui, c'est même l'endroit idéal pour débuter : pas de regard des autres, pas de trajet, et tu vas à ton rythme. Commence par 2 ou 3 séances courtes par semaine."),
    ("Combien ça coûte pour s'équiper ?", "Pour commencer, un tapis et un lot d'élastiques suffisent : c'est un petit budget. Les haltères réglables viennent ensuite, quand tu as pris l'habitude."),
    ("J'ai très peu de place, c'est possible ?", "Oui. Un espace de 2 mètres sur 1 mètre suffit, et tout le matériel du début se range sous un lit ou dans un tiroir."),
    ("Combien de temps par séance ?", "30 à 40 minutes suffisent, trois fois par semaine. Mieux vaut des séances courtes et régulières que longues et rares."),
]

def org_ld():
    return {"@context": "https://schema.org", "@graph": [
        {"@type": "WebSite", "@id": url("#site"), "name": SITE["name"], "url": url(""), "description": SITE["description"], "inLanguage": "fr-FR",
         "publisher": {"@id": url("#org")}},
        {"@type": "Organization", "@id": url("#org"), "name": SITE["name"], "url": url(""), "logo": url("favicon.svg"), "sameAs": ["https://www.pinterest.com/sport2m2/"]}]}


def build_index():
    cards = "".join(product_card(i + 1, p) for i, p in enumerate(PRODUCTS))
    guides = "".join(f'<a class="guide" href="{g["slug"]}.html"><span class="gi">{icon(GICON.get(g["slug"], "tapis"), 44)}</span><span class="tag">{e(g["kicker"])}</span><h3>{e(g["title"])}</h3><p>{e(g["desc"])}</p></a>' for g in GUIDES)
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in HOME_FAQ)
    itemlist = {"@context": "https://schema.org", "@type": "ItemList", "name": "Le matériel pour s'entraîner chez soi",
                "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": p["name"]} for i, p in enumerate(PRODUCTS)]}
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage",
              "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in HOME_FAQ]}
    page = head(f"{SITE['name']} : faire du sport à la maison, même dans un petit espace",
                "Tu veux te mettre au sport à la maison ? Découvre ce qui tient chez toi, le matériel simple pour débuter et un programme facile à suivre.",
                "", [org_ld(), itemlist, faq_ld])
    page += header("index.html")
    page += f"""<main id="contenu">
<div class="hero-band">
<div class="wrap hero">
<div>
<span class="pill"><i>—</i>Le sport à la maison, pour débutants</span>
<h1>Ta salle de sport à la maison. <span class="o">Dans 2&nbsp;m².</span></h1>
<p class="lead">Pas d'abonnement à payer chaque mois, pas de trajet, pas de regard des autres. Tu t'équipes une fois, et tu t'entraînes quand tu veux, pendant des années.</p>
<div class="actions"><a class="btn" href="#quiz">Trouver mon kit en 30 secondes</a><a class="btn ghost" href="#materiel">Voir le matériel</a></div>
{DISCLOSE}
</div>
{hero_art()}
</div>
<div class="ticker" aria-hidden="true"><div>{TICK}{TICK}</div></div>
</div>

<section class="section dark" id="quiz"><div class="wrap">
<div class="section-head"><span class="eyebrow">30 secondes, 3 questions</span><h2>Trouve ton kit idéal</h2><p>Réponds à 3 questions : on te dit exactement quoi acheter, et dans quel ordre.</p></div>
{QUIZ.replace("__TAG__", SITE['amazon_tag']).replace("__PRODUCTS__", json.dumps([{**{k: p[k] for k in ("icon", "name", "why")}, "url": link(p)} for p in PRODUCTS], ensure_ascii=False))}
</div></section>

<section class="section" id="excuses"><div class="wrap">
<div class="section-head center"><span class="eyebrow">On se connaît</span><h2>Les 3 excuses qu'on se donne</h2><p>Et pourquoi, à la maison, elles ne tiennent plus.</p></div>
<div class="steps">{"".join(f'<div class="stepcard excuse"><span class="q">?</span><h3>{e(t)}</h3><p>{e(a)}</p></div>' for t, a in OBJECTIONS)}</div>
<p class="oms"><span>L'OMS recommande aux adultes au moins <b>deux séances de renforcement musculaire par semaine</b>, en plus de 150 à 300 minutes d'activité modérée. <a href="https://www.who.int/europe/fr/publications/i/item/9789240014886" rel="noopener" target="_blank">Source : OMS</a></span></p>
</div></section>

<section class="section alt" id="commencer"><div class="wrap">
<div class="section-head"><span class="eyebrow">Par où commencer ?</span><h2>3 étapes, c'est tout</h2><p>Pas de jargon. Suis les étapes dans l'ordre, et ton coin sport grandit avec toi.</p></div>
<div class="steps">
<a class="stepcard" href="#espace"><span class="n">1</span><h3>Regarde la place que tu as</h3><p>Choisis ta pièce : on te montre ce qui rentre chez toi.</p><span class="more">Voir ma place →</span></a>
<a class="stepcard" href="#materiel"><span class="n">2</span><h3>Commence avec les essentiels</h3><p>Un tapis, des élastiques, des haltères pour démarrer. Puis complète au fil de tes progrès.</p><span class="more">Voir le matériel →</span></a>
<a class="stepcard" href="programme-musculation-maison-debutant.html"><span class="n">3</span><h3>Suis un programme simple</h3><p>3 séances de 40 minutes par semaine, expliquées pas à pas.</p><span class="more">Voir le programme →</span></a>
</div>
</div></section>

<section class="section" id="espace"><div class="wrap">
<div class="section-head"><span class="eyebrow">Étape 1</span><h2>Qu'est-ce qui rentre chez toi ?</h2><p>Clique sur l'endroit où tu veux t'entraîner. On dessine ton espace avec le matériel qui rentre.</p></div>
{CALC.replace("__TAG__", SITE['amazon_tag']).replace("__URLS__", json.dumps({k: link(next(p for p in PRODUCTS if p["icon"] == v)) for k, v in {"tapis": "tapis", "elast": "elastiques", "halt": "halteres", "barre": "barre", "kb": "kettlebell", "corde": "corde", "banc": "banc"}.items()}))}
</div></section>

<section class="section alt" id="materiel"><div class="wrap">
<div class="section-head"><span class="eyebrow">Étape 2</span><h2>Le matériel, expliqué simplement</h2><p>Commence par les essentiels. Ensuite, chaque nouvel objet débloque de nouveaux exercices et te fait progresser plus vite.</p></div>
{kits_html()}
<h3 class="subhead">Chaque objet en détail</h3>
<div class="kit">{cards}</div>
</div></section>

<section class="section" id="guides"><div class="wrap">
<div class="section-head"><span class="eyebrow">Pour aller plus loin</span><h2>Nos guides</h2><p>Pour bien choisir ton matériel et t'entraîner sans te blesser.</p></div>
<div class="guides">{guides}</div>
</div></section>

<section class="section alt" id="questions"><div class="wrap">
<div class="section-head center"><span class="eyebrow">Tu te poses la question ?</span><h2>Les questions des débutants</h2></div>
<div class="faq">{faq}</div>
</div></section>
</main>"""
    page += footer()
    return page


def build_guide(g):
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage",
              "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in g["faq"]]}
    art_ld = {"@context": "https://schema.org", "@type": "Article", "headline": g["title"], "description": g["desc"],
              "datePublished": g["date"], "dateModified": TODAY, "inLanguage": "fr-FR",
              "author": {"@type": "Organization", "name": SITE["name"], "url": url("a-propos.html")}, "publisher": {"@type": "Organization", "name": SITE["name"]},
              "image": url("og.png"), "mainEntityOfPage": url(g["slug"] + ".html")}
    crumb_ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Accueil", "item": url("")},
        {"@type": "ListItem", "position": 2, "name": g["short"], "item": url(g["slug"] + ".html")}]}
    body = g["body"].replace("{{TAG}}", SITE["amazon_tag"])
    for key, q in g.get("links", {}).items():
        prod = next((p for p in PRODUCTS if p["query"] == q), None)
        if q.startswith("dp:"):   # modèle précis choisi pour ce guide
            href = f"https://www.amazon.fr/dp/{q[3:]}?tag={SITE['amazon_tag']}"
        else:
            href = link(prod) if prod else aff(q)
        body = body.replace("{{" + key + "}}", href)
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in g["faq"])
    others = "".join(f'<li><a href="{o["slug"]}.html">{e(o["short"])}</a></li>' for o in GUIDES if o["slug"] != g["slug"])
    toc = "".join(f"<li>{e(t)}</li>" for t in g["toc"])
    used = " ".join(g.get("links", {}).values())
    picks = [p for p in PRODUCTS if p["query"] not in used and p.get("guide") != g["slug"]][:3]
    upsell = "".join(f'<div class="buy"><div><strong>{e(p["name"])}</strong><span>{e(p["why"])}</span></div><a class="btn" href="{link(p)}" rel="sponsored nofollow noopener" target="_blank">Voir le prix</a></div>' for p in picks)
    page = head(g["title"], g["desc"], g["slug"] + ".html", [art_ld, faq_ld, crumb_ld], "article", g.get("seo_title"))
    page += header("")
    page += f"""<div class="progress" id="progress"></div>
<main id="contenu">
<div class="article-band"><div class="wrap">
<div class="crumbs"><a href="index.html">Accueil</a> / {e(g['short'])}</div>
<header class="article-head">
<div><span class="tag">{e(g['kicker'])}</span>
<h1>{e(g['title'])}</h1>
<p class="lead">{e(g['desc'])}</p>
<p class="meta">Par <a href="a-propos.html#qui">l'équipe 2 m²</a> · Mis à jour le {datetime.date.today().strftime('%d/%m/%Y')} · {g['minutes']} min de lecture</p>{DISCLOSE}</div>
<div class="big-ico">{icon(GICON.get(g['slug'], 'tapis'), 120)}</div>
</header>
</div></div>
<div class="wrap article-body">
<article class="prose">{body}
{share(g)}
<h2>Complète ton coin sport</h2>
<p>Ces objets vont bien avec ce que tu viens de lire, et ajoutent de nouveaux exercices.</p>
{upsell}
<h2 id="faq">Questions fréquentes</h2><div class="faq">{faq}</div>
</article>
<aside class="aside">
<div class="box"><h3>Dans ce guide</h3><ol>{toc}</ol></div>
<div class="box cta"><h3>Tu débutes ?</h3><p style="margin:0 0 12px;font-size:16px;color:var(--muted)">Regarde ce qui rentre chez toi en un clic.</p><a class="btn" href="index.html#espace">Voir ma place</a></div>
<div class="box"><h3>Autres guides</h3><ul>{others}</ul></div>
</aside>
</div>
</main>
<script>(() => {{ const bar = document.getElementById("progress"); const f = () => {{ const h = document.documentElement; bar.style.width = (h.scrollTop / Math.max(1, h.scrollHeight - h.clientHeight) * 100) + "%"; }}; addEventListener("scroll", f, {{passive: true}}); f(); }})();</script>"""
    page += footer()
    return page


PIN_OF = {"salle-de-sport-petit-appartement": "petit-appartement", "halteres-reglables": "halteres",
          "barre-traction-sans-percer": "traction", "elastiques-musculation": "elastiques",
          "programme-musculation-maison-debutant": "programme", "creatine-proteines-complements": "creatine"}


def share(g):
    from urllib.parse import quote
    u, t = quote(url(g["slug"] + ".html"), safe=""), quote(g["title"], safe="")
    pin = PIN_OF.get(g["slug"])
    img = quote(url(f"pins/{pin}-a.jpg") if pin else url("og.png"), safe="")
    pinblock = (f"""<figure class="pinit"><img src="pins/{pin}-a.jpg" width="1000" height="1500" loading="lazy" alt="{e(g['title'])} : visuel à épingler"
 data-pin-description="{e(g['title'])} : {e(g['desc'])}"><figcaption>Garde ce guide pour plus tard : <a href="https://www.pinterest.com/pin/create/button/?url={u}&media={img}&description={t}" rel="noopener" target="_blank">l'épingler sur Pinterest</a></figcaption></figure>""" if pin else "")
    return pinblock + f"""<div class="share"><span>Partager ce guide</span>
<a href="https://www.pinterest.com/pin/create/button/?url={u}&media={img}&description={t}" rel="noopener" target="_blank">Pinterest</a>
<a href="https://www.facebook.com/sharer/sharer.php?u={u}" rel="noopener" target="_blank">Facebook</a>
<a href="https://wa.me/?text={t}%20{u}" rel="noopener" target="_blank">WhatsApp</a>
<button type="button" class="copy" data-url="{url(g['slug'] + '.html')}">Copier le lien</button></div>
<script>document.querySelectorAll(".copy").forEach(b => b.addEventListener("click", async () => {{ try {{ await navigator.clipboard.writeText(b.dataset.url); b.textContent = "Lien copié"; }} catch (e) {{ b.textContent = b.dataset.url; }} }}));</script>"""


def build_simple(slug, title, desc, inner):
    page = head(title, desc, slug + ".html", [org_ld()])
    page += header(slug + ".html")
    page += f'<main id="contenu"><div class="article-band"><div class="wrap"><header class="article-head"><div><h1>{e(title)}</h1></div></header></div></div><div class="wrap"><div class="prose" style="padding:40px 0 80px;max-width:68ch">{inner}</div></div></main>'
    page += footer()
    return page


ABOUT = """<h2 id="qui">Qui sommes-nous ?</h2>
<p><strong>2 m²</strong> est un site indépendant consacré au sport à la maison quand on a peu de place. On s'entraîne nous-mêmes, en musculation comme en course à pied, et on a créé ce site pour une raison simple : quand on débute, on se retrouve noyé sous les fiches produits, les avis douteux et les programmes trop compliqués.</p>
<p>Notre but : te dire quoi acheter en premier, combien de place ça prend, et quoi faire avec.</p>
<p>Nous ne sommes ni coachs diplômés ni médecins. Ce que tu lis ici, ce sont des critères de choix concrets, des programmes simples pour débuter, et, pour la nutrition, uniquement ce qui est confirmé par des sources officielles (autorités de santé, études reconnues), avec les liens pour vérifier.</p>
<h2>Notre méthode</h2>
<p>La plupart des gens n'ont ni la place ni le budget pour une vraie salle de sport. Ils ont un bout de salon, de chambre ou de couloir. C'est suffisant, à condition de bien choisir. Pour chaque équipement, on regarde trois choses : l'utilité (combien d'exercices il permet), l'emprise au sol (la place réellement occupée) et le rangement (où il va quand on ne s'en sert pas).</p>
<p>On explique les critères pour que tu puisses comparer toi-même. On n'invente ni tests, ni avis, ni notes. Quand on donne des mesures, ce sont des moyennes à vérifier sur la fiche du produit.</p>
<h2>Comment le site est financé</h2>
<p>Certains liens sont des liens affiliés, notamment vers Amazon. Si tu achètes après avoir cliqué, on touche une petite commission. Le prix reste le même pour toi. Ça ne change pas nos conseils : on recommande aussi du matériel qui ne coûte presque rien, comme les élastiques.</p>
<h2>Nous suivre</h2>
<p>Retrouve les guides en images sur <a href="https://www.pinterest.com/sport2m2/" rel="noopener" target="_blank">Pinterest</a>.</p>"""


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
    pages["a-propos.html"] = build_simple("a-propos", "À propos de 2 m²", "Qui est derrière 2 m², comment le matériel est choisi et comment le site est financé.", ABOUT)
    pages["404.html"] = build_simple("404", "Page introuvable", "Cette page n'existe pas ou a été déplacée.",
        '<p>Cette page n\'existe pas ou a été déplacée.</p><p><a class="btn" href="index.html">Retour à l\'accueil</a></p>')
    pages["mentions-legales.html"] = build_simple("mentions-legales", "Mentions légales", "Mentions légales, liens affiliés et données personnelles du site 2 m².", LEGAL)
    import re as _re
    fix = lambda m: 'href="' + _re.sub(r"&(?!amp;|#\d+;|[a-zA-Z]+;)", "&amp;", m.group(1)) + '"'
    for name, content in pages.items():
        content = _re.sub(r'href="([^"]*)"', fix, content)
        with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
            f.write(content)
    for name in ("style.css", "favicon.svg", "og.png"):
        if os.path.exists(os.path.join(SRC, name)):
            shutil.copy(os.path.join(SRC, name), OUT)
    sitemap = "".join(f"<url><loc>{url('' if n == 'index.html' else n)}</loc><lastmod>{TODAY}</lastmod></url>"
                      for n in pages if n not in ("mentions-legales.html", "404.html"))
    with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{sitemap}</urlset>')
    open(os.path.join(OUT, ".nojekyll"), "w").close()
    shutil.copytree(os.path.join(SRC, "pins"), os.path.join(OUT, "pins"))
    # page technique listant les épingles (source pour Pinterest, non indexée)
    import pins as P
    imgs = "".join(f'<figure><img src="pins/{p["f"]}.jpg" width="500" height="750" alt="{e(" ".join(p["title"]) + " " + p["hi"])}"><figcaption>{p["f"]}</figcaption></figure>' for p in P.PINS)
    open(os.path.join(OUT, "epingles.html"), "w").write(f'<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><meta name="robots" content="noindex"><title>Épingles 2 m²</title><style>body{{margin:0;padding:20px;background:#0c0d10;color:#eee;font-family:sans-serif;display:flex;flex-wrap:wrap;gap:20px}}img{{width:250px;height:auto;display:block}}</style></head><body>{imgs}</body></html>')
    # fichier de vérification Google Search Console (ne pas supprimer)
    gsc = "google4ff7b37beb931c1d.html"
    open(os.path.join(OUT, gsc), "w").write(f"google-site-verification: {gsc}")
    with open(os.path.join(OUT, "robots.txt"), "w") as f:
        f.write(f"User-agent: *\nAllow: /\nSitemap: {url('sitemap.xml')}\n")
    print("OK :", ", ".join(sorted(os.listdir(OUT))))


if __name__ == "__main__":
    build()

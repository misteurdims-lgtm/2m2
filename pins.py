"""Génère les visuels d'épingles Pinterest (1000x1500) dans docs/pins/."""
import os
from playwright.sync_api import sync_playwright
import iso

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "src", "pins")
ANTON = os.path.join(HERE, "src", "fonts", "anton-400.woff2")
SANS = os.path.join(HERE, "src", "fonts", "instrument-sans-400.woff2")
SANS_B = os.path.join(HERE, "src", "fonts", "instrument-sans-700.woff2")

# Chaque épingle : fichier, page cible, style, titre (lignes), mot mis en avant, sous-titre, points
PINS = [
    dict(f="accueil-a", page="", style="hero", kicker="Sport à la maison",
         title=["Ta salle de sport", "à la maison."], hi="Dans 2 m².",
         sub="Le matériel compact qui tient dans un petit appart. Trouve ton kit en 30 secondes."),
    dict(f="accueil-b", page="", style="list", kicker="Débutant ? Commence ici",
         title=["Le kit de départ", "pour t'entraîner"], hi="chez toi",
         points=["Un tapis", "Des élastiques", "Des haltères réglables", "Une barre de traction (sans percer)"]),
    dict(f="petit-appartement-a", page="salle-de-sport-petit-appartement.html", style="hero", kicker="Petit appartement",
         title=["Une salle de sport", "dans ton salon"], hi="en 2 m²",
         sub="Le bon matériel, les voisins, le rangement en 2 minutes : tout est dans le guide."),
    dict(f="petit-appartement-b", page="salle-de-sport-petit-appartement.html", style="list", kicker="Petit espace, gros résultats",
         title=["Aménager ta salle", "de sport en"], hi="4 étapes",
         points=["Trouver tes 2 m²", "Acheter dans le bon ordre", "Zéro bruit pour les voisins", "Tout ranger en 2 minutes"]),
    dict(f="halteres-a", page="halteres-reglables.html", style="hero", kicker="Guide d'achat",
         title=["Haltères réglables :", "comment"], hi="bien choisir",
         sub="Une paire qui remplace un rack entier. Les critères qui comptent vraiment."),
    dict(f="halteres-b", page="halteres-reglables.html", style="list", kicker="Avant d'acheter",
         title=["Haltères réglables :", "les"], hi="4 vérifs",
         points=["Le type de réglage", "La bonne plage de poids", "Le temps pour changer de charge", "Les erreurs à éviter"]),
    dict(f="traction-a", page="barre-traction-sans-percer.html", style="hero", kicker="Location ? Pas de souci",
         title=["Barre de traction", ""], hi="sans percer",
         sub="Laquelle choisir, comment mesurer ta porte, l'installer en sécurité."),
    dict(f="traction-b", page="barre-traction-sans-percer.html", style="list", kicker="Zéro trou dans le mur",
         title=["Ta barre de traction", "sans percer en"], hi="4 points",
         points=["Les deux types de barres", "Mesurer ta porte avant", "L'installer en sécurité", "Débuter sans réussir une traction"]),
    dict(f="elastiques-a", page="elastiques-musculation.html", style="hero", kicker="Le matériel le moins cher",
         title=["Élastiques de", "musculation :"], hi="le guide",
         sub="Quels élastiques, quelle résistance, et 5 exercices pour commencer."),
    dict(f="elastiques-b", page="elastiques-musculation.html", style="list", kicker="Muscu sans haltères",
         title=["5 exercices", "avec des"], hi="élastiques",
         points=["Squat", "Rowing", "Développé", "Curl biceps", "Pont fessier"]),
    dict(f="programme-a", page="programme-musculation-maison-debutant.html", style="hero", kicker="Programme gratuit",
         title=["Muscu à la maison", "pour"], hi="débutant",
         sub="3 séances par semaine, du matériel simple, et comment progresser."),
    dict(f="programme-b", page="programme-musculation-maison-debutant.html", style="list", kicker="Débutant",
         title=["Ton programme", "muscu maison en"], hi="3 séances",
         points=["Séance A : bas du corps", "Séance B : haut du corps", "Séance C : corps entier", "+ comment progresser chaque semaine"]),
    dict(f="creatine-a", page="creatine-proteines-complements.html", style="hero", kicker="Ce que dit la science",
         title=["Créatine et", "protéines :"], hi="les 2 qui marchent",
         sub="Les seuls compléments validés pour débuter. Doses, précautions, ceux à éviter."),
    dict(f="creatine-b", page="creatine-proteines-complements.html", style="list", kicker="Compléments",
         title=["Créatine :", "ce qu'il faut"], hi="savoir",
         points=["3 g par jour suffisent", "Monohydrate pure, rien d'autre", "Pas besoin de « phase de charge »", "Avis médical si problème de reins"]),
    dict(f="blackfriday-a", page="#materiel", style="list", kicker="Black Friday",
         title=["Black Friday :", "équipe-toi"], hi="pour l'année",
         points=["Tapis, élastiques, haltères, barre…", "3 kits complets, 3 budgets", "Tout le panier en 1 clic", "Les prix du moment sur Amazon"]),
    dict(f="blackfriday-b", page="#quiz", style="hero", kicker="Black Friday",
         title=["Ta salle de sport", "à la maison"], hi="pendant le Black Friday",
         sub="Réponds à 3 questions, on te dit quoi acheter. Tu vois les prix du moment sur Amazon."),
    dict(f="abdos-a", page="programme-abdos-maison.html", style="hero", kicker="Programme gratuit",
         title=["Programme abdos", "à la maison :"], hi="15 minutes",
         sub="5 exercices sur un tapis, 3 fois par semaine, sans se faire mal au dos."),
    dict(f="abdos-b", page="programme-abdos-maison.html", style="list", kicker="Abdos maison",
         title=["Abdos maison :", ""], hi="5 exercices",
         points=["La planche", "Le dead bug", "La planche latérale", "Le crunch", "Le relevé de bassin"]),
    dict(f="kettlebell-a", page="kettlebell-debutant.html", style="hero", kicker="Guide débutant",
         title=["Kettlebell :", "quel poids"], hi="choisir ?",
         sub="Le bon poids pour débuter, fixe ou réglable, et 6 exercices pour tout le corps."),
    dict(f="kettlebell-b", page="kettlebell-debutant.html", style="list", kicker="Tout le corps",
         title=["Kettlebell :", ""], hi="5 exercices",
         points=["Soulevé de terre", "Squat gobelet", "Swing", "Rowing", "Développé"]),
    dict(f="materiel-a", page="materiel.html", style="list", kicker="Sport à la maison",
         title=["Le matériel", "expliqué"], hi="simplement",
         points=["Ce que chaque objet fait travailler", "3 exercices pour s'en servir", "2 modèles, la différence expliquée", "Tout le panier en 1 clic"]),
]

CSS = f"""
@font-face {{ font-family: Anton; src: url(file://{ANTON}); }}
@font-face {{ font-family: IS; src: url(file://{SANS}); }}
@font-face {{ font-family: IS; src: url(file://{SANS_B}); font-weight: 700; }}
:root {{ --iso-floor: #2a2d35; --iso-floor-l: #16171c; --iso-floor-r: #1e2027; --iso-grid: #383c47;
  --iso-ink: #e9e6df; --iso-ink-r: #c9c5bc; --iso-blue-l: #2a4fd0; --iso-blue-r: #3560e6;
  --iso-or-l: #c63a05; --iso-or-r: #ea4b10; --iso-shadow: rgba(0,0,0,.5); --blue: #2b56d6; --green: #157a45; --orange: #ff5a1f; --mist: #8a8f9c; }}
.iso .dim line {{ stroke: #8a8f9c; stroke-width: 1; stroke-dasharray: 3 5; }}
.iso .dim text {{ font-family: Anton; font-size: 22px; fill: #fff; }}
.iso {{ filter: drop-shadow(0 40px 40px rgba(0,0,0,.55)); }}
* {{ margin: 0; box-sizing: border-box; }}
body {{ width: 1000px; height: 1500px; background: #0c0d10; color: #f4f1ea; font-family: IS; overflow: hidden; position: relative; }}
body::before {{ content: ""; position: absolute; inset: 0;
  background: radial-gradient(900px 700px at 85% 70%, rgba(255,90,31,.32), transparent 65%),
              radial-gradient(600px 500px at 0% 0%, rgba(43,86,214,.18), transparent 70%); }}
.brand {{ position: absolute; top: 64px; left: 72px; font-family: Anton; font-size: 64px; letter-spacing: 1px; }}
.brand sup {{ color: #ff5a1f; font-size: 36px; }}
.kick {{ position: absolute; top: 84px; right: 72px; font-weight: 700; font-size: 26px; letter-spacing: 4px; text-transform: uppercase;
  color: #0c0d10; background: #ff5a1f; padding: 12px 22px; }}
h1 {{ font-family: Anton; font-weight: 400; text-transform: uppercase;
  font-size: 116px; line-height: 1.02; letter-spacing: .5px; }}
h1 .o {{ color: #ff5a1f; display: block; }}
.sub {{ margin-top: 36px; max-width: 820px; font-size: 38px; line-height: 1.35; color: #d8d3c8; }}
.art {{ flex: 1; display: flex; align-items: center; justify-content: center; min-height: 0; margin: 10px -40px 0; }}
.art svg {{ max-height: 100%; width: auto; max-width: 100%; }}

ol {{ list-style: none; padding: 0; margin-top: 56px; }}
li {{ display: flex; align-items: center; gap: 30px; font-size: 46px; font-weight: 700; padding: 30px 0; border-top: 2px solid rgba(244,241,234,.16); }}
li:last-child {{ border-bottom: 2px solid rgba(244,241,234,.16); }}
li b {{ font-family: Anton; font-weight: 400; font-size: 64px; color: #ff5a1f; width: 70px; }}
main {{ position: absolute; top: 200px; left: 72px; right: 72px; bottom: 190px; display: flex; flex-direction: column; padding-bottom: 40px; }}
.cta {{ position: absolute; left: 0; right: 0; bottom: 0; height: 190px; background: #ff5a1f; color: #0c0d10;
  display: flex; flex-direction: column; justify-content: center; padding: 0 72px; }}
.cta strong {{ font-family: Anton; font-weight: 400; font-size: 64px; text-transform: uppercase; line-height: 1; }}
.cta span {{ font-size: 28px; font-weight: 700; margin-top: 12px; letter-spacing: .5px; }}
"""


def html(p):
    lines = [l for l in p["title"] if l]
    h1 = " ".join(lines) + f'<span class="o">{p["hi"]}</span>'
    body = f'<div class="brand">2M<sup>²</sup></div><div class="kick">{p["kicker"]}</div><main><h1>{h1}</h1>'
    if p["style"] == "hero":
        body += f'<p class="sub">{p["sub"]}</p><div class="art">{iso.scene()}</div></main>'
        cta = "Lire le guide gratuit →"
    else:
        items = "".join(f"<li><b>{i + 1}</b>{t}</li>" for i, t in enumerate(p["points"]))
        body += f'<ol>{items}</ol></main>'
        cta = "Le guide complet →"
    if p["f"].startswith("accueil") or p["f"] == "blackfriday-b":
        cta = "Trouve ton kit en 30 s →"
    if p["f"] == "blackfriday-a":
        cta = "Voir les 3 kits →"
    if p["f"] == "materiel-a":
        cta = "Voir tout le matériel →"
    body += f'<div class="cta"><strong>{cta}</strong><span>2 m² · la salle de sport qui tient chez toi</span></div>'
    return f"<!DOCTYPE html><html lang=fr><head><meta charset=utf-8><style>{CSS}</style></head><body>{body}</body></html>"


def main():
    os.makedirs(OUT, exist_ok=True)
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files"])
        pg = b.new_page(viewport={"width": 1000, "height": 1500})
        import sys
        only = set(sys.argv[1:])
        for p in PINS:
            if only and p["f"] not in only:
                continue
            tmp = os.path.join("/tmp", f"pin-{p['f']}.html")
            open(tmp, "w").write(html(p).replace('class="f1"', "").replace("animation", "x-anim"))
            pg.goto("file://" + tmp)
            pg.wait_for_timeout(300)
            png = os.path.join("/tmp", f"pin-{p['f']}.png")
            pg.screenshot(path=png)
            from PIL import Image
            Image.open(png).convert("RGB").save(os.path.join(OUT, f"{p['f']}.jpg"), quality=86, optimize=True, progressive=True)
            print("ok", p["f"])
        b.close()


if __name__ == "__main__":
    main()

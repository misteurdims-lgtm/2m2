# Contenu du site 2 m². Pour ajouter un guide : copier un bloc de GUIDES, changer le slug et le texte, puis lancer build.py.

SITE = {
    "name": "2 m²",
    "tagline": "La salle de sport qui tient chez toi",
    "description": "Le guide du matériel pour s'entraîner chez soi dans un petit espace : emprise au sol, rangement, critères de choix et programmes.",
    "base_url": "https://misteurdims-lgtm.github.io/2m2",   # à remplacer par le nom de domaine quand il sera acheté
    "amazon_tag": "VOTRE-TAG-21",                # à remplacer par ton identifiant Amazon Partenaires
    "goatcounter": "",                           # code GoatCounter (statistiques sans cookie), vide = désactivé
}

PRODUCTS = [
    {"icon": "tapis", "tier": "Essentiel", "pair": "rouleau", "name": "Un tapis de sol", "start": True, "budget": "€", "compare": "un tapis de bain un peu long",
     "w": 183, "d": 61, "storage": "Roulé dans un coin",
     "why": "Ta base : plus confortable pour les genoux, et il protège le sol. C'est ton coin sport.",
     "query": "tapis de sol fitness épais 15 mm", "guide": "salle-de-sport-petit-appartement"},
    {"icon": "elastiques", "tier": "Essentiel", "pair": "barre", "name": "Des élastiques", "start": True, "budget": "€", "compare": "une boîte à chaussures",
     "w": 30, "d": 20, "storage": "Dans un tiroir",
     "why": "Le meilleur achat pour commencer : pas cher, et ils servent pour tout le corps.",
     "query": "élastiques de résistance musculation lot", "guide": "elastiques-musculation"},
    {"icon": "halteres", "tier": "Essentiel", "pair": "banc", "name": "Des haltères réglables", "start": True, "budget": "€€", "compare": "une petite valise",
     "w": 45, "d": 40, "storage": "Sous le lit",
     "why": "Les petits poids qu'on règle selon sa force. Une seule paire suffit pour progresser des mois.",
     "query": "haltères réglables", "guide": "halteres-reglables"},
    {"icon": "barre", "tier": "Pour progresser", "pair": "elastiques", "name": "Une barre de traction", "budget": "€", "compare": "rien : elle se pose sur une porte",
     "w": 0, "d": 0, "storage": "Reste sur la porte",
     "why": "Pour muscler le dos et les bras. Elle tient sur un cadre de porte, sans percer.",
     "query": "barre de traction porte sans perçage", "guide": "barre-traction-sans-percer"},
    {"icon": "kettlebell", "tier": "Pour progresser", "pair": "tapis", "name": "Un kettlebell", "budget": "€", "compare": "un pot de fleurs",
     "w": 22, "d": 22, "storage": "Au pied d'un meuble",
     "why": "Un poids avec une poignée, pour les jambes, les fesses et le cardio en même temps.",
     "query": "kettlebell fonte"},
    {"icon": "corde", "tier": "Pour progresser", "pair": "tapis", "name": "Une corde à sauter", "budget": "€", "compare": "rien : elle tient dans une poche",
     "w": 0, "d": 0, "storage": "Dans un tiroir",
     "why": "Le cardio le plus simple qui soit : 10 minutes et tu es essoufflé. Il faut un plafond assez haut.",
     "query": "corde à sauter roulements"},
    {"icon": "rouleau", "tier": "Pour récupérer", "pair": "tapis", "name": "Un rouleau de massage", "budget": "€", "compare": "une bouteille d'eau",
     "w": 33, "d": 14, "storage": "Sur une étagère",
     "why": "Pour détendre les muscles après la séance. Ça fait du bien, surtout au début.",
     "query": "rouleau de massage mousse"},
    {"icon": "banc", "tier": "Pour aller plus loin", "pair": "halteres", "name": "Un banc pliable", "budget": "€€", "compare": "une planche à repasser, une fois plié",
     "w": 125, "d": 50, "storage": "Plié contre un mur",
     "why": "Pour plus tard, quand tu as pris l'habitude. Il ajoute beaucoup d'exercices.",
     "query": "banc de musculation pliable"},
    {"icon": "pot", "tier": "Nutrition (en option)", "pair": "shaker", "name": "De la créatine", "budget": "€", "compare": "un petit pot sur une étagère",
     "w": 0, "d": 0, "storage": "Dans un placard",
     "why": "Le complément le plus étudié en sport. 3 g par jour, pour les efforts courts et intenses comme la musculation.",
     "query": "créatine monohydrate pure", "guide": "creatine-proteines-complements"},
    {"icon": "shaker", "tier": "Nutrition (en option)", "pair": "pot", "name": "Des protéines en poudre", "budget": "€€", "compare": "un pot sur une étagère",
     "w": 0, "d": 0, "storage": "Dans un placard",
     "why": "Pratique pour atteindre ses besoins en protéines quand on se muscle, sans cuisiner plus.",
     "query": "protéine whey", "guide": "creatine-proteines-complements"},
]

GUIDES = [
    {
        "slug": "salle-de-sport-petit-appartement",
        "short": "Salle de sport en petit appartement",
        "kicker": "Bien s'installer",
        "title": "Aménager une salle de sport dans un petit appartement",
        "desc": "Comment s'équiper pour s'entraîner chez soi avec 2 m², sans gêner les voisins ni encombrer le salon : plan, matériel, rangement.",
        "date": "2026-11-19", "minutes": 6,
        "toc": ["Les 2 m² qu'il te faut", "Le matériel, dans l'ordre", "Les voisins et le bruit", "Tout ranger en 2 minutes"],
        "links": {"tapis": "tapis de sol fitness épais 15 mm", "halt": "haltères réglables", "elast": "élastiques de résistance musculation lot"},
        "body": """
<p>Pas besoin d'une pièce dédiée. Une zone libre de <strong>2 mètres sur 1 mètre</strong> suffit pour un entraînement complet : c'est la taille d'un tapis de sol, plus un peu de marge pour bouger les bras.</p>
<h2>Les 2 m² qu'il te faut</h2>
<p>Mesure l'espace réellement libre, une fois la table basse poussée ou le fauteuil décalé. Il te faut :</p>
<ul>
<li><strong>200 cm de long</strong> pour t'allonger sur le tapis, bras tendus au-dessus de la tête ;</li>
<li><strong>100 cm de large</strong> pour les pompes, les fentes et le gainage ;</li>
<li><strong>une porte solide</strong> si tu veux ajouter une barre de traction (elle ne prend rien au sol) ;</li>
<li><strong>environ 2,40 m sous plafond</strong> pour la corde à sauter. Sinon, remplace-la par des montées de genoux.</li>
</ul>
<div class="note"><span class="label">Astuce</span>Le couloir est souvent le meilleur endroit : il est long, rarement encombré, et il y a toujours un cadre de porte pour la barre.</div>
<h2>Le matériel, dans l'ordre</h2>
<p>Achète en trois temps. Chaque étape permet déjà de s'entraîner, et tu sauras si tu tiens le rythme avant de dépenser plus.</p>
<div class="tbl"><table>
<tr><th>Étape</th><th>Matériel</th><th>Emprise au sol</th><th>Ce que ça débloque</th></tr>
<tr><td>1</td><td>Tapis + élastiques</td><td>≈ 183 × 61 cm</td><td>Gainage, pompes, tirage, jambes</td></tr>
<tr><td>2</td><td>Haltères réglables</td><td>≈ 45 × 40 cm</td><td>Vraie progression en force</td></tr>
<tr><td>3</td><td>Barre de traction, kettlebell</td><td>≈ 22 × 22 cm</td><td>Dos complet, cardio-force</td></tr>
</table></div>
<div class="buy"><div><strong>Tapis de sol épais (10 à 15 mm)</strong><span>La base de tout : il délimite ta zone et protège le sol.</span></div><a class="btn" href="{{tapis}}" rel="sponsored nofollow noopener" target="_blank">Voir les prix</a></div>
<div class="buy"><div><strong>Lot d'élastiques de résistance</strong><span>Le meilleur achat pour commencer, à petit prix.</span></div><a class="btn" href="{{elast}}" rel="sponsored nofollow noopener" target="_blank">Voir les prix</a></div>
<h2>Les voisins et le bruit</h2>
<p>En appartement, le bruit vient surtout des chocs : sauts, haltères qu'on pose trop fort. Trois règles suffisent :</p>
<ul>
<li>pose toujours les poids sur le tapis, jamais directement sur le sol ;</li>
<li>remplace les sauts par des variantes sans impact (squats lents, montées de genoux) aux heures calmes ;</li>
<li>pour la corde à sauter, saute bas, sur l'avant du pied, sur un tapis épais.</li>
</ul>
<h2>Tout ranger en 2 minutes</h2>
<p>Un coin d'entraînement qu'on doit ranger pendant dix minutes finit par ne plus servir. Vise un rangement en deux gestes : le tapis roulé debout dans un angle, et le reste dans une seule caisse ou sous le lit. Les <a href="halteres-reglables.html">haltères réglables</a> sont faits pour ça : une paire au lieu d'une rangée de poids.</p>
<div class="buy"><div><strong>Haltères réglables</strong><span>Une paire remplace tout un rack, rangée sous le lit.</span></div><a class="btn" href="{{halt}}" rel="sponsored nofollow noopener" target="_blank">Voir les prix</a></div>
""",
        "faq": [
            ("Quelle surface faut-il pour faire du sport chez soi ?", "Une zone libre d'environ 2 mètres sur 1 mètre suffit pour un entraînement complet au poids du corps et avec des haltères."),
            ("Comment faire du sport en appartement sans déranger les voisins ?", "Pose les poids sur un tapis épais, évite les sauts aux heures calmes et préfère des variantes sans impact."),
            ("Par quoi commencer pour s'équiper à la maison ?", "Un tapis de sol et un lot d'élastiques. Ensuite des haltères réglables, puis une barre de traction de porte."),
        ],
    },
    {
        "slug": "halteres-reglables",
        "short": "Bien choisir ses haltères réglables",
        "kicker": "Choisir son matériel",
        "title": "Haltères réglables : comment bien les choisir",
        "desc": "À disques ou à sélecteur, quelle plage de poids, quel encombrement : les critères pour choisir des haltères réglables qui dureront.",
        "date": "2026-11-19", "minutes": 5,
        "toc": ["Les deux grandes familles", "Quelle plage de poids", "Les critères qui comptent", "Les erreurs à éviter"],
        "links": {"disques": "haltères réglables disques", "selecteur": "haltères réglables sélecteur rapide"},
        "body": """
<p>Les haltères réglables sont l'achat le plus rentable pour s'entraîner chez soi : une seule paire remplace une dizaine de paires fixes, et se range sous un lit.</p>
<h2>Les deux grandes familles</h2>
<h3>À disques (avec écrous ou bagues)</h3>
<p>Une barre courte, des disques qu'on ajoute et qu'on bloque. C'est simple, solide et le moins cher. En contrepartie, changer de poids prend une minute, et les disques se rangent à côté.</p>
<div class="buy"><div><strong>Haltères réglables à disques</strong><span>Le meilleur prix, increvables, réglage plus lent.</span></div><a class="btn" href="{{disques}}" rel="sponsored nofollow noopener" target="_blank">Voir les prix</a></div>
<h3>À sélecteur (molette ou goupille)</h3>
<p>L'haltère reste dans son socle : on tourne une molette ou on déplace une goupille, et on soulève seulement le poids choisi. Le réglage prend quelques secondes, tout tient dans deux socles. C'est nettement plus cher, et le haltère est plus long qu'un modèle classique, ce qui gêne un peu pour certains exercices.</p>
<div class="buy"><div><strong>Haltères à sélecteur rapide</strong><span>Réglage en secondes, rangement net.</span></div><a class="btn" href="{{selecteur}}" rel="sponsored nofollow noopener" target="_blank">Voir les prix</a></div>
<h2>Quelle plage de poids</h2>
<div class="tbl"><table>
<tr><th>Profil</th><th>Plage par haltère</th><th>Pour quoi</th></tr>
<tr><td>Débutant</td><td>2 à 12 kg</td><td>Épaules, bras, rowing, squats légers</td></tr>
<tr><td>Intermédiaire</td><td>2 à 20 kg</td><td>Tout le corps pendant longtemps</td></tr>
<tr><td>Confirmé</td><td>jusqu'à 30 kg et plus</td><td>Jambes et dos lourds</td></tr>
</table></div>
<p>Dans le doute, prends plus large : on progresse vite les premiers mois, surtout sur les jambes et le dos.</p>
<h2>Les critères qui comptent</h2>
<ul>
<li><strong>Le pas entre deux charges.</strong> Des sauts de 2 à 2,5 kg sont idéaux. Au-delà, la progression sur les petits muscles (épaules, bras) devient difficile.</li>
<li><strong>Le verrouillage.</strong> Les disques ne doivent avoir aucun jeu une fois serrés. C'est une question de sécurité.</li>
<li><strong>La poignée.</strong> Moletée, ni trop épaisse ni trop fine, pour ne pas glisser.</li>
<li><strong>L'encombrement.</strong> Vérifie la longueur de l'haltère et la taille du socle sur la fiche produit, surtout si tu as peu de place.</li>
</ul>
<h2>Les erreurs à éviter</h2>
<ul>
<li>Acheter trop léger : tu devras racheter dans six mois.</li>
<li>Oublier le tapis : un haltère posé trop fort abîme le sol et dérange les voisins (voir <a href="salle-de-sport-petit-appartement.html">notre guide petit appartement</a>).</li>
<li>Négliger la poignée en plastique lisse : ça glisse dès qu'on transpire.</li>
</ul>
""",
        "faq": [
            ("Quel poids d'haltères pour débuter ?", "Une plage de 2 à 12 kg par haltère suffit pour débuter. Une plage de 2 à 20 kg dure beaucoup plus longtemps."),
            ("Haltères réglables ou fixes ?", "Réglables si tu manques de place ou de budget, fixes si tu changes souvent de charge dans la même séance."),
            ("Les haltères à sélecteur sont-ils fiables ?", "Oui s'ils sont bien utilisés : on vérifie le verrouillage avant chaque série et on les repose dans leur socle sans les lâcher."),
        ],
    },
    {
        "slug": "barre-traction-sans-percer",
        "short": "Barre de traction sans percer",
        "kicker": "Choisir son matériel",
        "title": "Barre de traction sans percer : laquelle choisir",
        "desc": "Télescopique ou en appui sur le cadre de porte : comment choisir une barre de traction qui tient sans vis ni trou, et l'installer en sécurité.",
        "date": "2026-11-19", "minutes": 5,
        "toc": ["Les deux types de barres", "Mesurer avant d'acheter", "Installer en sécurité", "Si tu n'arrives pas encore aux tractions"],
        "links": {"cadre": "barre de traction cadre de porte multiprise", "telesco": "barre de traction télescopique porte", "bandes": "élastiques assistance traction"},
        "body": """
<p>La traction est le meilleur exercice pour le dos et les bras, et la barre de porte est le seul équipement qui ne prend <strong>aucune place au sol</strong>. Bonne nouvelle : il existe des modèles qui tiennent sans percer.</p>
<h2>Les deux types de barres</h2>
<h3>La barre en appui sur le cadre de porte</h3>
<p>Elle se pose sur le haut du chambranle et prend appui sur le mur de part et d'autre. Pas de vis : c'est ton poids qui la plaque. Elle se décroche en deux secondes, et elle offre souvent plusieurs prises (larges, serrées, neutres).</p>
<div class="buy"><div><strong>Barre en appui sur le cadre, multiprise</strong><span>Sans vis, se pose et s'enlève en secondes.</span></div><a class="btn" href="{{cadre}}" rel="sponsored nofollow noopener" target="_blank">Voir les prix</a></div>
<h3>La barre télescopique</h3>
<p>Elle se visse en longueur jusqu'à se bloquer entre les deux montants de l'encadrement. Elle est discrète et peu chère, mais sa tenue dépend de la solidité de ton encadrement et du serrage. Certains modèles fournissent des supports à visser pour plus de sécurité.</p>
<div class="buy"><div><strong>Barre télescopique</strong><span>Discrète et économique, à bien serrer.</span></div><a class="btn" href="{{telesco}}" rel="sponsored nofollow noopener" target="_blank">Voir les prix</a></div>
<h2>Mesurer avant d'acheter</h2>
<ul>
<li><strong>La largeur intérieure</strong> de l'encadrement : compare-la à la plage indiquée sur la fiche produit.</li>
<li><strong>L'épaisseur du mur</strong> au-dessus de la porte, pour les barres en appui sur le cadre.</li>
<li><strong>La charge maximale</strong> annoncée : prends une bonne marge au-dessus de ton poids.</li>
<li><strong>Le type de cadre</strong> : un chambranle très fin ou décoratif ne supporte pas toujours la pression. Dans le doute, choisis un modèle avec supports de sécurité.</li>
</ul>
<h2>Installer en sécurité</h2>
<p>Teste toujours la barre progressivement : d'abord en tirant vers le bas avec les bras, puis en te suspendant pieds au sol, avant de lever les jambes. Contrôle le serrage d'une barre télescopique avant chaque séance. Les mousses de protection évitent les marques sur la peinture.</p>
<h2>Si tu n'arrives pas encore aux tractions</h2>
<p>C'est le cas de la plupart des débutants. Deux solutions : les tractions négatives (tu montes avec une chaise, tu descends le plus lentement possible) et l'assistance avec une grande bande élastique accrochée à la barre, sous le pied ou le genou.</p>
<div class="buy"><div><strong>Bandes d'assistance pour tractions</strong><span>Plusieurs résistances pour progresser jusqu'à la première traction.</span></div><a class="btn" href="{{bandes}}" rel="sponsored nofollow noopener" target="_blank">Voir les prix</a></div>
<p>Plus de détails dans <a href="elastiques-musculation.html">notre guide des élastiques</a>.</p>
""",
        "faq": [
            ("Une barre de traction sans percer est-elle solide ?", "Oui si elle est adaptée à ton encadrement, installée selon la notice et testée progressivement avant chaque séance."),
            ("Est-ce que la barre abîme la porte ?", "Les modèles avec mousses de protection limitent les marques. Évite les chambranles très fins ou fragiles."),
            ("Comment faire sa première traction ?", "Avec des tractions négatives et une bande élastique d'assistance, en réduisant l'aide au fil des semaines."),
        ],
    },
    {
        "slug": "elastiques-musculation",
        "short": "Élastiques de musculation",
        "kicker": "Choisir son matériel",
        "title": "Élastiques de musculation : le guide pour bien débuter",
        "seo_title": "Élastiques de musculation : guide débutant",
        "desc": "Mini-bandes, grandes boucles ou tubes à poignées : quels élastiques choisir, quelle résistance, et quels exercices faire avec.",
        "date": "2026-11-19", "minutes": 5,
        "toc": ["Les trois types d'élastiques", "Choisir la résistance", "5 exercices pour commencer", "Durée de vie et sécurité"],
        "links": {"boucles": "élastique musculation grande boucle lot", "mini": "mini bandes élastiques tissu", "tubes": "élastiques avec poignées ancrage porte"},
        "body": """
<p>Les élastiques sont l'équipement le plus sous-estimé : ils tiennent dans un tiroir, coûtent peu, et permettent de travailler tout le corps. Ils sont aussi parfaits en complément des haltères.</p>
<h2>Les trois types d'élastiques</h2>
<div class="tbl"><table>
<tr><th>Type</th><th>À quoi ça sert</th><th>Pour qui</th></tr>
<tr><td>Grandes boucles (environ 2 m)</td><td>Tirage, développé, assistance aux tractions</td><td>Tout le monde : le plus polyvalent</td></tr>
<tr><td>Mini-bandes</td><td>Fessiers, hanches, échauffement</td><td>En complément</td></tr>
<tr><td>Tubes à poignées</td><td>Mouvements proches des machines de salle</td><td>Ceux qui aiment avoir des poignées</td></tr>
</table></div>
<div class="buy"><div><strong>Lot de grandes boucles</strong><span>Le plus polyvalent, idéal aussi pour les tractions assistées.</span></div><a class="btn" href="{{boucles}}" rel="sponsored nofollow noopener" target="_blank">Voir les prix</a></div>
<div class="buy"><div><strong>Tubes avec poignées et ancrage de porte</strong><span>Pour reproduire les exercices de salle à la maison.</span></div><a class="btn" href="{{tubes}}" rel="sponsored nofollow noopener" target="_blank">Voir les prix</a></div>
<h2>Choisir la résistance</h2>
<p>Les fabricants indiquent souvent une résistance en kilos. C'est une équivalence approximative : un élastique résiste de plus en plus à mesure qu'on l'étire. Le plus simple est d'acheter <strong>un lot de 4 à 5 résistances</strong>, du plus léger au plus fort, pour s'adapter à chaque exercice et progresser.</p>
<h2>5 exercices pour commencer</h2>
<ol>
<li><strong>Rowing debout</strong> : élastique accroché à la porte, tire vers le ventre en serrant les omoplates.</li>
<li><strong>Développé épaules</strong> : debout sur l'élastique, pousse au-dessus de la tête.</li>
<li><strong>Squat avec élastique</strong> : élastique sous les pieds et sur les épaules.</li>
<li><strong>Écartés arrière</strong> : bras tendus devant, ouvre en écartant l'élastique.</li>
<li><strong>Pont fessier avec mini-bande</strong> : bande au-dessus des genoux, pousse les genoux vers l'extérieur.</li>
</ol>
<div class="buy"><div><strong>Mini-bandes en tissu</strong><span>Ne roulent pas sur les cuisses, parfaites pour les fessiers.</span></div><a class="btn" href="{{mini}}" rel="sponsored nofollow noopener" target="_blank">Voir les prix</a></div>
<h2>Durée de vie et sécurité</h2>
<p>Inspecte tes élastiques avant chaque séance. Une petite fissure, une zone blanchie ou collante : on remplace. Range-les à l'abri du soleil et de la chaleur, qui fragilisent le latex. En cas d'allergie au latex, choisis des modèles en tissu.</p>
""",
        "faq": [
            ("Quels élastiques acheter pour débuter ?", "Un lot de grandes boucles avec 4 à 5 résistances : c'est le plus polyvalent, et il sert aussi aux tractions assistées."),
            ("Peut-on prendre du muscle avec des élastiques ?", "Oui, à condition d'augmenter régulièrement la difficulté : résistance plus forte, plus de répétitions ou un tempo plus lent."),
            ("Combien de temps dure un élastique ?", "Souvent plusieurs mois à quelques années selon l'usage. Remplace-le dès qu'il présente une fissure ou une zone abîmée."),
        ],
    },
    {
        "slug": "programme-musculation-maison-debutant",
        "short": "Programme musculation maison débutant",
        "kicker": "S'entraîner",
        "title": "Programme de musculation à la maison pour débutant",
        "desc": "Trois séances de 40 minutes par semaine avec un tapis, des élastiques et des haltères : le programme complet, et comment progresser.",
        "date": "2026-11-19", "minutes": 6,
        "toc": ["Le principe", "Les trois séances", "Comment progresser", "Échauffement et récupération", "Et côté alimentation ?"],
        "links": {"halt": "haltères réglables", "elast": "élastiques de résistance musculation lot", "kb": "kettlebell fonte", "crea": "créatine monohydrate pure", "whey": "protéine whey"},
        "body": """
<p>Trois séances par semaine, environ 40 minutes chacune, avec le matériel du kit 2 m². C'est assez pour progresser nettement pendant plusieurs mois, et assez court pour tenir sur la durée.</p>
<h2>Le principe</h2>
<p>On alterne haut du corps, bas du corps et corps entier, avec au moins un jour de repos entre deux séances (par exemple lundi, mercredi, vendredi). Repos de 60 à 90 secondes entre les séries.</p>
<h2>Les trois séances</h2>
<div class="tbl"><table>
<tr><th>Séance</th><th>Exercices</th><th>Séries × répétitions</th><th>Matériel</th></tr>
<tr><td>A · Haut du corps</td><td>Pompes, rowing haltère, développé épaules, tirage élastique, gainage</td><td>3 × 8 à 12</td><td>Haltères, élastiques, tapis</td></tr>
<tr><td>B · Bas du corps</td><td>Squat gobelet, fentes, soulevé de terre jambes tendues, pont fessier</td><td>3 × 10 à 15</td><td>Haltère ou kettlebell</td></tr>
<tr><td>C · Corps entier</td><td>Tractions ou tirage élastique, swing kettlebell, pompes, gainage latéral</td><td>4 tours</td><td>Barre, kettlebell</td></tr>
</table></div>
<div class="buy"><div><strong>Haltères réglables</strong><span>Indispensables pour les séances A et B.</span></div><a class="btn" href="{{halt}}" rel="sponsored nofollow noopener" target="_blank">Voir les prix</a></div>
<h2>Comment progresser</h2>
<p>Utilise la <strong>double progression</strong> : garde le même poids jusqu'à réussir le haut de la fourchette (par exemple 3 séries de 12) avec une bonne technique. À ce moment-là, augmente un peu la charge et repars du bas de la fourchette.</p>
<p>Note tes charges et tes répétitions après chaque séance. Un simple carnet ou une appli suffit : c'est ce qui permet de voir les progrès et de rester motivé.</p>
<div class="note"><span class="label">Bon à savoir</span>La technique passe avant la charge. Si le mouvement se dégrade sur les dernières répétitions, garde le même poids à la séance suivante.</div>
<h2>Échauffement et récupération</h2>
<p>Commence chaque séance par 5 minutes d'échauffement : rotations des épaules et des hanches, squats sans poids, une série légère du premier exercice. Termine par quelques minutes de mobilité ou de rouleau de massage.</p>
<div class="buy"><div><strong>Lot d'élastiques</strong><span>Pour le tirage et l'échauffement des épaules.</span></div><a class="btn" href="{{elast}}" rel="sponsored nofollow noopener" target="_blank">Voir les prix</a></div>
<div class="buy"><div><strong>Kettlebell</strong><span>Pour le squat gobelet et le swing de la séance C.</span></div><a class="btn" href="{{kb}}" rel="sponsored nofollow noopener" target="_blank">Voir les prix</a></div>
<h2>Et côté alimentation ?</h2>
<p>Pour progresser, l'entraînement ne suffit pas : il faut aussi assez de protéines et de sommeil. Deux compléments sont validés par les experts pour la musculation : <strong>la créatine</strong> (3 g par jour) et <strong>les protéines en poudre</strong>, pratiques pour atteindre ses besoins. On explique tout, avec les précautions, dans <a href="creatine-proteines-complements.html">notre guide créatine et protéines</a>.</p>
<div class="buy"><div><strong>Créatine monohydrate</strong><span>Le complément le plus étudié pour les efforts courts et intenses.</span></div><a class="btn" href="{{crea}}" rel="sponsored nofollow noopener" target="_blank">Voir le prix du jour</a></div>
<div class="buy"><div><strong>Protéine whey</strong><span>Un shaker après la séance pour atteindre tes besoins en protéines.</span></div><a class="btn" href="{{whey}}" rel="sponsored nofollow noopener" target="_blank">Voir le prix du jour</a></div>
<p>Ces conseils sont généraux. En cas de douleur, de blessure ou de problème de santé, demande l'avis d'un médecin avant de commencer, et avant de prendre un complément.</p>
""",
        "faq": [
            ("Combien de séances par semaine pour débuter la musculation ?", "Trois séances par semaine, avec un jour de repos entre chaque, suffisent pour progresser au début."),
            ("Peut-on prendre du muscle à la maison ?", "Oui, avec des haltères et des élastiques et en augmentant progressivement la difficulté."),
            ("Combien de temps avant de voir des résultats ?", "Les gains de force arrivent souvent en quelques semaines. Les changements visibles prennent généralement plusieurs mois de régularité."),
        ],
    },
    {
        "slug": "creatine-proteines-complements",
        "short": "Créatine et protéines",
        "kicker": "Nutrition",
        "title": "Créatine et protéines : les 2 compléments validés par la science",
        "seo_title": "Créatine et protéines : ce que dit la science",
        "desc": "Ce que disent vraiment les experts sur la créatine et les protéines en poudre, comment les prendre, et les compléments à éviter.",
        "date": "2026-11-19", "minutes": 6,
        "toc": ["La créatine", "Les protéines", "Les compléments à éviter", "Qui doit demander l'avis d'un médecin"],
        "links": {"crea": "créatine monohydrate pure", "whey": "protéine whey", "vegan": "protéine végétale poudre", "shaker": "shaker protéine"},
        "body": """
<p>Les compléments ne remplacent ni l'entraînement ni une alimentation équilibrée. Mais deux d'entre eux sont solidement étudiés et utiles quand on fait de la musculation : <strong>la créatine</strong> et <strong>les protéines en poudre</strong>. Le reste est souvent du marketing.</p>
<h2>La créatine</h2>
<p>C'est le complément le plus étudié du sport. En Europe, une seule allégation est autorisée : la créatine augmente les performances physiques lors de séries successives d'exercices très intenses et de courte durée, pour un apport de <strong>3 g par jour</strong>. Elle ne vaut que pour les adultes qui font des efforts intenses, comme la musculation (<a href="https://www.vidal.fr/parapharmacie/complements-alimentaires/creatine.html" rel="noopener" target="_blank">Vidal</a>).</p>
<p>Côté sécurité, la Société internationale de nutrition sportive (ISSN) a passé en revue les études en 2017 : la supplémentation, à court et à long terme, est jugée sûre et bien tolérée chez les personnes en bonne santé (<a href="https://read.qxmd.com/read/28615996/international-society-of-sports-nutrition-position-stand-safety-and-efficacy-of-creatine-supplementation-in-exercise-sport-and-medicine" rel="noopener" target="_blank">ISSN, 2017</a>).</p>
<h3>Comment la prendre</h3>
<ul>
<li><strong>3 g par jour</strong>, tous les jours, même les jours sans séance. La régularité compte plus que l'heure.</li>
<li>Dans un verre d'eau ou un shaker. Pas besoin de « phase de charge ».</li>
<li>Une légère prise de poids peut arriver au début : c'est de l'eau stockée dans les muscles.</li>
<li>Choisis de la <strong>créatine monohydrate</strong> pure : c'est la forme la plus étudiée.</li>
</ul>
<div class="buy"><div><strong>Créatine monohydrate</strong><span>Pure, sans additif. Un pot dure plusieurs mois à 3 g par jour.</span></div><a class="btn" href="{{crea}}" rel="sponsored nofollow noopener" target="_blank">Voir le prix du jour</a></div>
<h2>Les protéines</h2>
<p>Quand on se muscle, on a besoin de plus de protéines. Selon l'ISSN, un apport de <strong>1,4 à 2,0 g de protéines par kilo de poids de corps et par jour</strong> suffit à la plupart des personnes qui s'entraînent pour construire et garder leur muscle (<a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5477153/" rel="noopener" target="_blank">ISSN, 2017</a>). Pour une personne de 70 kg, cela fait environ 100 à 140 g par jour.</p>
<p>L'alimentation peut suffire (viande, poisson, œufs, laitages, légumineuses). La poudre est simplement <strong>pratique</strong> : un shaker après la séance ou au petit-déjeuner, et l'objectif est plus facile à atteindre.</p>
<div class="buy"><div><strong>Protéine whey</strong><span>Issue du lait, se mélange facilement à l'eau ou au lait.</span></div><a class="btn" href="{{whey}}" rel="sponsored nofollow noopener" target="_blank">Voir le prix du jour</a></div>
<div class="buy"><div><strong>Protéine végétale</strong><span>Sans lactose, pour les végétariens ou les estomacs sensibles.</span></div><a class="btn" href="{{vegan}}" rel="sponsored nofollow noopener" target="_blank">Voir le prix du jour</a></div>
<div class="buy"><div><strong>Un shaker</strong><span>Pour la créatine et les protéines, sans grumeaux.</span></div><a class="btn" href="{{shaker}}" rel="sponsored nofollow noopener" target="_blank">Voir le prix du jour</a></div>
<h2>Les compléments à éviter</h2>
<p>L'Anses, l'agence française de sécurité sanitaire, met en garde contre les compléments vendus pour « prendre du muscle » ou « brûler les graisses ». Entre 2016 et février 2024, elle a recensé 154 cas d'effets indésirables, dont 18 très graves (<a href="https://www.anses.fr/fr/content/complements-alimentaires-et-aliments-enrichis-pour-sportifs-des-consommations-risque" rel="noopener" target="_blank">Anses</a>). Évite donc :</p>
<ul>
<li>les « brûleurs de graisse » et les produits minceur miracles ;</li>
<li>les boosters riches en caféine avant ou pendant le sport : l'Anses les déconseille ;</li>
<li>le cumul de plusieurs compléments, ou leur association avec des médicaments.</li>
</ul>
<div class="note"><span class="label">Bon réflexe</span>Préfère les produits qui affichent la norme AFNOR NF V 94-001, un repère de sécurité recommandé par l'Anses pour les sportifs.</div>
<h2>Qui doit demander l'avis d'un médecin</h2>
<p>Parle à ton médecin ou à ton pharmacien avant de prendre un complément si tu as moins de 18 ans, si tu es enceinte ou allaitante, si tu as un problème de reins, de foie ou de cœur, ou si tu prends un traitement. Ces conseils sont généraux et ne remplacent pas un avis médical.</p>
""",
        "faq": [
            ("La créatine est-elle dangereuse ?", "Chez l'adulte en bonne santé, la créatine est jugée sûre et bien tolérée par la Société internationale de nutrition sportive. Demande un avis médical en cas de problème rénal, de grossesse ou de traitement."),
            ("Combien de créatine par jour ?", "3 g par jour, c'est la dose retenue par l'allégation européenne pour les efforts courts et intenses."),
            ("Les protéines en poudre sont-elles obligatoires ?", "Non. L'alimentation peut couvrir les besoins. La poudre est simplement pratique pour atteindre 1,4 à 2 g de protéines par kilo et par jour."),
        ],
    },
]

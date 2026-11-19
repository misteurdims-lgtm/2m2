# Contenu du site 2 m². Pour ajouter un guide : copier un bloc de GUIDES, changer le slug et le texte, puis lancer build.py.

SITE = {
    "name": "2 m²",
    "tagline": "La salle de sport qui tient chez toi",
    "description": "Le guide du matériel pour s'entraîner chez soi dans un petit espace : emprise au sol, rangement, critères de choix et programmes.",
    "base_url": "https://deuxmetrescarres.fr",   # à remplacer par le vrai domaine
    "amazon_tag": "VOTRE-TAG-21",                # à remplacer par ton identifiant Amazon Partenaires
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
        "toc": ["Le principe", "Les trois séances", "Comment progresser", "Échauffement et récupération"],
        "links": {"halt": "haltères réglables", "elast": "élastiques de résistance musculation lot", "kb": "kettlebell fonte"},
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
<p>Ces conseils sont généraux. En cas de douleur, de blessure ou de problème de santé, demande l'avis d'un médecin avant de commencer.</p>
""",
        "faq": [
            ("Combien de séances par semaine pour débuter la musculation ?", "Trois séances par semaine, avec un jour de repos entre chaque, suffisent pour progresser au début."),
            ("Peut-on prendre du muscle à la maison ?", "Oui, avec des haltères et des élastiques et en augmentant progressivement la difficulté."),
            ("Combien de temps avant de voir des résultats ?", "Les gains de force arrivent souvent en quelques semaines. Les changements visibles prennent généralement plusieurs mois de régularité."),
        ],
    },
]

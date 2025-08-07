<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <title>Pitch Deck Oriasol</title>
    <link rel="stylesheet" href="reveal.js/dist/reveal.css"> <!-- Assure-toi d'avoir Reveal.js dans ton dossier -->
    <link rel="stylesheet" href="reveal.js/dist/theme/black.css"> <!-- Thème noir pro, adaptable -->
    <style>
        .reveal section { font-size: 1.5em; text-align: left; color: #fff; background: #000; } /* Style global pour présentation pro */
        .reveal h1 { color: #00ff00; font-size: 2.5em; } /* Vert solaire pour titres */
        .reveal ul { list-style-type: disc; margin-left: 40px; }
        .reveal p { margin: 10px 0; }
        .reveal .graph-container { width: 80%; height: 300px; margin: auto; } /* Pour graphiques */
    </style>
    <!-- Inclu Chart.js pour graphiques (CDN, pas besoin d'install) -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <div class="reveal">
        <div class="slides">
            <!-- Slide 1 : Titre et Vision Globale -->
            <section>
                <h1>Oriasol – La Marketplace Photovoltaïque Nouvelle Génération</h1>
                <p>Révolutionner le solaire : Hub sécurisé pour dossiers validés et projets sans risque</p>
                <p>Porté par Mohammed Djedir, 15 ans d'expérience. Objectif : Devenir référence nationale en 2026.</p>
                <!-- Visuel : Image (remplace par une URL ou local file) -->
                <img src="https://example.com/logo-oriasol.png" alt="Logo Oriasol" style="width: 300px;">
            </section>

            <!-- Slide 2 : Présentation de l'Équipe et Parcours Personnel -->
            <section>
                <h1>Qui Suis-Je ?</h1>
                <ul>
                    <li>Mohammed Djedir, Président de La Rosace Bleue.</li>
                    <li>Expérience photovoltaïque depuis 2009 : Vu les failles des méthodes traditionnelles.</li>
                    <li>Encouragé par un contact privilégié à aller au bout de l'idée.</li>
                </ul>
                <!-- Visuel : Timeline -->
                <div style="display: flex; justify-content: center;">
                    <svg width="600" height="100">
                        <line x1="50" y1="50" x2="550" y2="50" stroke="white" stroke-width="2"/>
                        <circle cx="50" cy="50" r="5" fill="#00ff00"/><text x="30" y="70">2009</text>
                        <circle cx="300" cy="50" r="5" fill="#00ff00"/><text x="280" y="70">Idée Oriasol</text>
                        <circle cx="550" cy="50" r="5" fill="#00ff00"/><text x="530" y="70">2025</text>
                    </svg>
                </div>
            </section>

            <!-- Slide 3 : Origine de l'Idée -->
            <section>
                <h1>Comment Oriasol est Né</h1>
                <p>Depuis 2009, méthodes identiques : Devis opaques, clients opaques par ignorance.</p>
                <p>Idée : Créer une nouvelle façon de faire du PV – sécuriser, offrir choix, assurer bon choix.</p>
                <!-- Visuel : Icônes problème vs solution -->
                <div style="display: flex; justify-content: space-around;">
                    <div><img src="https://example.com/probleme-icon.png" alt="Problème" width="150"><p>Problème</p></div>
                    <div><img src="https://example.com/solution-icon.png" alt="Solution" width="150"><p>Solution</p></div>
                </div>
            </section>

            <!-- Slide 4 : Le Problème dans le Photovoltaïque -->
            <section>
                <h1>Le Problème Actuel</h1>
                <ul>
                    <li>Méthodes dépassées : Offres toutes faites profitant de l'ignorance.</li>
                    <li>Clients risquent des projets non rentables.</li>
                    <li>Installateurs à court d'idées marketing.</li>
                </ul>
                <!-- Visuel : Graphique -->
                <canvas id="problemeChart" class="graph-container"></canvas>
                <script>
                    new Chart(document.getElementById('problemeChart'), {
                        type: 'bar',
                        data: { labels: ['Hésitants'], datasets: [{ label: 'Foyers', data: [30], backgroundColor: '#ff0000' }] },
                        options: { scales: { y: { beginAtZero: true } } }
                    });
                </script>
            </section>

            <!-- Slide 5 : Tendances du Marché 2025 -->
            <section>
                <h1>Marché en Explosion</h1>
                <ul>
                    <li>30 GW installés en France ; croissance 20%/an.</li>
                    <li>Puissance raccordée : 1 407 MW au Q1 2025.</li>
                    <li>Autoconsommation collective : 1 111 opérations, 161 MW.</li>
                </ul>
                <!-- Visuel : Graphique croissance -->
                <canvas id="marcheChart" class="graph-container"></canvas>
                <script>
                    new Chart(document.getElementById('marcheChart'), {
                        type: 'line',
                        data: { labels: ['2020', '2025', '2027'], datasets: [{ label: 'Croissance', data: [10, 30, 60], borderColor: '#00ff00' }] }
                    });
                </script>
            </section>

            <!-- Slide 6 : Lois et Réglementations Clés -->
            <section>
                <h1>Contexte Légal Favorable</h1>
                <ul>
                    <li>Simplification autoconsommation collective (décret 2016-1696, étendu 2023).</li>
                    <li>Article 175 : Modification contrats soutien.</li>
                    <li>Fin obligations d'achat, focus autoconsommation.</li>
                </ul>
                <!-- Visuel : Icônes -->
                <div style="display: flex; justify-content: space-around;">
                    <img src="https://example.com/loi-icon.png" alt="Lois" width="150">
                </div>
            </section>

            <!-- Slide 7 : Hausses des Coûts Électricité -->
            <section>
                <h1>Crainte des Consommateurs</h1>
                <ul>
                    <li>+20% d'ici 2030 ; fin ARENH 31/12/2025 augmente factures.</li>
                    <li>Coût autoconsommée : ~14 c€/kWh (Sud France).</li>
                    <li>Tarif rachat surplus : 4 c€/kWh résidentiel.</li>
                </ul>
                <!-- Visuel : Graphique hausses -->
                <canvas id="coutChart" class="graph-container"></canvas>
                <script>
                    new Chart(document.getElementById('coutChart'), {
                        type: 'line',
                        data: { labels: ['2025', '2030'], datasets: [{ label: 'Hausse', data: [0, 20], borderColor: '#ff0000' }] }
                    });
                </script>
            </section>

            <!-- Slide 8 : Solution Oriasol – Concept Central -->
            <section>
                <h1>Oriasol : La Solution</h1>
                <ul>
                    <li>Hub sécurisé : Gère projets A à Z, produit dossiers validés.</li>
                    <li>Pas de risques : Traçabilité CRM, freelances formés.</li>
                </ul>
                <!-- Visuel : Schéma -->
                <img src="https://example.com/ecosysteme-schema.png" alt="Écosystème" width="500">
            </section>

            <!-- Slide 9 : Acteurs Impliqués -->
            <section>
                <h1>Les Acteurs d'Oriasol</h1>
                <ul>
                    <li>Clients (particuliers/entreprises) : Choix sécurisés.</li>
                    <li>Freelances : Commissions 200€-8%.</li>
                    <li>Installateurs : Chantiers prêts (1 200€).</li>
                    <li>Oriasol : Supervise.</li>
                </ul>
                <!-- Visuel : Icônes connectés -->
                <img src="https://example.com/acteurs-icon.png" alt="Acteurs" width="400">
            </section>

            <!-- Slide 10 : Outils de la Plateforme -->
            <section>
                <h1>Nos Outils</h1>
                <ul>
                    <li>CRM : Pilotage (historique, RDV, simulateur).</li>
                    <li>Boutique : Kits/matériel.</li>
                    <li>Espaces freelance/installateur.</li>
                </ul>
                <!-- Visuel : Mockup -->
                <img src="https://example.com/mockup-crm.png" alt="CRM" width="500">
            </section>

            <!-- Slide 11 : Modèle Économique -->
            <section>
                <h1>Modèle Économique Équilibré</h1>
                <ul>
                    <li>Client : Paye étude/kit.</li>
                    <li>Installateur : 1 200€/chantier.</li>
                    <li>Freelance : Commission fixe.</li>
                    <li>Oriasol : Marge nette ~1 600€/dossier min. Sans avance trésorerie.</li>
                </ul>
                <!-- Visuel : Flux -->
                <img src="https://example.com/flux-financiers.png" alt="Flux" width="400">
            </section>

            <!-- Slide 12 : Valeurs et Promesses -->
            <section>
                <h1>Nos Valeurs</h1>
                <ul>
                    <li>Sécurité (pas de devis bidon).</li>
                    <li>Liberté (choix libre).</li>
                    <li>Performance (suivi mesuré).</li>
                    <li>Sens (autonomie énergétique).</li>
                </ul>
                <!-- Visuel : Icônes -->
                <div style="display: flex; justify-content: space-around;">
                    <img src="https://example.com/securite-icon.png" alt="Sécurité" width="100">
                </div>
            </section>

            <!-- Slide 13 : Plan de Déploiement -->
            <section>
                <h1>Roadmap</h1>
                <ul>
                    <li>2025 : Lancement plateforme, premiers freelances.</li>
                    <li>2026 : IA/CRM, national.</li>
                    <li>2027+ : Afrique (Algérie), agri.</li>
                </ul>
                <!-- Visuel : Timeline -->
                <svg width="600" height="150">
                    <line x1="50" y1="75" x2="550" y2="75" stroke="white" stroke-width="2"/>
                    <rect x="50" y="60" width="100" height="30" fill="#00ff00"/><text x="60" y="80">2025</text>
                    <rect x="200" y="60" width="100" height="30" fill="#00ff00"/><text x="210" y="80">2026</text>
                    <rect x="350" y="60" width="100" height="30" fill="#00ff00"/><text x="360" y="80">2027+</text>
                </svg>
            </section>

            <!-- Slide 14 : Plan d'Investissement Refait -->
            <section>
                <h1>Besoins en Investissement</h1>
                <ul>
                    <li>Total : 500 000 €.</li>
                    <li>Breakdown : 200k développement plateforme, 100k formation/marketing, 100k opérations, 100k réserve.</li>
                    <li>Utilisation : Lancement 2025.</li>
                </ul>
                <!-- Visuel : Camembert -->
                <canvas id="investChart" class="graph-container"></canvas>
                <script>
                    new Chart(document.getElementById('investChart'), {
                        type: 'pie',
                        data: { labels: ['Développement', 'Formation', 'Opérations', 'Réserve'], datasets: [{ data: [40, 20, 20, 20], backgroundColor: ['#00ff00', '#ff00ff', '#ffff00', '#00ffff'] }] }
                    });
                </script>
            </section>

            <!-- Slide 15 : Projections Financières -->
            <section>
                <h1>Projections</h1>
                <ul>
                    <li>Y1 (2025) : 500 dossiers, 800k€ marge.</li>
                    <li>Y2 : 1 000 dossiers, 1,6M€.</li>
                    <li>Y3 : 2 000 dossiers, 3,2M€. ROI : 18-24 mois.</li>
                </ul>
                <!-- Visuel : Graphique revenus -->
                <canvas id="projChart" class="graph-container"></canvas>
                <script>
                    new Chart(document.getElementById('projChart'), {
                        type: 'bar',
                        data: { labels: ['Y1', 'Y2', 'Y3'], datasets: [{ label: 'Marge', data: [800000, 1600000, 3200000], backgroundColor: '#00ff00' }] },
                        options: { scales: { y: { beginAtZero: true } } }
                    });
                </script>
            </section>

            <!-- Slide 16 : Concurrence et Différenciation -->
            <section>
                <h1>Pourquoi Oriasol Gagne</h1>
                <ul>
                    <li>Concurrence : Plateformes basiques (mise en relation).</li>
                    <li>Diff : Hub sécurisé, dossiers validés, sans risque.</li>
                    <li>Partenariats installateurs.</li>
                </ul>
                <!-- Visuel : Tableau -->
                <table style="border-collapse: collapse; width: 80%; margin: auto; color: #fff;">
                    <tr><th style="border: 1px solid white;">Critère</th><th style="border: 1px solid white;">Concurrence</th><th style="border: 1px solid white;">Oriasol</th></tr>
                    <tr><td style="border: 1px solid white;">Sécurité</td><td style="border: 1px solid white;">Faible</td><td style="border: 1px solid white;">Haute</td></tr>
                    <tr><td style="border: 1px solid white;">Traçabilité</td><td style="border: 1px solid white;">Non</td><td style="border: 1px solid white;">Oui</td></tr>
                </table>
            </section>

            <!-- Slide 18 : Appel à l'Action et Contact -->
            <section>
                <h1>Rejoignez Oriasol</h1>
                <p>Investissez pour changer le PV.</p>
                <p>Contact : Mohammed Djedir, [ton email/tel]. Prochaines étapes : RDV pour détails.</p>
                <!-- Visuel : Bouton -->
                <a href="mailto:tonemail@example.com" style="background: #00ff00; color: black; padding: 10px 20px; text-decoration: none;">Contactez-moi</a>
            </section>
        </div>
    </div>
    <script src="reveal.js/dist/reveal.js"></script>
    <script>
        Reveal.initialize({
            transition: 'slide', // Transition fluide
            backgroundTransition: 'fade'
        });
    </script>
</body>
</html>
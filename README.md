 Projet d’Optimisation — Recherche Opérationnelle

 Description

Ce projet contient trois problèmes d’optimisation appliqués à des cas réels en Mauritanie (RIM) :

- 6.1 : Transport de poissons (VRP simplifié)
- 6.2 : Files d’attente (modèle M/M/c)
- 6.3 : Routage des camions d’eau (VRP)

---

📂 Structure du projet

project/
│
├── poissons_vrp.py     # Transport de poissons
├── queue_mmc.py        # Files d’attente (M/M/c)
├── eau_vrp.py          # Routage des camions d’eau

---

⚙️ Technologies utilisées

- Python 🐍
- OR-Tools (Google) pour les problèmes VRP
- Calcul mathématique pour M/M/c

---

#Problèmes traités

---

🔹 6.1 Transport de poissons

Objectif :
Minimiser la distance pour livrer du poisson depuis un port vers plusieurs villes.

Contraintes :

- Capacité des camions
- Chaque ville visitée une seule fois

Méthode :

- Modélisation VRP
- Résolution avec OR-Tools

---

🔹 6.2 Files d’attente (M/M/c)

Objectif :
Déterminer le nombre optimal de serveurs pour minimiser le temps d’attente.

Formule utilisée :
ρ = λ / (c × μ)

Interprétation :

- ρ < 1 → système stable
- ρ ≥ 1 → système instable

Résultat :
Choix du nombre minimal de serveurs assurant la stabilité.

---

🔹 6.3 Routage des camions d’eau

Objectif :
Optimiser la distribution d’eau vers plusieurs quartiers.

Contraintes :

- Capacité des camions
- Minimisation de la distance totale

Résultat :

- Routes optimales pour chaque camion
- Distance par camion
- Distance totale

---

▶ Exécution

🔹 Installer OR-Tools

pip install ortools

---

🔹 Lancer les fichiers

python poissons_vrp.py
python queue_mmc.py
python eau_vrp.py

---

#Exemple de sortie

Route 0 : [0, 3, 0]
Distance : 40

Route 1 : [0, 1, 2, 4, 0]
Distance : 70

Distance totale : 110

---

# Remarques

- OR-Tools est utilisé pour les problèmes complexes (VRP)
- Le modèle M/M/c est résolu par calcul direct
- Les données utilisées sont simulées

---

# Conclusion

Ce projet montre comment utiliser :

- Les modèles mathématiques
- Les outils d’optimisation
- La programmation Python

pour résoudre des problèmes réels de logistique et de gestion.

---

👨‍💻 Auteur

Nom : [medlemine/med el moustapha/elhamewi]
Projet universitaire — Recherche Opérationnelle

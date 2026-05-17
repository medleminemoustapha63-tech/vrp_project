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

<<<<<<< HEAD
Nom : [medlemine/med el moustapha/elhamewi]
Projet universitaire — Recherche Opérationnelle
=======
Nom : [Ton Nom]
Projet universitaire — Recherche Opérationnelle


# 🚦 Optimisation de la circulation routière

##  Description

Ce projet utilise OR-Tools pour optimiser les feux de circulation dans une intersection.

L’objectif est de :
- réduire le temps d’attente des voitures
- améliorer la circulation
- optimiser les durées des feux verts

---

# Technologies utilisées

- Python 🐍
- OR-Tools CP-SAT

---

# Principe du projet

Chaque route possède :
- un nombre de voitures
- un temps de feu vert

Le solver cherche :
- la meilleure durée des feux
- avec un temps total limité

---

#  Objectif

Minimiser :
- le temps d’attente total des voitures

---

#  Contraintes

- Temps minimum des feux
- Temps maximum des feux
- Somme des feux limitée


---


#  Planification des examens universitaires

##  Description

Ce projet utilise OR-Tools pour organiser les examens universitaires sans conflits.

Le système attribue :
- des créneaux horaires
- aux différentes matières

tout en respectant les contraintes.

---

#  Technologies utilisées

- Python 🐍
- OR-Tools CP-SAT

---

#  Principe du projet

Chaque matière reçoit :
- un créneau d’examen

Le solver vérifie :
- qu’aucune matière ne partage le même créneau

---

#  Objectif

Créer un planning :
- simple
- optimisé
- sans conflits

---

# Contraintes

- Deux examens ne peuvent pas avoir le même horaire
- Respect des créneaux disponibles

---

>>>>>>> ed6e670 (Add README files for traffic and exam projects)

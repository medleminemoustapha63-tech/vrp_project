# Projet : Optimisation des feux de circulation

from ortools.sat.python import cp_model

# 🔹 Création du modèle
model = cp_model.CpModel()

# 🔹 Variables : durée du feu vert pour chaque route
green_north = model.NewIntVar(10, 60, "green_north")
green_south = model.NewIntVar(10, 60, "green_south")
green_east = model.NewIntVar(10, 60, "green_east")
green_west = model.NewIntVar(10, 60, "green_west")

# 🔹 Nombre de voitures sur chaque route
cars_north = 40
cars_south = 30
cars_east = 20
cars_west = 10

# 🔹 Temps d’attente estimé
waiting_time = (
    cars_north * (60 - green_north) +
    cars_south * (60 - green_south) +
    cars_east * (60 - green_east) +
    cars_west * (60 - green_west)
)

# 🔹 Contrainte :
# somme des temps verts ≤ 120 secondes
model.Add(
    green_north +
    green_south +
    green_east +
    green_west <= 120
)

# 🔹 Objectif :
# minimiser le temps d’attente
model.Minimize(waiting_time)

# 🔹 Solver
solver = cp_model.CpSolver()
status = solver.Solve(model)

# 🔹 Résultats
if status == cp_model.OPTIMAL:
    print("🚦 Solution optimale :\n")

    print("Nord :", solver.Value(green_north), "secondes")
    print("Sud :", solver.Value(green_south), "secondes")
    print("Est :", solver.Value(green_east), "secondes")
    print("Ouest :", solver.Value(green_west), "secondes")

    print("\n⏳ Temps d’attente total :",
          solver.ObjectiveValue())
from ortools.sat.python import cp_model

model = cp_model.CpModel()

# 🔹 créneaux horaires
math = model.NewIntVar(1, 3, "Math")
physics = model.NewIntVar(1, 3, "Physics")
info = model.NewIntVar(1, 3, "Info")

# 🔹 contraintes
model.Add(math != physics)
model.Add(math != info)
model.Add(physics != info)

# 🔹 solver
solver = cp_model.CpSolver()
status = solver.Solve(model)

# 🔹 affichage
if status == cp_model.FEASIBLE or status==cp_model.OPTIMAL:
    print("Math :", solver.Value(math))
    print("Physics :", solver.Value(physics))
    print("Info :", solver.Value(info))
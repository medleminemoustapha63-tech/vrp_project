# Sujet 6.2 - Files d'attente (M/M/c)

# 🔹 paramètres
lam = 10   # λ : taux d'arrivée (clients/heure)
mu = 5     # μ : taux de service par serveur (clients/heure)

# 🔹 tester plusieurs valeurs de c
for c in range(1, 6):  # de 1 à 5 serveurs
    rho = lam / (c * mu)

    print(f"c = {c}")
    print(f"rho = {rho:.2f}")

    if rho >= 1:
        print("❌ système instable (attente infinie)")
    else:
        print("✅ système stable")

    print("-" * 30)
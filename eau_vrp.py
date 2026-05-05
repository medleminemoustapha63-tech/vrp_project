# Sujet 6.3 - Routage des camions d’eau (VRP)

from ortools.constraint_solver import pywrapcp, routing_enums_pb2

# 🔹 distances entre les points
distance_matrix = [
    [0, 10, 15, 20, 25],
    [10, 0, 35, 25, 30],
    [15, 35, 0, 30, 20],
    [20, 25, 30, 0, 15],
    [25, 30, 20, 15, 0],
]

# 🔹 demandes (quantité d’eau)
demands = [0, 200, 300, 400, 100]

# 🔹 paramètres
vehicle_capacity = 1000
num_vehicles = 2
depot = 0

# 🔹 manager + model
manager = pywrapcp.RoutingIndexManager(len(distance_matrix), num_vehicles, depot)
routing = pywrapcp.RoutingModel(manager)

# 🔹 cost function (distance)
def distance_callback(from_index, to_index):
    return distance_matrix[manager.IndexToNode(from_index)][manager.IndexToNode(to_index)]

routing.SetArcCostEvaluatorOfAllVehicles(
    routing.RegisterTransitCallback(distance_callback)
)

# 🔹 demand (capacity constraint)
def demand_callback(from_index):
    return demands[manager.IndexToNode(from_index)]

routing.AddDimensionWithVehicleCapacity(
    routing.RegisterUnaryTransitCallback(demand_callback),
    0,
    [vehicle_capacity] * num_vehicles,
    True,
    "Capacity"
)

# 🔹 solve
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
solution = routing.SolveWithParameters(search_parameters)

# 🔹 affichage avec distances
if solution:
    total_distance = 0  # 🔥 distance totale

    for v in range(num_vehicles):
        index = routing.Start(v)
        route = []
        route_distance = 0  # 🔥 distance de ce camion

        while not routing.IsEnd(index):
            previous_index = index
            route.append(manager.IndexToNode(index))

            index = solution.Value(routing.NextVar(index))

            # 🔥 calcul de distance
            route_distance += routing.GetArcCostForVehicle(
                previous_index, index, v
            )

        route.append(0)

        print(f"Route {v}: {route}")
        print(f"Distance: {route_distance}")
        print("------------")

        total_distance += route_distance

    print(f"Total distance: {total_distance}")
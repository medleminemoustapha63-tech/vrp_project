from ortools.constraint_solver import pywrapcp, routing_enums_pb2

# distances entre port et villes
distance_matrix = [
    [0, 20, 30, 25],
    [20, 0, 15, 35],
    [30, 15, 0, 20],
    [25, 35, 20, 0],
]

# demandes (quantité de poisson)
demands = [0, 100, 150, 200]

vehicle_capacity = 400
num_vehicles = 2
depot = 0

manager = pywrapcp.RoutingIndexManager(len(distance_matrix), num_vehicles, depot)
routing = pywrapcp.RoutingModel(manager)

def distance_callback(from_index, to_index):
    return distance_matrix[manager.IndexToNode(from_index)][manager.IndexToNode(to_index)]

routing.SetArcCostEvaluatorOfAllVehicles(
    routing.RegisterTransitCallback(distance_callback)
)

def demand_callback(from_index):
    return demands[manager.IndexToNode(from_index)]

routing.AddDimensionWithVehicleCapacity(
    routing.RegisterUnaryTransitCallback(demand_callback),
    0,
    [vehicle_capacity] * num_vehicles,
    True,
    "Capacity"
)

search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC

solution = routing.SolveWithParameters(search_parameters)

if solution:
   for v in range(num_vehicles):
    index = routing.Start(v)
    route = []
    route_distance = 0   # 🔥 initialisation

    while not routing.IsEnd(index):
        previous_index = index
        route.append(manager.IndexToNode(index))

        index = solution.Value(routing.NextVar(index))

        # 🔥 ajouter la distance de l’arc
        route_distance += routing.GetArcCostForVehicle(
            previous_index, index, v
        )

    route.append(0)

    print(f"Route {v} : {route}")
    print(f"Distance : {route_distance}")
    print("-----------")
    
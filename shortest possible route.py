def nearest_neighbor(cities, distances):
    start_city = cities[0]
    unvisited_cities = set(cities)
    unvisited_cities.remove(start_city)
    current_city = start_city
    tour = [start_city]

    while unvisited_cities:
        nearest_city = min(unvisited_cities, key=lambda city: distances[current_city][city])
        tour.append(nearest_city)
        unvisited_cities.remove(nearest_city)
        current_city = nearest_city

    tour.append(start_city) 
    total_distance = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    return tour, total_distance

if __name__ == "__main__":
    cities = ['A', 'B', 'C']
    distances = {
        'A': {'A': 0, 'B': 10, 'C': 15},
        'B': {'A': 10, 'B': 0, 'C': 20},
        'C': {'A': 15, 'B': 20, 'C': 0}
    }
    tour, total_distance = nearest_neighbor(cities, distances)
    print("Optimal Path:", tour)
    print("Total Distance:", total_distance)

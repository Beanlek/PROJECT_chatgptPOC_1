import math
import heapq
import matplotlib.pyplot as plt

# Data from your CSV with timestamps
van_data = [
    ("V2XV001", "1/7/2023", 376882, 100.7183, 4.85454, "2023-07-01 10:36:24.865 +0800"),
    ("V2XV001", "1/7/2023", 815056, 100.73165, 4.85208, "2023-07-01 10:39:18.468 +0800"),
    ("V2XV001", "1/7/2023", 21108180, 100.72157, 4.85204, "2023-07-01 10:46:37.656 +0800"),
    ("V2XV001", "1/7/2023", 21108181, 100.7216, 4.85192, "2023-07-01 10:50:35.525 +0800"),
    ("V2XV001", "1/7/2023", 816261, 100.72155, 4.85158, "2023-07-01 10:56:02.518 +0800"),
    ("V2XV001", "1/7/2023", 245941, 100.72076, 4.85139, "2023-07-01 10:59:17.304 +0800"),
    ("V2XV001", "1/7/2023", 722409, 100.72067, 4.85199, "2023-07-01 11:08:48.511 +0800"),
    ("V2XV001", "1/7/2023", 774608, 100.71812, 4.85412, "2023-07-01 11:20:45.935 +0800"),
    ("V2XV001", "1/7/2023", 669662, 100.71192, 4.8528, "2023-07-01 11:31:05.755 +0800"),
    ("V2XV001", "1/7/2023", 21108046, 100.71208, 4.85317, "2023-07-01 11:32:00.687 +0800"),
    ("V2XV001", "1/7/2023", 21108044, 100.71202, 4.85324, "2023-07-01 11:32:48.878 +0800"),
    ("V2XV001", "1/7/2023", 21108042, 100.71285, 4.85304, "2023-07-01 11:33:30.480 +0800"),
    ("V2XV001", "1/7/2023", 21108049, 100.71275, 4.85286, "2023-07-01 11:34:34.805 +0800"),
    ("V2XV001", "1/7/2023", 21108050, 100.71282, 4.85297, "2023-07-01 11:35:18.643 +0800"),
    ("V2XV001", "1/7/2023", 21108122, 100.71109, 4.84972, "2023-07-01 11:41:00.422 +0800"),
    ("V2XV001", "1/7/2023", 21101013, 100.71856, 4.85454, "2023-07-01 12:05:25.460 +0800"),
    ("V2XV001", "1/7/2023", 829233, 100.71258, 4.85244, "2023-07-01 12:09:32.579 +0800"),
]

# Sort van_data based on timestamps
van_data.sort(key=lambda x: x[5])

# Extract coordinates for plotting
coordinates = [(data[3], data[4]) for data in van_data]

def euclidean_distance(coord1, coord2):
    # Calculate the Euclidean distance between two coordinates
    x1, y1 = coord1
    x2, y2 = coord2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Create a graph as a dictionary where nodes are coordinates
# and edges represent the distance between coordinates
graph = {}
for i in range(len(coordinates)):
    for j in range(i + 1, len(coordinates)):
        coord1, coord2 = coordinates[i], coordinates[j]
        distance = euclidean_distance(coord1, coord2)
        if coord1 not in graph:
            graph[coord1] = []
        if coord2 not in graph:
            graph[coord2] = []
        graph[coord1].append((coord2, distance))
        graph[coord2].append((coord1, distance))

def dijkstra(graph, start, end):
    # Dijkstra's algorithm code (same as previous)
    distances = {node: float('inf') for node in graph}
    predecessors = {node: None for node in graph}
    distances[start] = 0
    visited = set()

    # Priority queue for storing (distance, node) pairs
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node == end:
            # Found the shortest path
            path = []
            while current_node is not None:
                path.insert(0, current_node)
                current_node = predecessors[current_node]
            return path

        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor in graph[current_node]:
            distance = current_distance + neighbor[1]

            if distance < distances[neighbor[0]]:
                distances[neighbor[0]] = distance
                predecessors[neighbor[0]] = current_node
                heapq.heappush(priority_queue, (distance, neighbor[0]))

    # If no path is found
    return None

# Define your start and end points
start_point = (100.7183, 4.85454)  # Replace with your desired start point
end_point = (100.73165,4.85208)   # Replace with your desired end point

# Find the shortest path
shortest_path = dijkstra(graph, start_point, end_point)

if shortest_path:
    print("Shortest Path:", shortest_path)
else:
    print("No path found.")

# Plot the points and paths
lng_values = [coord[0] for coord in coordinates]
lat_values = [coord[1] for coord in coordinates]

plt.figure(figsize=(10, 6))
plt.scatter(lat_values, lng_values, c='blue', marker='o', label='Van V2XV001')

for i in range(len(coordinates) - 1):
    plt.plot([coordinates[i][1], coordinates[i+1][1]], [coordinates[i][0], coordinates[i+1][0]], c='gray')

for i, (lat, lng) in enumerate(coordinates):
    plt.annotate(f'Point {i}', (lat, lng), textcoords="offset points", xytext=(0,10), ha='center')

plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.title('Van Movement')
plt.legend()
plt.grid(True)
plt.xlim(min(lat_values) - 0.01, max(lat_values) + 0.01)  # Adjust the x-axis range
plt.ylim(min(lng_values) - 0.01, max(lng_values) + 0.01)  # Adjust the y-axis range
plt.show()

import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Data from your CSV with timestamps
van_data = [
    # van_id  ,visit_date, outlet_id, lng,lat, created_at
    ("V2XV001", "6/7/2023", 21114052, 100.74605, 4.857, "2023-07-06 17:04:00.433 +0800"),
    ("V2XV001", "6/7/2023", 698148, 100.73873, 4.85025, "2023-07-06 17:04:10.680 +0800"),
]

# Sort van_data based on timestamps
van_data.sort(key=lambda x: x[5])

# Extract coordinates and outlet_ids for plotting
lng_values = [data[3] for data in van_data]
lat_values = [data[4] for data in van_data]
outlet_ids = [data[2] for data in van_data]

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(lat_values, lng_values, c='blue', marker='o', label=van_data[0][0])

# Draw directional paths between consecutive points
for i in range(len(lat_values) - 1):
    plt.plot([lat_values[i], lat_values[i+1]], [lng_values[i], lng_values[i+1]], c='gray')

# Annotate points with outlet_id labels
for i, (lat, lng, outlet_id) in enumerate(zip(lat_values, lng_values, outlet_ids)):
    plt.annotate(f'Outlet: {outlet_id}', (lat, lng), textcoords="offset points", xytext=(0, 10), ha='center')

plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.title(f'Van Movement for V2XV001 on {van_data[0][1]}')
plt.legend()
plt.grid(True)
# plt.xlim(min(lat_values) - 0.01, max(lat_values) + 0.01)  # Adjust the x-axis range
# plt.ylim(min(lng_values) - 0.01, max(lng_values) + 0.01)  # Adjust the y-axis range
plt.show()

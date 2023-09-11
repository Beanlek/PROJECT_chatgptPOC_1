import matplotlib.pyplot as plt
import matplotlib.patches as patches
import csv

# Define the path to the CSV file in your folder
# csv_file_path = 'route_data_1-7-23.csv'
# C:\Users\USER\Desktop\INTERN AMAST\PROJECT_chatgptPOC_1\csv\route_data_1-7-23.csv

filename = "./csv/route_data_1-7-23.csv"
file = open(filename, "r")
file_data = file.read()
file.close()

# Split the input data into lines
lines = file_data.strip().split('\n')[1:]

# Initialize an empty list to store the transformed data
van_data = []

# Iterate through the lines and format the fields into tuples
for line in lines:
    fields = line.split(',')
    formatted_data = (
        fields[0],        # Field 1
        fields[1],        # Field 2
        int(fields[2]),   # Field 3 as an integer
        float(fields[3]), # Field 4 as a float
        float(fields[4]), # Field 5 as a float
        fields[5]         # Field 6
    )
    van_data.append(formatted_data)

# Sort van_data based on timestamps
van_data.sort(key=lambda x: x[5])

# Extract coordinates and outlet_ids for plotting
lng_values = [data[3] for data in van_data]
lat_values = [data[4] for data in van_data]
outlet_ids = [data[2] for data in van_data]

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(lat_values, lng_values, c='blue', marker='o', label=van_data[0][0])

# Draw arrows between consecutive points
for i in range(len(lat_values) - 1):
    dx = lat_values[i + 1] - lat_values[i]
    dy = lng_values[i + 1] - lng_values[i]
    arrow = patches.Arrow(lat_values[i], lng_values[i], dx, dy, width=0.0001, color='gray')
    plt.gca().add_patch(arrow)

# Annotate points with outlet_id labels
for i, (lat, lng, outlet_id) in enumerate(zip(lat_values, lng_values, outlet_ids)):
    plt.annotate(f'Outlet: {outlet_id}', (lat, lng), textcoords="offset points", xytext=(0, 10), ha='center')

plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.title(f'Van Movement for V2XV001 on {van_data[0][1]}')
plt.legend()
plt.grid(True)
plt.show()

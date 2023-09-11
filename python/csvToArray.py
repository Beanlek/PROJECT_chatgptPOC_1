import csv

# Define the path to the CSV file in your folder
# csv_file_path = 'route_data_1-7-23.csv'
# C:\Users\USER\Desktop\INTERN AMAST\PROJECT_chatgptPOC_1\csv\route_data_1-7-23.csv

filename = "./csv/route_data_1-7-23.csv"
file = open(filename, "r")

file_data = file.read()

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

# Print the transformed data
for data in van_data:
    print(data)
# print(van_data)
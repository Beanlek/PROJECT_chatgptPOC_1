from tkinter import *
from tkinter import filedialog
# from tkinter import ttk
# import tkinter as tk
import re
# import csv
import matplotlib.pyplot as plt
# import matplotlib.patches as patches

root=Tk()
root.geometry("700x700")
isFileChosen = False
isClickedOnce = False

def clear_labels():
    global isClickedOnce
    global isFileChosen
    global error_label
    global van_data
    global csv_data
    global frame
    frame.destroy()
    error_label.destroy()
    isFileChosen = False
    isClickedOnce = False

def open_file():
    global isClickedOnce
    global isFileChosen
    global error_label
    global van_data
    global csv_data
    global frame

    if isClickedOnce == True:
        print("IsClickedOnce Tag: "+str(isClickedOnce))
        return
    if isFileChosen == True:
        error_message = "Please clear the window first."
        error_label = Label(root, text=error_message)
        error_label.grid(row=1, column=0, columnspan=2,padx=10, pady=10)
        print("IsFileChosen Tag 1: "+str(isClickedOnce))
        isClickedOnce = True
        print("IsFileChosen Tag 2: "+str(isClickedOnce))
        return
    
    isFileChosen = True
    isClickedOnce = False
    
    van_data = []
    filepath = filedialog.askopenfilename()
    if filepath == "":
        isFileChosen = False
        return
    # print("filepath: "+filepath) #debug
    

    file = open(filepath, 'r')
    iscsv = re.search("\w.csv$",filepath)
    # print("iscsv: "+str(iscsv)) #debug

    if iscsv == None:
        error_message = "The file provided is not in csv format."
        error_label = Label(root, text=error_message)
        error_label.grid(row=1, column=0, columnspan=2,padx=10, pady=10)
        print("IsCsv Tag 1: "+str(isClickedOnce))
        isClickedOnce = True
        print("IsCsv Tag 2: "+str(isClickedOnce))
        isFileChosen = False
        return

    # print('SUCCESS 1') #debug

    file_data = file.read()
    # print("\nfile_data: "+file_data) #debug

    lines = file_data.strip().split('\n')[1:]
    # print("lines: "+str(lines)) #debug

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
    
    file.close()
    frame = Frame(root) 
    frame.grid(row=3, column=0,columnspan=2, padx=20, pady=2)

    for index, data in enumerate(van_data):
        csv_data = []
        csv_data = Label(frame, text=data, wraplength=700)
        csv_data.grid(row=index, column=0,columnspan=2, padx=20, pady=2)

    # print(van_data)
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
    plt.show()

open_button = Button(text="Choose file", command=open_file)
open_button.grid(row=0, column=0, padx=60, pady=20)

clear_button = Button(text="Clear Window", command=clear_labels)
clear_button.grid(row=0, column=1, padx=60, pady=20)

csv_data_header = Label(root, text='van_id\tvisit_date\toutlet_id\t\tlng\tlat\tcreated_at')
csv_data_header.grid(row=2, column=0, columnspan=2,padx=20, pady=5)

root.mainloop()
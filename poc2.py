import openai
from tkinter import *
from tkinter import filedialog
import re
# import matplotlib.pyplot as plt

root=Tk()
root.geometry("700x700")

API_KEY = open('key.txt', 'r')

openai.api_key = API_KEY.read()

model_engine = "text-davinci-003"
prompt = "Hello, how are you Robot?"

def open_file():
    global prompt
    global van_data
    global filepath

    van_data = []
    filepath = filedialog.askopenfilename()
    # print("filepath: "+filepath) #debug
    
    file = open(filepath, 'r')
    iscsv = re.search("\w.csv$",filepath)
    # print("iscsv: "+str(iscsv)) #debug
    fileChosen_message = str(filepath)+" is selected."
    fileChosen_label = Label(root, text=fileChosen_message)
    fileChosen_label.grid(row=2, column=0, columnspan=2,padx=10, pady=10)

    if iscsv == None:
        error_message = "The file provided is not in csv format."
        error_label = Label(root, text=error_message)
        error_label.grid(row=2, column=0, columnspan=2,padx=10, pady=10)
        return

    # print('SUCCESS 1') #debug

    file_data = file.read()
    # print("\nfile_data: "+file_data) #debug

    prompt = str(file_data)+'''

This is a CSV data from a .csv file. Rearrange the columns into ONLY van_id, visit_date, outlet_id, lng, lat, and created_at columns. Then sort the data by ascending visit_date. Give the answer in the above format.
    '''
    completion = openai.Completion.create(
        engine = model_engine,
        prompt = prompt,
        max_tokens = 1024,
        n = 1,
        stop = None,
        temperature = 0.5
    )

    response = completion.choices[0].text

    lines = response.strip().split('\n')[1:]
    # print("lines: "+str(lines)) #debug
    try:
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
    except IndexError:
      print('Sorry, the the file is incomprehensible.')
    except:
       print('Sorry, an error occured on our end.')

    
    
    van_data.sort(key=lambda x: x[5])
    # print(van_data)
    file.close()

    frame = Frame(root) 
    frame.grid(row=3, column=0,columnspan=2, padx=20, pady=2)

    for index, data in enumerate(van_data):
        csv_data = []
        csv_data = Label(frame, text=data, wraplength=700)
        csv_data.grid(row=index, column=0,columnspan=2, padx=20, pady=2)

title_header = Label(root, text='POC Test to sort data into\nvan_id | visit_date | outlet_id | lng | lat | created_at')
title_header.grid(row=0, column=0, columnspan=2,padx=20, pady=5)

open_button = Button(text="Choose file", command=open_file)
open_button.grid(row=1, column=0, padx=60, pady=20)

root.mainloop()
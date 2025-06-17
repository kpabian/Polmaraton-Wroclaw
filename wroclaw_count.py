import re
import json
from datetime import datetime

    
def main():
    time_array = count()
    percents(time_array)

def count():
        
    with open('results_wro.json', 'r') as f:
        d = json.load(f)
        f.close()

    time_array = [[0 for _ in range(7)] for _ in range(6)]
    arr_bib = []

    for i in range(1, len(d)):
        bib_number = int(re.search(r'\((\d+)\)', d[i][3]).group(1))
        arr_bib.append(bib_number)
        if d[i][7] == '' or d[i][7] == 'DNF':
            time = None
            time_group = 6
                
        else:
            time = datetime.strptime(d[i][7], '%H:%M:%S')

            if time < datetime.strptime('01:30:00', '%H:%M:%S'):
                time_group = 0
            elif time < datetime.strptime('01:40:00', '%H:%M:%S'):
                time_group = 1
            elif time < datetime.strptime('01:50:00', '%H:%M:%S'):
                time_group = 2
            elif time < datetime.strptime('02:00:00', '%H:%M:%S'):
                time_group = 3
            elif time < datetime.strptime('02:10:00', '%H:%M:%S'):
                time_group = 4
            else: 
                time_group = 5 
        

        if bib_number < 975:
            predicted_time_group = 0
        elif bib_number < 2561:
            predicted_time_group = 1
        elif bib_number < 5423:
            predicted_time_group = 2
        elif bib_number < 9404:
            predicted_time_group = 3
        elif bib_number < 12215:
            predicted_time_group = 4
        else: 
            predicted_time_group = 5
       
        time_array[predicted_time_group][time_group] += 1

    print(time_array)

    with open ('results_array.txt', 'w') as f:
        f.write(str(time_array))
    
    return time_array

def percents(time_array):
    time_percentage = [0 for _ in range(6)]
    for i in range(0, 6):
        time_percentage[i] = sum(time_array[i][1:7])

    print(time_percentage)
    print(sum(time_array[1]))

main()
import pandas as pd 
import re 
import os

irms_file = 'xa-VDD_acpc.ascii'
processed_file = 'cleaned.txt'
report_file = 'report_acpc_violation.csv'

# adjust coordinates in um
x_min, y_min = 31, 2 
x_max, y_max = 250, 20

if not os.path.exists(processed_file):
    with open(irms_file, 'r') as f, open(processed_file, 'w') as w: 
        lines = f.readlines() 
        first_line = lines[0].replace(',','_').replace('/','_')
        first_line = re.sub(r'(?<!\s) (?!\s)', '_', first_line) 
        w.write(first_line) 
        for line in lines[5:]:
            w.write(line)

df = pd.read_csv(processed_file, sep='\s+')


filtered_data = df[
    (df['Violation'] >= 6) &
    (df['X'] >= x_min) & (df['X'] <= x_max) &
    (df['Y'] >= y_min) & (df['Y'] <= y_max)
]

filtered_data.to_csv(report_file, index=False, header=True)
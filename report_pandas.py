import pandas as pd 
import re 

irms_file = 'xa-VDD_irms.ascii'
processed_file = 'cleaned.txt'
report_file = 'report_irms_violation.txt'

with open(irms_file, 'r') as f, open(processed_file, 'w') as w: 
    # clean data, remove backslashes and commas for easier pandas processing
    lines = f.readlines() 
    first_line = lines[0].replace(',','_').replace('/','_')
    first_line = re.sub(r'(?<!\s) (?!\s)', '_', first_line) 

    w.write(first_line) 

    # remove the processing net line 
    for line in lines[5:]:
        w.write(line)

df = pd.read_csv(processed_file, sep='\s+')
filtered_data = df[df['Violation'] > 2] 

filtered_data.to_csv(report_file, sep='\t' ,index=False, header=True)
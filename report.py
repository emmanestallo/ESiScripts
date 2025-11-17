vmax_file = 'xa-VDD_vmax.ascii' 
irms_file = 'xa-VDD_irms.ascii'

metal_layers = ["ME5_C", "ME6_7", "ME7_C", "ALRDL_C"]


with open(vmax_file, 'r') as f, open('report_vmax.txt', 'w') as w:
    for line in f: 
        columns = line.split() 
        if len(columns) >= 5:
            if any(sub in columns[1] for sub in metal_layers):
                w.write(line)

with open(irms_file, 'r') as f, open('report_irms.txt', 'w') as w:
    for line in f: 
        columns = line.split() 
        if len(columns) >= 5:
            if any(sub in columns[1] for sub in metal_layers):
                w.write(line)



import pandas as pd
import re
import os
import argparse

parser = argparse.ArgumentParser(description='Filter ACPC Violation')
parser.add_argument('-xmin', type=float, default=0, help='Minimum X coordinate (um)')
parser.add_argument('-xmax', type=float, default=1000, help='Maximum X coordinate (um)')
parser.add_argument('-ymin', type=float, default=0, help='Minimum Y coordinate (um)')
parser.add_argument('-ymax', type=float, default=1000, help='Maximum Y coordinate (um)')
parser.add_argument('-violation', type=float, default=6, help='Minimum violation threshold')
args = parser.parse_args()

irms_file = 'xa-VDD_acpc.ascii'
processed_file = 'cleaned.txt'
report_file = 'report_acpc_violation.csv'

if not os.path.exists(processed_file):
    with open(irms_file, 'r') as f, open(processed_file, 'w') as w:
        lines = f.readlines()
        first_line = lines[0].replace(',', '_').replace('/', '_')
        first_line = re.sub(r'(?<!\s) (?!\s)', '_', first_line)
        w.write(first_line)
        for line in lines[5:]:
            w.write(line)

df = pd.read_csv(processed_file, sep=r'\s+')

filtered_data = df[
    (df['Violation'] >= args.violation) &
    (df['X'] >= args.xmin) & (df['X'] <= args.xmax) &
    (df['Y'] >= args.ymin) & (df['Y'] <= args.ymax)
]

filtered_data.to_csv(report_file, index=False, header=True)
print(f"Filtered {len(filtered_data)} rows to {report_file}")
import csv

input_file = "ai_agile.csv"
output_file = "ai_agile_cleaned.csv"

with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

raw_header = lines[0].strip().strip('"')
header = [col.strip().strip('"') for col in raw_header.split(",")]

data_lines = [line for line in lines[1:] if line.strip() and "Here’s why" not in line]

parsed_rows = list(csv.reader(data_lines, skipinitialspace=True))

header = header[:len(parsed_rows[0])]

with open(output_file, "w", encoding="utf-8", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(parsed_rows)

print(f"Cleaned CSV saved as: {output_file}")

import csv

# Input and output file paths
input_file = "ai_agile.csv"
output_file = "ai_agile_cleaned.csv"

# Read the original file
with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Extract and clean the header
raw_header = lines[0].strip().strip('"')
header = [col.strip().strip('"') for col in raw_header.split(",")]

# Filter out empty lines and junk (e.g., "Here’s why this is transformative:")
data_lines = [line for line in lines[1:] if line.strip() and "Here’s why" not in line]

# Parse the data lines correctly with csv.reader
parsed_rows = list(csv.reader(data_lines, skipinitialspace=True))

# Adjust header length if data rows are shorter
header = header[:len(parsed_rows[0])]

# Write cleaned data to a new file
with open(output_file, "w", encoding="utf-8", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(parsed_rows)

print(f"Cleaned CSV saved as: {output_file}")

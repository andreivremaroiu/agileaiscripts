import pandas as pd

# === CONFIGURATION ===
input_file = "ai_strategy.xlsx"        # Replace with your Excel file
output_file = "ai.csv"   # Desired name for the CSV file

# === CONVERT EXCEL TO CSV ===
try:
    df = pd.read_excel(input_file)  # Reads the first sheet by default
    df.to_csv(output_file, index=False)
    print(f"✅ Successfully converted '{input_file}' to '{output_file}'.")
except FileNotFoundError:
    print(f"❌ File '{input_file}' not found.")
except Exception as e:
    print(f"⚠️ An error occurred: {e}")

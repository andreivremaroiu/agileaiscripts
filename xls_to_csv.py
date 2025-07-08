import pandas as pd

input_file = "ai_strategy.xlsx"      
output_file = "ai.csv"   

try:
    df = pd.read_excel(input_file) 
    df.to_csv(output_file, index=False)
    print(f"✅ Successfully converted '{input_file}' to '{output_file}'.")
except FileNotFoundError:
    print(f"❌ File '{input_file}' not found.")
except Exception as e:
    print(f"⚠️ An error occurred: {e}")

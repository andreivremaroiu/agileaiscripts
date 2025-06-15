# === Imports ===
import pandas as pd
import seaborn as sns
from wordcloud import WordCloud
import matplotlib
import matplotlib.pyplot as plt
import csv

# Use a backend for matplotlib that supports GUI interaction (adjust as needed)
matplotlib.use('TkAgg')
plt.ion()

# === File Configuration ===
file_path = 'ai.csv'

# === Step 1: Detect Delimiter Automatically ===
with open(file_path, 'r', encoding='utf-8-sig') as f:
    sample = f.read(2048)
    dialect = csv.Sniffer().sniff(sample)
    delimiter = dialect.delimiter
    print(f"🔍 Detected delimiter: '{delimiter}'")

# === Step 2: Load CSV File ===
df = pd.read_csv(file_path, delimiter=delimiter, encoding='utf-8-sig', engine='python', on_bad_lines='skip')
df.columns = df.columns.str.strip().str.replace(r'\s+', ' ', regex=True)

print(f"✅ Data loaded: {df.shape[0]} rows × {df.shape[1]} columns")
print("📋 Columns:\n", df.columns.tolist())

# === Step 3: Pie Chart — Company Age Distribution ===
age_col = 'How many years has your company been operating?'
if age_col in df.columns:
    df[age_col].value_counts().plot.pie(
        autopct='%1.1f%%',
        startangle=140,
        figsize=(6, 6),
        title='Company Age Distribution'
    )
    plt.ylabel('')
    plt.tight_layout()
    plt.show()

# === Step 4: Histogram — AI Usage Level in Strategy ===
ai_usage_col = 'To what extent is AI currently used in your company’s strategic planning?'
if ai_usage_col in df.columns:
    df[ai_usage_col] = pd.to_numeric(df[ai_usage_col], errors='coerce')
    usage_counts = df[ai_usage_col].dropna().value_counts().sort_index()
    
    plt.figure(figsize=(8, 5))
    bars = plt.bar(usage_counts.index.astype(int), usage_counts.values, color='cornflowerblue', edgecolor='black')
    
    plt.title('AI Usage in Strategic Planning')
    plt.xlabel('AI Usage Level (1–5)')
    plt.ylabel('Number of Companies')
    plt.xticks(range(1, 6))
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Add data labels on bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height + 1, str(int(height)), ha='center', va='bottom')
    
    plt.tight_layout()
    plt.show()


# === Step 5: Bar Chart — Agile Frameworks Used ===
agile_col = 'Which Agile framework(s) does your organization follow?'
if agile_col in df.columns:
    frameworks = df[agile_col].dropna().str.split(',').explode().str.strip()
    counts = frameworks.value_counts().sort_values(ascending=True)  # Ascending for horizontal bars
    
    plt.figure(figsize=(10, 6))
    bars = plt.barh(counts.index, counts.values, color='skyblue')
    
    plt.title('Agile Frameworks Used')
    plt.xlabel('Mentions')
    plt.ylabel('Agile Framework')
    
    # Add data labels on bars
    for bar in bars:
        width = bar.get_width()
        plt.text(width + 0.3, bar.get_y() + bar.get_height()/2, str(width), va='center')
    
    plt.tight_layout()
    plt.show()


# === Step 6: Bar Chart — AI Technologies in Use ===
ai_tech_col = 'Which AI technologies are used in your company?'
if ai_tech_col in df.columns:
    ai_tech = df[ai_tech_col].dropna().str.split(',').explode().str.strip()
    counts = ai_tech.value_counts().sort_values(ascending=True)  # Sort ascending for horizontal bar chart
    
    plt.figure(figsize=(10, 6))
    bars = plt.barh(counts.index, counts.values, color='mediumseagreen')
    
    plt.title('AI Technologies in Use')
    plt.xlabel('Mentions')
    plt.ylabel('AI Technology')
    
    # Add data labels
    for bar in bars:
        width = bar.get_width()
        plt.text(width + 0.5, bar.get_y() + bar.get_height()/2, str(width), va='center')
    
    plt.tight_layout()
    plt.show()


# === Step 7: Word Clouds for Open-ended Responses ===
def plot_wordcloud(series, title):
    text = ' '.join(series.dropna().astype(str))
    if not text.strip():
        print(f"⚠️ No data to generate word cloud: {title}")
        return
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title, fontsize=14)
    plt.tight_layout()
    plt.show()

benefit_col = 'In your opinion, what is the greatest benefit of using AI in strategy development?'
if benefit_col in df.columns:
    plot_wordcloud(df[benefit_col], 'Greatest Benefit of AI in Strategy Development')

challenges_col = 'Have you encountered any challenges when implementing AI into your Agile processes? Please describe.'
if challenges_col in df.columns:
    plot_wordcloud(df[challenges_col], 'Challenges in Implementing AI into Agile')

# === Step 8: Cross-tab — AI Usage vs. Company Age ===
if ai_usage_col in df.columns and age_col in df.columns:
    crosstab = pd.crosstab(df[age_col], df[ai_usage_col])
    crosstab.plot(kind='bar', stacked=True, colormap='viridis')
    plt.title('AI Usage Level vs. Company Age')
    plt.xlabel('Company Age')
    plt.ylabel('Number of Companies')
    plt.legend(title='AI Usage Level')
    plt.tight_layout()
    plt.show()

# === Step 9: Cross-tab — Agile Use vs. Company Size ===
company_size_col = 'What is the size of your company?'
if agile_col in df.columns and company_size_col in df.columns:
    agile_use_flag = df[agile_col].apply(
        lambda x: 'Yes' if pd.notna(x) and 'don’t use' not in str(x).lower() else 'No'
    )
    crosstab2 = pd.crosstab(df[company_size_col], agile_use_flag)
    crosstab2.plot(kind='bar', stacked=True, colormap='Set2')
    plt.title('Agile Use vs. Company Size')
    plt.xlabel('Company Size')
    plt.ylabel('Number of Companies')
    plt.legend(title='Uses Agile')
    plt.tight_layout()
    plt.show()

# === Final Step: Hold Terminal Open ===
input("📊 Press Enter to exit...")

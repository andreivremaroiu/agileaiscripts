import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df_cleaned = pd.read_csv("ai_agile_strategy_cleaned.csv")

sns.set_theme(style="whitegrid")

def plot_bar(column, title, xlabel, rotation=45):
    plt.figure(figsize=(8, 5))
    df_cleaned[column].value_counts().sort_values(ascending=False).plot(kind='bar')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel("Count")
    plt.xticks(rotation=rotation)
    plt.tight_layout()
    plt.show()

def plot_hist(column, title, xlabel):
    plt.figure(figsize=(7, 4))
    sns.histplot(df_cleaned[column].dropna(), bins=5, kde=True)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

plot_bar("role", "Distribution of Roles", "Role")
plot_bar("company_size", "Company Sizes of Respondents", "Company Size")
plot_bar("company_age", "Company Age Distribution", "Years in Operation")

plot_hist("ai_use_extent", "Extent of AI Use in Strategic Planning", "AI Use (1=Low, 5=High)")
plot_hist("ai_improves_decision", "AI Improves Strategic Decisions", "Agreement Scale (1–5)")

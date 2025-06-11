import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('ai_agile_strategy_cleaned.csv')
sns.set(style="whitegrid")

plt.figure(figsize=(7, 4))
sns.histplot(df['agile_enables_adaptability'].dropna(), bins=5, kde=True)
plt.title("Agile Enables Organizational Adaptability")
plt.xlabel("Agreement Scale (1–5)")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

plt.figure(figsize=(7, 4))
sns.histplot(df['ai_disruption_response'].dropna(), bins=5, kde=True)
plt.title("AI Helps Respond to Unexpected Disruptions")
plt.xlabel("Agreement Scale (1–5)")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

plt.figure(figsize=(7, 4))
sns.histplot(df['ai_enables_fast_adjustment'].dropna(), bins=5, kde=True)
plt.title("AI Enables Fast Strategic Adjustments")
plt.xlabel("Agreement Scale (1–5)")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

plt.figure(figsize=(7, 4))
sns.histplot(df['ai_agile_improves_adaptability'].dropna(), bins=5, kde=True)
plt.title("AI + Agile Improves Business Adaptability")
plt.xlabel("Agreement Scale (1–5)")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('ai_agile_strategy_cleaned.csv')
sns.set(style="whitegrid")

plt.figure(figsize=(8, 5))
df['agile_frameworks'].value_counts().sort_values(ascending=False).plot(kind='bar')
plt.title("Agile Frameworks in Use")
plt.xlabel("Agile Frameworks")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(7, 4))
sns.histplot(df['agile_ceremony_frequency'].dropna(), bins=5, kde=True)
plt.title("Frequency of Agile Ceremonies")
plt.xlabel("Frequency (1 = Never, 5 = Very Regularly)")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

plt.figure(figsize=(7, 4))
sns.histplot(df['agile_in_strategy'].dropna(), bins=5, kde=True)
plt.title("Agile Practices Embedded in Strategy")
plt.xlabel("Agreement Scale (1–5)")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

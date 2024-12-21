import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# File path to the dataset
File_Path = r"C:\Users\Admin\Desktop\EXCEL PROJECT\realistic_e_commerce_sales_data.csv"
df = pd.read_csv(File_Path)

# Display basic information about the dataset
print(df.head())
print(df.info())
print(df.describe())

# Set the style for all plots
sns.set(style="whitegrid")

# 1. Count Plot of Product Name (Top 5 Products)
top_products = df['Product Name'].value_counts().nlargest(5).index
df_top_products = df[df['Product Name'].isin(top_products)]

plt.figure(figsize=(10, 6))
ax = sns.countplot(x="Product Name", data=df_top_products, palette="viridis")
ax.bar_label(ax.containers[0])
plt.title("Count Of Top 5 Products", fontsize=14, fontweight='bold')
plt.xlabel("Product Name", fontsize=12)
plt.ylabel("Count", fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# 2. Pie Chart of Shipping Status (Compact)
gb = df.groupby("Shipping Status").agg({"Shipping Status": "count"})
plt.figure(figsize=(6, 6))
plt.pie(gb["Shipping Status"], labels=gb.index, autopct="%1.2f%%", startangle=140, colors=sns.color_palette("viridis"))
plt.title("Product Shipping Status", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# 3. Count Plot of Gender by Product Name (Top 5 Products)
plt.figure(figsize=(10, 6))
sns.countplot(x="Gender", data=df_top_products, hue="Product Name", palette="viridis")
plt.title("Count of Gender by Top 5 Products", fontsize=14, fontweight='bold')
plt.xlabel("Gender", fontsize=12)
plt.ylabel("Count", fontsize=12)
plt.legend(title="Product Name", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()


# 4.Histogram of Shipping Fee by Product Name (Top 5 Products)
plt.figure(figsize=(16, 8))
sns.histplot(x="Shipping Fee", data=df_top_products, bins=30, hue="Product Name", multiple="stack", palette="viridis")
plt.title("Shipping Fee By Top 5 Products", fontsize=16, fontweight='bold')
plt.xlabel("Shipping Fee", fontsize=14)
plt.ylabel("Frequency", fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(title="Product Name", bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=12, title_fontsize='13')
plt.tight_layout()
plt.show()


# 5. Count Plot of Product Category by Quantity (Top 5 Products)
plt.figure(figsize=(10, 6))
ax = sns.countplot(x="Category", data=df_top_products, hue="Quantity", palette="viridis")
ax.bar_label(ax.containers[0])
plt.title("Count Of Products Category (Top 5 Products)", fontsize=14, fontweight='bold')
plt.xlabel("Category", fontsize=12)
plt.ylabel("Count", fontsize=12)
plt.legend(title="Quantity", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# 6. Bar Plot of Total Price by Product Name (Top 5 Products)
plt.figure(figsize=(10, 6))
ax = sns.barplot(x='Product Name', y='Total Price', data=df_top_products, palette="viridis")
# Adding annotations for each bar
for i in ax.containers:
    ax.bar_label(i, label_type="edge", fontsize=10, weight='bold', color='red')
# Setting the title and labels
plt.title("Total Price By Top 5 Products", fontsize=14, fontweight='bold')
plt.xlabel("Product Name", fontsize=12)
plt.ylabel("Total Price", fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

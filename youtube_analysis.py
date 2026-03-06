import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# load dataset
data = pd.read_csv("USvideos.csv")

# style
plt.style.use("dark_background")
sns.set_style("darkgrid")

# figure
fig = plt.figure(figsize=(18,10))

# MAIN HEADING
fig.suptitle(
    "YouTube Trending Video Analysis Dashboard",
    fontsize=24,
    color="white",
    fontweight="bold"
)

# SUB HEADING
plt.figtext(
    0.5, 0.92,
    "Insights from US Trending Dataset (Views • Likes • Categories • Channels)",
    ha="center",
    fontsize=14,
    color="Black"
)

# 1️⃣ Category Distribution
plt.subplot(2,3,1)
sns.countplot(x="category_id", data=data, palette="viridis")
plt.title("Video Category Distribution")
plt.xticks(rotation=45)

# 2️⃣ Views vs Likes
plt.subplot(2,3,2)
sns.scatterplot(x="views", y="likes", data=data, alpha=0.6, color="cyan")
plt.title("Views vs Likes")

# 3️⃣ Likes vs Dislikes
plt.subplot(2,3,3)
sns.scatterplot(x="likes", y="dislikes", data=data, alpha=0.6, color="orange")
plt.title("Likes vs Dislikes")

# 4️⃣ Pie Chart
plt.subplot(2,3,4)
top_categories = data["category_id"].value_counts().head(6)
plt.pie(
    top_categories,
    labels=top_categories.index,
    autopct="%1.1f%%",
    startangle=140
)
plt.title("Top Video Categories Share")

# 5️⃣ Correlation Heatmap
plt.subplot(2,3,5)
sns.heatmap(
    data[["views","likes","dislikes","comment_count"]].corr(),
    annot=True,
    cmap="coolwarm"
)
plt.title("Correlation Heatmap")

# 6️⃣ Top Channels
plt.subplot(2,3,6)
top_channels = data["channel_title"].value_counts().head(10)
sns.barplot(x=top_channels.values, y=top_channels.index, palette="magma")
plt.title("Top 10 Channels with Most Trending Videos")

plt.tight_layout(rect=[0,0,1,0.9])

plt.show()

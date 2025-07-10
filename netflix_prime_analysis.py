import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud

netflix = pd.read_csv("netflix_titles.csv")
prime = pd.read_csv("amazon_prime_titles.csv")

netflix["platform"] = "Netflix"
prime["platform"] = "Prime"

data = pd.concat([netflix, prime], ignore_index=True)

data["rating"] = data["rating"].fillna("Unknown")
data["duration"] = data["duration"].fillna("Unknown")
data["listed_in"] = data["listed_in"].fillna("Unknown")

sns.countplot(x="platform", data=data)
plt.title("Total Titles by Platform")
plt.show()

genres = data["listed_in"].str.split(", ", expand=True).stack()
top_genres = genres.value_counts().head(10)

sns.barplot(x=top_genres.values, y=top_genres.index)
plt.title("Top 10 Genres")
plt.xlabel("Count")
plt.ylabel("Genre")
plt.show()

text = " ".join(data["description"].dropna())
wordcloud = WordCloud(width=1000, height=500, background_color="black").generate(text)

plt.figure(figsize=(12,6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Most Common Words in Descriptions")
plt.show()

top_ratings = data["rating"].value_counts().nlargest(10).index
filtered = data[data["rating"].isin(top_ratings)]

sns.countplot(x="rating", hue="platform", data=filtered, order=top_ratings)
plt.title("Top Ratings per Platform")
plt.xticks(rotation=45)
plt.show()

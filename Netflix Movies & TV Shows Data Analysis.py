import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("netflix_titles.csv")

df.head()

df.shape

df.info()

df.describe()

df.isnull().sum()

df.duplicated().sum()

df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

df["year_added"] = df["date_added"].dt.year

content_type = df["type"].value_counts()

print(content_type)

country_count = df["country"].value_counts().head(10)

print(country_count)

release_year = df["release_year"].value_counts().sort_index()

print(release_year)

rating_count = df["rating"].value_counts()

print(rating_count)

top_directors = df["director"].value_counts().head(10)

print(top_directors)

movie_count = len(df[df["type"] == "Movie"])

tv_show_count = len(df[df["type"] == "TV Show"])

print("Movies:", movie_count)

print("TV Shows:", tv_show_count)

print("Total Titles:", len(df))

print("Most Common Content Type:", content_type.idxmax())

print("Most Common Rating:", rating_count.idxmax())

print("Most Common Release Year:", release_year.idxmax())

content_type.plot(
    kind="bar",
    figsize=(8, 5)
)

plt.title("Movies vs TV Shows")
plt.xlabel("Content Type")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.show()

country_count.plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Top 10 Countries by Netflix Titles")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

release_year.tail(20).plot(
    figsize=(12, 6)
)

plt.title("Netflix Titles by Release Year")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.show()

rating_count.plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Netflix Content Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

year_added_count = df["year_added"].value_counts().sort_index()

year_added_count.plot(
    figsize=(10, 6)
)

plt.title("Netflix Titles Added by Year")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.show()

top_directors.plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Top 10 Directors")
plt.xlabel("Director")
plt.ylabel("Number of Titles")
plt.xticks(rotation=75)
plt.tight_layout()
plt.show()

print("Total Titles:", len(df))

print("Total Movies:", movie_count)

print("Total TV Shows:", tv_show_count)

print("Top Country:", country_count.idxmax())

print("Most Common Rating:", rating_count.idxmax())

print("Most Common Release Year:", release_year.idxmax())

print("Top Director:", top_directors.idxmax())
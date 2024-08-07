import pandas as pd

url = 'https://github.com/pullz6/Anime_Recommendor/blob/main/Input/anime-dataset-2023.csv?raw=true'
df = pd.read_csv(url, index_col=0)

print(df.info())
import pandas as pd
from scipy.spatial import distance
from sentence_transformers import SentenceTransformer
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import os
import pandas as pd
import re

url = 'https://github.com/pullz6/Anime_Recommendor/blob/main/Input/anime-dataset-2023.csv?raw=true'
df_new = pd.read_csv(url, index_col=0)

#Importing universal sentence encoder model
module_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
model_U = hub.load(module_url)
print("module %s loaded" % module_url)

def embed(input):
    return model_U(input)

#Creating the transformer model
model_t = SentenceTransformer('all-MiniLM-L6-v2')

# Creating and prepping the corpus with all the descriptions of the dataframe for the transformer
sentences_t = df_new['Synopsis']

#Prep the corpus for the USE model
sentences = df_new['Synopsis']
sentences = np.asarray(sentences)
sentences_u = np.expand_dims(sentences, axis=1)

#Input
test = "titans attacking through the wall, there is an army of soliders, eren."

#Print input
print('Test sentence:',test)

#Prep input for the transformer model
test_vec_t = model_t.encode([test])[0]

#Prep input for the USE model
test_u = []
test_u.append(test)
test_vec_u = embed(test_u)

#Creating holding arrays
similarity_anime = []
similarity_scores_t = []
similarity_scores_U = []

#Evaluating for the corpus and given input with the transformer model
i = 0
for sent in sentences_t:
    similarity_score = 1-distance.cosine(test_vec_t, model_t.encode([sent])[0])
    similarity_anime.append(df_new.iloc[i, 2])
    similarity_scores_t.append(similarity_score)
    i = i + 1

#Evaluating for the corpus and given input with the USE model
i = 0
for sent in sentences_u:
    similarity_score = 1-distance.cosine(test_vec_u[0,:],embed(sent)[0,:])
    #print(f'\nFor {sent}\nSimilarity Score = {similarity_score} ')
    similarity_scores_U.append(similarity_score)
    i = i +1

#Creating the dataframe to be returned with the recommendation
final_df = pd.DataFrame()
final_df['Recommended_anime'] = similarity_anime
final_df['Recommended_score_T'] = similarity_scores_t
final_df['Recommended_score_U'] = similarity_scores_U
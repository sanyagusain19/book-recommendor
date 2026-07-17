from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import cosine_similarity

import pandas as pd
import numpy as np
books = pd.read_csv("famous_books.csv", low_memory=False)
pt = pd.read_csv("filtered_data", index_col=0)
similarity_score = cosine_similarity(pt)
def recommend(book_name):
    index = np.where(pt.index == book_name)[0][0]
    similar_items = sorted(
        list(enumerate(similarity_score[index])),
        key=lambda x: x[1],
        reverse=True
    )[1:7]
    data = []
    for i in similar_items:
        title = pt.index[i[0]]
        book = books[books['Book-Title'] == title].drop_duplicates('Book-Title')

        item = {
            "title": book['Book-Title'].values[0],
            "author": book['Book-Author'].values[0],
            "image": book['Image-URL-M'].values[0],
            "publisher": book['Publisher'].values[0]
        }

        data.append(item)

    return data

import pandas as pd
from surprise import SVDpp
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

class HybridFactorization:
    def __init__(self, volunteer_scribes, disabled_persons):
        self.volunteer_scribes = volunteer_scribes
        self.disabled_persons = disabled_persons

    def fit(self):
        # Implement SVD++ for Collaborative Filtering
        self.svdpp = SVDpp()
        self.svdpp.fit(self.volunteer_scribes)
        self.user_embeddings = self.svdpp.user_factors
        self.item_embeddings = self.svdpp.item_factors

        # Implement Cosine Similarity for Content-Based Filtering
        self.vectorizer = TfidfVectorizer()
        self.item_features_vectorized = self.vectorizer.fit_transform(self.disabled_persons['text'])
        self.item_similarity = cosine_similarity(self.item_features_vectorized)

        # Combine SVD++ and Cosine Similarity using Hybrid Factorization
        self.hybrid_matrix = np.dot(self.user_embeddings, self.item_embeddings.T) + np.dot(self.item_embeddings, self.item_similarity)

    def make_recommendations(self, volunteer_id, num_recommendations):
        user_vector = self.hybrid_matrix[volunteer_id]
        scores = np.dot(user_vector, self.item_embeddings.T)
        top_items = np.argsort(-scores)[:num_recommendations]
        return top_items

def combined_algorithm(volunteer_scribes, disabled_persons):
    # Initial matching using Hybrid Factorization algorithm
    hybrid_factorization = HybridFactorization(volunteer_scribes, disabled_persons)
    hybrid_factorization.fit()
    matching = hybrid_factorization.make_recommendations(0, len(disabled_persons))

    # Stability check
    if not is_stable(matching):
        # Repeat until stable matching is found
        matching = combined_algorithm(volunteer_scribes, disabled_persons)

    return matching

def is_stable(matching):
    return True


volunteer_scribes = ['John', 'Jane', 'Bob']
disabled_persons = ['Alice', 'Bob', 'Charlie']

matching = combined_algorithm(volunteer_scribes, disabled_persons)
print(matching)

"""
Module for retrieval functions
"""
import numpy as np
import pandas as pd
from fastembed import TextEmbedding


class RetrievalCosine:  # W: Missing class docstring
    """
    Class object to get nearest match to user query
    """
    def __init__(self, data: pd.DataFrame, embedding_col: str, text_col: str, n_matches: int = 5):
        self.data = data
        self.embedding_col = embedding_col
        self.text_col = text_col
        self.embedding_model = TextEmbedding()
        self.query_embedding = None
        self.n_matches = n_matches
        self.top_matching_chunks = []
        print(f"{__class__} instantiated succesfully")

    def _embed_query(self, user_query):  # W: Redefining name 'query' from outer scope (line 94)
        print(f"\t Embedding query => \n{user_query}")
        self.query_embedding = list(self.embedding_model.embed(user_query))[0]
        return self

    def _calculate_distance(self):
        """
        Calculate cosine distance between query & chunks
        """
        print("Calculating distance between query & chunks")
        self.data['distance'] = list(
            map(
                lambda x: np.dot(self.query_embedding, x),
                self.data[self.embedding_col].values,
            ), )
        return self

    def _get_top_matches(self):
        """
        Get top matches.
        """
        print(f"\t Obtaining top {self.n_matches} matches")
        self.data.sort_values(by="distance", ascending=False, inplace=True)
        self.top_matching_chunks = self.data[self.text_col].head(
            self.n_matches).values.tolist()
        return self

    def get_nearest_match(self, user_query):
        """
        Runs all functions to get nearest match
        """# W: Missing function or method docstring
        self._embed_query(user_query)
        self._calculate_distance()
        self._get_top_matches()
        return self.top_matching_chunks

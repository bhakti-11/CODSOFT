import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Sample book data
data = {
    'Title': ['Book 1', 'Book 2', 'Book 3', 'Book 4'],
    'Author': ['Author A', 'Author B', 'Author A', 'Author C'],
    'Genre': ['Fiction', 'Mystery', 'Fiction', 'Non-Fiction'],
    'Description': [
        'A gripping novel about...',
        'A thrilling mystery set in...',
        'An emotional journey through...',
        'A non-fiction book on...'
    ]
}

df = pd.DataFrame(data)

# Create a TF-IDF vectorizer to convert descriptions into numerical form
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(df['Description'])

# Calculate cosine similarity between descriptions
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Define a function to get book recommendations based on user preferences
def get_recommendations(title, cosine_sim=cosine_sim):
    # Get the index of the book that matches the title
    idx = df[df['Title'] == title].index[0]

    # Get the pairwsie similarity scores of all books with that book
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the books based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the top 5 most similar books
    sim_scores = sim_scores[1:6]

    # Get the book indices
    book_indices = [i[0] for i in sim_scores]

    # Return the top 5 most similar books
    return df['Title'].iloc[book_indices]

# Example: Recommend books similar to 'Book 1'
recommended_books = get_recommendations('Book 1')
print("Recommended Books for 'Book 1':")
print(recommended_books)

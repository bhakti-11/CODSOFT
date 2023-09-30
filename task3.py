import pandas as pd

# Sample user-item ratings dataset
data = {
    'User': ['User1', 'User2', 'User3', 'User4', 'User5'],
    'Item1': [5, 4, 0, 0, 3],
    'Item2': [0, 5, 4, 3, 0],
    'Item3': [2, 0, 5, 4, 0],
    'Item4': [0, 0, 0, 0, 5],
    'Item5': [4, 0, 3, 5, 4]
}

# Create a DataFrame from the dataset
df = pd.DataFrame(data)

# Function to get recommendations for a user
def get_recommendations(user, df):
    # Select the user's ratings
    user_ratings = df[df['User'] == user].iloc[:, 1:]

    # Calculate the mean ratings of other users
    mean_ratings = df.drop(user, axis=0).mean()

    # Calculate the weighted average of item ratings based on user's ratings and mean ratings
    user_recommendations = (user_ratings * mean_ratings).sum() / mean_ratings.sum()

    # Sort recommendations in descending order
    user_recommendations = user_recommendations.sort_values(ascending=False)

    # Filter out items the user has already rated
    user_recommendations = user_recommendations[user_ratings.iloc[0] == 0]

    return user_recommendations

# Get recommendations for a specific user (e.g., 'User1')
user = 'User1'
recommendations = get_recommendations(user, df)

# Display recommended items for the user
print(f'Recommended items for {user}:')
print(recommendations)

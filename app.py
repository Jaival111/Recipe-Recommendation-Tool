import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = pd.read_csv('indian_food_cleaned.csv')
df = pd.read_csv('vector_data.csv')

ingredients_set = []
for i in list(data['ingredients']):
    low = [j.lower() for j in i.split(', ')]
    ingredients_set.extend(low)
ingredients_set = set(ingredients_set)

cv = CountVectorizer()
ingredients_matrix = cv.fit_transform(df['ingredients']).toarray()

def recommend(user_ingredients):
    user_ingredients = ' '.join([ingredient.lower().strip() for ingredient in user_ingredients])
    user_ingredients_matrix = cv.transform([user_ingredients])
    similarity = cosine_similarity(user_ingredients_matrix, ingredients_matrix).flatten()
    top_indices = similarity.argsort()[-5:][::-1]
    recommendations = data.iloc[top_indices].copy()
    return recommendations[['name', 'ingredients', 'diet', 'prep_time', 'cook_time']]

st.title('Indian Food Recommendation Tool')
user_ingredients = st.multiselect('What do you have?', ingredients_set)
left, right = st.columns(2)
btn = left.button('Recommend', type='primary')

if btn:
    recommended_data = recommend(user_ingredients)
    st.dataframe(recommended_data, hide_index=True)

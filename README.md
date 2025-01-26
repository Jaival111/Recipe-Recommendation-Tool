# Recipe Recommendation Tool

This project is a Python-based tool that recommends recipes based on the ingredients provided by the user. It uses cosine similarity to match user-provided ingredients with the recipes in a dataset of Indian dishes.

## Features
- Accepts a list of user-provided ingredients.
- Recommends the top N recipes based on ingredient similarity.
- Provides detailed recipe information, including:
  - Name
  - Ingredients
  - Diet (vegetarian or non-vegetarian)
  - Preparation and cooking times

## Dataset
The tool uses an Indian food dataset containing 255 recipes with the following columns:
- `name`: The name of the recipe.
- `ingredients`: Ingredients used in the recipe.
- `diet`: Indicates whether the recipe is vegetarian or non-vegetarian.
- `prep_time`: Preparation time in minutes.
- `cook_time`: Cooking time in minutes.
- `flavor_profile`: The flavor profile of the dish (e.g., sweet, spicy).
- `course`: The course of the dish (e.g., dessert, main course).
- `state`: The Indian state where the dish originated.
- `region`: The region of India associated with the dish.

## Dependencies
- Python 3.x
- pandas
- scikit-learn
- nltk
- streamlit

## Usage
1. Clone the repository and navigate to the project directory.
2. Ensure the dataset file (`indian_food.csv`) is in the same directory as the script.
3. Run the Python script:

## Implementation Details
1. **Preprocessing**:
   - Ingredients are normalized (converted to lowercase and cleaned of extra spaces).
   - Missing values in preparation and cooking times are replaced with `'-'`.

2. **Vectorization**:
   - The `ingredients` column is transformed into a vector space using `CountVectorizer`.

3. **Similarity Calculation**:
   - Cosine similarity is calculated between the user-provided ingredients and the dataset recipes.

4. **Recommendation**:
   - Recipes are ranked based on similarity, and the top N recipes are returned.

## Limitations
- The recommendations are based solely on ingredient matching, which may not account for cooking methods or specific user tastes.
- The dataset is limited to Indian recipes and may not support global cuisines.

## Website
- You can access the project and explore it online [here](https://recipe-recommendation-tool.onrender.com).

## Acknowledgements
- The dataset used in this project was sourced from [Kaggle](https://www.kaggle.com/datasets/nehaprabhavalkar/indian-food-101).

## Future Enhancements
- Add user filtering options for diet, region, and flavor profiles.
- Extend the dataset to include recipes from other cuisines.

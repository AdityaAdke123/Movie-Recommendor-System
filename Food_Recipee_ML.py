# Adding grams for each ingredient, adjusting calories per serving, and including food type (Vegetarian, Non-Vegetarian, Vegan)
import pandas as pd
def main():

    data={
        "Ingredients": [
                           "Spaghetti (100g), ground beef (150g), tomatoes (100g), garlic (10g), onions (50g)",
                           "Chicken (150g), curry powder (10g), coconut milk (100g), onions (50g)",
                           "Salmon (150g), olive oil (20g), lemon (50g), garlic (10g)",
                           "Broccoli (100g), carrots (100g), bell peppers (50g), soy sauce (20g)",
                           "Ground beef (150g), taco shells (50g), lettuce (50g), cheese (50g)",
                           "Romaine lettuce (100g), Caesar dressing (50g), croutons (30g), parmesan (20g)",
                           "Lentils (150g), carrots (50g), onions (50g), vegetable broth (200g)",
                           "Pizza dough (100g), mozzarella (100g), tomatoes (50g), basil (10g)",
                           "Greek yogurt (150g), granola (50g), berries (50g)",
                           "Vegan patty (150g), lettuce (50g), tomato (50g), vegan bun (100g)",
                           # More ingredients with grams for the other recipes
                           "Mushrooms (100g), arborio rice (150g), parmesan (20g), white wine (50g)",
                           "Flour (100g), milk (150ml), eggs (2), butter (20g)",
                           "Chicken (150g), lettuce (50g), Caesar dressing (30g), tortilla (1)",
                           "Quinoa (100g), cucumbers (50g), tomatoes (50g), feta (50g)",
                           "Beef (150g), sour cream (50g), mushrooms (100g), onions (50g)",
                           "Mixed vegetables (150g), curry powder (10g), coconut milk (100g)",
                           "White fish (150g), potatoes (200g), tartar sauce (50g)",
                           "Chickpeas (150g), spinach (50g), onions (50g), garlic (10g)",
                           "Tomatoes (100g), basil (20g), cream (50g)",
                           "Tofu (150g), broccoli (100g), soy sauce (20g)",
                           # More ingredients for the other 50 recipes
                           "Avocado (100g), bread (50g), olive oil (20g)",
                           "Eggplant (150g), marinara sauce (100g), mozzarella (50g)",
                           "Chicken (150g), fettuccine (100g), Alfredo sauce (100g)",
                           "Shrimp (150g), garlic (10g), butter (20g), pasta (100g)",
                           "Clams (150g), potatoes (100g), cream (50g)",
                           "Falafel (150g), pita bread (100g), tahini sauce (50g)",
                           "Beetroot (150g), goat cheese (50g), walnuts (30g)",
                           "Turkey (150g), lettuce (50g), tomato (50g), sandwich bread (100g)",
                           "Flour (100g), cocoa powder (30g), sugar (50g), eggs (2)",
                           "Berries (150g), yogurt (150g), honey (20g)"
                       ] * 5,

        "Calories": [
                        450, 400, 300, 250, 350, 300, 200, 350, 150, 200,
                        # More calories per serving
                        350, 250, 300, 250, 450, 350, 500, 200, 150, 250,
                        120, 300, 500, 350, 400, 250, 200, 300, 500, 150
                    ] * 5,

        "Food_Type": [
                         "Non-Vegetarian", "Non-Vegetarian", "Non-Vegetarian", "Vegetarian", "Non-Vegetarian",
                         "Vegetarian", "Vegetarian", "Vegetarian", "Vegetarian", "Vegan",
                         # More food types
                         "Vegetarian", "Vegetarian", "Non-Vegetarian", "Vegetarian", "Non-Vegetarian",
                         "Vegetarian", "Non-Vegetarian", "Vegetarian", "Vegetarian", "Vegan",
                         "Vegetarian", "Vegetarian", "Non-Vegetarian", "Non-Vegetarian", "Non-Vegetarian",
                         "Vegan", "Vegetarian", "Non-Vegetarian", "Vegetarian", "Vegetarian"
                     ] * 5
    }

    # Updating the DataFrame
    df = pd.DataFrame(data)
    print(df.head())
if __name__ == '__main__':
    main()
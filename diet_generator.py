"""
Diet Plan Generator Functions
"""

def calculate_bmr(weight, height, age, gender):
    """
    Calculate Basal Metabolic Rate using the Mifflin-St Jeor Equation
    
    Parameters:
    weight (float): Weight in kg
    height (float): Height in cm
    age (int): Age in years
    gender (str): 'male' or 'female'
    
    Returns:
    float: BMR value
    """
    if gender.lower() == 'male':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:  # female
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    
    return bmr

def adjust_calories(bmr, fitness_goal):
    """
    Adjust calories based on fitness goal
    
    Parameters:
    bmr (float): Basal Metabolic Rate
    fitness_goal (str): 'Lose Weight', 'Maintain Weight', or 'Gain Muscle'
    
    Returns:
    float: Adjusted calories
    """
    if fitness_goal == 'Lose Weight':
        return bmr - 500
    elif fitness_goal == 'Maintain Weight':
        return bmr
    elif fitness_goal == 'Gain Muscle':
        return bmr + 300
    else:
        raise ValueError(f"Invalid fitness goal: {fitness_goal}")

def generate_diet_plan(total_calories):
    """
    Generate a simple daily diet plan based on total calories
    
    Parameters:
    total_calories (float): Total daily calories
    
    Returns:
    dict: Diet plan with meals and calorie distributions
    """
    # Determine number of meals based on calorie intake
    if total_calories < 1500:
        num_meals = 3  # Breakfast, lunch, dinner
    elif total_calories < 2000:
        num_meals = 4  # Add afternoon snack
    else:
        num_meals = 5  # Add morning and afternoon snacks
    
    # Default distribution for 3 meals
    meal_distribution = {
        'Breakfast': 0.25,
        'Lunch': 0.40,
        'Dinner': 0.35
    }
    
    # Adjust distribution for more meals
    if num_meals >= 4:
        meal_distribution = {
            'Breakfast': 0.25,
            'Morning Snack': 0.10,
            'Lunch': 0.30,
            'Dinner': 0.35
        }
    
    if num_meals >= 5:
        meal_distribution = {
            'Breakfast': 0.20,
            'Morning Snack': 0.10,
            'Lunch': 0.30,
            'Afternoon Snack': 0.10,
            'Dinner': 0.30
        }
    
    # Calculate calories for each meal
    meal_calories = {}
    for meal, percentage in meal_distribution.items():
        meal_calories[meal] = round(total_calories * percentage)
    
    # Generate meal suggestions based on calorie allocations
    meal_suggestions = {}
    
    # Breakfast suggestions
    breakfast_calories = meal_calories.get('Breakfast', 0)
    if breakfast_calories < 300:
        meal_suggestions['Breakfast'] = "Greek yogurt with berries and a sprinkle of granola"
    elif breakfast_calories < 400:
        meal_suggestions['Breakfast'] = "Oatmeal with banana, cinnamon, and a tablespoon of peanut butter"
    else:
        meal_suggestions['Breakfast'] = "2 eggs with whole grain toast, avocado, and a side of fruit"
    
    # Morning Snack suggestions
    if 'Morning Snack' in meal_calories:
        snack_calories = meal_calories['Morning Snack']
        if snack_calories < 150:
            meal_suggestions['Morning Snack'] = "Apple with a small handful of almonds"
        else:
            meal_suggestions['Morning Snack'] = "Protein smoothie with berries and a scoop of protein powder"
    
    # Lunch suggestions
    lunch_calories = meal_calories.get('Lunch', 0)
    if lunch_calories < 400:
        meal_suggestions['Lunch'] = "Salad with grilled chicken, mixed vegetables, and light dressing"
    elif lunch_calories < 600:
        meal_suggestions['Lunch'] = "Turkey and avocado wrap with a side of vegetables"
    else:
        meal_suggestions['Lunch'] = "Grilled salmon with quinoa and roasted vegetables"
    
    # Afternoon Snack suggestions
    if 'Afternoon Snack' in meal_calories:
        snack_calories = meal_calories['Afternoon Snack']
        if snack_calories < 150:
            meal_suggestions['Afternoon Snack'] = "Carrot sticks with hummus"
        else:
            meal_suggestions['Afternoon Snack'] = "Greek yogurt with honey and a small handful of nuts"
    
    # Dinner suggestions
    dinner_calories = meal_calories.get('Dinner', 0)
    if dinner_calories < 400:
        meal_suggestions['Dinner'] = "Baked chicken breast with steamed vegetables"
    elif dinner_calories < 600:
        meal_suggestions['Dinner'] = "Lean steak with sweet potato and green beans"
    else:
        meal_suggestions['Dinner'] = "Grilled fish with brown rice, avocado, and a side salad"
    
    # Create the final diet plan
    diet_plan = {
        'total_calories': round(total_calories),
        'num_meals': num_meals,
        'meal_calories': meal_calories,
        'meal_suggestions': meal_suggestions
    }
    
    return diet_plan

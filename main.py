
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate

df = pd.read_csv('diet_data.csv')

def recommend_daily_diet(min_calories=1800):
    daily_plan = {}
    total_nutrients = {'Calories': 0, 'Protein (g)': 0, 'Carbs (g)': 0, 'Fiber (g)': 0}

    for meal_type in ['Breakfast', 'Lunch', 'Dinner', 'Snack']:
        meals = df[df['MealType'] == meal_type]
        if meals.empty:
            continue
        selected_meal = meals.sample(1).iloc[0]
        quantity = selected_meal['Quantity']
        meal_data = {
            'MealName': selected_meal['MealName'],
            'Quantity': quantity,
            'Calories': selected_meal['Calories'],
            'Protein (g)': selected_meal['Protein (g)'],
            'Carbs (g)': selected_meal['Carbs (g)'],
            'Fiber (g)': selected_meal['Fiber (g)']
        }
        daily_plan[meal_type] = meal_data
        for key in total_nutrients:
            total_nutrients[key] += meal_data[key]

    return daily_plan, total_nutrients

def print_diet_plan(diet_plan, day, total_nutrients):
    print(f"\n--- Day {day} Diet Plan ---")
    table = []
    for meal_time, meal in diet_plan.items():
        table.append([
            meal_time,
            meal['MealName'],
            meal['Quantity'],
            meal['Calories'],
            meal['Protein (g)'],
            meal['Carbs (g)'],
            meal['Fiber (g)']
        ])
    table.append(['Total', '', '', total_nutrients['Calories'], total_nutrients['Protein (g)'],
                  total_nutrients['Carbs (g)'], total_nutrients['Fiber (g)']])
    print(tabulate(table, headers=['Meal Time', 'Meal', 'Qty', 'Calories', 'Protein (g)', 'Carbs (g)', 'Fiber (g)'], tablefmt='grid'))

def plot_tracker(log, title, ylabel, color):
    days = list(log.keys())
    values = list(log.values())
    plt.figure(figsize=(8, 4))
    plt.plot(days, values, marker='o', linestyle='-', color=color)
    plt.title(title)
    plt.xlabel('Day')
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    num_days = int(input("Enter number of days to track diet: "))
    sugar_log, calorie_log, protein_log, carbs_log, fiber_log = {}, {}, {}, {}, {}

    for day in range(1, num_days + 1):
        print(f"\n--- Day {day} ---")
        sugar_level = float(input("Enter your sugar level: "))
        sugar_log[day] = sugar_level

        diet_plan, nutrients = recommend_daily_diet()
        print_diet_plan(diet_plan, day, nutrients)

        calorie_log[day] = nutrients['Calories']
        protein_log[day] = nutrients['Protein (g)']
        carbs_log[day] = nutrients['Carbs (g)']
        fiber_log[day] = nutrients['Fiber (g)']

    plot_tracker(sugar_log, 'Sugar Level Over Days', 'Sugar Level (mg/dL)', 'red')
    plot_tracker(calorie_log, 'Calories Intake', 'Calories', 'blue')
    plot_tracker(protein_log, 'Protein Intake', 'Protein (g)', 'green')
    plot_tracker(carbs_log, 'Carbohydrates Intake', 'Carbs (g)', 'orange')
    plot_tracker(fiber_log, 'Fiber Intake', 'Fiber (g)', 'purple')

    plt.figure(figsize=(8, 4))
    plt.plot(protein_log.keys(), protein_log.values(), label='Protein', marker='o')
    plt.plot(carbs_log.keys(), carbs_log.values(), label='Carbs', marker='s')
    plt.plot(fiber_log.keys(), fiber_log.values(), label='Fiber', marker='^')
    plt.title('Nutrient Intake Over Days')
    plt.xlabel('Day')
    plt.ylabel('Grams')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()

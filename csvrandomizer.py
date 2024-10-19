import csv
import random
from datetime import datetime, timedelta

def generate_mood(sleep, stress, activity, day):
    base_mood = 5  # Start with a neutral mood
    
    # Sleep effect (more sleep -> better mood)
    sleep_effect = (sleep - 5) * 0.5
    
    # Stress effect (more stress -> worse mood)
    stress_effect = (5 - stress) * 0.4
    
    # Activity effect (more activity -> better mood, with diminishing returns)
    activity_effect = min(activity - 5, 3) * 0.3
    
    # Weekend effect (slight mood boost on weekends)
    weekend_effect = 0.5 if day in [5, 6] else 0
    
    # Random factor to add some variability
    random_factor = random.uniform(-1, 1)
    
    mood = base_mood + sleep_effect + stress_effect + activity_effect + weekend_effect + random_factor
    return max(1, min(10, round(mood, 1)))  # Ensure mood is between 1 and 10

start_date = datetime(2022, 1, 1)
data = []

for i in range(500):
    date = start_date + timedelta(days=i)
    sleep_quality = random.randint(3, 10)
    stress_level = random.randint(1, 10)
    physical_activity = random.randint(1, 10)
    day_of_week = date.weekday()
    mood = generate_mood(sleep_quality, stress_level, physical_activity, day_of_week)
    
    data.append([
        date.strftime('%Y-%m-%d'),
        sleep_quality,
        stress_level,
        physical_activity,
        day_of_week,
        mood
    ])

with open('mood_data_500_logical.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['date', 'sleep_quality', 'stress_level', 'physical_activity', 'day_of_week', 'mood'])
    writer.writerows(data)

print("CSV file 'mood_data_500_logical.csv' has been created with 500 entries.")
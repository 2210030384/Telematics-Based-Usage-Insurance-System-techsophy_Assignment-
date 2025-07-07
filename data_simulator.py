import csv
import random

def generate_data(filename="telematics.csv", records=100):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['speed', 'acceleration', 'braking', 'phone_usage'])

        # Randomize driving profile type: 0 = safe, 1 = average, 2 = risky
        behavior_type = random.choice([0, 1, 2])

        for _ in range(records):
            if behavior_type == 0:
                speed = random.uniform(20, 80)
                acceleration = random.uniform(-2, 2)
                phone_usage = random.choices([0, 1], weights=[4, 1])[0]
            elif behavior_type == 1:
                speed = random.uniform(60, 110)
                acceleration = random.uniform(-3, 3)
                phone_usage = random.choices([0, 1], weights=[2, 2])[0]
            else:  # risky driver
                speed = random.uniform(90, 130)
                acceleration = random.uniform(-5, 5)
                phone_usage = random.choices([0, 1], weights=[1, 4])[0]

            braking = 1 if acceleration < -2 else 0
            writer.writerow([speed, acceleration, braking, phone_usage])

# Run automatically when called
generate_data()

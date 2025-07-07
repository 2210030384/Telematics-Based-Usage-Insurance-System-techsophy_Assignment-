import pandas as pd

def analyze_behavior(file='telematics.csv'):
    df = pd.read_csv(file)
    df['speeding'] = df['speed'] > 100
    df['harsh_braking'] = df['acceleration'] < -3
    df['distracted'] = df['phone_usage'] == 1
    return df

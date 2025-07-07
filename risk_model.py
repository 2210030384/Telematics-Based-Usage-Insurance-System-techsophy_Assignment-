def risk_score(df):
    score = 0
    score += df['speeding'].mean() * 40
    score += df['harsh_braking'].mean() * 30
    score += df['distracted'].mean() * 30
    return round(score, 2)

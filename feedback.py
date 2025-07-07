def get_feedback(df):
    tips = []
    if df['harsh_braking'].mean() > 0.2:
        tips.append("Avoid harsh braking")
    if df['speeding'].mean() > 0.2:
        tips.append("Drive within speed limits")
    if df['distracted'].mean() > 0.1:
        tips.append("Avoid phone usage while driving")
    return tips

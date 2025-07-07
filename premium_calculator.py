def calculate_premium(base, score):
    if score > 80:
        return base * 1.4
    elif score > 50:
        return base * 1.2
    else:
        return base * 0.9

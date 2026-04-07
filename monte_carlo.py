import random

def simulate_crashes(days):
    crashes = 0
    for _ in range(days):
        if random.random() < 0.045:
            crashes += 1
    return crashes, crashes / days

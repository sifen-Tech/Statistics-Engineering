# main.py
import sys
import os

# Add src folder to path so imports work
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from stat_engine import StatEngine
from monte_carlo import simulate_crashes

def main():
    # Sample data
    data = [1000, 2000, 3000, 100000, 5000, 7000, 9000]
    stats = StatEngine(data)

    print("=== StatEngine Results ===")
    print("Mean:", stats.get_mean())
    print("Median:", stats.get_median())
    print("Mode:", stats.get_mode())
    print("Sample Variance:", stats.get_variance(is_sample=True))
    print("Population Variance:", stats.get_variance(is_sample=False))
    print("Standard Deviation:", stats.get_standard_deviation())
    print("Outliers:", stats.get_outliers())

    print("\n=== Monte Carlo Simulation of Server Crashes ===")
    for days in [30, 100, 1000, 10000]:
        crashes, prob = simulate_crashes(days)
        print(f"Days: {days} | Crashes: {crashes} | Simulated Probability: {prob:.4f}")

if __name__ == "__main__":
    main()

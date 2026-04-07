# src/stat_engine.py
import math

class StatEngine:
    def __init__(self, data):
        if not data:
            raise ValueError("Data cannot be empty")
        # Keep only numeric values
        self.data = [float(x) for x in data if isinstance(x, (int, float))]
        if not self.data:
            raise TypeError("Data must contain at least one numeric value")

    # Central Tendency
    def get_mean(self):
        return sum(self.data) / len(self.data)

    def get_median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]

    def get_mode(self):
        freq = {}
        for val in self.data:
            freq[val] = freq.get(val, 0) + 1
        max_freq = max(freq.values())
        if max_freq == 1:
            return "No mode (all values are unique)"
        return [k for k, v in freq.items() if v == max_freq]

    # Dispersion
    def get_variance(self, is_sample=True):
        n = len(self.data)
        if is_sample and n < 2:
            raise ValueError("Sample variance requires at least 2 data points")
        mean = self.get_mean()
        squared_diff = [(x - mean) ** 2 for x in self.data]
        return sum(squared_diff) / (n - 1) if is_sample else sum(squared_diff) / n

    def get_standard_deviation(self, is_sample=True):
        return math.sqrt(self.get_variance(is_sample))

    # Outliers
    def get_outliers(self, threshold=2):
        mean = self.get_mean()
        std_dev = self.get_standard_deviation()
        return [x for x in self.data if abs(x - mean) > threshold * std_dev]

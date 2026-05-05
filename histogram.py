import numpy as np
import matplotlib.pyplot as plt

# -----------------------------

# Set random seed for reproducibility
np.random.seed(42)

# Simulate 500 Filipino users' social media usage (% of time spent)
# Mean is high because PH has heavy social media usage
num_users = 500
mean_usage = 80
std_dev = 10

usage_data = np.random.normal(loc=mean_usage, scale=std_dev, size=num_users)

# Ensure values stay within realistic bounds (0% to 100%)
usage_data = np.clip(usage_data, 0, 100)

# -----------------------------

plt.figure(figsize=(10, 6))

plt.hist(
    usage_data,
    bins=12,
    edgecolor="black"
)

# -----------------------------


plt.title("Distribution of Social Media Usage Among Filipinos", fontsize=14)
plt.xlabel("Usage Percentage (%)", fontsize=12)
plt.ylabel("Number of Users", fontsize=12)

# Add grid for readability
plt.grid(axis="y", linestyle="--", alpha=0.7)

# -----------------------------

mean_value = np.mean(usage_data)

plt.axvline(mean_value, linestyle="dashed", linewidth=2)
plt.text(mean_value + 1, 40, f"Mean: {mean_value:.2f}%", rotation=90)

# -----------------------------

plt.show()

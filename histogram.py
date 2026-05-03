import numpy as np
import matplotlib.pyplot as plt

# -----------------------------

np.random.seed(42)

num_users = 500

# Simulated usage distributions (% of usage intensity per user)
# Higher mean = more commonly used in the Philippines

facebook = np.clip(np.random.normal(90, 5, num_users), 0, 100)
youtube = np.clip(np.random.normal(85, 7, num_users), 0, 100)
tiktok = np.clip(np.random.normal(80, 9, num_users), 0, 100)
instagram = np.clip(np.random.normal(75, 10, num_users), 0, 100)
twitter = np.clip(np.random.normal(60, 12, num_users), 0, 100)

# -----------------------------

plt.figure(figsize=(12, 7))

# Histogram styling for better comparison
bins = 12
alpha = 0.5

plt.hist(facebook, bins=bins, alpha=alpha, label="Facebook")
plt.hist(youtube, bins=bins, alpha=alpha, label="YouTube")
plt.hist(tiktok, bins=bins, alpha=alpha, label="TikTok")
plt.hist(instagram, bins=bins, alpha=alpha, label="Instagram")
plt.hist(twitter, bins=bins, alpha=alpha, label="Twitter")

# -----------------------------

plt.title("Social Media Usage Distribution per Platform (Philippines)", fontsize=14)
plt.xlabel("Usage Percentage (%)", fontsize=12)
plt.ylabel("Number of Users", fontsize=12)

plt.grid(axis="y", linestyle="--", alpha=0.4)
plt.legend()

# -----------------------------

for data, name in [
    (facebook, "Facebook"),
    (youtube, "YouTube"),
    (tiktok, "TikTok"),
    (instagram, "Instagram"),
    (twitter, "Twitter")
]:
    mean_val = np.mean(data)
    plt.axvline(mean_val, linestyle="dashed", alpha=0.3)

# -----------------------------

plt.show()
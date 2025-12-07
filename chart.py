import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Styling
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate synthetic marketing data
np.random.seed(42)
n = 200

acquisition_cost = np.random.uniform(20, 300, n)
lifetime_value = acquisition_cost * np.random.uniform(3, 10, n) + np.random.normal(0, 50, n)

df = pd.DataFrame({
    "Acquisition_Cost": acquisition_cost,
    "Lifetime_Value": lifetime_value
})

# Figure for exact 512x512 pixels → 8 inches * 64 dpi = 512 px
plt.figure(figsize=(8, 8), dpi=64)

# Scatter plot
sns.scatterplot(
    data=df,
    x="Acquisition_Cost",
    y="Lifetime_Value",
    palette="deep",
    s=60,
    edgecolor="black"
)

# Titles & labels
plt.title("Customer Lifetime Value vs Acquisition Cost")
plt.xlabel("Customer Acquisition Cost ($)")
plt.ylabel("Customer Lifetime Value ($)")

# Save EXACTLY 512x512
plt.savefig("chart.png", dpi=64, bbox_inches="tight")

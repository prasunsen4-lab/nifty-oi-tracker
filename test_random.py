import random
import string
import pandas as pd
import matplotlib.pyplot as plt

# Generate random data
letters = string.ascii_uppercase
data = {
    "Letter": [random.choice(letters) for _ in range(10)],
    "Value": [random.randint(1, 100) for _ in range(10)]
}

# Create DataFrame
df = pd.DataFrame(data)
print("Random DataFrame:")
print(df)

# Save to Excel
excel_filename = "random_test.xlsx"
df.to_excel(excel_filename, index=False)
print(f"Excel file saved as {excel_filename}")

# Plot bar chart
plt.figure(figsize=(8,5))
plt.bar(df["Letter"], df["Value"], color="skyblue")
plt.title("Random Test Chart")
plt.xlabel("Letter")
plt.ylabel("Value")
plt.tight_layout()

chart_filename = "random_test.png"
plt.savefig(chart_filename)
plt.close()
print(f"Chart saved as {chart_filename}")
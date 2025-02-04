import random
from datetime import datetime, timedelta

import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

# Number of rows
n_rows = 120000

# Generate unique IDs (pnr)
pnr = range(1, n_rows + 1)

# Generate child birthdates
child_start = datetime(2000, 1, 1)
child_end = datetime(2018, 12, 31)
child_days = (child_end - child_start).days
child_birthdates = [
    child_start + timedelta(days=random.randint(0, child_days)) for _ in range(n_rows)
]

# Generate mother birthdates
mother_start = datetime(1970, 1, 1)
mother_end = datetime(2000, 12, 31)
mother_days = (mother_end - mother_start).days
mother_birthdates = [
    mother_start + timedelta(days=random.randint(0, mother_days)) for _ in range(n_rows)
]

# Generate father birthdates
father_birthdates = [
    mother_start + timedelta(days=random.randint(0, mother_days)) for _ in range(n_rows)
]

# Generate fm_living categories
fm_living = np.random.randint(1, 7, n_rows)

# Generate diagnosis dates (5% of rows)
diagnosis_dates = [None] * n_rows
diagnosis_indices = np.random.choice(n_rows, size=int(n_rows * 0.05), replace=False)

for idx in diagnosis_indices:
    child_bd = child_birthdates[idx]
    # Random date within 0-5 years after child birthdate
    max_days = 5 * 365
    days_after = random.randint(0, max_days)
    diagnosis_dates[idx] = child_bd + timedelta(days=days_after)

# Create DataFrame
df = pd.DataFrame(
    {
        "pnr": pnr,
        "child_birthdate": child_birthdates,
        "mother_birthdate": mother_birthdates,
        "father_birthdate": father_birthdates,
        "fm_living": fm_living,
        "diagnosis_date": diagnosis_dates,
    }
)

# Convert dates to datetime format
df["child_birthdate"] = pd.to_datetime(df["child_birthdate"])
df["mother_birthdate"] = pd.to_datetime(df["mother_birthdate"])
df["father_birthdate"] = pd.to_datetime(df["father_birthdate"])
df["diagnosis_date"] = pd.to_datetime(df["diagnosis_date"])

# Display first few rows and basic information
print(df.head())
print("\nDataset Info:")
print(df.info())

# Save to CSV (optional)
df.to_csv("data/generated_data.csv", index=False)

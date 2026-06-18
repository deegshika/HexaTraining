import os

print("Current Working Directory:")
print(os.getcwd())
import pandas as pd
import numpy as np

# Read CSV
df = pd.read_csv("attendance.csv")

print("Original Dataset")
print(df)

# Convert datetime columns
df['clock_in'] = pd.to_datetime(df['clock_in'])
df['clock_out'] = pd.to_datetime(df['clock_out'])

# Remove missing values
df.dropna(inplace=True)

# Calculate work hours
df['work_hours'] = (
    df['clock_out'] - df['clock_in']
).dt.total_seconds() / 3600

# Assume 1 hour break
df['break_time'] = 1

# Productivity Score
df['productivity_score'] = (
    df['tasks_completed'] /
    df['work_hours']
)

# Save cleaned dataset
df.to_csv(
    "cleaned_attendance.csv",
    index=False
)

print("\nCleaned Dataset")
print(df)

# Top Performers
top_performers = df.sort_values(
    by='productivity_score',
    ascending=False
)

print("\nTop Performers")
print(
    top_performers[
        ['employee_name',
         'department',
         'productivity_score']
    ]
)

# Bottom Performers
bottom_performers = df.sort_values(
    by='productivity_score'
)

print("\nBottom Performers")
print(
    bottom_performers[
        ['employee_name',
         'department',
         'productivity_score']
    ]
)

# Frequent Absentees
absentees = df[
    df['work_hours'] < 6
]

print("\nFrequent Absentees")
print(absentees)

# Department Summary
summary = df.groupby(
    'department'
)[
    ['work_hours',
     'productivity_score']
].mean()

print("\nDepartment Summary")
print(summary)

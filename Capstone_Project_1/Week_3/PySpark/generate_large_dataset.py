import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

departments = ['IT', 'HR', 'Finance', 'Sales']

data = []

for i in range(1, 2001):

    department = np.random.choice(departments)

    clock_in_hour = np.random.randint(8, 11)
    clock_in_min = np.random.randint(0, 60)

    clock_in = datetime(
        2026, 6, 15,
        clock_in_hour,
        clock_in_min
    )

    work_hours = np.random.randint(4, 10)

    clock_out = clock_in + timedelta(hours=work_hours)

    tasks_completed = np.random.randint(0, 20)

    data.append([
        i,
        department,
        clock_in,
        clock_out,
        tasks_completed
    ])

df = pd.DataFrame(
    data,
    columns=[
        'employee_id',
        'department',
        'clock_in',
        'clock_out',
        'tasks_completed'
    ]
)

df.to_csv(
    'large_attendance.csv',
    index=False
)

print("large_attendance.csv created successfully")

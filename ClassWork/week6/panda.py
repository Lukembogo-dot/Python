import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'salary': [50000, 60000, 70000]
}

result = pd.DataFrame(data)
#print("DataFrame is:\n", result)  # This will print the DataFrame with names, ages, and salaries
print(result[result['salary'] > 40000])  # This will print the rows where salary is greater than 60000)

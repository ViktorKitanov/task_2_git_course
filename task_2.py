import pandas as pd

# Let's suppose we have the following DataFrame
df = pd.DataFrame({
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [23, 78, 22, 19],
    'Country': ['USA', 'USA', 'Canada', 'Australia']
})

# Print the entire DataFrame
print(df)

# Task 1: Implement a function to calculate and print the average age of people in the DataFrame.
def calculate_average_age(data_frame):
    average_age = data_frame['Age'].mean()
    print(f"Average Age: {average_age:.2f}")

# Task 2: Implement a function that counts and prints the number of unique countries represented in the DataFrame.
def count_unique_countries(data_frame):
    unique_countries = data_frame['Country'].nunique()
    print(f"Number of Unique Countries: {unique_countries}")

# Task 1
calculate_average_age(df)

# Task 2
count_unique_countries(df)



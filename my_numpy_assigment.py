import numpy as np

# Given array
prices = np.array([100, 250, 400, 150, 300])

# 1. Apply a 10% discount (multiply by 0.90)
discounted_prices = prices * 0.90

# 2. Find the average of the discounted prices
avg_discounted_price = np.mean(discounted_prices)

# Display results
print("Discounted Prices:", discounted_prices)
print("Average Discounted Price:", avg_discounted_price)
print("Question 2")
import pandas as pd

# Given Pandas Series
sales = pd.Series(
    [120000, 150000, 95000, 175000, 200000, 180000],
    index=["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
)

# 1. Total Sales
total_sales = sales.sum()

# 2. Average Monthly Sales
avg_sales = sales.mean()

# 3. Highest-sales Month
highest_month = sales.idxmax()

# 4. Lowest-sales Month
lowest_month = sales.idxmin()

# 5. Months with sales above 150,000
above_150k = sales[sales > 150000]

# 6. Percentage contribution of each month to total sales
percentage_contribution = (sales / total_sales) * 100

# Display Results
print(f"Total Sales: {total_sales}")
print(f"Average Monthly Sales: {avg_sales:.2f}")
print(f"Highest-Sales Month: {highest_month} ({sales[highest_month]})")
print(f"Lowest-Sales Month: {lowest_month} ({sales[lowest_month]})")
print("\nMonths with sales > 150,000:")
print(above_150k)
print("\nPercentage Contribution (%):")
print(percentage_contribution.round(2))
print("===========QUESTION 3===========")
import pandas as pd

# Given Pandas Series
temperatures = pd.Series(
    [29, 31, 28, 33, 35, 30, 27, 32, 34, 36],
    index=[
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
    ],
)

# 1. Average temperature
avg_temp = temperatures.mean()

# 2. Hottest day
hottest_day = temperatures.idxmax()

# 3. Coldest day
coldest_day = temperatures.idxmin()

# 4. Days above 32°C
days_above_32 = temperatures[temperatures > 32]

# 5. Number of days above average
num_days_above_avg = (temperatures > avg_temp).sum()

# 6. Difference between hottest and coldest temperatures
temp_diff = temperatures.max() - temperatures.min()

# Display Results
print(f"Average Temperature: {avg_temp:.2f}°C")
print(f"Hottest Day: {hottest_day} ({temperatures.max()}°C)")
print(f"Coldest Day: {coldest_day} ({temperatures.min()}°C)")
print("\nDays with temperature above 32°C:")
print(days_above_32)
print(f"\nNumber of days above average: {num_days_above_avg}")
print(f"Difference between hottest and coldest: {temp_diff}°C")
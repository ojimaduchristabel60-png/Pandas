import pandas as pd
import matplotlib.pyplot as plt

# Initial Dataset Setup
data = {
    "Name": [
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Eva",
        "Frank",
        "Grace",
        "Henry",
        "Ivy",
        "Jack",
    ],
    "Age": [22, 25, 28, 21, 30, 26, 24, 29, 23, 27],
    "Department": [
        "IT",
        "HR",
        "IT",
        "Finance",
        "HR",
        "IT",
        "Finance",
        "IT",
        "HR",
        "Finance",
    ],
    "Salary": [
        350000,
        280000,
        450000,
        320000,
        390000,
        420000,
        300000,
        500000,
        310000,
        370000,
    ],
    "Experience": [1, 3, 5, 2, 6, 4, 2, 7, 1, 4],
    "Performance": [78, 85, 92, 74, 88, 95, 80, 97, 82, 89],
}

df = pd.DataFrame(data)

# ==========================================
# QUESTION 1: Boolean Indexing
# ==========================================

print("--- Question 1: Salary > 350,000 ---")
salary_filter = df["Salary"] > 350000
ans1_1 = df[salary_filter]
print(ans1_1)

print("\n--- Question 1: Age < 25 ---")
age_filter = df["Age"] < 25
ans1_2 = df[age_filter]
print(ans1_2)

print("\n--- Question 1: Experience > 3 ---")
exp_filter = df["Experience"] > 3
ans1_3 = df[exp_filter]
print(ans1_3)

print("\n--- Question 1: Performance > 90 ---")
perf_filter = df["Performance"] > 90
ans1_4 = df[perf_filter]
print(ans1_4)

print("\n--- Question 1: Department == 'IT' ---")
it_filter = df["Department"] == "IT"
ans1_5 = df[it_filter]
print(ans1_5)

# ==========================================
# QUESTION 2: Combined Conditions
# ==========================================

print("\n--- Question 2: IT & Salary > 400,000 ---")
it_high_salary = (df["Department"] == "IT") & (df["Salary"] > 400000)
ans2_1 = df[it_high_salary]
print(ans2_1)

print("\n--- Question 2: HR & Performance > 80 ---")
hr_high_perf = (df["Department"] == "HR") & (df["Performance"] > 80)
ans2_2 = df[hr_high_perf]
print(ans2_2)

print("\n--- Question 2: Experience > 3 & Salary > 350,000 ---")
exp_and_salary = (df["Experience"] > 3) & (df["Salary"] > 350000)
ans2_3 = df[exp_and_salary]
print(ans2_3)

print("\n--- Question 2: Age < 25 OR Performance > 90 ---")
young_or_high_perf = (df["Age"] < 25) | (df["Performance"] > 90)
ans2_4 = df[young_or_high_perf]
print(ans2_4)

# ==========================================
# QUESTION 3: Sorting the DataFrame
# ==========================================

print("\n--- Question 3: Salary Lowest to Highest ---")
ans3_1 = df.sort_values(by="Salary", ascending=True)
print(ans3_1)

print("\n--- Question 3: Salary Highest to Lowest ---")
ans3_2 = df.sort_values(by="Salary", ascending=False)
print(ans3_2)

print("\n--- Question 3: Performance Highest to Lowest ---")
ans3_3 = df.sort_values(by="Performance", ascending=False)
print(ans3_3)

print(
    "\n--- Question 3: Department Alphabetical & Salary Highest to Lowest ---"
)
ans3_4 = df.sort_values(by=["Department", "Salary"], ascending=[True, False])
print(ans3_4)
# ==========================================
# QUESTION 4: Descriptive Statistics
# ==========================================

total_salary = df["Salary"].sum()
avg_salary = df["Salary"].mean()
highest_salary = df["Salary"].max()
lowest_salary = df["Salary"].min()
avg_age = df["Age"].mean()
avg_experience = df["Experience"].mean()
avg_performance = df["Performance"].mean()

print("--- Question 4: Descriptive Statistics ---")
print("Total Salary:", total_salary)
print("Average Salary:", avg_salary)
print("Highest Salary:", highest_salary)
print("Lowest Salary:", lowest_salary)
print("Average Age:", avg_age)
print("Average Experience:", avg_experience)
print("Average Performance:", avg_performance)

# ==========================================
# QUESTION 5: Finding Specific Employees
# ==========================================

highest_sal_emp = df.loc[df["Salary"].idxmax(), ["Name", "Salary"]]
lowest_sal_emp = df.loc[df["Salary"].idxmin(), ["Name", "Salary"]]
highest_perf_emp = df.loc[df["Performance"].idxmax(), ["Name", "Performance"]]
most_exp_emp = df.loc[df["Experience"].idxmax(), ["Name", "Experience"]]

print("\n--- Question 5: Specific Employees ---")
print(
    f"Highest Salary: {highest_sal_emp['Name']} ({highest_sal_emp['Salary']})"
)
print(f"Lowest Salary: {lowest_sal_emp['Name']} ({lowest_sal_emp['Salary']})")
print(
    f"Highest Performance: {highest_perf_emp['Name']} ({highest_perf_emp['Performance']})"
)
print(
    f"Most Experience: {most_exp_emp['Name']} ({most_exp_emp['Experience']} years)"
)

# ==========================================
# QUESTION 6: Bar Chart
# ==========================================

plt.figure(figsize=(8, 5))
plt.bar(df["Name"], df["Performance"], color="skyblue")
plt.xlabel("Employee Name")
plt.ylabel("Performance Score")
plt.title("Employee Performance Score")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ==========================================
# QUESTION 7: Histogram
# ==========================================

plt.figure(figsize=(8, 5))
plt.hist(df["Age"], bins=5, color="lightgreen", edgecolor="black")
plt.xlabel("Age Range")
plt.ylabel("Frequency")
plt.title("Distribution of Employee Ages")
plt.tight_layout()
plt.show()

print("\n--- Question 7: Highest Frequency Age Range ---")
print("The age range with the highest frequency is 21–25 (5 employees).")
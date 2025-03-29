employees = [
    {"dept_no": 101, "roll_no": 1, "salary": 50000},
    {"dept_no": 102, "roll_no": 2, "salary": 60000},
    {"dept_no": 101, "roll_no": 3, "salary": 45000},
    {"dept_no": 103, "roll_no": 4, "salary": 70000},
    {"dept_no": 102, "roll_no": 5, "salary": 65000},
    {"dept_no": 103, "roll_no": 6, "salary": 72000},
]

dept_salaries = {}
for emp in employees:
    dept_no = emp["dept_no"]
    salary = emp["salary"]
    if dept_no not in dept_salaries:
        dept_salaries[dept_no] = []
    dept_salaries[dept_no].append(salary)

for dept, salaries in dept_salaries.items():
    print(f"Department {dept}: Min Salary = {min(salaries)}, Max Salary = {max(salaries)}")

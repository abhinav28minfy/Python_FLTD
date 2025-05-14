def group_by_department(employees):
    d={}
    for name,department,salary in employees:
        if department not in d:
            d[department] = {"total_salary":0, "employees":[], "count":0}
        d[department]["total_salary"] += salary
        d[department]["employees"].append(name)
        d[department]["count"] += 1

    #print(d)
    #print("********************************")

    result={}
    for department, data in d.items():
        #print(data)
        #print("..................................")
        avg_salary = data["total_salary"] / data["count"]
        result[department] = {
            "average_salary": avg_salary,
            "employees": data["employees"]
        }
    return result


employees = [
    ("Alice", "Engineering", 80000),
    ("Bob", "Marketing", 70000),
    ("Charlie", "Engineering", 90000),
    ("Diana", "HR", 65000),
    ("Eve", "Marketing", 75000)
]

print(group_by_department(employees))
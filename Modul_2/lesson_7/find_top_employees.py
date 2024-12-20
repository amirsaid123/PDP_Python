with open("employees.txt", "r") as f:
    lines = f.readlines()





sorted_employees = [line for line in lines if int(line.split(",", )[2]) > 4000]


with open("high_salary.txt", "w") as f:
    f.writelines(sorted_employees)


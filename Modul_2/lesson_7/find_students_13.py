with open("students.txt", "r") as f:
    lines = f.readlines()


filtered_points = [line for line in lines if int(line.split(",")[1]) > 80]

with open("top_students.txt", "w") as f:
    f.writelines(filtered_points)
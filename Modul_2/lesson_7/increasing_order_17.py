
threshold = 50


with open("students.txt", "r") as f:
    filtered_students = [
        line.strip() for line in f if int(line.split(", ")[1]) > threshold
    ]


filtered_students.sort(key=lambda x: int(x.split(", ")[1]))


with open("students.txt", "w") as f:
    f.write("\n".join(filtered_students))

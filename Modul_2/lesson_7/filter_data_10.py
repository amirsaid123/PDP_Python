with open("data.txt", "r") as f:
    lines = f.readlines()


filtered_lines = [line for line in lines if int(line.split(",")[1]) > 25]

with open("filtered_data.txt", "w") as f:
    f.writelines(filtered_lines)
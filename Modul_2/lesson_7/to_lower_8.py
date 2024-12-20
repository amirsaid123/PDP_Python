
with open("sample.txt", "r") as f:
    text = f.read().lower()


with open("sample.txt", "w") as f:
    f.write(text)

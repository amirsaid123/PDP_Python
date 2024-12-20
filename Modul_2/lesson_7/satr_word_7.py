with open("sample.txt", "r") as f:
    words = f.read().split()
    for word in words:
        if "satr" in word:
            print(word)
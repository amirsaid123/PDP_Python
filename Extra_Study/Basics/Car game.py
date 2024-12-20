command = ""
stared = False
while command != "quit":
    command = input("Enter your command: ").lower()
    if command == "start":
        if stared:
            print("Car is already started!")
        else:
            stared = True
            print("Car started...")

    elif command == "stop":
        if not stared:
            print("Car is already stopped!")
        else:
            stared = False
            print("Car stopped...")

    elif command == "help":
        print('''
        start - to start the car
        stop - to stop the car
        quit - to quit the car
        ''')
    elif command == "quit":
        break
    else:
        print("Invalid command")
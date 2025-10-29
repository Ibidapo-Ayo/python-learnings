def get_command():
    return input("> ").lower()


while True:
    command = get_command()
    if command == "start":
        print("Car started... Ready to go!")
    elif command == "stop":
        print("Car stopped... Parked!")
    elif command == "help":
        print(
            "start - to start the car\nstop - to stop the car\nquit - to quit the game"
        )
    elif command == "quit":
        break
    else:
        print("I don't understand that...")

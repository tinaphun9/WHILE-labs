def main():
    print("Starting While Loop")

    try:
        user = int(input("Enter a number 0 to 9: "))
    except:
        print("Not a number")
        return

    number = 0

    while number < 10:
        print(number)

        if user == number:
            print("User =", user, "Count =", number)

        number = number + 1

    print("Ending While Loop")

main()

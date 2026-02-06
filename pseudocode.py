# Python WHILE - Do Math On User Input Lab - Scratch Pad
def main():
    print("Starting Code Challenge")

    try:
        user_number = int(input("Enter an number greater than 20 >"))
    except:
        print("That's not a number.")
        return

    if user_number <= 20:
        print("Number is less than 20. try again.")
        return

    print("Your number", user_number, "is valid. Thanks")

    count = 0
    current = user_number

    print("The user input started as", current)

    while current > 1:
        current = current / 2
        count = count + 1
        print("The current value of the user input after some math is", current)
        print("The while loop has looped", count, "time" + ("s" if count > 1 else ""))

    print("Ending While Loop")
    print("The While Loop looped a total of", count, "times")
    print("Ending Code Challenge")

main()

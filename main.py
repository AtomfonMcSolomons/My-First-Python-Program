import calculator
import vital_signs
import datetime
import games

def main():
    while True:
        print("A: Calculator")
        print("B: Email Slicer")
        print("C: Games")
        print("D: Vital Signs Check")
        print("E: Today's date")
        print("Q: Program ended")

        your_option = input("Select an option from A - E")

        if your_option == "a" or your_option == "A":
            print("You have chosen the calculator")
            main_calculator()
        elif your_option == "c" or your_option == "C":
            print("Let's play a game")
            games.guess(10)
        elif your_option == "d" or your_option == "D":
            print("You have chosen Vital Signs Check")
            vital_signs_check()
        elif your_option == "e" or your_option == "E":
            date = datetime.datetime.today()
            print(date)
        elif your_option == "q" or your_option == "Q":
            quit()


def main_calculator():
    while True:
        print("A: Addition")
        print("B: Subtraction")
        print("C: Multiplication")
        print("D: Division")
        print("E: Square Root")
        print("F: Exit")

        choice = input("Choose your option")

        if choice == "a" or choice == "A":
            print("Addition")
            a = int(input("Enter the value of a: "))
            b = int(input("Enter the value of b: "))
            calculator.add(a, b)
        elif choice == "b" or choice == "B":
            print("Subtraction")
            a = int(input("Enter the value of a: "))
            b = int(input("enter the value of b: "))
            calculator.subtract(a, b)
        elif choice == "c" or choice == "C":
            print("Multiplication")
            a = int(input("Enter the value of a: "))
            b = int(input("enter the value of b: "))
            calculator.multiply(a, b)
        elif choice == "d" or choice == "D":
            print("Division")
            a = int(input("Enter the value of a: "))
            b = int(input("enter the value of b: "))
            calculator.divide(a, b)
        elif choice == "e" or choice == "E":
            print("Square Root")
            x = int(input("What is the value of x? "))
            calculator.square(x)
        elif choice == "f" or choice == "F":
            print("Program Ended")
            quit()

def vital_signs_check():
    while True:
        vital_signs.main()

print("Welcome! What will you like me to do?")
print("Chose from the options below")

main()

# PERSONAL MINI-TOOLKIT
# Week 8 Final Project

# TOOL 1: SIMPLE CALCULATOR
def calculator():
    print("\n--- SIMPLE CALCULATOR ---")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    operation = input("Choose operation (+, -, *, /): ")

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            print("Cannot divide by zero.")
            return
        result = num1 / num2
    else:
        print("Invalid operation.")
        return

    print(f"Your answer is: {result}")


# TOOL 2: TO-DO LIST
def todo_list():
    tasks = []

    while True:
        print("\n--- TO-DO LIST ---")
        print("1. Add task")
        print("2. View tasks")
        print("3. Remove task")
        print("4. Back to main menu")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter your task: ")
            tasks.append(task)
            print(f"Task added: {task}")

        elif choice == "2":
            if len(tasks) == 0:
                print("Your list is empty.")
            else:
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice == "3":
            if len(tasks) == 0:
                print("No tasks to remove.")
            else:
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")
                try:
                    number = int(input("Enter task number to remove: "))
                    if 1 <= number <= len(tasks):
                        removed = tasks.pop(number - 1)
                        print(f"Removed: {removed}")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "4":
            break

        else:
            print("Invalid choice. Try again.")


# TOOL 3: NUMBER GUESSING GAME
def guessing_game():
    secret = 7

    print("\n--- NUMBER GUESSING GAME ---")
    print("Guess a number between 1 and 10.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if guess < 1 or guess > 10:
            print("Choose between 1 and 10.")
        elif guess < secret:
            print("Too low! Try again.")
        elif guess > secret:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed {secret} correctly.")
            break


# MAIN MENU
def main():
    print("WELCOME TO MY PERSONAL MINI-TOOLKIT!")

    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Simple Calculator")
        print("2. To-Do List")
        print("3. Number Guessing Game")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            calculator()
        elif choice == "2":
            todo_list()
        elif choice == "3":
            guessing_game()
        elif choice == "4":
            print("Thank you for using my toolkit. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose from 1 to 4.")


# Run the program
if __name__ == "__main__":
    main()

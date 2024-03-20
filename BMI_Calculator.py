

def get_user_input(prompt):
    while True:
        try:
            user_input = float(input(prompt))
            if user_input <= 0:
                print("Please enter a valid positive number.")
            else:
                return user_input
        except ValueError:
            print("Invalid input. Please enter a valid number.")


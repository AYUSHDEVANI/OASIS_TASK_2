

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

def claculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    
    elif 18.5 <= bmi < 25:
        return "Normal Weight"

    elif 25 <= bmi < 30:
        return "Overweight"

    else:
        return "Obese"




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

def display_results(weight, height, bmi, category):
    print("\nBMI CALCULATOR RESULTS")
    print(f"Weight: {weight} kg")
    print(f"Height: {height} m")
    print(f"BMI: {bmi:.2f}")
    print(f"Category: {category}")

def main():
    print("Welcome to the BMI Calculator!!")

    weight = get_user_input("Enter your weight in kilograms: ")
    height = get_user_input("Enter your height in meters: ")

    bmi = claculate_bmi(weight=weight, height=height)
    bmi_category = interpret_bmi(bmi)

    display_results(weight=weight, height=height, bmi=bmi, category=bmi_category)


if __name__ == "__main__":
    main()
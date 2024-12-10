import math
import time

# Define operations
operations = {
    "1": ("Add", lambda a, b: a + b),
    "2": ("Subtract", lambda a, b: a - b),
    "3": ("Multiply", lambda a, b: a * b),
    "4": ("Divide", lambda a, b: a / b if b != 0 else "Error! Division by zero."),
    "5": ("Power", lambda a, b: a ** b),
    "6": ("Square Root", lambda a: math.sqrt(a) if a >= 0 else "Error! Cannot compute square root of a negative number."),
    "7": ("Sine", lambda a: math.sin(math.radians(a))),
    "8": ("Cosine", lambda a: math.cos(math.radians(a))),
    "9": ("Tangent", lambda a: math.tan(math.radians(a))),
    "10": ("Arcsine", lambda a: math.degrees(math.asin(a)) if -1 <= a <= 1 else "Error! Input value out of range."),
    "11": ("Arccosine", lambda a: math.degrees(math.acos(a)) if -1 <= a <= 1 else "Error! Input value out of range."),
    "12": ("Arctangent", lambda a: math.degrees(math.atan(a))),
    "13": ("Logarithm", lambda a: math.log(a) if a > 0 else "Error! Logarithm undefined for non-positive values."),
    "14": ("Exponential", lambda a: math.exp(a)),
    "15": ("Factorial", lambda a: math.factorial(a) if a >= 0 and int(a) == a else "Error! Factorial undefined for negative numbers or non-integers."),
    "16": ("Absolute", lambda a: abs(a)),
    "17": ("GCD", lambda a, b: math.gcd(int(a), int(b))),
    "18": ("LCM", lambda a, b: abs(int(a) * int(b)) // math.gcd(int(a), int(b))),
    "19": ("Percentage", lambda a, b: (a / b) * 100 if b != 0 else "Error! Division by zero."),
    "20": ("Floor", lambda a: math.floor(a)),
    "21": ("Ceil", lambda a: math.ceil(a)),
    "22": ("Radians", lambda a: math.radians(a)),
    "23": ("Degrees", lambda a: math.degrees(a)),
    "24": ("Hypotenuse", lambda a, b: math.hypot(a, b)),
    "25": ("Area of Circle", lambda r: math.pi * r ** 2),
    "26": ("Circumference of Circle", lambda r: 2 * math.pi * r),
    "27": ("Area of Rectangle", lambda l, w: l * w),
    "28": ("Perimeter of Rectangle", lambda l, w: 2 * (l + w)),
    "29": ("Volume of Cube", lambda s: s ** 3),
    "30": ("Surface Area of Cube", lambda s: 6 * s ** 2)
}

def carbon_footprint_calculator(transport, electricity, waste, food, recycling):
    recycling_emissions = recycling * -0.01  # Assuming 0.01 kg of CO2 is saved per pound of recycling
    total_emissions = transport + electricity + waste + food + recycling_emissions
    return total_emissions

def splash_screen():
    print("#####################################")
    print("#####################################")
    print("##   CARBONFOOTPRINT CALCULATOR    ##")
    print("##     for 6A's Skill - Expo       ##")
    print("#####################################")
    print("#####################################")
    time.sleep(0.5)

def main():
    splash_screen()
    name = input("\nHello! What is your name? ")
    print(f"Nice to meet you, {name}!")
    time.sleep(1)
    print(f"\nWelcome to the Futuristic Calculator, {name}! Let's get started")
    time.sleep(1)

    while True:
        print("\nChoose an operation:")
        for key, value in operations.items():
            print(f"{key}. {value[0]}")
        print("31. Carbon Footprint Calculator")
        print("32. Exit")

        try:
            choice = input(f"{name}, enter your choice (1-32): ")
            if choice == "32":
                print(f"Exiting the calculator. Goodbye, {name}!")
                break

            if choice == "31":
                transport = float(input("Enter your monthly transportation CO2 emissions in kg: "))
                electricity = float(input("Enter your monthly electricity usage CO2 emissions in kg: "))
                waste = float(input("Enter your monthly waste CO2 emissions in kg: "))
                food = float(input("Enter your monthly food CO2 emissions in kg: "))
                recycling = float(input("Enter pounds of recycling done: "))
                total_emissions = carbon_footprint_calculator(transport, electricity, waste, food, recycling)
                print(f"Your total monthly CO2 emissions: {total_emissions} kg")
            elif choice in operations:
                func = operations[choice][1]
                if func.__code__.co_argcount == 2:
                    a = float(input("Enter first number: "))
                    b = float(input("Enter second number: "))
                    print(f"Result: {func(a, b)}")
                else:
                    a = float(input("Enter the number: "))
                    print(f"Result: {func(a)}")
            else:
                print("Invalid choice. Please choose again.")
        except ValueError:
            print("Error! Invalid input. Please enter a valid number.")

        cont = input(f"{name}, do you want to continue? (yes/no): ").strip().lower()
        if cont == "no":
            print(f"Goodbye, {name}!")
            break

if __name__ == "__main__":
    main()
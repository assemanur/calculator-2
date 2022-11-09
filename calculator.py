"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod,)



while True:
    user_input = input("Please enter the operation and 2 numbers: ").split(' ')
    
    if user_input[0] == "q":
        print("Goodbye!")
        break
    
    else:
        num1 = user_input[1]
        if len(user_input) < 3:
            num2 = 0
        else:
            num2 = user_input[2]
        
        
        if user_input[0] == "+":
            result = add(int(num1), int(num2))
        elif user_input[0] == "-":
            result = subtract(int(num1), int(num2))
        elif user_input[0] == "*":
            result = multiply(int(num1), int(num2))
        elif user_input[0] == "/":
            result = round(divide(int(num1), int(num2)), 2)
        elif user_input[0] == "square":
            result = square(int(num1))
        elif user_input[0] == "cube":
            result = cube(int(num1))
        elif user_input[0] == "pow":
            result = power(int(num1), int(num2))
        elif user_input[0] == "mod":
            result = mod(int(num1), int(num2))
    
    print(result)






# Replace this with your code

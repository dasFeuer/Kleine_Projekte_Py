num = float(input("Enter the 1st number: "))
operator = input("Enter the operator +, -, /, *, %: ")
num1 = float(input("Enter the 2nd number: "))

match operator:
    case "+":
        print("Output:", num + num1)
    case "-":
        print("Output:", num - num1)
    case "/":
        print("Output:", num / num1)
    case "*":
        print("Output:", num * num1)
    case "%":
        print("Output:", num % num1)
    case _:
        print("SyntaxError")
            


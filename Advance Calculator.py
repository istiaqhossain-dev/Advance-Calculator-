import math

print("===========================================")
print("🔷 Welcome to Advanced Calculator 🔷")
print("🛠️  Made by Istiaq for testing purpose")
print("➤ Here you can do any kind of calculation you want")
print("===========================================\n")

print("Supported operations:")
print(" +  : Addition")
print(" -  : Subtraction")
print(" *  : Multiplication")
print(" /  : Division")
print(" ** : Exponentiation (e.g., 2 ** 3)")
print(" %  : Modulo")
print("Use parentheses for complex expressions.")
print("\nAdvanced functions:")
print(" sqrt(x)    : Square root")
print(" log(x)     : Natural logarithm (base e)")
print(" log10(x)   : Logarithm base 10")
print(" sin(x)     : Sine (x in radians)")
print(" cos(x)     : Cosine (x in radians)")
print("Type 'exit' or 'quit' to stop.\n")

# Define allowed names for eval to restrict scope for security
allowed_names = {
    'sqrt': math.sqrt,
    'log': math.log,
    'log10': math.log10,
    'sin': math.sin,
    'cos': math.cos,
    'pi': math.pi,
    'e': math.e,
    # basic math functions and constants
}

while True:
    expr = input("Enter expression: ")

    if expr.lower() in ['exit', 'quit']:
        print("Exiting the calculator. Thank you!")
        break

    try:
        # Evaluate expression using only allowed names
        result = eval(expr, {"__builtins__": None}, allowed_names)
        print("Result:", result)
    except ZeroDivisionError:
        print("❌ Error: Division by zero is not allowed.")
    except Exception:
        print("❌ Invalid expression. Please try again.")

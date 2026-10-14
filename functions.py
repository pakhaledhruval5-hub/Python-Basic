# ==========================================
# STAGE 1: PYTHON BASICS
# TOPIC 6: FUNCTIONS
# ==========================================
"""
SUMMARY DEFINITION:
English: Functions are reusable blocks of code that perform specific tasks.
They help organize code and avoid repeating the same instructions.
Gujarati: ફંક્શન્સ એ કોડના ફરીથી ઉપયોગ કરી શકાય એવા ભાગો છે,
જે ચોક્કસ કાર્ય કરે છે અને કોડને વ્યવસ્થિત રાખવામાં મદદ કરે છે.
"""

# 1. simple_function (સરળ ફંક્શન)
def greet():
    message = "Hello, Python!"
    print(message)  # Output: Hello, Python!

greet()

# 2. function_with_parameter (પેરામીટરવાળું ફંક્શન)
def greet_user(name):
    message = f"Hello, {name}!"
    print(message)  # Output: Hello, Dhruval!

greet_user("Dhruval")

# 3. function_with_return (વેલ્યુ રિટર્ન કરતું ફંક્શન)
def add_numbers(num1, num2):
    result = num1 + num2
    return result

answer = add_numbers(10, 5)
print(answer)  # Output: 15

# 4. subtract_function (બાદબાકીનું ફંક્શન)
def subtract(num1, num2):
    result = num1 - num2
    return result

answer = subtract(20, 8)
print(f"Difference: {answer}")  # Output: Difference: 12

# 5. multiply_function (ગુણાકારનું ફંક્શન)
def multiply(price, quantity):
    total = price * quantity
    return total

bill = multiply(50, 4)
print(bill)  # Output: 200

# 6. default_parameter (ડિફોલ્ટ પેરામીટર)
def welcome(name="Guest"):
    message = f"Welcome, {name}!"
    return message

result = welcome()
print(f"Message: {result}")  # Output: Message: Welcome, Guest!

# 7. keyword_arguments (કીવર્ડ આર્ગ્યુમેન્ટ્સ)
def student_info(name, age):
    details = f"{name} is {age} years old."
    return details

result = student_info(age=17, name="Dhruval")
print(result)  # Output: Dhruval is 17 years old.

# 8. square_function (સંખ્યાનો વર્ગ)
def square(num):
    result = num ** 2
    return result

answer = square(6)
print(f"Square: {answer}")  # Output: Square: 36

# 9. even_odd_function (બેકી કે એકી સંખ્યા)
def check_number(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

result = check_number(7)
print(result)  # Output: Odd

# 10. maximum_function (મોટી સંખ્યા શોધતું ફંક્શન)
def find_max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

largest = find_max(25, 40)
print(f"Largest number: {largest}")  # Output: Largest number: 40

# 11. calculate_average (સરેરાશ ગણતું ફંક્શન)
def calculate_average(num1, num2, num3):
    total = num1 + num2 + num3
    average = total / 3
    return average

result = calculate_average(70, 80, 90)
print(f"Average: {result}")  # Output: Average: 80.0

# 12. discount_function (ડિસ્કાઉન્ટ ગણતું ફંક્શન)
def calculate_discount(price, percentage):
    discount = price * percentage / 100
    final_price = price - discount
    return final_price

result = calculate_discount(1000, 10)
print(f"Final price: {result}")  # Output: Final price: 900.0

# 13. list_sum_function (યાદીનો સરવાળો)
def calculate_total(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

result = calculate_total([10, 20, 30, 40])
print(result)  # Output: 100

# 14. count_items_function (આઇટમ્સની ગણતરી)
def count_items(items):
    total = len(items)
    return total

result = count_items(["Apple", "Banana", "Mango"])
print(f"Total items: {result}")  # Output: Total items: 3

# 15. string_length_function (શબ્દની લંબાઈ)
def get_length(word):
    length = len(word)
    return length

result = get_length("Python")
print(result)  # Output: 6

# 16. temperature_converter (તાપમાન રૂપાંતર)
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

result = celsius_to_fahrenheit(25)
print(f"Temperature: {result}")  # Output: Temperature: 77.0

# 17. multiple_return_values (એકથી વધુ વેલ્યુ રિટર્ન કરવી)
def calculate_numbers(num1, num2):
    total = num1 + num2
    difference = num1 - num2
    return total, difference

addition, subtraction = calculate_numbers(20, 5)
print(f"Addition: {addition}, Subtraction: {subtraction}")  # Output: Addition: 25, Subtraction: 15

# 18. variable_arguments (ઘણા આર્ગ્યુમેન્ટ્સ)
def add_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

result = add_all(10, 20, 30, 40)
print(f"Total sum: {result}")  # Output: Total sum: 100

# 19. keyword_variable_arguments (ઘણા કીવર્ડ આર્ગ્યુમેન્ટ્સ)
def show_details(**details):
    name = details["name"]
    age = details["age"]
    return f"{name} is {age} years old."

result = show_details(name="Riya", age=18)
print(result)  # Output: Riya is 18 years old.

# 20. nested_function (ફંક્શનની અંદર ફંક્શન)
def calculate_square(num):
    def multiply_numbers(value):
        return value * value

    result = multiply_numbers(num)
    return result

answer = calculate_square(5)
print(f"Square result: {answer}")  # Output: Square result: 25

# 21. recursive_function (પોતાને ફરીથી બોલાવતું ફંક્શન)
def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num - 1)

result = factorial(5)
print(result)  # Output: 120

# 22. function_with_condition (શરતવાળું ફંક્શન)
def check_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 70:
        return "A"
    elif marks >= 33:
        return "Pass"
    else:
        return "Fail"

result = check_grade(85)
print(f"Grade: {result}")  # Output: Grade: A

# 23. lambda_function (લેમ્બડા ફંક્શન)
calculate_area = lambda length, width: length * width
area = calculate_area(10, 5)
print(f"Rectangle area: {area}")  # Output: Rectangle area: 50

# 24. mini_calculator_function (નાનું કેલ્ક્યુલેટર ફંક્શન)
def calculator(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/" and num2 != 0:
        return num1 / num2
    else:
        return "Invalid operation"

result = calculator(20, 5, "*")
print(f"Calculator result: {result}")  # Output: Calculator result: 100
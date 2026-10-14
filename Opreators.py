# ==========================================
# STAGE 1: PYTHON BASICS
# TOPIC 3: OPERATORS
# ==========================================
"""
SUMMARY DEFINITION:
English: Operators are special symbols used to perform calculations,
compare values, and make logical decisions in Python.
Gujarati: ઓપરેટર્સ એ ખાસ ચિહ્નો છે જેનો ઉપયોગ Python માં ગણતરી,
મૂલ્યોની સરખામણી અને લોજિકલ નિર્ણયો લેવા માટે થાય છે.
"""

# 1. addition_operator (સરવાળાનો ઓપરેટર)
num1 = 10
num2 = 5
result = num1 + num2
print(result)  # Output: 15

# 2. subtraction_operator (બાદબાકીનો ઓપરેટર)
price = 100
discount = 20
result = price - discount
print(f"Final price: {result}")  # Output: Final price: 80

# 3. multiplication_operator (ગુણાકારનો ઓપરેટર)
price = 50
quantity = 4
total = price * quantity
print(f"Total cost: {total}")  # Output: Total cost: 200

# 4. division_operator (ભાગાકારનો ઓપરેટર)
total_marks = 400
subjects = 5
average = total_marks / subjects
print(average)  # Output: 80.0

# 5. floor_division_operator (પૂર્ણાંક ભાગાકારનો ઓપરેટર)
apples = 17
friends = 5
each_friend = apples // friends
print(f"Apples per friend: {each_friend}")  # Output: Apples per friend: 3

# 6. modulus_operator (શેષ શોધવાનો ઓપરેટર)
num1 = 17
num2 = 5
remainder = num1 % num2
print(f"Remainder: {remainder}")  # Output: Remainder: 2

# 7. exponent_operator (ઘાતનો ઓપરેટર)
base = 2
power = 4
result = base ** power
print(result)  # Output: 16

# 8. combined_arithmetic (સંયુક્ત ગણતરી)
price = 200
quantity = 3
delivery = 50
total = price * quantity + delivery
print(f"Total bill: {total}")  # Output: Total bill: 650

# 9. addition_assignment (સરવાળાનું અસાઇનમેન્ટ)
score = 50
bonus = 10
score += bonus
print(f"Updated score: {score}")  # Output: Updated score: 60

# 10. subtraction_assignment (બાદબાકીનું અસાઇનમેન્ટ)
balance = 500
spent = 150
balance -= spent
print(balance)  # Output: 350

# 11. multiplication_assignment (ગુણાકારનું અસાઇનમેન્ટ)
number = 6
multiplier = 3
number *= multiplier
print(f"Updated number: {number}")  # Output: Updated number: 18

# 12. division_assignment (ભાગાકારનું અસાઇનમેન્ટ)
money = 100
people = 4
money /= people
print(f"Money per person: {money}")  # Output: Money per person: 25.0

# 13. equal_comparison (સમાનતા તપાસવાનો ઓપરેટર)
age1 = 18
age2 = 18
result = age1 == age2
print(result)  # Output: True

# 14. not_equal_comparison (અસમાનતા તપાસવાનો ઓપરેટર)
password1 = 1234
password2 = 5678
result = password1 != password2
print(f"Passwords are different: {result}")  # Output: Passwords are different: True

# 15. greater_than_comparison (કરતાં મોટો ઓપરેટર)
marks = 85
passing_marks = 33
result = marks > passing_marks
print(f"Passed: {result}")  # Output: Passed: True

# 16. less_than_comparison (કરતાં નાનો ઓપરેટર)
temperature = 20
limit = 30
result = temperature < limit
print(result)  # Output: True

# 17. greater_equal_comparison (મોટો અથવા સમાન ઓપરેટર)
score = 75
required_score = 75
result = score >= required_score
print(f"Eligible: {result}")  # Output: Eligible: True

# 18. less_equal_comparison (નાનો અથવા સમાન ઓપરેટર)
items = 4
maximum_items = 5
result = items <= maximum_items
print(f"Within limit: {result}")  # Output: Within limit: True

# 19. logical_and_operator (લોજિકલ AND ઓપરેટર)
age = 20
has_id = True
result = age >= 18 and has_id
print(result)  # Output: True

# 20. logical_or_operator (લોજિકલ OR ઓપરેટર)
has_ticket = False
has_pass = True
result = has_ticket or has_pass
print(f"Can enter: {result}")  # Output: Can enter: True

# 21. logical_not_operator (લોજિકલ NOT ઓપરેટર)
is_raining = False
result = not is_raining
print(f"Can play outside: {result}")  # Output: Can play outside: True

# 22. membership_in_operator (સભ્યતા તપાસતો IN ઓપરેટર)
fruits = ["apple", "banana", "mango"]
search_fruit = "banana"
result = search_fruit in fruits
print(result)  # Output: True

# 23. membership_not_in_operator (સભ્યતા ન હોવાનો NOT IN ઓપરેટર)
colors = ["red", "blue", "green"]
search_color = "yellow"
result = search_color not in colors
print(f"Color not found: {result}")  # Output: Color not found: True

# 24. operator_precedence (ઓપરેટરની પ્રાથમિકતા)
num1 = 10
num2 = 5
num3 = 2
result = num1 + num2 * num3
print(f"Final result: {result}")  # Output: Final result: 20
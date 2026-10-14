# ==========================================
# STAGE 1: PYTHON BASICS
# TOPIC 4: CONDITIONALS
# ==========================================
"""
SUMMARY DEFINITION:
English: Conditionals allow a program to make decisions based on conditions.
Python uses if, elif, and else to execute different blocks of code.
Gujarati: કન્ડિશનલ્સ પ્રોગ્રામને શરતોના આધારે નિર્ણયો લેવામાં મદદ કરે છે.
Python માં if, elif અને else દ્વારા અલગ-અલગ કોડ ચલાવી શકાય છે.
"""

# 1. simple_if (સરળ if શરત)
age = 20
minimum_age = 18
if age >= minimum_age:
    result = "Eligible"
else:
    result = "Not eligible"
print(result)  # Output: Eligible

# 2. if_else (if-else શરત)
num = 7
if num % 2 == 0:
    result = "Even number"
else:
    result = "Odd number"
print(f"Result: {result}")  # Output: Result: Odd number

# 3. positive_or_negative (ધન કે ઋણ સંખ્યા)
num = -5
if num > 0:
    result = "Positive"
else:
    result = "Zero or negative"
print(f"Number type: {result}")  # Output: Number type: Zero or negative

# 4. check_zero (શૂન્ય તપાસવું)
num = 0
if num == 0:
    result = "Zero"
else:
    result = "Not zero"
print(result)  # Output: Zero

# 5. elif_grades (elif દ્વારા ગ્રેડ નક્કી કરવો)
marks = 85
if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
else:
    grade = "B or below"
print(f"Your grade: {grade}")  # Output: Your grade: A

# 6. pass_or_fail (પાસ કે નાપાસ)
marks = 72
passing_marks = 33
if marks >= passing_marks:
    result = "Pass"
else:
    result = "Fail"
print(result)  # Output: Pass

# 7. largest_of_two (બે સંખ્યામાં મોટી સંખ્યા)
num1 = 25
num2 = 40
if num1 > num2:
    largest = num1
else:
    largest = num2
print(f"Largest number: {largest}")  # Output: Largest number: 40

# 8. voting_age (મતદાન માટેની ઉંમર)
age = 18
if age >= 18:
    result = "Can vote"
else:
    result = "Cannot vote"
print(result)  # Output: Can vote

# 9. discount_check (ડિસ્કાઉન્ટ તપાસવું)
price = 1200
if price >= 1000:
    discount = price * 0.10
else:
    discount = 0
final_price = price - discount
print(f"Final price: {final_price}")  # Output: Final price: 1080.0

# 10. temperature_check (તાપમાન તપાસવું)
temperature = 35
if temperature > 30:
    weather = "Hot"
else:
    weather = "Pleasant"
print(f"Weather: {weather}")  # Output: Weather: Hot

# 11. multiple_grade_ranges (અલગ-અલગ ગ્રેડ)
marks = 65
if marks >= 90:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 50:
    grade = "C"
else:
    grade = "D"
print(f"Grade: {grade}")  # Output: Grade: C

# 12. login_check (લોગિન તપાસવું)
saved_password = "python123"
entered_password = "python123"
if entered_password == saved_password:
    result = "Login successful"
else:
    result = "Incorrect password"
print(result)  # Output: Login successful

# 13. largest_of_three (ત્રણ સંખ્યામાં સૌથી મોટી)
num1 = 15
num2 = 28
num3 = 20
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num3:
    largest = num2
else:
    largest = num3
print(f"Largest number: {largest}")  # Output: Largest number: 28

# 14. divisible_by_five (પાંચ વડે વિભાજ્યતા)
num = 45
if num % 5 == 0:
    result = "Divisible by 5"
else:
    result = "Not divisible by 5"
print(result)  # Output: Divisible by 5

# 15. leap_year_check (લીપ વર્ષ તપાસવું)
year = 2024
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    result = "Leap year"
else:
    result = "Not a leap year"
print(f"Year status: {result}")  # Output: Year status: Leap year

# 16. age_category (ઉંમર પ્રમાણે કેટેગરી)
age = 16
if age < 13:
    category = "Child"
elif age < 20:
    category = "Teenager"
else:
    category = "Adult"
print(f"Age category: {category}")  # Output: Age category: Teenager

# 17. electricity_bill (વીજળીનું બિલ)
units = 150
if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = 100 * 2 + (units - 100) * 3
else:
    bill = 100 * 2 + 100 * 3 + (units - 200) * 5
print(f"Electricity bill: {bill}")  # Output: Electricity bill: 350

# 18. shopping_free_delivery (મફત ડિલિવરી તપાસવી)
order_amount = 650
delivery_fee = 50
if order_amount >= 500:
    delivery_fee = 0
total = order_amount + delivery_fee
print(f"Total payment: {total}")  # Output: Total payment: 650

# 19. username_check (યુઝરનેમ તપાસવું)
username = "dhruval"
minimum_length = 5
if len(username) >= minimum_length:
    result = "Username accepted"
else:
    result = "Username too short"
print(result)  # Output: Username accepted

# 20. sports_eligibility (રમત માટે લાયકાત)
age = 17
has_permission = True
if age >= 16 and has_permission:
    result = "Allowed to participate"
else:
    result = "Not allowed"
print(f"Participation: {result}")  # Output: Participation: Allowed to participate

# 21. library_membership (લાઇબ્રેરી સભ્યપદ)
has_membership = False
has_guest_pass = True
if has_membership or has_guest_pass:
    result = "Entry allowed"
else:
    result = "Entry denied"
print(result)  # Output: Entry allowed

# 22. nested_if (નેસ્ટેડ if શરત)
age = 22
has_id = True
if age >= 18:
    if has_id:
        result = "Entry approved"
    else:
        result = "ID required"
else:
    result = "Age requirement not met"
print(f"Entry status: {result}")  # Output: Entry status: Entry approved

# 23. calculator_conditions (શરત આધારિત કેલ્ક્યુલેટર)
num1 = 20
num2 = 5
operator = "/"
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/" and num2 != 0:
    result = num1 / num2
else:
    result = "Invalid operation"
print(f"Calculator result: {result}")  # Output: Calculator result: 4.0

# 24. mini_result_system (નાની પરિણામ પ્રણાલી)
marks = 82
attendance = 90
if marks >= 80 and attendance >= 75:
    result = "Excellent performance"
elif marks >= 33 and attendance >= 75:
    result = "Passed"
elif marks < 33:
    result = "Failed"
else:
    result = "Attendance too low"
print(f"Final result: {result}")  # Output: Final result: Excellent performance
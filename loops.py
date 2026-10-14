# ==========================================
# STAGE 1: PYTHON BASICS
# TOPIC 5: LOOPS
# ==========================================
"""
SUMMARY DEFINITION:
English: Loops are used to repeat a block of code multiple times.
Python provides for loops and while loops to perform repeated tasks.
Gujarati: લૂપ્સનો ઉપયોગ કોડને વારંવાર ચલાવવા માટે થાય છે.
Python માં for અને while લૂપ દ્વારા એક જ કાર્ય ઘણી વખત કરી શકાય છે.
"""

# 1. simple_for_loop (સરળ for લૂપ)
for i in range(1, 6):
    print(i)  # Output: 1, 2, 3, 4, 5

# 2. print_names (નામ છાપવા માટેનો લૂપ)
names = ["Amit", "Riya", "Dhruval"]
for name in names:
    print(f"Student: {name}")  # Output: Student: Amit / Student: Riya / Student: Dhruval

# 3. sum_of_numbers (સંખ્યાઓનો સરવાળો)
total = 0
for num in range(1, 6):
    total += num
print(f"Total sum: {total}")  # Output: Total sum: 15

# 4. multiplication_table (ગુણાકારનો કોઠો)
num = 3
for i in range(1, 6):
    result = num * i
    print(f"{num} x {i} = {result}")  # Output: 3 x 1 = 3 / 3 x 2 = 6 / 3 x 3 = 9 / 3 x 4 = 12 / 3 x 5 = 15

# 5. countdown_loop (ઉલટી ગણતરીનો લૂપ)
for i in range(5, 0, -1):
    print(i)  # Output: 5, 4, 3, 2, 1

# 6. even_numbers (બેકી સંખ્યાઓ)
for num in range(2, 11, 2):
    print(f"Even number: {num}")  # Output: Even number: 2 / Even number: 4 / Even number: 6 / Even number: 8 / Even number: 10

# 7. while_counter (while લૂપથી ગણતરી)
count = 1
while count <= 5:
    print(count)  # Output: 1, 2, 3, 4, 5
    count += 1

# 8. sum_of_even_numbers (બેકી સંખ્યાઓનો સરવાળો)
total = 0
for num in range(2, 11, 2):
    total += num
print(total)  # Output: 30

# 9. list_prices (કિંમતોની યાદી)
prices = [100, 200, 300]
for price in prices:
    print(f"Product price: {price}")  # Output: Product price: 100 / Product price: 200 / Product price: 300

# 10. calculate_total_price (કુલ કિંમતની ગણતરી)
prices = [100, 250, 150]
total = 0
for price in prices:
    total += price
print(f"Total price: {total}")  # Output: Total price: 500

# 11. odd_numbers (એકાકી સંખ્યાઓ)
for num in range(1, 11, 2):
    print(num)  # Output: 1, 3, 5, 7, 9

# 12. factorial_calculation (ફેક્ટોરિયલની ગણતરી)
num = 5
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"Factorial of {num}: {factorial}")  # Output: Factorial of 5: 120

# 13. break_statement (break દ્વારા લૂપ રોકવો)
for num in range(1, 10):
    if num == 5:
        break
    print(num)  # Output: 1, 2, 3, 4

# 14. continue_statement (continue દ્વારા આગળ વધવું)
for num in range(1, 6):
    if num == 3:
        continue
    print(f"Number: {num}")  # Output: Number: 1 / Number: 2 / Number: 4 / Number: 5

# 15. nested_for_loop (નેસ્ટેડ for લૂપ)
for row in range(1, 4):
    for col in range(1, 3):
        print(f"Row {row}, Column {col}")  # Output: Row 1, Column 1 / Row 1, Column 2 / Row 2, Column 1 / Row 2, Column 2 / Row 3, Column 1 / Row 3, Column 2

# 16. character_loop (અક્ષરો પર લૂપ)
word = "PYTHON"
for letter in word:
    print(f"Letter: {letter}")  # Output: Letter: P / Letter: Y / Letter: T / Letter: H / Letter: O / Letter: N

# 17. count_vowels (સ્વરોની ગણતરી)
word = "education"
vowels = "aeiou"
count = 0
for letter in word:
    if letter in vowels:
        count += 1
print(f"Vowel count: {count}")  # Output: Vowel count: 5

# 18. find_largest_number (સૌથી મોટી સંખ્યા શોધવી)
numbers = [12, 45, 23, 67, 34]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print(f"Largest number: {largest}")  # Output: Largest number: 67

# 19. reverse_countdown (ઉલટી ગણતરી)
count = 5
while count >= 1:
    print(f"Countdown: {count}")  # Output: Countdown: 5 / Countdown: 4 / Countdown: 3 / Countdown: 2 / Countdown: 1
    count -= 1

# 20. number_search (સંખ્યા શોધવી)
numbers = [10, 20, 30, 40, 50]
target = 30
found = False
for num in numbers:
    if num == target:
        found = True
        break
print(f"Number found: {found}")  # Output: Number found: True

# 21. square_numbers (સંખ્યાના વર્ગ)
for num in range(1, 6):
    square = num ** 2
    print(f"Square of {num}: {square}")  # Output: Square of 1: 1 / Square of 2: 4 / Square of 3: 9 / Square of 4: 16 / Square of 5: 25

# 22. running_total (ક્રમશઃ સરવાળો)
numbers = [5, 10, 15]
total = 0
for num in numbers:
    total += num
    print(f"Running total: {total}")  # Output: Running total: 5 / Running total: 15 / Running total: 30

# 23. multiplication_grid (ગુણાકારનું ટેબલ)
for row in range(1, 4):
    for col in range(1, 4):
        result = row * col
        print(f"{row} x {col} = {result}")  # Output: 1 x 1 = 1 / 1 x 2 = 2 / 1 x 3 = 3 / 2 x 1 = 2 / 2 x 2 = 4 / 2 x 3 = 6 / 3 x 1 = 3 / 3 x 2 = 6 / 3 x 3 = 9

# 24. mini_guessing_game (નાની નંબર ગેસિંગ રમત)
secret_number = 7
guesses = [3, 5, 7, 9]
found = False
for guess in guesses:
    if guess == secret_number:
        found = True
        break
print(f"Correct guess found: {found}")  # Output: Correct guess found: True
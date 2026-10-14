# ==========================================
# STAGE 1: PYTHON BASICS
# TOPIC 8: TUPLES
# ==========================================
"""
SUMMARY DEFINITION:
English: A tuple is an ordered collection of items that cannot be changed after creation.
Tuples allow duplicate values and can store different data types.
Gujarati: ટ્યુપલ એ વસ્તુઓનો ક્રમબદ્ધ સંગ્રહ છે, જેને બનાવ્યા પછી બદલી શકાતો નથી.
ટ્યુપલમાં એકસરખી વેલ્યુ અને અલગ-અલગ ડેટા ટાઇપ રાખી શકાય છે.
"""

# 1. create_tuple (ટ્યુપલ બનાવવું)
fruits = ("Apple", "Banana", "Mango")
print(fruits)  # Output: ('Apple', 'Banana', 'Mango')

# 2. access_tuple_item (ટ્યુપલમાંથી આઇટમ મેળવવી)
colors = ("Red", "Green", "Blue")
selected_color = colors[1]
print(f"Selected color: {selected_color}")  # Output: Selected color: Green

# 3. negative_indexing (નકારાત્મક ઇન્ડેક્સનો ઉપયોગ)
numbers = (10, 20, 30, 40)
last_number = numbers[-1]
print(last_number)  # Output: 40

# 4. tuple_length (ટ્યુપલની લંબાઈ શોધવી)
subjects = ("Maths", "English", "Science", "Computer")
count = len(subjects)
print(f"Total subjects: {count}")  # Output: Total subjects: 4

# 5. tuple_with_duplicates (ડુપ્લિકેટ વેલ્યુ ધરાવતું ટ્યુપલ)
numbers = (10, 20, 10, 30, 10)
total = numbers.count(10)
print(total)  # Output: 3

# 6. find_tuple_index (ટ્યુપલમાં આઇટમનું સ્થાન શોધવું)
fruits = ("Apple", "Banana", "Mango")
position = fruits.index("Mango")
print(f"Index of Mango: {position}")  # Output: Index of Mango: 2

# 7. tuple_membership (ટ્યુપલમાં આઇટમ છે કે નહીં તે તપાસવું)
colors = ("Red", "Green", "Blue")
search_color = "Green"
found = search_color in colors
print(found)  # Output: True

# 8. tuple_slicing (ટ્યુપલનો અમુક ભાગ મેળવવો)
numbers = (10, 20, 30, 40, 50)
selected_numbers = numbers[1:4]
print(f"Selected numbers: {selected_numbers}")  # Output: Selected numbers: (20, 30, 40)

# 9. tuple_concatenation (બે ટ્યુપલ જોડવા)
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print(combined)  # Output: (1, 2, 3, 4, 5, 6)

# 10. repeat_tuple (ટ્યુપલની વેલ્યુ વારંવાર ઉમેરવી)
numbers = (1, 2, 3)
repeated = numbers * 3
print(f"Repeated tuple: {repeated}")  # Output: Repeated tuple: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# 11. tuple_minimum (સૌથી નાની વેલ્યુ શોધવી)
numbers = (45, 12, 78, 23, 9)
smallest = min(numbers)
print(smallest)  # Output: 9

# 12. tuple_maximum (સૌથી મોટી વેલ્યુ શોધવી)
scores = (65, 90, 78, 88, 72)
highest_score = max(scores)
print(f"Highest score: {highest_score}")  # Output: Highest score: 90

# 13. tuple_sum (ટ્યુપલની સંખ્યાઓનો સરવાળો)
prices = (100, 200, 300, 400)
total_price = sum(prices)
print(total_price)  # Output: 1000

# 14. tuple_loop (લૂપ દ્વારા ટ્યુપલની આઇટમ મેળવવી)
fruits = ("Apple", "Banana", "Mango")
for fruit in fruits:
    print(f"Fruit: {fruit}")  # Output: Fruit: Apple / Fruit: Banana / Fruit: Mango

# 15. tuple_unpacking (ટ્યુપલની વેલ્યુ અલગ વેરિએબલમાં મૂકવી)
student = ("Dhruval", 17, "Commerce")
name, age, stream = student
print(f"Name: {name}, Age: {age}, Stream: {stream}")  # Output: Name: Dhruval, Age: 17, Stream: Commerce

# 16. single_item_tuple (એક આઇટમવાળું ટ્યુપલ)
number = (25,)
print(number)  # Output: (25,)

# 17. convert_list_to_tuple (લિસ્ટને ટ્યુપલમાં ફેરવવું)
numbers = [10, 20, 30, 40]
converted = tuple(numbers)
print(f"Converted tuple: {converted}")  # Output: Converted tuple: (10, 20, 30, 40)

# 18. convert_tuple_to_list (ટ્યુપલને લિસ્ટમાં ફેરવવું)
fruits = ("Apple", "Banana", "Mango")
converted = list(fruits)
converted.append("Orange")
print(f"Updated list: {converted}")  # Output: Updated list: ['Apple', 'Banana', 'Mango', 'Orange']

# 19. nested_tuple (ટ્યુપલની અંદર ટ્યુપલ)
students = (("Amit", 85), ("Riya", 92), ("Dhruval", 88))
student_name = students[1][0]
student_marks = students[1][1]
print(f"Student: {student_name}, Marks: {student_marks}")  # Output: Student: Riya, Marks: 92

# 20. tuple_comparison (બે ટ્યુપલની સરખામણી)
tuple1 = (10, 20, 30)
tuple2 = (10, 20, 30)
result = tuple1 == tuple2
print(f"Tuples are equal: {result}")  # Output: Tuples are equal: True

# 21. tuple_count_items (ટ્યુપલમાં કુલ આઇટમની ગણતરી)
items = ("Pen", "Book", "Pencil", "Bag")
total_items = len(items)
print(total_items)  # Output: 4

# 22. sorted_tuple (ટ્યુપલની વેલ્યુ ક્રમમાં ગોઠવવી)
numbers = (40, 10, 30, 20)
sorted_numbers = tuple(sorted(numbers))
print(f"Sorted tuple: {sorted_numbers}")  # Output: Sorted tuple: (10, 20, 30, 40)

# 23. tuple_unpacking_with_star (સ્ટાર વડે ટ્યુપલની વેલ્યુ અલગ કરવી)
numbers = (10, 20, 30, 40, 50)
first, *middle, last = numbers
print(f"First: {first}, Middle: {middle}, Last: {last}")  # Output: First: 10, Middle: [20, 30, 40], Last: 50

# 24. mini_student_record (નાનો વિદ્યાર્થી રેકોર્ડ)
student = ("Dhruval", 17, "Commerce", 85)
name, age, stream, marks = student
result = "Pass" if marks >= 33 else "Fail"
print(f"Name: {name}, Age: {age}, Stream: {stream}, Marks: {marks}, Result: {result}")  # Output: Name: Dhruval, Age: 17, Stream: Commerce, Marks: 85, Result: Pass
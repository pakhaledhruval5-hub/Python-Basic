# ==========================================
# STAGE 1: PYTHON BASICS
# TOPIC 7: LISTS
# ==========================================
"""
SUMMARY DEFINITION:
English: A list is a collection used to store multiple items in a single variable.
Lists are ordered, changeable, and allow duplicate values.
Gujarati: લિસ્ટ એ એક જ વેરિએબલમાં ઘણી વસ્તુઓ સંગ્રહિત કરવા માટેનો ડેટા પ્રકાર છે.
લિસ્ટ ક્રમબદ્ધ હોય છે, તેમાં ફેરફાર કરી શકાય છે અને એકસરખી વેલ્યુ પણ રાખી શકાય છે.
"""

# 1. create_list (લિસ્ટ બનાવવી)
fruits = ["Apple", "Banana", "Mango"]
print(fruits)  # Output: ['Apple', 'Banana', 'Mango']

# 2. access_list_item (લિસ્ટમાંથી આઇટમ મેળવવી)
colors = ["Red", "Green", "Blue"]
selected_color = colors[1]
print(f"Selected color: {selected_color}")  # Output: Selected color: Green

# 3. change_list_item (લિસ્ટની આઇટમ બદલવી)
numbers = [10, 20, 30]
numbers[1] = 25
print(numbers)  # Output: [10, 25, 30]

# 4. append_item (લિસ્ટમાં આઇટમ ઉમેરવી)
fruits = ["Apple", "Banana"]
fruits.append("Mango")
print(fruits)  # Output: ['Apple', 'Banana', 'Mango']

# 5. insert_item (ચોક્કસ જગ્યાએ આઇટમ ઉમેરવી)
names = ["Amit", "Riya"]
names.insert(1, "Dhruval")
print(f"Student names: {names}")  # Output: Student names: ['Amit', 'Dhruval', 'Riya']

# 6. remove_item (લિસ્ટમાંથી આઇટમ દૂર કરવી)
animals = ["Dog", "Cat", "Cow"]
animals.remove("Cat")
print(animals)  # Output: ['Dog', 'Cow']

# 7. pop_item (લિસ્ટમાંથી છેલ્લી આઇટમ કાઢવી)
numbers = [10, 20, 30, 40]
removed_number = numbers.pop()
print(f"Removed number: {removed_number}")  # Output: Removed number: 40

# 8. list_length (લિસ્ટની લંબાઈ શોધવી)
subjects = ["Maths", "English", "Science", "Computer"]
count = len(subjects)
print(count)  # Output: 4

# 9. check_membership (લિસ્ટમાં આઇટમ છે કે નહીં તે તપાસવું)
fruits = ["Apple", "Banana", "Mango"]
search_fruit = "Banana"
found = search_fruit in fruits
print(f"Fruit found: {found}")  # Output: Fruit found: True

# 10. sort_numbers (સંખ્યાઓને ક્રમમાં ગોઠવવી)
numbers = [40, 10, 30, 20]
numbers.sort()
print(numbers)  # Output: [10, 20, 30, 40]

# 11. reverse_list (લિસ્ટનો ક્રમ ઊલટો કરવો)
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(f"Reversed list: {numbers}")  # Output: Reversed list: [5, 4, 3, 2, 1]

# 12. count_duplicates (એકસરખી આઇટમની ગણતરી)
numbers = [10, 20, 10, 30, 10]
total = numbers.count(10)
print(total)  # Output: 3

# 13. find_index (આઇટમનું સ્થાન શોધવું)
fruits = ["Apple", "Banana", "Mango"]
position = fruits.index("Mango")
print(f"Index of Mango: {position}")  # Output: Index of Mango: 2

# 14. extend_list (બીજી લિસ્ટની આઇટમ ઉમેરવી)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)  # Output: [1, 2, 3, 4, 5, 6]

# 15. list_slicing (લિસ્ટનો અમુક ભાગ મેળવવો)
numbers = [10, 20, 30, 40, 50]
selected_numbers = numbers[1:4]
print(f"Selected numbers: {selected_numbers}")  # Output: Selected numbers: [20, 30, 40]

# 16. sum_list (લિસ્ટની સંખ્યાઓનો સરવાળો)
prices = [100, 200, 300, 400]
total_price = sum(prices)
print(total_price)  # Output: 1000

# 17. minimum_value (સૌથી નાની વેલ્યુ શોધવી)
numbers = [45, 12, 78, 23, 9]
smallest = min(numbers)
print(f"Smallest number: {smallest}")  # Output: Smallest number: 9

# 18. maximum_value (સૌથી મોટી વેલ્યુ શોધવી)
scores = [65, 90, 78, 88, 72]
highest_score = max(scores)
print(highest_score)  # Output: 90

# 19. list_loop (લૂપ દ્વારા લિસ્ટની આઇટમ મેળવવી)
fruits = ["Apple", "Banana", "Mango"]
for fruit in fruits:
    print(f"Fruit: {fruit}")  # Output: Fruit: Apple / Fruit: Banana / Fruit: Mango

# 20. list_comprehension (લિસ્ટ કમ્પ્રિહેન્શન)
numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers]
print(f"Squares: {squares}")  # Output: Squares: [1, 4, 9, 16, 25]

# 21. filter_even_numbers (બેકી સંખ્યાઓ અલગ કરવી)
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)  # Output: [2, 4, 6]

# 22. copy_list (લિસ્ટની નકલ બનાવવી)
original = [10, 20, 30]
copied = original.copy()
copied.append(40)
print(f"Original: {original}, Copy: {copied}")  # Output: Original: [10, 20, 30], Copy: [10, 20, 30, 40]

# 23. nested_list (લિસ્ટની અંદર લિસ્ટ)
students = [["Amit", 85], ["Riya", 92], ["Dhruval", 88]]
student_name = students[1][0]
student_marks = students[1][1]
print(f"Student: {student_name}, Marks: {student_marks}")  # Output: Student: Riya, Marks: 92

# 24. mini_shopping_cart (નાની શોપિંગ કાર્ટ)
cart = ["Book", "Pen", "Bag"]
prices = [200, 20, 500]
total = sum(prices)
cart.append("Pencil")
prices.append(10)
total = sum(prices)
print(f"Items: {cart}, Total bill: {total}")  # Output: Items: ['Book', 'Pen', 'Bag', 'Pencil'], Total bill: 730
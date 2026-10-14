# ==========================================
# STAGE 1: PYTHON BASICS
# TOPIC 9: SETS
# ==========================================
"""
SUMMARY DEFINITION:
English: A set is a collection of unique items in Python.
Sets are unordered, do not allow duplicate values, and can be modified.
Gujarati: સેટ એ Python માં અનન્ય વેલ્યુનો સંગ્રહ છે.
સેટમાં ડુપ્લિકેટ વેલ્યુ હોતી નથી અને તેમાં ફેરફાર કરી શકાય છે.
"""

# 1. create_set (સેટ બનાવવો)
fruits = {"Apple", "Banana", "Mango"}
print(fruits)  # Output: {'Apple', 'Banana', 'Mango'} (order may vary)

# 2. remove_duplicates (ડુપ્લિકેટ દૂર કરવા)
numbers = {10, 20, 10, 30, 20}
unique_numbers = sorted(numbers)
print(f"Unique numbers: {unique_numbers}")  # Output: Unique numbers: [10, 20, 30]

# 3. add_item (સેટમાં આઇટમ ઉમેરવી)
colors = {"Red", "Green"}
colors.add("Blue")
print(f"Colors: {sorted(colors)}")  # Output: Colors: ['Blue', 'Green', 'Red']

# 4. remove_item (સેટમાંથી આઇટમ દૂર કરવી)
animals = {"Dog", "Cat", "Cow"}
animals.remove("Cat")
print(sorted(animals))  # Output: ['Cow', 'Dog']

# 5. discard_item (આઇટમ સુરક્ષિત રીતે દૂર કરવી)
numbers = {10, 20, 30}
numbers.discard(40)
print(f"Numbers: {sorted(numbers)}")  # Output: Numbers: [10, 20, 30]

# 6. set_length (સેટની લંબાઈ શોધવી)
subjects = {"Maths", "English", "Science"}
count = len(subjects)
print(f"Total subjects: {count}")  # Output: Total subjects: 3

# 7. membership_check (સેટમાં આઇટમ તપાસવી)
fruits = {"Apple", "Banana", "Mango"}
found = "Banana" in fruits
print(f"Fruit found: {found}")  # Output: Fruit found: True

# 8. set_union (બે સેટ જોડવા)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.union(set2)
print(f"Union: {sorted(result)}")  # Output: Union: [1, 2, 3, 4, 5]

# 9. set_intersection (સામાન્ય આઇટમ શોધવી)
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
result = set1.intersection(set2)
print(f"Common items: {sorted(result)}")  # Output: Common items: [30, 40]

# 10. set_difference (ફરકવાળી આઇટમ શોધવી)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
result = set1.difference(set2)
print(f"Difference: {sorted(result)}")  # Output: Difference: [1, 2]

# 11. symmetric_difference (બંને સેટમાં અલગ આઇટમ)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.symmetric_difference(set2)
print(f"Different items: {sorted(result)}")  # Output: Different items: [1, 2, 4, 5]

# 12. subset_check (સબસેટ તપાસવું)
set1 = {1, 2}
set2 = {1, 2, 3, 4}
result = set1.issubset(set2)
print(f"Is subset: {result}")  # Output: Is subset: True

# 13. superset_check (સુપર સેટ તપાસવું)
set1 = {1, 2, 3, 4}
set2 = {1, 2}
result = set1.issuperset(set2)
print(result)  # Output: True

# 14. disjoint_check (સામાન્ય આઇટમ ન હોવી)
set1 = {1, 2, 3}
set2 = {4, 5, 6}
result = set1.isdisjoint(set2)
print(f"No common items: {result}")  # Output: No common items: True

# 15. update_set (બીજા સેટની આઇટમ ઉમેરવી)
numbers = {1, 2, 3}
numbers.update({3, 4, 5})
print(f"Updated set: {sorted(numbers)}")  # Output: Updated set: [1, 2, 3, 4, 5]

# 16. intersection_update (સામાન્ય આઇટમ રાખવી)
numbers = {1, 2, 3, 4}
numbers.intersection_update({3, 4, 5, 6})
print(f"Common numbers: {sorted(numbers)}")  # Output: Common numbers: [3, 4]

# 17. difference_update (અન્ય સેટની આઇટમ દૂર કરવી)
numbers = {1, 2, 3, 4, 5}
numbers.difference_update({2, 4})
print(f"Remaining numbers: {sorted(numbers)}")  # Output: Remaining numbers: [1, 3, 5]

# 18. pop_item (સેટમાંથી કોઈ એક આઇટમ કાઢવી)
numbers = {10, 20, 30}
removed = numbers.pop()
print(f"Removed item: {removed}")  # Output: Removed item: 10 (an arbitrary item is removed)

# 19. clear_set (સેટ ખાલી કરવો)
fruits = {"Apple", "Banana", "Mango"}
fruits.clear()
print(f"Empty set: {fruits}")  # Output: Empty set: set()

# 20. copy_set (સેટની નકલ બનાવવી)
original = {10, 20, 30}
copied = original.copy()
copied.add(40)
print(f"Original: {sorted(original)}, Copy: {sorted(copied)}")  # Output: Original: [10, 20, 30], Copy: [10, 20, 30, 40]

# 21. set_loop (લૂપ દ્વારા સેટની આઇટમ મેળવવી)
colors = {"Red", "Blue", "Green"}
for color in sorted(colors):
    print(f"Color: {color}")  # Output: Color: Blue / Color: Green / Color: Red

# 22. convert_list_to_set (લિસ્ટને સેટમાં ફેરવવું)
numbers = [1, 2, 2, 3, 3, 4]
unique_numbers = set(numbers)
print(f"Unique values: {sorted(unique_numbers)}")  # Output: Unique values: [1, 2, 3, 4]

# 23. set_comparison (બે સેટની સરખામણી)
set1 = {10, 20, 30}
set2 = {30, 20, 10}
result = set1 == set2
print(f"Sets are equal: {result}")  # Output: Sets are equal: True

# 24. mini_course_registration (નાની કોર્સ રજિસ્ટ્રેશન સિસ્ટમ)
python_students = {"Amit", "Riya", "Dhruval"}
ai_students = {"Riya", "Dhruval", "Neha"}
both_courses = python_students.intersection(ai_students)
all_students = python_students.union(ai_students)
print(f"Both courses: {sorted(both_courses)}, Total students: {len(all_students)}")  # Output: Both courses: ['Dhruval', 'Riya'], Total students: 4
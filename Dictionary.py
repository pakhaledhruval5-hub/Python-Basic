# ==========================================
# STAGE 1: PYTHON BASICS
# TOPIC 10: DICTIONARIES
# ==========================================
"""
SUMMARY DEFINITION:
English: A dictionary is a collection of key-value pairs used to store and access data.
Gujarati: Dictionary એ key-value pairs માં ડેટા સ્ટોર કરવા અને મેળવવા માટેનો ડેટા ટાઇપ છે.
"""

# 1. create_dictionary (ડિક્શનરી બનાવવી)
student = {"name": "Rahul", "age": 17}
print(student)  # Output: {'name': 'Rahul', 'age': 17}

# 2. access_value (વેલ્યુ મેળવવી)
student = {"name": "Amit", "age": 16}
name = student["name"]
print(f"Student name: {name}")  # Output: Student name: Amit

# 3. access_age (ઉંમર મેળવવી)
student = {"name": "Riya", "age": 17}
age = student["age"]
print(age)  # Output: 17

# 4. add_item (નવી માહિતી ઉમેરવી)
student = {"name": "Neha"}
student["city"] = "Surat"
print(f"Updated dictionary: {student}")  # Output: Updated dictionary: {'name': 'Neha', 'city': 'Surat'}

# 5. update_value (વેલ્યુ બદલવી)
student = {"name": "Raj", "age": 16}
student["age"] = 17
print(student)  # Output: {'name': 'Raj', 'age': 17}

# 6. remove_item (માહિતી દૂર કરવી)
student = {"name": "Raj", "age": 17}
student.pop("age")
print(f"After removal: {student}")  # Output: After removal: {'name': 'Raj'}

# 7. dictionary_length (ડિક્શનરીની લંબાઈ)
product = {"name": "Laptop", "price": 50000, "brand": "Dell"}
count = len(product)
print(count)  # Output: 3

# 8. check_key (કી હાજર છે કે નહીં તે તપાસવું)
student = {"name": "Aman", "age": 16}
exists = "name" in student
print(f"Name key exists: {exists}")  # Output: Name key exists: True

# 9. get_method (get નો ઉપયોગ)
student = {"name": "Karan", "age": 17}
city = student.get("city", "Not available")
print(city)  # Output: Not available

# 10. dictionary_keys (બધી કી મેળવવી)
student = {"name": "Mira", "age": 16, "grade": "A"}
keys = list(student.keys())
print(f"Dictionary keys: {keys}")  # Output: Dictionary keys: ['name', 'age', 'grade']

# 11. dictionary_values (બધી વેલ્યુ મેળવવી)
marks = {"Math": 90, "English": 85, "Science": 95}
values = list(marks.values())
print(values)  # Output: [90, 85, 95]

# 12. dictionary_items (કી અને વેલ્યુ મેળવવી)
fruit = {"apple": 10, "banana": 20}
items = list(fruit.items())
print(f"Fruit items: {items}")  # Output: Fruit items: [('apple', 10), ('banana', 20)]

# 13. loop_through_keys (કી પર લૂપ ચલાવવો)
student = {"name": "Jay", "age": 17}
for key in student:
    print(f"Key: {key}")  # Output: Key: name / Key: age

# 14. loop_through_values (વેલ્યુ પર લૂપ ચલાવવો)
marks = {"Math": 80, "Science": 90}
for value in marks.values():
    print(value)  # Output: 80 / 90

# 15. loop_through_items (કી-વેલ્યુ પર લૂપ ચલાવવો)
person = {"name": "Asha", "city": "Surat"}
for key, value in person.items():
    print(f"{key}: {value}")  # Output: name: Asha / city: Surat

# 16. dictionary_membership (કીની હાજરી તપાસવી)
book = {"title": "Python Basics", "pages": 200}
if "title" in book:
    message = "Title found"
else:
    message = "Title not found"
print(message)  # Output: Title found

# 17. setdefault_method (કી ન હોય તો ઉમેરવી)
settings = {"theme": "dark"}
settings.setdefault("language", "English")
print(f"Settings: {settings}")  # Output: Settings: {'theme': 'dark', 'language': 'English'}

# 18. update_method (બીજી ડિક્શનરીથી અપડેટ કરવી)
student = {"name": "Dev", "age": 16}
student.update({"age": 17, "city": "Surat"})
print(student)  # Output: {'name': 'Dev', 'age': 17, 'city': 'Surat'}

# 19. copy_dictionary (ડિક્શનરીની નકલ બનાવવી)
original = {"apple": 5, "banana": 3}
copied = original.copy()
print(f"Copied dictionary: {copied}")  # Output: Copied dictionary: {'apple': 5, 'banana': 3}

# 20. clear_dictionary (ડિક્શનરી ખાલી કરવી)
data = {"name": "Mihir", "age": 17}
data.clear()
print(data)  # Output: {}

# 21. nested_dictionary (ડિક્શનરીની અંદર ડિક્શનરી)
students = {
    "student1": {"name": "Aarav", "marks": 90},
    "student2": {"name": "Diya", "marks": 85}
}
print(f"First student: {students['student1']['name']}")  # Output: First student: Aarav

# 22. dictionary_calculation (ડિક્શનરીમાંથી ગણતરી કરવી)
marks = {"Math": 80, "English": 70, "Science": 90}
total = sum(marks.values())
print(total)  # Output: 240

# 23. dictionary_comprehension (ડિક્શનરી કમ્પ્રિહેન્શન)
squares = {number: number ** 2 for number in range(1, 5)}
print(f"Squares: {squares}")  # Output: Squares: {1: 1, 2: 4, 3: 9, 4: 16}

# 24. dictionary_frequency (દરેક અક્ષરની સંખ્યા ગણવી)
word = "banana"
frequency = {}
for letter in word:
    frequency[letter] = frequency.get(letter, 0) + 1
print(f"Letter frequency: {frequency}")  # Output: Letter frequency: {'b': 1, 'a': 3, 'n': 2}
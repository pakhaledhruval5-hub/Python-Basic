# ==========================================
# STAGE 1: PYTHON BASICS
# TOPIC 2: DATA TYPES
# ==========================================
"""
SUMMARY DEFINITION:
English: Data types define the kind of value a variable holds, telling Python 
how to treat, store, and process that specific data.
Gujarati: ડેટા ટાઇપ્સ વેરિએબલમાં સંગ્રહિત કિંમતનો પ્રકાર નક્કી કરે છે, જે પાયથનને 
જણાવે છે કે તે ચોક્કસ ડેટાને કેવી રીતે સાચવવો અને તેના પર શું પ્રક્રિયા કરવી.
"""
# ==========================================

# 1. integer type (પૂર્ણાંક સંખ્યા પ્રકાર)
runs = 85
extras = 5
total_runs = runs + extras
print(total_runs)  # Output: 90

# 2. float type (દશાંશ સંખ્યા પ્રકાર)
price = 99.50
tax = 10.50
total_bill = price + tax
print(f"Total Amount to Pay: {total_bill}")  # Output: Total Amount to Pay: 110.0

# 3. complex type (જટિલ સંખ્યા પ્રકાર)
n1 = 2 + 3j
n2 = 1 + 2j
n3 = n1 + n2
print(f"Complex Number Sum: {n3}")  # Output: Complex Number Sum: (3+5j)

# 4. string type (લખાણ પ્રકાર)
first = "Python"
second = "Language"
full_name = first + " " + second
print(full_name)  # Output: Python Language

# 5. boolean true type (સાચું બૂલિયન પ્રકાર)
score = 95
passing = 35
has_passed = score >= passing
print(has_passed)  # Output: True

# 6. boolean false type (ખોટું બૂલિયન પ્રકાર)
age = 15
limit = 18
can_drive = age >= limit
print(f"Driving License Status: {can_drive}")  # Output: Driving License Status: False

# 7. list type (લિસ્ટ પ્રકાર)
items = ["bag", "pen"]
items.append("book")
items.sort()
print(items)  # Output: ['bag', 'book', 'pen']

# 8. tuple type (ટપલ પ્રકાર)
point = (10, 20)
x = point[0]
y = point[1]
print(f"Coordinates X: {x} and Y: {y}")  # Output: Coordinates X: 10 and Y: 20

# 9. range type (શ્રેણી પ્રકાર)
start = 1
stop = 5
numbers = range(start, stop)
print(list(numbers))  # Output: [1, 2, 3, 4]

# 10. dictionary type (ડિક્શનરી પ્રકાર)
user = {"id": 1, "name": "Mitesh"}
user["city"] = "Surat"
print(f"User Hometown: {user['city']}")  # Output: User Hometown: Surat

# 11. set type (સેટ પ્રકાર)
numbers_set = {1, 2, 2, 3, 1}
numbers_set.add(4)
print(numbers_set)  # Output: {1, 2, 3, 4}

# 12. frozenset type (ન બદલાતો સેટ પ્રકાર)
words = frozenset(["apple", "banana"])
my_fruits = words
print(f"Fruits In Frozen Set: {my_fruits}")  # Output: Fruits In Frozen Set: frozenset({'apple', 'banana'})

# 13. none type (ખાલી કિંમત પ્રકાર)
data = None
is_empty = data is None
print(is_empty)  # Output: True

# 14. nonetype class classification (નનટાઇપ વર્ગ પ્રકાર)
empty_box = None
box_type = type(empty_box)
print(f"Data Class Type: {box_type}")  # Output: Data Class Type: <class 'NoneType'>

# 15. bytes type (બાઇટ્સ પ્રકાર)
text = "ABC"
byte_data = text.encode("utf-8")
print(byte_data)  # Output: b'ABC'

# 16. bytearray type (બાઇટએરે પ્રકાર)
buffer = bytearray(b"Hello")
buffer[0] = 65  # Change 'H' to 'A'
print(f"Updated Byte Array: {buffer}")  # Output: Updated Byte Array: bytearray(b'Aello')

# 17. memoryview type (મેમરીવ્યુ પ્રકાર)
binary = b"XYZ"
view = memoryview(binary)
first_byte = view[0]
print(f"Byte Value At Index 0: {first_byte}")  # Output: Byte Value At Index 0: 88

# 18. slice type (સ્લાઇસ પ્રકાર)
word = "ABCDEF"
my_slice = slice(0, 4, 2)
result = word[my_slice]
print(result)  # Output: AC

# 19. datetime type (તારીખ અને સમય પ્રકાર)
from datetime import datetime
my_date = datetime(2026, 10, 13, 0, 0)
clean_date = my_date.strftime("%Y-%m-%d")
print(f"Target Project Date: {clean_date}")  # Output: Target Project Date: 2026-10-13

# 20. precise decimal type (ડેસિમલ પ્રકાર)
from decimal import Decimal
d1 = Decimal("0.1")
d2 = Decimal("0.2")
d3 = d1 + d2
print(f"Exact Decimal Sum: {d3}")  # Output: Exact Decimal Sum: 0.3

# 21. fraction type (અપૂર્ણાંક પ્રકાર)
from fractions import Fraction
f1 = Fraction(1, 2)
f2 = Fraction(1, 4)
f3 = f1 + f2
print(f3)  # Output: 3/4

# 22. array type (એરે પ્રકાર)
import array
my_arr = array.array('i', [1, 2, 3])
my_arr.append(4)
print(my_arr)  # Output: array('i', [1, 2, 3, 4])

# 23. custom object type (ઓબ્જેક્ટ પ્રકાર)
class Demo:
    def __init__(self):
        self.val = "Test"
obj = Demo()
print(f"Object Class Name: {type(obj)}")  # Output: Object Class Name: <class '__main__.Demo'>

# 24. typecasting conversion (પ્રકાર રૂપાંતરણ પ્રકાર)
num_str = "500"
num_int = int(num_str)
ans = num_int * 2
print(f"Typecasted Final Answer: {ans}")  # Output: Typecasted Final Answer: 1000

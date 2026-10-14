# ==========================================
# STAGE 1: PYTHON BASICS
# TOPIC 1: VARIABLES
# ==========================================
"""
SUMMARY DEFINITION:
English: A variable is an easy named box used to store data values in memory 
that can be changed anytime.
Gujarati: વેરિએબલ એટલે મેમરીમાં ડેટા સાચવવાનું એક સરળ નામવાળું બોક્સ, 
જેની કિંમત ગમે ત્યારે બદલી શકાય છે.
"""
# ==========================================

# 1. single assignment (સામાન્ય વેરિએબલ અને ગણતરી)
price = 500
discount = 50
total = price - discount
print(total)  # Output: 450

# 2. multiple assignment (એક સાથે અલગ કિંમતો)
x, y, z = 10, 20, 30
ans = x + y + z
print(f"Total Sum: {ans}")  # Output: Total Sum: 60

# 3. chained assignment (એક જ કિંમત બધા વેરિએબલને)
a = b = c = 50
b = b + 10
res = a + b
print(f"Result Value: {res}")  # Output: Result Value: 110

# 4. dynamic reassignment (કિંમત અને ડેટા પ્રકાર બદલવો)
score = 100
print(f"Old Score: {score}")  # Output: Old Score: 100
score = "Pass"
print(f"New Status: {score}")  # Output: New Status: Pass

# 5. variable swapping (બે વેરિએબલની કિંમત અદલાબદલી કરવી)
num1 = 5
num2 = 10
num1, num2 = num2, num1
print(num1)  # Output: 10
print(num2)  # Output: 5

# 6. list unpacking (લિસ્ટમાંથી કિંમતો વેરિએબલમાં લેવી)
colors = ["Red", "Green", "Blue"]
c1, c2, c3 = colors
print(c1)  # Output: Red
print(c2)  # Output: Green

# 7. extended unpacking (બાકીની કિંમતો નવા લિસ્ટમાં સ્ટોર કરવી)
marks = [90, 80, 70, 60]
first, *rest = marks
print(first)  # Output: 90
print(rest)   # Output: [80, 70, 60]

# 8. tuple unpacking (ટપલ ડેટામાંથી વેરિએબલ્સ અલગ કરવા)
point = (12, 15)
x_pos, y_pos = point
print(x_pos)  # Output: 12
print(y_pos)  # Output: 15

# 9. underscore variable name (અંડરસ્કોરથી શરૂ થતું નામ)
_secret = 999
check = _secret + 1
print(f"Secret Number: {check}")  # Output: Secret Number: 1000

# 10. case sensitivity check (કેપિટલ અને સ્મોલ અક્ષરોનો તફાવત)
val = 5
VAL = 10
total_val = val * VAL
print(f"Multiplied Answer: {total_val}")  # Output: Multiplied Answer: 50

# 11. snake_case convention (પાયથન સ્ટાન્ડર્ડ નામકરણ પદ્ધતિ)
user_age = 20
gift_year = 5
next_age = user_age + gift_year
print(f"Future Age: {next_age}")  # Output: Future Age: 25

# 12. constant variable (ન બદલાતી કિંમત દર્શાવવા મોટો અક્ષર)
PI = 3.14
r = 10
area = PI * r * r
print(f"Circle Area: {area}")  # Output: Circle Area: 314.0

# 13. type hint variable (પ્રકાર દર્શાવીને વેરિએબલ બનાવવો)
count: int = 5
msg: str = "Hello"
print(f"Message count: {msg} {count}")  # Output: Message count: Hello 5

# 14. global variable (ફંક્શનની બહારનો ગ્લોબલ વેરિએબલ)
name = "Mitesh"
def say_hello():
    msg = "Welcome"
    print(f"{msg} {name}")
say_hello()  # Output: Welcome Mitesh

# 15. local variable (ફંક્શનની અંદરનો લોકલ વેરિએબલ)
def make_sum():
    n1 = 20
    n2 = 30
    print(f"Local Sum: {n1 + n2}")
make_sum()  # Output: Local Sum: 50

# 16. global keyword (ફંક્શનની અંદરથી બહારનો વેરિએબલ બદલવો)
run = 0
def add_run():
    global run
    run = run + 4
add_run()
print(f"Total Runs: {run}")  # Output: Total Runs: 4

# 17. nonlocal keyword (નેસ્ટેડ ફંક્શનમાં અંદરની કિંમત બદલવી)
def outer():
    num = 1
    def inner():
        nonlocal num
        num = 5
    inner()
    print(f"Final Count: {num}")
outer()  # Output: Final Count: 5

# 18. walrus operator (અસાઇનમેન્ટ અને પ્રિન્ટ એક જ લાઈનમાં)
a = 10
print(b := a + 5)  # Output: 15

# 19. string concatenation (વેરિએબલ્સને ભેગા કરીને જોડવા)
start = "Hello"
end = "World"
full = start + " " + end
print(full)  # Output: Hello World

# 20. expression assignment (ગણતરી કરીને સ્ટોર કરવું)
n1 = 10
n2 = 5
res = (n1 + n2) * 2
print(f"Expression Output: {res}")  # Output: Expression Output: 30

# 21. variable memory address (વેરિએબલનું મેમરી એડ્રેસ જાણવું)
m = 100
addr = id(m)
print(f"Memory Address Number: {addr}")  # Output: Memory Address Number: <Address_Number>

# 22. same memory reference (બે વેરિએબલ એક જ મેમરી એડ્રેસ પોઇન્ટ કરે છે)
list1 = [1, 2]
list2 = list1
check = id(list1) == id(list2)
print(f"Reference Match Status: {check}")  # Output: Reference Match Status: True

# 23. eval function assignment (વેરિએબલની સ્ટ્રિંગને કોડ તરીકે ચલાવવી)
code_str = "10 + 20"
ans = eval(code_str)
print(f"String Calculation Output: {ans}")  # Output: String Calculation Output: 30

# 24. delete variable (વેરિએબલને મેમરીમાંથી ડીલીટ કરવો)
temp = "Delete"
del temp
status = "Variable Removed"
print(f"System Message: {status}")  # Output: System Message: Variable Removed



# 🐍 Python Variables & Scope Tutorial

## 1. What is a Variable
#A variable is a **name that stores a value**.
score = 42
player = "Arjun"

print(score)     # Output: 42
print(player)    # Output: Arjun


## 2. Rules for Naming Variables
# - ✅ Letters, digits, underscores allowed
# - ❌ Cannot start with a digit
# - ✅ Case-sensitive (`data` ≠ `Data`)
# - ❌ Avoid keywords (`class`, `for`, `while`)

student_age = 19
favorite_color = "turquoise"
exam_score = 88

# ❌ Invalid
# 2city = "Error"
# def = 25
# user-name = "Alice"


## 3. Assigning Values
height = 175
weight = 68.5
message = "Welcome!"


## 4. Dynamic Typing
#Python variables can change type during execution.
data = 42          # int
data = "forty-two" # str


## 5. Multiple Assignments
#- **Same Value to Multiple Variables**
p = q = r = 200
print(p, q, r)   # Output: 200 200 200


#- **Different Values in One Line**
alpha, beta, gamma = "dog", 7.2, False
print(alpha, beta, gamma)   # Output: dog 7.2 False


## 6. Object References
#Variables point to objects, not values directly.
num1 = 15
num2 = num1   # num2 references the same object as num1

num1 = "changed"
print(num2)   # Still 15


## 7. Type and Casting
price = "499"
print(type(price))        # <class 'str'>

converted_price = int(price)
print(converted_price + 1)  # Output: 500


value = 15
print(type(value))   # <class 'int'>

amount = "250"
converted = float(amount)
print(converted + 50)       # Output: 300.0


## 8. Deleting Variables
temp = 99
del temp
print(temp)   # NameError: temp is not defined


## 9. Practical Examples
#- **Swapping Two Variables**
first, second = "left", "right"
first, second = second, first
print(first, second)   # Output: right left


#- **Counting Characters**
phrase = "OpenAI Copilot"
length = len(phrase)
print("Length:", length)   # Output: Length: 14


## 🔑 Scope in Python (LEGB Rule)

### 1. Local Scope
def greet():
    message = "Hello from local scope"
    print(message)

greet()
# print(message) → Error


### 2. Enclosing Scope
def outer():
    text = "Outer variable"
    def inner():
        print(text)   # Access enclosing scope
    inner()

outer()


### 3. Global Scope
site_name = "Python.org"

def show():
    print(site_name)   # Access global variable

show()
print(site_name)


### 4. Built-in Scope
print(len("Bangalore"))   # Uses built-in len()


## 📝 Key Takeaways

# - Variables are **names pointing to objects**.
# - Python is **dynamically typed**.
# - Multiple assignments make code concise.
# - Variables reference objects, not values directly.
# - Use `type()` and casting functions for conversions.
# - `del` removes variables from memory.
# - Scope follows the **LEGB rule**: Local → Enclosing → Global → Built-in.


# Section 1 - Variables and Types
name = "Mariana"
age = 39
height = 5.5
is_student = True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))

# Section 2 - User Input Mat
name = input("What is your name?")
birth_year = input("what year were you born?")
birth_year = int(birth_year)
age = 2026 - birth_year
print(f"Hi, {name}! You are aproximately {age} years old.")


# Section 3 - Type Conversion and f-strings

num1 = input("18")
num2 = input("87")

num1 = float(num1)
num2 = float(num2)

result = num1 * num2

print(f"{num1} x {num2} = {result}")

# Section 4 - Formatted Receipt

Item = "String of Hearts Plant"
price = 15.99
quantity = 2

total = price * quantity

print("=================")
print("    RECEIPT")
print("=================")
print(f"Item: {Item}")
print(f"Price: ${price:.2f}")
print(f"Quantity: {quantity}")
print("----------------")
print(f"Total: ${total:.2f}")
print("=================")


# Section 5 

name = input("What is your name?")
hometown = input("What is your hometown?")
hobby = input("What is your favorite hobby?")
fun_fact = input("Tell me one fun fact about yourself")
birth_year = input("What year were you born?")

birth_year = int(birth_year)
age = 2026 - birth_year

print("===========")
print(f"     PROFILE:{name}")
print("===========")
print(f"Hometown: {hometown}")
print(f"Hobby:    {hobby}")
print(f"Fun fact: {fun_fact}")
print(f"Age:      {age}")
print("===================")

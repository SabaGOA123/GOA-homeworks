# 3)მოიყვანეთ მინიმუმ 5 მაგალითი Implicit Type Conversion-ზე

# 1: int + float → float
a = 10        # int
b = 3.5       # float
result = a + b   # a ავტომატურად გარდაიქმნება float-ად
print(result)    # 13.5
print(type(result))  # <class 'float'>

# 2: გაყოფა int / int → float
x = 5
y = 2
z = x / y   # მიუხედავად იმისა, რომ ორივე int-ია, შედეგი float-ია
print(z)         # 2.5
print(type(z))   # <class 'float'>

# 3: bool + int → int
a = True     # მნიშვნელობა არის 1 (bool არის int-ის ქვეტიპი)
b = 4
result = a + b
print(result)       # 5
print(type(result)) # <class 'int'>

# 4: int გადადის complex-ში 
a = 7          # int
b = 3 + 2j     # complex
result = a + b
print(result)       # (10+2j)
print(type(result)) # <class 'complex'>

# 5: int + bool
a = 0
b = False     # False არის 0, True კი 1
print(a + b)        # 0
print(type(a + b))  # <class 'int'>

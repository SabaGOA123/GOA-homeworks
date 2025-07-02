# 4)მოიყვანეთ მინიმუმ 5 მაგალითი Explicit Type Conversion-ზე

# 1: str → int
a = "25"
b = int(a)
print(b + 5)     # 30
print(type(b))   # <class 'int'>

# 2: float → int
x = 7.8
y = int(x)
print(y)         # 7
print(type(y))   # <class 'int'>

# 3: int → float
a = 10
b = float(a)
print(b)         # 10.0
print(type(b))   # <class 'float'>

# 4: int → str
num = 100
text = str(num)
print(text)         # "100"
print(type(text))   # <class 'str'>

# 5: list → tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)         # (1, 2, 3)
print(type(my_tuple))   # <class 'tuple'>

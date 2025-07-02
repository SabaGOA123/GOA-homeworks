# 5)თქვენი სიტყვებით აღწერეთ რა არის concatenation , მოიყვანეთ მაგალითები


# Concatenation ნიშნავს სტრინგების შეერთებას (გადაბმას)
# 1: ორი სტრინგის შეერთება
a = "Hello"
b = "World"
c = a + " " + b
print(c)   # შედეგი: Hello World

# 2: სტრინგი + რიცხვი (რიცხვი გადავაქციეთ სტრინგად)
age = 18
text = "I am " + str(age) + " years old"
print(text)   # შედეგი: I am 18 years old

# 3: სტრინგების შეერთება პირდაპირ
print("Python " + "is " + "awesome!")  # შედეგი: Python is awesome!

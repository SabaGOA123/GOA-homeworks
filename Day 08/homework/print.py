# 1)ჩამოწერეთ ყველა მონაცემთა ტიპი რაც ვისწავლეთ და გვერდით მიუწერეთ დეტალური აღწერა


# int - მთელი რიცხვი
whole_number = 42
print(type(whole_number))  # <class 'int'>

# float - ათწილადი რიცხვი
decimal_number = 3.14159
print(type(decimal_number))  # <class 'float'>

# str - სტრინგი, ტექსტი
text = "გამარჯობა, Level 9!"
print(type(text))  # <class 'str'>

# bool - ბულიანი ტიპი (True ან False)
is_sunny = True
print(type(is_sunny))  # <class 'bool'>

# list - სია, ელემენტების შეკრება, რომელიც შეიცვლება
fruits = ["ვაშლი", "ბანანი", "გრეიფრუტი"]
print(type(fruits))  # <class 'list'>

# tuple - ტუპლი, ელემენტების შეკრება, უცვლადი
coordinates = (10.0, 20.0)
print(type(coordinates))  # <class 'tuple'>

# set - არანაკლებად უნიკალური ელემენტები, წესრიგი არ არსებობს
unique_numbers = {1, 2, 3, 3, 2}
print(unique_numbers)  # {1, 2, 3}
print(type(unique_numbers))  # <class 'set'>

# dict - ლექსიკონი, გასაღები-მნიშვნელობის წყვილები
person = {
    "სახელი": "saba",
    "ასაკი": 14,
    "თემატიკა": "Python"
}
print(type(person))  # <class 'dict'>

# NoneType - None, ცარიელი მნიშვნელობა
nothing = None
print(type(nothing))  # <class 'NoneType'>

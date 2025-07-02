# 6)მომხმარებელს შემოატანინეთ დაბადების წელი  , შემდეგ age-ცვლადში გამოთვალეთ რამდენი წლის არის მომხმარებელი ახლა და საბოლოოდ ტერმინალში დაბეჭდეთ შედეგი

from datetime import datetime

birth_year = int(input("2010"))

current_year = datetime.now(2025).year

age = current_year - birth_year

print("შენ ხარ", age, "წლის.")

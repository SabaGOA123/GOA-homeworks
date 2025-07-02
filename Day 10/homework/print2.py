# 2)თქვენი სიტყვებით აღწერეთ რა არის , Implicit Type Conversion და Explicit Type Conversion

#  Implicit Type Conversion (ფარული ტიპის გარდაქმნა)
# ეს არის მონაცემის ტიპის ავტომატური შეცვლა, რომელსაც Python (ან სხვა ენა) თვითონ აკეთებს პროგრამისტის ჩარევის გარეშე 
a = 5       # int
b = 2.0     # float
result = a + b  # Python ავტომატურად გარდაქმნის 'a'-ს float-ში
print(result)   # 7.0 (float)

#  Explicit Type Conversion (ხილული /ცხადი ტიპის გარდაქმნა)
# ეს არის შემთხვევა, როცა პროგრამისტი თვითონ ცვლის ტიპს შესაბამისი ფუნქციებით (int, float,str და ა.შ.)
a = "10"        # str
b = int(a)      # აქ ხდება 'str' → 'int' გარდაქმნა
print(b + 5)    # 15

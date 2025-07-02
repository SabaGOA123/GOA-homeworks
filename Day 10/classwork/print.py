# 1)შექმენი 2 ცვლადი , შიგნით შეინახე integer-ტიპის მნიშვნელობები , თქვენი მიზანია ამ ორი ცვლადს(რიცხვის) გამოყენებით მოახდინოთ implicit convertion (ტიპის შეცვლა ფარულად)

a = 5       # integer ტიპის ცვლადი
b = 2       # integer ტიპის ცვლადი

result = a / b   # აქ ხდება implicit conversion: int / int → float

print("შედეგი:", result)
print("ტიპი:", type(result))

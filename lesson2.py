import math
side = int(input("請輸入對邊"))
another_side = int(input("請輸入斜邊"))
sin = side/another_side
radian = math.asin(side/another_side)
degree = math.degrees(radian)
print(round(degree,2)) # 小數點後位數ndigits的默認值= 0
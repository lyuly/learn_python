cars = ['bmw', 'audi', 'toyota', 'subaru']
# 从小到大排序且排序不可逆转
# cars.sort()
# print(cars)
# # 从大到小排序
# cars.sort(reverse=True)
# print(cars)

# print("Here is the original list:")
# print(cars)

# # 临时排序
# print("\nHere is the sorted list:")
# print(sorted(cars))

# print("\nHere is the original again:")
# print(cars)

# # 反转列表
# cars.reverse()
# print(cars)

# # 确定列表长度
# print(len(cars))

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
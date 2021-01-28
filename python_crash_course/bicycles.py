bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# message = "My first bicycle was a " + bicycles[0].title() + "."
# print(message)

# 向列表末尾添加元素
# bicycles.append('Ok')

# for i in range(0,4):
#     print(bicycles[i])

# 向列表0处插入元素，既有的每个元素都右移一个位置
# bicycles.insert(0,'Hello')

# for i in bicycles:
#     print(i)

# 删除指定的列表元素
# del bicycles[0]

# for i in range(len(bicycles)):
#     print(bicycles[i])

# pop删除列表末尾的元素
# pop_bicycles = bicycles.pop()
# print(bicycles)
# print(pop_bicycles)

# 移除指定的元素
bicycles.remove('trek')
print(bicycles)
name = ['zhangsan', 'lisi', 'wangwu']
print(name)

print(name[2] + "无法赴约.")
name[2] = 'liusan'
print(name)

print("找到了一张更大的餐桌")
name.insert(0, 'zhaoxi')
name.insert(2,'shenhan')
name.append('suner')
print(name)

print("只能邀请两位")
name1 = name.pop()
print("很抱歉" + name1)
name2 = name.pop()
print("很抱歉" + name2)
name3 = name.pop()
print("很抱歉" + name3)
name4 = name.pop()
print("很抱歉" + name4)
name5 = name.pop(1)
print("欢迎" + name5)
name6 = name.pop(0)
print("欢迎" + name6)
# del name[0]
# del name[1]
print(name)
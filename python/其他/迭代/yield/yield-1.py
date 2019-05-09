#coding=utf-8

# Intialize the list
my_list = [1, 3, 6, 10]

a = (x**2 for x in my_list)

print(type(a))

# Output: 1
print(next(a))
# print(a.next())   = print(next(a))

# Output: 9
print(next(a))

# Output: 36
print(next(a))

# Output: 100
print(next(a))


print(my_list.__iter__())
print(my_list.__iter__())
print(my_list.__iter__())
print(my_list.__iter__())
# print(my_list.__iter__())
print(iter(my_list))
print(iter(my_list))
print(iter(my_list))
print(iter(my_list))
print(iter(my_list))




# Output: StopIteration
# next(a)

# 生成器可用于管理一系列操作，下面使用一个例子说明。假设我们有一个快餐连锁店的日志文件。
# 志文件有一列(第4列)，用于跟踪每小时销售的比萨饼数量，我们想算出在5年内销售的总萨饼数量。假设一切都是字符串，不可用的数字标记为“N / A”。
# 这样做的生成器实现可以如下。with open('sells.log') as file:
#     pizza_col = (line[3] for line in file)
#     per_hour = (int(x) for x in pizza_col if x != 'N/A')
#     print("Total pizzas sold = ",sum(per_hour))

name = "Jagan"
num = 10
print(id(name))
print(id(num))

a = 10
b = a
print(id(a))
print(id(b))
# If the data value is same, variable store at only one place of memory like below
# O/P will be
# 1728726236080
# 1728724730384
# 1728724730384
# 1728724730384
# _*_coding : utf-8 _*_
# @Time : 22/8/2022  下午9:49
# @Author : Bay
# @File : Py016_类型转换_转换为布尔类型,
# @Project : Python_learn

# a =1
# print(type(a))
# # 将整数类型变为布尔类型的数据
# b = bool(a)
# print(b)
# print(type(b))

# a = 2
# print(type(a))
#
# b = bool(a)
# print(b)
# print(type(b))


# 对非零整数(包含正数负数)进行布尔类型的转换，那全是True


# a = -1
# print(type(a))
#
# print(type(a))
#
# b = bool(a)
#
# print(b)
# print(type(b))

# a = 0
# print(type(a))
# #在整数范围内，0强制为转换为bool类型结果为false
# b =bool(a)
# print (b)
# print(type(b))


#浮点数
#
# a =1.0
# print(type(a))
#
# b = bool(a)
# print(type(b))
# print(b)
# a = -1.0
# print(type(a))
#
# b = bool(a)
# print(type(b))
# print(b)

# a = 0.0
# print(type(a))
#
# b = bool(a)
# print(type(b))
# print(b)

#字符串
#只要字符串有内容，转换bool类型时，返回True
#字符串无内容，转换bool类型时，返回False
# a = "王国灌灌灌灌"
# print(type(a))
#
# b = bool(a)
#
# print(b)
# print(type(b))




# a = "    "
# print(type(a))
#
# b = bool(a)
#
# print(b)
# print(type(b))

# a = ""
# print(type(a))
#
# b = bool(a)
#
# print(b)
# print(type(b))

#列表
#只要列表有数据，那么强制转换为Bool则为True
#如果列表什么数据都么有，返回的数字为False

a = ['s','sdd','eqdqef','sacawwscasdc']
print(type(a))

b = bool(a)
print(b)
print(type(b))
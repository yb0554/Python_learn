# # _*_coding : utf-8 _*_
# # @Time : 18/8/2022  下午4:32
# # @Author : Bay
# # @File : Py013_类型转换_转为整型,
# # @Project : Python_learn
#
# # 转换为整型
# # str -->int
#
# a = '123'
# print(type(a))
# # 将字符串转为整数
# b = int(a)
# print(type(b))
#
# # float --> int
# c = 1.23
# # 如果浮点数转为整数，会返回小数点的前的数
#
# print(type(c))
# d = int(c)
# print(d)
# print(type(d))
#
# # boolean -->int
# e =True
# # True -->1 False -->0
# print(type(e))
# f = int(e)
# print(f)
# print(type(f))


# 1.23和12ba字符串，包含非法字符，不能转换为整数，则报错
# 如果字符传包含非法字符，则报错
# a = '1.23'
# print(type(a))
# b = int(a)
# print(b)

# a = '12ba'
# print(type(a))
# b = int(a)
# print(b)
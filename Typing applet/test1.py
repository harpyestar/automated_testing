# from datetime import datetime
#
# print(datetime.now())

# def square():
#     for x in range(4): # 0123
#         yield x ** 2
#
# square_gen = square()
#
# for x in square_gen:
#     print(x)

# # 包含yield关键字，就变成了生成器函数
# # 调用函数并不会执行语句
# def foo():
#     print('Starting.....')
#     while True:
#         res = yield 4
#         print("res:", res)
#
# # 下面调用函数并没有执行，可以先将后面的语句注释掉
# # 逐行运行代码观察效果
# g = foo()
# print("第一次调用执行结果：")
# print(next(g))
# print("*" * 100)
# print("第二次调用执行结果：")
# print(next(g))
# print("*" * 100)
# print("第三次调用执行结果：")
# print(next(g))
# print("*" * 100)

# str1 = "123"
# int1 = 8
# a = "开始：%s,%d \n" % (str1,int1)
#
# print(a)

# def func(*args, **kwargs): # *args:不定长参数, **kwargs：不定长的关键字传参
#     for i in args:
#         print(i)
#
#     for key, value in kwargs.items():
#         print(key, value)
#
# func(1,2,3,key="1", key1="2")

func = lambda x:x+2

a = func(2)
print(a)


b = list(map(func, [1,2,3]))
print(b)
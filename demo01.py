"""
print("你好！") #字符串
print(2.333) #小数
print(True) #布尔值  用来判断对错  TRUE or False
print(()) #元组
print([]) #数组
print({}) #字典

锄禾日当午
   汗滴禾下土


print("哈哈",2333,2.333)

print("哈哈"+"嘻嘻") #字符串的拼接  注意：只能用于相同的数据类型
print("哈哈哈"*100)  #加倍的效果，打印100个“哈哈哈”

print(((1+2)*100-99)/2) #做数学运算
print(((1+2)*100-9.9)/2)

print(2>3)

#重要概念：变量和赋值   注：变量必须是小写字母，而且不要用特殊符号
name = "张三"   #表示把“张三”这个值赋给了名字叫name的这个变量
print(name)

"""

"""
a = input("请输入：")
b = input("请输入：")
print("input获取的内容：",a+b)
"""

"""
#数据格式的转换
print(type("哈哈"))
print(type(2333))
print(type(2.33))
print(type(True))
print(type(()))
print(type([]))
print(type({}))

a = input("请输入：")
b = input("请输入：")
a = int (a)
b = int   (b)
print("input获取的内容：",a+b)
"""

#练习：通过代码获取两段内容，并且计算它们的长度的和。(python第一节萌芽计划作业)
'''自己下写的代码：
a='dhkfjfmjweifjladf'
b='qwudhgasneerhudfjkgjhmlsaldjfkgl'

print(len(a))
print(len(b))
print(len(a+b))
'''

#浪老师写的的代码：
a=input("请输入:")
b=input("请输入:")
print("两端字符串的长度是：",len(a)+len(b))
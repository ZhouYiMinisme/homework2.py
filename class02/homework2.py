#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/9/10 16:09
# @Author : 毅敏
# @Version：V 0.1
# @File : homework2.py
# @desc :

"""
1、用print函数打印多个值
"""
import math
import random

name='yimin'
sex='男'
print(f'姓名：{name} 性别：{sex}')

"""
2、用print函数不换行打印

"""
like='comic'
age=18
print("爱好"+like,"年龄"+str(age), end=' ')
print('haha')

"""
3、导入模块的方式有哪些
方式一：使用 import 语句来引入模块
方式二：使用from…import 语句来引入模块
方式三：使用from…import* 语句来引入模块
"""

"""
4、python有哪六种数据类型？不可变数据类型有哪些？可变数据类型有哪些？

在Python中不可变的数据类型有3种，分别是整型、字符串和元组。
可变数据类型：列表list和字典dict

"""
"""
5、python3中可以支持哪些数值类型？
Python3 中有六个标准的数据类型：Number（数字） + String（字符串） + List（列表） + Tuple（元组） + Sets（集合） + Dictionary（字典）。
"""
"""
6、判断变量类型有哪些方式，分别可以用哪些函数？
1、isinstance(变量名，类型)
2、通过与其他已知类型的常量进行对比
"""

"""
7、分别对49.698作如下打印
	1）四舍五入，保留两位小数
	2）向上入取整
	3）向下舍取整
	4）计算8除以5返回整型
	5）求4的2次幂
	6）返回一个（1,100）随机整数
"""
num=49.698
print("四舍五入%.2f"%num)
print("四舍五入{:.2f}".format(num))
print("向上取整%d" %math.ceil(num))
print("向下取整%d" %math.floor(num))

print("8除以5返回整形%u" %(8/5))

num2 = 4 ** 2
print("4的2次幂", num2)

print("返回1到100随机数%d"%random.randint(1,101))

"""
8、依次对变量a,b,c赋值为1,2,3
"""
a,b,c=1,2,3
print(a,b,c)

"""
9、截取某字符串中从2索引位置到最后的字符子串
"""
str1 = "zymisme"
print(str1[2:])
"""
10、对字符串“testcode”做如下处理：
"""
str2="testcode"
print("翻转"+str2[::-1])


print("大写首字母"+str2.capitalize())

list1=['test', 'code']
print(''.join(list1))



#3)，查找是否包含code子串，并返回索引值

print(str2.find('code'))
print(str2.index('code'))

   #4）判断字符串的长度
print(len(str2))

   #5）从头部截取4个长度字符串
print(str2[0:4])

   #6）把code替换为123
#print(str2[0:4]+'123')
print(str2.replace('code','123'))     #replace(原字符串，替换字符，替换次数)，replace只改变副本的值，不会改变原值

#7）把“test code”字符串中的两个单词转换为列表中的元素，并打印处理
str3="test code"
print(str3.split(" "))       #split（字符/字符串），分割后的元素会存放到列表中

#8）把['test','code']把list变量中的元素连接起来
list1=['test', 'code']
print(''.join(list1))   #jion(连接字符，原字符串)

   #11、如何打印出字符串“test\ncode”
print(r'test\ncode')

    #12、如何创建一个空元组
tuple1=()

    #13、创建一个只包含元素1的元组，并打印出该变量的类型
tuple2=(1,)
print(type(tuple2) )

    #14、元组中元素可以修改？如何更新元组中的元素？
#修改字符串只能通过拼接+


#15、对元组（1,2,3,4,5)做如下操作：
tuple3=(1,2,3,4,5)
   #1）取倒数第二个元素
print(tuple3[-2])

   #2）截取前三个元组元素
print(tuple3 [0:3])

   #3）依次打印出元组中所有元素
print(tuple3[:])

#16、把元组(1,2,3,4,5,6)元素格式化成字符串

tup1=(1, 2, 3, 4, 5, 6)
print('{}'.format(tup1))
print(type(tup1))
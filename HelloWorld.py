#coding=utf-8
Total = "nihao"+\
    "zhege "+\
    "shijie"

# print Total;

days = ['Monday',"Tuesday",
        "Friday"]
# print days;

word = 'word';
sentence = "zhe shi yi ge ju zi";
paragraph = """这是一段话，这是一段话，
这是一段话,包含了多个语句""";

# print word,sentence,paragraph;
"""
奇葩的注释
"""
'''
奇葩的注释
'''
# 记住：空行也是程序代码的一部分。


# raw_input("按下enter退出，其他任意键显示……\n")

# import sys; x = 'runoob'; sys.stdout.write(x + '\n')

# a = b = c = 100;
# a,b,c = "nihao","wohao","dajiahao"
# print a,b,c

s = "abcdef";
# print s[1:4]
# print s * 5 +"  nihao"
'''
元组是另一个数据类型，类似于List（列表）。
元组用"()"标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。
'''

'''
Python 字典
字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象集合，字典是无序的对象集合。
两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典用"{ }"标识。字典由索引(key)和它对应的值value组成。
'''
dict = {}
dict['one'] = "this is one"
dict[2] = "this is two"
tinydict = {"name":"john","age":"23","sex":"male"}

print dict['one']
print dict[2]
print tinydict
print tinydict.keys()
print tinydict.values()

#!/usr/bin/env python3
# coding=utf-8
from math import exp, log, sqrt
import re

# Print a simple string
print ("Output #1:I'm excited to learn Python.")

# This line and the next line are comment lines
# Add two numbers together
x = 4
y = 5
z = x + y
print ("Output #2:Four plus five equals {0:d}".format(z))

# This Line and the next line are comment lines
# Add two lists together
a = [1, 2, 3, 4]
b = ["first", "second", "third", "fourth"]
c = a + b
print ("Output #3: {0},{1},{2}".format(a, b, c))

x = 9
print ("Output #4: {0}".format(x))
print ("Output #5: {0}".format(3 ** 4))
print ("Output #6: {0}".format(int(8.3) / int(2.7)))
print ("Output #7: {0:.3f}".format(8.3 / 2.7))
y = 2.5 * 4.8
print ("Output #8: {0:.1f}".format(y))
r = 8 / float(3)
print ("Output #9: {0:.2f}".format(r))
print ("Output #10: {0:.4f}".format(8.0 / 3))

print ("Output #11: {0:.4f}".format(exp(3)))
print ("Output #12: {0:.2f}".format(log(4)))
print ("Output #13: {0:.1f}".format(sqrt(81)))

# 单引号的字符串中的‘前需要加\,双引号内就不需要
print ("Output #14: {0:s}".format('I\'m enjoying learning Python.'))

# 用3个单引号或者3个双引号来创建多行字符串
print ("Output #15: {0:s}".format("This is a long string.Without the backslash\
it would run off of the page on the right in the text editor and be very\
difficult to read and edit."))
print ("Output #16:{0:s}".format('''you can use triple single quotes for multi-line comment strings.'''))
print ("Output #17:{0:s}".format("""you can also use triple double quotes for multi-line comment strings."""))

string1 = "This is a "
string2 = "short string."
sentence = string1 + string2
print ("Output #18: {0:s}".format(sentence))
print ("Output #19: {0:s} {1:s} {2:s}".format("She is", "very " * 4, "beautiful"))
m = len(sentence)
print ("Output #20: {0:d}".format(m))

# split 函数
str1 = "My deliverable is due in May"
str1_list1 = str1.split()
str1_list2 = str1.split(" ", 2)
print("Output #21: {0}".format(str1_list1))
print("Output #22: FIRST PIECE:{0} SECOND PIECE:{1} THIRD PIECE:{2}".format(str1_list2[0]
                                                                            , str1_list2[1]
                                                                            , str1_list2[2]))
str2 = "Your,delivery,is,due,in,June"
str2_list = str2.split(',')
print("Output #23:{0}".format(str2_list))
print("Output #24:{0}{1}{2}".format(str2_list[1], str2_list[5],
                                    str2_list[-1]))

# 2017年11月23日
# join
print("Output #25:{0}".format(','.join(str2_list)))  # 表示使用，将字符串链接起来

# strip 删除字符串两端的空格( )、制表符（\t）、换行符(\n)
string3 = "  Remove unwanted characters   from this string.\t\t    \n"
print("Output #26: string3: {0:s}".format(string3))
string3_lstrip = string3.lstrip()
print("Output #27: lstrip: {0:s}".format(string3_lstrip))
string3_rstrip = string3.rstrip()
print("Output #28: rstrip: {0:s}".format(string3_rstrip))
string3_strip = string3.strip()
print("Output #29: strip: {0:s}".format(string3_strip))

# strip删除字符串两端的其他字符
string4 = "$$Here's another string that has unwanted characters.__++----"
print("Output #30: {0:s}".format(string4))
string4_strip = string4.strip('$_+-')
print("Output #31: {0:s}".format(string4_strip))

# replace
string5 = "Let's replace the space in this sentence with other characters."
string5_replace = string5.replace(" ", "!@!")
print("Output #32: {0:s}".format(string5_replace))
string5_replace = string5.replace(" ", ",")
print("Output #33: {0:s}".format(string5_replace))

# lower upper capitalize
string6 = "Here's WHAT Happens WHEN You Use lower."
print("Output #34: {0:s}".format(string6.lower()))
string7 = "Here's what Happens when You Use UPPER."
print("Output #35: {0:s}".format(string7.upper()))
string8 = "here's WHAT Happens WHEN you use Capitalize."
print("Output #36: {0:s}".format(string8.capitalize()))
string8_list = string8.split()
print("Output #37(on each word): ")
for word in string8_list:
    print("{0:s}".format(word.capitalize()))


# 计算字符串中模式出现的次数
string = "The quick brown fox jumps over the lazy dog."
string_list = string.split()
pattern = re.compile(r"The",re.I)
count = 0
for word in string_list:
    if pattern.search(word):
        count += 1
print ("Output #38:{0:d}".format(count))

# 欢迎来到Excel编程项目

在这个项目里，你将着手编写一个实现一些简易功能的Excel。该Excel需要实现的功能已经在/test/model中的三个测试文件中定义完成，
请你从test_spreadsheet1.py开始，按照定义好的测试案例来完善在/src/model下的spreadsheet.py文件。请你尽可能多得完善Excel的功能来
满足测试案例。由于测试案例过多，你只需要在规定时间内完成你能做到的即可。请自由地添加更多你认为需要的测试案例。

## 用到的技术
- Python
- unittest

## 关于该Excel对象的基本功能介绍
该Excel只有一行。列数为A到Z，AA到ZZ等。没有储值的列数默认存储值为空字符串。

- get(column: str), 该函数的目的是获取在column列的值，内容为等式的话需要计算并返回其结果。举例，若在"A1"列存储的值为"=7+3"，sheet.get("A1")应返回"10"。
- getLiteral(column: str), 该函数的目的是获取在column列的字符串值，内容为等式的话不需要计算，直接返回字符串。举例，若在"A1"列存储的值为"=7+3"，sheet.getLiteral("A1")应返回"=7+3"。
- put(column: str, value: str), 该函数的目的是在column列存储value的值。如果该列已经被占用，则替换为当前值。

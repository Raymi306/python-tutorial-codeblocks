<<[prev]({{int_variables}}) [index]({{int_index}})

[TOC]

# Operators
## Arithmetic
---
### +
---
The addition operator adds numbers together. If used with strings or sequences, it concatenates, or combines them.
```py
>>> 2 + 2
4
>>> "Hello " + "world"
"Hello world"
>>> [1, 2] + [3, 4]
[1, 2, 3, 4]
```
---
### -
---
The subtraction operator subtracts numbers from each other. It can also be used to negate a single number.
```py
>>> 2 - 2
0
>>> var = 2
>>> var = -var
>>> var
-2
>>> var = -var
>>> var
2
```
---
### *
---
The multiplication operator multiplies numbers. Multiplying a string or other sequence with a number n will repeat that sequence n times.
```py
>>> 3 * 3
9
>>> 'Hello' * 3
'HelloHelloHello'
>>> [0] * 3
[0, 0, 0]
```
---
### **
---
The power operator raises a number to a power. Do not confuse ** with ^, ^ is the bitwise xor operator which operates on the binary representation of the value. Bitwise operators will be a topic for another time.
```py
>>> 2 ** 31
2147483648
>>> 2 ^ 31
29
# 0b0000_0010 ^ 0b0001_1111 = 0b0001_1101
```
---
### / 
---
The true division operator divides numbers with the result being a float.
```py
>>> 3 / 2
1.5
```
---
### //
---
The floor division operator divides numbers with the result being an integer rounded down.
```py
>>> 3 // 2
1
>>> -3 // 2
-2
```
---
### %
---
The modulo operator provides the remainder after a division.
It is particularly useful for testing if a number is even or odd, and for clock arithmetic where a number cycles back to 0 after reaching a given point.
You may see it being used with strings as a formatting operator in older Python code.
```py
>>> 5 % 2
1
>>> 4 % 2
0
>>> 25 % 24
1
```
## Precedence
You may group operators together using parentheses to change their precedence.
Here, I defer to the [official documentation]({{ext_python3_operator_precedence}}) for a full explanation of which operators take precedence over others.
```py
>>> 3 + 3 * 3
12
>>> (3 + 3) * 3
18
```
## Assignment
---
### =
---
The assignment operator is used for assigning variables.
```py
>>> var = 3
>>> var
3
```
---
### :=
---
The walrus operator is also used for assigning variables. It is used for assignment expressions rather than assignment statements.
Expressions differ from statements by the fact that they return a value.
```py
>>> var := 3
3
```
## Comparison and Boolean
---
### <, <=, \>, \>=
---
```py
>>> 3 < 2
False
>>> 3 > 2
True
>>> 2 >= 2
True
>>> 2 <= 1.9
False
>>> 'a' < 'b'
True
# Strings are converted to their UTF-8 values and then compared
>>> 'B' < 'a'
True
```
---
### ==, !=
---
When comparing the equality of values, == and != can be used. '!=' is read as 'not equal'.
```py
>>> 3 == 3
True
>>> 'foo' != 'bar'
True
```
---
### and
---
You may combine conditions and require that both hold True with 'and'.
Given the expression "x and y", "x" is evaluated first. If it is false, "x" is returned, otherwise "y" is evaluated and returned.
```py
>>> 3 > 1 and 3 < 1000
True
>>> 3 > 1 and 3 < 2
False
```
---
### or
---
You may combine conditions and require that at least one hold True with 'or'.
```py
>>> 3 > 1 or 3 < 1000
True
>>> 3 > 1 or 3 < 2
True
```
Given the expression "x or y", "x" is evaluated first. If it is true, "x" is returned, otherwise "y" is evaluated and returned.
This can be useful for assigning a default value in the case that a variable ends up being falsey.
```py
>>> s = ""
>>> q = s or "foo"
>>> q
"foo"
```
---
### not
---
You may negate conditions by placing 'not' in front of them.
```py
>>> not True
False
>>> not (True and False) 
True
```
---
### is
---
Objects in Python all have a unique id. To check if two objects are the same, you may use 'is'. The most common use of this is checking to see if a value is None.
```py
>>> v = None
>>> v is None
True
>>> v = 0
>>> v is None
False
```
---
### in
---
You may check if a value or subsequence is contained within another sequence with 'in'.
```py
>>> 3 in [1, 2, 3, 4, 5]
True
>>> 42 in [2, 1, 3]
False
>>> 'bar' in 'foobarbaz'
True
```

<<[prev]({{int_variables}}) [index]({{int_index}})

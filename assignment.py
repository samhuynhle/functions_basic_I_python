#1
# def a():
#     return 5
# print(a())

# Defined is function a, which has no defined paramaters for the function. Within function a, the code that is executed returns the value of 5.
# Function a is called within the print method.
# Predicted output: 5
# Predicted output is correct.

#2
# def a():
#     return 5
# print(a()+a())

# Defined is function a, which has no defined parameters for the function. Within function a, the code that is execute returns a value of 5.
# Function a is called twice within the print method. Within the print method, the values of the functions are added together. Since both values are integers,
# The value the is printed will be the addition of both function's value.
# Predicted output: 10
# Predicted output is correct.

#3
# def a():
#     return 5
#     return 10 # A warning is given by the terminal stating this line of code is unreachable. The way this function is written, 'return 10' will never be reached as 'return 5' precedes it and ends the function.
# print(a())

# Defined is function a, which has no defined parameters for the function. Within function a, the code has two returns, the first one returning a value of 5
# and the second returning the value of 10. When a function returns a value, the function is completed, since the first line of code for function a is 'return 5',
# the function will be completed as the value of 5 is returned.
# Function a is called within the print method.
# Predicted output: 5
# Predicted output is correct.

# #4
# def a():
#     return 5
#     print(10)
# print(a())

# Defined is function a, which has no defined parameters for the function. Within function a, the code returns the value of 5 and prints the interger 10, but since
# the first line of code in the function is 'return 5', the function will be completed immediately after 'return 5' is executed. 'print(10)' will not be reached 
# and executed.
# Function a is called within the print mehtod.
# Predicted outcome: 5
# Predicted outcome is correct.

#5
# def a():
#     print(5)
# x = a()
# print(x)

# Defined is function a, which has no defined parameters for the function. Within function a, the code prints the integer 5 and after this line is completed.
# The variable x is assigned the value of function a, but function a does not have a return value, therefore the value of function x is None (similar to undefined in JavaScript).
# Function a is still executed and prints 5.
# When printing x, the value will be None.
# Predicted outcome: 5, None
# Predicted outcome is correct.

#6
# def a(b,c):
#     print(b+c)
# print(a(1,2) + a(2,3))

# Defined is function a, which has two defined parameters, b and c, for the function. Within function a, the code prints the result of the expression 'b+c'.
# Fuction a has no return, so the value of the function will be None.
# Function a is called by the print method twice. The first time passing in the arguements of 1 and 2; the second time passing in the arguements of 2 and 3.
# The values of the functions will be None, but the functions will run and execute the print methods within them.
# Predicted outcome: 3, 5, None
# Predicted outcome was correct for 3, 5. The terminal gave an error when the print method attempted to add None values together.

#7
# def a(b,c):
#     return str(b)+str(c)
# print(a(2,5))

# Defined is function a, which has two defined parameters, b and c, for the function. Within function a, the code returns a concatentation of b and c as both strings.
# Fuction a is called within the print method, which passed in 2 and 5 as arguements.
# Predicted outcome: 25
# Predicted outcome is correct.
# In this case, 25 is a string, not an integer.

#8
# def a():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
#         return 10
#     return 7
# print(a())

# Defined is function a, which has no defined parameters for the function. Within function a, variable b is assigned the value of 100.
# Fuction a will print the value of function b, then has an if conditional with a return and else with a return. The if conditional checks if b is less than 10, if True, return the value of 5.
# If the first conditional was False, the else returns the value of 10. Addittionally, there is a return statement that returns the value of 7 after the conditionals (this
# line of code will not be reached).
# Function a is called within the print method. When called function a prints 100 and returns the value of 10. The print method prints function a, which has the value of 10.
# Predicted outcome: 100, 10
# Predicted outcome is correct.

#9
# def a(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(a(2,3))
# print(a(5,3))
# print(a(2,3) + a(5,3))

# Defined is function a, which has two defined parameters, b and c, for the function. Within function a, there is an if conditional.
# The if conditional checks if the value of b is less than c, if True, then return the value of 7. If False, the else returns the value of 14.
# There is an unreachable 'return 3' statement after the conditional.
# Function a is call by the first print method once, which passes in the arguements of 2 and 3. Function a in this case has the value of 7.
# Function a is called again by the second print method once, which passes in the arguements of 5 and 3. Funciton a in this case has the value of 14.
# Function a is called twice by the third print mehtod, passing in the arguements of 2 and 3 and 5 adn 3. The values of 7 and 14 are retured. This print method
# prints the result of the expression, which adds both values together.
# Predicted outcome: 7, 14, 21
# Predicted outcome is correct.

#10
# def a(b,c):
#     return b+c
#     return 10
# print(a(3,5))

# Defined is function a, which has two defined parameters, b and c, for the function. Wihtin function a, there are two return statements.
# The first return statement returns the result of the expression 'b+c'. The second return statement returns the value of 10, but will not be reached.
# Function a is called by the print method, which passes in two arguements, 3 and 5, into function a. The value of funcation a in this case is 8.
# Predicted outcome: 8
# Predicted outcome is correct.

#11
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
# print(b)
# a()
# print(b)

# Variable b is assigned the value of 500. The print method prints the value of variable b.
# Defined is funcation a, which has no defined parameters for the function. Within the scope of function a, variable b assigned the value of 300 and prints the value of b.
# Variable b is printed by the print method again.
# Function a is executed.
# Variable b is printed by the print method again.
# Predicted outcome: 500, 500, 300, 500
# Predicted outcome is correct.

#12
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# a()
# print(b)

# Variable b is assigned the value of 500, this is in the global scope.
# Variable b is printed by the print method.
# Defined is function a, which has no defined parameters for the function. Within the scope of function a, variable b is assigned the value of 300, prints the value of b,
# and returns the value of b.
# Variable b is printed by the print method again.
# Function a is executed.
# Variable b is printed by the print method again.
# Predicted outcome is: 500, 500, 300, 500
# Predicted outcome is correct.

#13
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# b=a()
# print(b)

# Variable b is assigned the value of 500, this is in the global scope.
# Variable b is printed by the print method.
# Defined is function a, which has no defined parameters for the function. Within the scope of function a, variable b is assigned the value of 300, prints the value of b,
# and returns the value of b.
# Variable b is printed by the print method.
# Variable b is reassigned to be the value of function a, which in is 300.
# Variable is is printed by the print method again, but it's value been recently assigned to 300.
# Predicted outcome: 500, 500, 300, 300
# Predicted outcome is correct.

#14
# def a():
#     print(1)
#     b()
#     print(2)
# def b():
#     print(3)
# a()

# Defined is function a, which has no defined parameters for the function. Within function a, the value of 1 is printed, then function b is called, and then the value of 2 is printed.
# Defined is function b, which has no defined parameters for the function. Within function b, the value of 3 is printed.
# Function a is called.
# Predicted outcome: 1, 3, 2
# Predicted outcome is correct.

#15
# def a():
#     print(1)
#     x = b()
#     print(x)
#     return 10
# def b():
#     print(3)
#     return 5
# y = a()
# print(y)

# Defined is function a, which has no defined parameters for the function.
# Within function a, the value of 1 is printed, then the variable x is assigned to be the value of function b, then the value of x is printed, and then returned is the value of 10.
# Defined is function b, which has no defined parameters for the function.
# Within function b, the value of 3 is printed and then returned is the value of 5.
# function a is called as the variable y is assigned the value of function a.
# Predicted outcome: 1, 3, 5, 10
# Predicted outcome is correct. When y was assigned to be the value of function a, function a printed 1, then called function b, whcih printed 3 and returned 5.
# After 5 was returned, variable x was assigned the value of 5, which was printed. Then, function a returned the value of 10. Variable y was assigned the value of function a,
# which was 10. The value of y was then printed the print method.
#1
# def a():
#     return 5
# print(a())

#          T-Diagram
#            Global 
#     var              value
#       
#            Console
#               5
#
#           Function1
#     var              value
#
#            Console
#
# ----------------------------

#2
# def a():
#     return 5
# print(a()+a())

#          T-Diagram
#            Global 
#     var              value
#       
#            Console
#               10
#
#           Function1
#     var              value
#
#            Console
#
# ----------------------------

#3
# def a():
#     return 5
#     return 10
# print(a())

#          T-Diagram
#            Global 
#     var              value
#       
#            Console
#               5
#
#           Function1
#     var              value
#
#            Console
#
# ----------------------------

#4
# def a():
#     return 5
#     print(10)
# print(a())

#          T-Diagram
#            Global 
#     var              value
#       
#            Console
#               5
#
#           Function1
#     var              value
#
#            Console
#
# ----------------------------

#5
# def a():
#     print(5)
# x = a()
# print(x)

#          T-Diagram
#            Global 
#     var              value
#      x             undefined
#            Console
#            undefined
#
#           Function1
#     var              value
#
#            Console
#               5
# ----------------------------

#6
# def a(b,c):
#     print(b+c)
# print(a(1,2) + a(2,3))

#          T-Diagram
#            Global 
#     var              value
#                        
#            Console
#               8 (Correct Answer: Doesn't return so value = undefined / none)
#
#           Function1
#     var              value
#
#            Console
#               3
#               5
# ----------------------------

#7
# def a(b,c):
#     return str(b)+str(c)
# print(a(2,5))

#          T-Diagram
#            Global 
#     var              value
#                        
#            Console
#              25
#
#           Function1
#     var              value
#
#            Console
#               
# ----------------------------

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

#          T-Diagram
#            Global 
#     var              value
#                        
#            Console
#               10
#
#           Function1
#     var              value
#      b                100
#            Console
#              100
# ----------------------------

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

#          T-Diagram
#            Global 
#     var              value
#                        
#            Console
#               7
#               14
#               21
#
#           Function1
#     var              value
#      b                100
#            Console
#              100
# ----------------------------

# #10
# def a(b,c):
#     return b+c
#     return 10
# print(a(3,5))

#          T-Diagram
#            Global 
#     var              value
#                        
#            Console
#               8
#
#           Function1
#     var              value
#                        
#            Console
#                
# ----------------------------

#11
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
# print(b)
# a()
# print(b)

#          T-Diagram
#            Global 
#     var              value
#      b                500
#            Console
#              500
#              500
#              500
#
#           Function1
#     var              value
#                        
#            Console
#              300
# ----------------------------

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

#          T-Diagram
#            Global 
#     var              value
#      b                500
#            Console
#              500
#              500
#              500
#
#           Function1
#     var              value
#      b                300
#            Console
#              300
# ----------------------------

# #13
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# b=a()
# print(b)

#          T-Diagram
#            Global 
#     var              value
#      b                500 -> 300
#            Console
#              500
#              500
#              300
#
#           Function1
#     var              value
#      b                300
#            Console
#              300
# ----------------------------

# #14
# def a():
#     print(1)
#     b()
#     print(2)
# def b():
#     print(3)
# a()

#          T-Diagram
#            Global 
#     var              value
#                        
#            Console
#               
#
#           Function a
#     var              value
#                         
#            Console
#               1
#               2
#
#           Function b
#     var              value
#                         
#            Console
#               3
# ----------------------------

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

#          T-Diagram
#            Global 
#     var              value
#      y                 10
#            Console
#               10
#
#           Function a
#     var              value
#      x                 5
#            Console
#               1
#               5
#
#           Function b
#     var              value
#                         
#            Console
#               3
# ----------------------------
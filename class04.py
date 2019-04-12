# # conditional statement
# # if
# # if else
# # if elif
# # Nested else if
#
# number_01 = 4
# number_02 = 5
# number_03 = 6
#
# if number_01 < number_02:
#     print('Number 01 is greater than 02')
#
# # if else
#
# if number_01 > number_02:
#     print('Number 01 is greater than 02')
# else:
#     print('number 02 is greater than 01')
#
#
# # if elif else
#
# if number_01 > number_02:
#     print('Number 02 is greater than 01')
# elif number_02 < number_03:
#     print('number 03 is greater than 02')
# else:
#     print('number 02 is greater than number 01')
#
# # Nested if else
# if number_01 > number_02:
#     print('Number 02 is greater then number 01  ')
# elif number_02 > number_03:
#     print('number 02 is greater than number 03')
# elif number_03 > number_02:
#     print('number 03 is greater then number 02')
# else:
#     print('number 02 is greater than number 03')
#
#
# # nested if else type2
# if number_01 < number_02:
#     if number_01 > number_03:
#         print('number 01 is max')
#     else:
#         print('number 03 is max')
#
#
# else:
#     if number_02 > number_03:
#         print('number 02 is max')
#     else:
#         print('number 03 is max')
#
#
# '''
# for i in range():
#     print(i)
# '''
# #for loop
#
# for i in range(0,5):
#     print(i)
#
# #while loop
#
# number = 0
# while number < 5:
#     print(number)
#     break
#     number += 1
# print("#################################################")
# #do while loop (by defult enters in loop)
#
# number = 0
# while True:
#     if number > 5:
#         break
#     print(number)
#     number += 1
# # nested loop
#     for i in range(0,5):
#         for j in range(0,i):
#             print(j, end=" ")
#         print('')
#
#
#
# # control statment
#
# for i in range(0, 11): # else use only for i in range(0, 11, 2)
#     if i % 2 == 0:
#         print(i)
#
#
#
#



#
# for i in range(1, 6):
#     for j in range(0, 5):
#         print('*', end=" ")
#     print('')
#
# print("####################################")
#
#for i in range(0, 5):
#     for j in range(0, 5):
#         print(i%2, end=" ")
#     print('')
#
#
# print("####################################")
#
# for i in range(1, 6):
#     for j in range(0, 5):
#         print('1', end=" ")
#         print('')
# print("##################################################")
# for i in range(0, 5):
#      for j in range(0, 5):
#          print(i%2, end=" ")
#      print(' ')
# print('##########################################################')
# for i in range(0, 5):
#     for j in range(1, 6):
#         print(j, end=" ")
#
#     print(' ')
#
#
# for i in range (0, 6):
#     for j in range(0, i):
#         print(2**(j+1), end="")
#         print('')
num = 1
for i in range(1, 6):
  for j in range(1, 6):
    print(num, end=" ")
    num += 1
  print(" ")















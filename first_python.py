# scores = [90,70,60,50,80]
# print(scores)
# scores.extend([50, 85, 40])
# print(scores)
# scores.append(70)
# print(scores)
# scores.insert(2, 30)
# print(scores)
# print(scores.count(50))
# scores.remove(50) 
# print(scores)
# print(scores.count(50))
# scores.pop()
# print(scores)
# scores.sort()
# print(scores)
# scores.reverse()
# print(scores)
# print(len(scores))

# def hello():
#   print("HELLO")

# rainy=True
# if rainy:
#   print("Rainy")
# else:
#   print("Sunny")

#   dic = {}

# for num in range(3, 100):
#   print(num)

# def power(num, power):
#   result=num
#   for index in range(power-1):
#     result=result*num
#   return result

# print(power(10,2))

# nums = [
#   [0,1,2], 
#   [3,4,5], 
#   [6,7,8], 
#   [9]
# ]

# for list in nums:
#   for num in list:
#     print(num)

# file = open("123.txt", mode="a", encoding="utf-8")
# # for line in file:
# #   print(line)
# # print(file.read())
# file.write("\n屌")
# file.close

# with open("123.txt", mode="a", encoding="utf-8") as file:
#   file.write("\n屌sb")

# import token
# import sys
# print(sys.path)

# print(token.tok_name)

# import numpy as np


class Phone:
  def __init__(self, os, number, is_waterproof):
    self.os = os
    self.number = number
    self.is_waterproof = is_waterproof
  
  def is_ios(self):
    if self.os == "ios":
      return True
    else:
      return False

phone1 = Phone("ios", 123, True)
phone2 = Phone("Android", 456, False)
print(phone1.number)
print(phone2.is_ios())

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def print_name(self):
    print(self.name)

  def print_age(self):
    print(self.age)

class Student(Person):
  def __init__(self, name, age, school):
    self.name = name
    self.age = age
    self.school = school
  def print_school(self):
    print(self.school)

melody = Student("Melody", 30, "Poly")

melody.print_name()
melody.print_age()
melody.print_school()

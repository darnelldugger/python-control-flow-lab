# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

first = input('Enter the length of the first side: ')

second = input('Enter the length of the second side: ')

third = input('Enter the length of the third side: ')

if first == second and first == third:
  print(f"Your triangle with sides of {first}, {second} & {third} is a equalateral triangle")

elif first != second and first != third and second != third:
  print(f"Your triangle withe sides of {first}, {second} & {third} is a scalene triangle")

else:
  print(f"Your triangle withe sides of {first}, {second} & {third} is a isosceles tiangle")
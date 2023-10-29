# first task

# print((int(input())**2 + int(input())**2) **(1/2))

side_a = int(input())
side_b = int(input())

hypotenuse = (side_a * side_a + side_b * side_b) **(1/2)
print(hypotenuse)

# second task

start_time_in_minutes = 9 * 60
odd_lesson_duration = 50
even_lesson_duration = 60

lesson_number = int(input())
odd_lesson_left = lesson_number // 2
even_lesson_left = (lesson_number - 1) // 2

lesson_time_in_minutes = start_time_in_minutes + odd_lesson_left * odd_lesson_duration + even_lesson_left * \
                         even_lesson_duration + 45

result_hours = lesson_time_in_minutes // 60
result_minutes = lesson_time_in_minutes % 60

print(result_hours, result_minutes)

# third task

num1, num2 = int(input()), int(input())

if num1 > num2:
    print(1)
else:
    print(2 if num2 > num1 else 0)

# fourth task

num1, num2, num3 = int(input()), int(input()), int(input())

if num1 > num2:
    print(num1 if num1 > num3 else num3)
else:
    print(num2 if num2 > num3 else num3)

# fifth task

num1, num2, num3 = int(input()), int(input()), int(input())

if num1 == num2 == num3:
    print(3)
elif num1 == num2 or num1 == num3 or num2 == num3:
    print(2)
else:
    print(0)

# sixth task

num1, num2, num3 = int(input()), int(input()), int(input())

if num2 < num1:
    num1, num2 = num2, num1
if num3 < num2:
    num2, num3 = num3, num2
if num2 < num1:
    num1, num2 = num2, num1
print(num1, num2, num3)

# seventh task


a, b, c = float(input()), float(input()), float(input())

D = b ** 2 - (4 * a * c)
if D > 0:
    x1 = (-b + D ** 0.5) / (2 * a)
    x2 = (-b - D ** 0.5) / (2 * a)
    print(x1, x2)
elif D == 0:
    x = -b / (2 * a)
    print(x)

# Написать калькулятор.

number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))
operation = input('Выберите операцию +, -, *, /, **: ')

if operation == '+':
    print(f'Результат: {number1 + number2}')
elif operation == '-':
    print(f'Результат: {number1 - number2}')
elif operation == '*':
    print(f'Результат: {number1 * number2}')
elif operation == '/':
    print(f'Результат: {number1 / number2}')
elif operation == '**':
    print(f'Результат: {number1 ** number2}')

else:
    print('Выбрана неверная операция. Попробуйте снова.')

# Квадраты натуральных чисел.

n = int(input())
q = 1
while q ** 2 <= n:
    print(q ** 2)
    q += 1

# Определить является ли введенное с клавиатуры число простым.

a = int(input("Введите число: "))
w = 0
for i in range(2, a // 2 + 1):
    if (a % i == 0):
        w += 1
if (w <= 0):
    print("Число простое")
else:
    print("Число не является простым")

# Приложение подбирающее правильное окончание к фразе:

k = int(input('Введите количество грибов, сколько нашла Маша в лесу: '))
j = ' гриб'
j2 = ' гриба'
j3 = ' грибов'
if k == 0:
    print('Маша нашла в лесу', str(k) + j3)
elif k % 100 >= 10 and k % 100 <= 20:
    print('Маша нашла в лесу', str(k) + j3)
elif k % 10 == 1:
    print('Маша нашла в лесу', str(k) + j)
elif k % 10 >= 2 and k % 10 <= 4:
    print('Маша нашла в лесу', str(k) + j2)
else:
    print('Маша нашла в лесу', str(k) + j3)

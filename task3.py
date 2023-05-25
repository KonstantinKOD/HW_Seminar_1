# Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех. Т.е.
# билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*
# 385916 -> yes
# 123456 -> no

print("Enter your ticket number")

ticket = int(input())

firstThreeDigit = int(ticket // 1000)
firstSumm = 0
while firstThreeDigit > 0:
    sum= firstThreeDigit % 10
    firstSumm += sum
    firstThreeDigit = firstThreeDigit // 10

secondThreeDigit = int(ticket % 1000)
secondSumm = 0
while secondThreeDigit > 0:
    sum= secondThreeDigit % 10
    secondSumm += sum
    secondThreeDigit = secondThreeDigit // 10

print('the sum of the first three digits',firstSumm)
print('the sum of the second three digits',secondSumm)

if firstSumm == secondSumm:
    print()
    print("Congratulations! Your ticket (",ticket,") turned out to be a lucky one :)")
    print()
else:
    print()
    print("Don't worry, you'll be lucky with another ticket ;)")
    print()


# Это должна была быть проверка на количество символов в строке, 
# чтоб работать только с шестью цифрами.
# Не получилось ¯\_(ツ)_/¯
# firstSumm = 0
# secondSumm = 0
# flag = True

# while flag:
#     if len(ticket < 6 and ticket > 6):
#         print("Your ticket is wrong, the ticket must be six-digit")
#         print("Try again")
#         ticket = int(input())
#         flag = False
#     else:
#         firstSumm = int(ticket // 1000)
#         secondSumm = int(ticket % 1000)
#         flag = False
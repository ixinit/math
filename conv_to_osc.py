num = int(input("Введите число в какой-либо системе счисления: "))
syst = int(input("Введите систему счисленияэтого числа: "))

while True:
    num = num // syst
    ost = num % syst
    if ost < syst:
        print(ost)
        break;

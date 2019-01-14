# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например,
# если введено число 3486, то надо вывести число 6843.
#
def endstart(newnumber, number):
    newnumber = newnumber * 10 + number % 10
    number = number // 10
    if number == 0:
        return print(newnumber)
    else:
        endstart(newnumber, number)


endstart(0, int(input("Введите число: ")))

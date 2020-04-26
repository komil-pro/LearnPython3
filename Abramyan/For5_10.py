def For5():
    # For5
    # for range of floats here we will not use: import numpy, but will multiply by 0.1
    # используем функцию round() чтобы округлять до десятых и сотых
    price = float(input("Введите стоимость 1кг конфет: ")) # example 12, 25.5
    for i in range(1, 11):
        massa = round(i * 0.1, 1)
        print("Стоимость "+str(massa)+"кг конфет =",round(massa*price,2))

#For5()

def For6():
    price = float(input("Введите стоимость 1кг конфет: "))
    for i in (1.2, 1.4, 1.6, 1.8, 2):
        print("Стоимость "+str(i)+"кг конфет =",round(i * price, 2))
#For6()

def For7():
    A = int(input("Введите значение A: "))
    B = int(input("Введите значение B: "))
    if A<B:
        sum = 0
        for i in range(A, B+1):
            sum += i
        print("Сумма чисел:",sum)
    else:
        print("Небходимо, чтобы A было меньше B!")
        For7()

#For7()

def For8():
    A = int(input("Введите значение A: "))
    B = int(input("Введите значение B: "))
    if A<B:
        result = 1
        for i in range(A, B+1):
            result *= i
        print("Произведение всех чисел:",result)
    else:
        print("Небходимо, чтобы A было меньше B!")
        For8()

#For8()

def For9():
    A = int(input("Введите значение A: "))
    B = int(input("Введите значение B: "))
    if A<B:
        result = 0
        for i in range(A, B+1):
            result += i ** 2
        print("Сумма квадратов чисел:",result)
    else:
        print("Небходимо, чтобы A было меньше B!")
        For9()

#For9()

def For10():
    N = int(input("Введите значение N: "))
    if N>0:
        sum = 0.
        for n in range(1,N+1):
            sum += 1/n
        print("Ответ:",sum)
    else:
        print("N должно быть больше нуля!")

#For10()

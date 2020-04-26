def if25(x):
    if (x < -2) or (x > 2):
        return 2*x
    else:
        return -3*x

#print(if25(5))

def if26(x):
    if x <= 0:
        return -x
    elif x>0 and x<2:
        return x**2
    elif x>=2:
        return 4

#print(if26(1.2))

def if27(x):
    if x < 0:
        return 0
    elif (x>=0 and x<1) or x>=2 and x<3:
        return 1
    elif x>=1 and x<2 or x>=3 and x<4:
        return -1

#print(if27(3.14))

def if28(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def if29(x):
    s=" число"
    if x == 0:
        return "нулевое"+s
    if x%2 == 0:
        s = " четное"+s
    else:
        s = " нечетное"+s
    if x<0:
        s = "отрицательное"+s
    else:
        s = "положительное"+s
    return s

#print(if29(3))

def if30(x):
    if x>0 and x<1000 and isinstance(x, int): # проверяем является ли x типом int
        s=" число"
        ln=len(str(x))
        if ln==1:
            s = " однозначное"+s
        elif ln==2:
            s = " двузначное"+s
        elif ln==3:
            s = " трехзначное"+s

        if x%2 == 0:
            s = "четное"+s
        else:
            s = "нечетное"+s

        return s
    else:
        return "Небходимо ввести целое число в диапазоне 1-999!"

#print(if30(555))
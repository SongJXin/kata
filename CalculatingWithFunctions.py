def calculat(number1,cal,number2):
    result=0
    if(cal=="+"):
        result=number1+number2
    if(cal=="-"):
        result=number1-number2
    if(cal=="*"):
        result=number1*number2
    if(cal=="/"):
        result=number1/number2
    return int(result)
def zero(calcul=None):  # your code here
    if calcul != None:
        return calculat(0,calcul[0],calcul[1])
    return 0


def one(calcul=None):  # your code here
    if calcul != None:
        return calculat(1, calcul[0], calcul[1])
    return 1


def two(calcul=None):  # your code here
    if calcul != None:
        return calculat(2, calcul[0], calcul[1])
    return 2


def three(calcul=None):  # your code here
    if calcul != None:
        return calculat(3, calcul[0], calcul[1])
    return 3


def four(calcul=None):  # your code here
    if calcul != None:
        return calculat(4, calcul[0], calcul[1])
    return 4


def five(calcul=None):  # your code here
    if calcul != None:
        return calculat(5, calcul[0], calcul[1])
    return 5


def six(calcul=None):  # your code here
    if calcul != None:
        return calculat(6, calcul[0], calcul[1])
    return 6


def seven(calcul=None):  # your code here
    if calcul != None:
        return calculat(7, calcul[0], calcul[1])
    return 7


def eight(calcul=None):  # your code here
    if calcul != None:
        return calculat(8, calcul[0], calcul[1])
    return 8


def nine(calcul=None):  # your code here
    if calcul != None:
        return calculat(9, calcul[0], calcul[1])
    return 9

def plus(number):  # your code here
    return ('+',number)


def minus(number):  # your code here
    return ('-',number)


def times(number):  # your code here
    return ('*',number)


def divided_by(number):  # your code here
    return ('/',number)
print(four(plus(four())))

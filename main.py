from sympy import symbols, evalf
import sys

def FibonacciNumber(N):
    F = 0
    if (N == 0 or N == 1):
        F = 1
    else:
        F = FibonacciNumber(N-1)+FibonacciNumber(N-2)
    return F


ourFunc = input('Введите функцию: ')
x = symbols('x')
result = eval(ourFunc)

a = int(input('Левая граница а: '))
b = int(input('Правая граница b: '))
if(a>=b):
    print("Некорректные границы")
    sys.exit()
delta = b-a
e = float(input('Точность: '))
estr = str(e)
afterpoint = abs(estr.find('.') - len(estr)) - 1
minFib = delta/e
print("Число Фибоначчи не менее: ", minFib)
i=0
fib = FibonacciNumber(i)
while fib<minFib:
    i+=1
    fib = FibonacciNumber(i)
print("Подходящее число Фибоначчи: ", fib)
NumberOfIter = i-1
print("Количество итераций: ", NumberOfIter-1)
i=0
alpha = 0
betha = 0

while i<(NumberOfIter-1):
    flag = True
    alpha = a + (FibonacciNumber(NumberOfIter - i - 1)/ FibonacciNumber(NumberOfIter - i + 1)) * delta
    betha = a+(FibonacciNumber(NumberOfIter - i)/FibonacciNumber(NumberOfIter - i + 1))*delta
    alpha = round(alpha,6)
    betha = round(betha,6)

    if(result.evalf(subs={x: alpha})<=result.evalf(subs={x:betha})):
        b = betha
    else:
        a = alpha
        flag
    delta = b-a
    print(i,"итерация\nalpha = ", alpha, " betha = ", betha)
    print('Новые границы и дельта: ')
    print('a = ', a, 'b = ', b, 'delta = ', round(delta,6),'\n')
    i+=1
if (flag == True):
    x = round(alpha, afterpoint)
else:
    x = round(betha, afterpoint)

print("ОТВЕТ: ")
print(x,"+-",e)
def solution(price, money, count):
    v = 0
    for i in range(1, count + 1):
        v += price * i
    return v - money if money < v else 0

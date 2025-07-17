def solution(phone_number):
    index = len(phone_number) - 4
    return '*' * (index) + phone_number[index::]

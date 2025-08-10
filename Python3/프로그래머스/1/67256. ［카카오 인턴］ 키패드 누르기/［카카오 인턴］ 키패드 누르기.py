def solution(numbers, hand):
    answer = ''
    left, right = 10, 12
    
    dic = {0: 0, 1: 1, 2: 2, 3: 1, 4: 2, 5: 3, 6: 2, 7: 3, 8: 4, 9: 3, 10: 4}
    
    for number in numbers:
        if number == 1 or number == 4 or number == 7:
            answer += 'L'
            left = number
        elif number == 3 or number == 6 or number == 9:
            answer += 'R'
            right = number
        else:
            if number == 0:
                number = 11
            ld = dic[abs(number - left)]
            rd = dic[abs(number - right)]
            if ld < rd or (ld == rd and hand == 'left'):
                answer += 'L'
                left = number
            elif ld > rd or (ld == rd and hand == 'right'):
                answer += 'R'
                right = number
                
    return answer

def solution(survey, choices):
    dic = {
        1: [0, 3],
        2: [0, 2],
        3: [0, 1],
        4: [0, 0],
        5: [1, 1],
        6: [1, 2],
        7: [1, 3],
    }
    
    characters = {"R": 0, "T": 0, "F": 0, "C": 0, "M": 0, "J": 0, "A": 0, "N": 0}
    
    for i in range(len(survey)):
        choice = dic[choices[i]]
        c = survey[i][choice[0]]
        score = choice[1]
        characters[c] += score
        print(characters)
        
    result = ""
    for c in ["RT", "CF", "JM", "AN"]:
        if characters[c[0]] >= characters[c[1]]:
            result += c[0]
        else:
            result += c[1]
            
    return result

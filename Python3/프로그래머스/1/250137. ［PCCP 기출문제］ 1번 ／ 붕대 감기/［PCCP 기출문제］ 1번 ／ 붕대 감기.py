def solution(bandage, health, attacks):
    default = health
    time = 0
    for attack in attacks:
        count = attack[0] - time - 1
        heal = bandage[1] * count + bandage[2] * (count // bandage[0])
        health = min(health + heal, default)
        time = attack[0]
        health -= attack[1]
        if health <= 0:
            return -1
    return health

def evaluate(problem,possibleSol):
    tmp1 = True
    for i in problem:
        tmp2 = False
        for j in i:
            if j.upper() in possibleSol:
                if j.isupper():
                    tmp2 |= possibleSol[j]
                elif j.islower():
                    tmp2 |= not possibleSol[j.upper()]
                # tmp2 |= possibleSol[j.upper()]
            else:
                tmp2 |= False
            if tmp2:
                break
        tmp1 &= tmp2
    
    if not tmp1:
        return True
    else:
        return None

d = {"A":False,"B":False,"D":True}
problem = [['A', 'D', 'b'], ['D', 'c', 'e'], ['b', 'E', 'c']]
ans = evaluate(problem,d)
print(ans)
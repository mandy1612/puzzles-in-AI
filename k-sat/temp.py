from ksat_agent import Agent
from queue import Queue

def VariableNeighbourhood(problem,initial):
    if len(initial) == n:
        if verify(problem,initial):
            return initial
        else:
            return None
    
    currSol = initial.copy()
    solutions = Queue()
    
    for key in currSol:
        newSol = currSol.copy()
        newSol[key] = not currSol[key]
        isCorrect = evaluate(problem,newSol)
        if isCorrect:
            solutions.put(newSol)
    
    while not solutions.empty():
        sol = solutions.get()
        currVar = set(sol.keys())
        if len(sol) != n:
            rem = list(variables-currVar)
            while not empty(rem):
                sol_0 = sol.copy()
                sol_1 = sol.copy()
                toInsert = rem.pop(0)
                sol_0[toInsert] = False
                sol_1[toInsert] = True
                newSol_0 = VariableNeighbourhood(problem,sol_0)
                newSol_1 = VariableNeighbourhood(problem,sol_1)
                if newSol_0 != None:
                    solutions.put(newSol_0)
                if newSol_1 != None:
                    solutions.put(newSol_1)
        else:
            return finalSolutions.append(sol)
    # return finalSolutions

# empty() method for list
def empty(lst):
    if len(lst) == 0:
        return True
    else:
        return False
    
# to generate initial solution by assigning least variables
def initSol(problem):
    res = {}
    for i in problem:
        if i[0].upper() not in res:           
            if i[0].isupper():
                res[i[0]] = True
            elif i[0].islower():
                res[i[0].upper()] = False
    return res


# to verify whether sol is correct or not
def verify(problem,sol):
    tmp1 = True
    for clause in problem:
        tmp2 = False
        for variable in clause:
            if variable.isupper():
                tmp2 |= sol[variable]
            elif variable.islower():
                tmp2 |= not sol[variable.upper()]
            # tmp2 |= sol[variable.upper()]
        tmp1 &= tmp2
    if tmp1:
        return True
    else:
        return False

# to evaluate problem on a possible solution
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


agt=Agent(3,7,10)
n = agt.tree.n  # no of var
k = agt.tree.k  # no of var in each clause
m = agt.tree.m  # no of clauses
variables = set()   # set of variables
finalSolutions = []
for i in range(n):
    variables.add(chr(65+i))


if __name__=="__main__":
    # problem = [['A', 'D', 'b'], ['D', 'c', 'e'], ['b', 'E', 'c']]
    file = open(r"solutions.txt","w+")
    problem = agt.tree.problem
    print(problem)
    initial = initSol(problem)
    print("\nInitial solution:",initial)
    VariableNeighbourhood(problem,initial)
    if not empty(finalSolutions):
        print("\nFinal solution in file 'solutions.txt'")
        file.write("After Variable Neighbourhood\n")
        for solution in finalSolutions:
            # print(solution)
            file.write(str(solution))
            file.write("\n")
    else:
        print("No solution exist")
    file.close()

    # x0x01xx
    
    # x1x01xx
    # 10x11xx->->1010110
    # x0x00xx
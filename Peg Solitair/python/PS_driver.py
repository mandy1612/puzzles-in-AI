from PS_agent import Agent

def driver():
    
    agnt=Agent()
    
    """
        search() takes an optimizer as an arguement
        3 type of optimizers are implemented
        1 -> manhattan (default)
        2 -> mismatching 
        3-> A*
    """

    node,iterations=agnt.search("manhattan")

    if not node:
        print("\n No solution exist")

    print("Total iterations:",iterations)
    agnt.printPath(node)


print("Welcome to Peg Solitaire")

if __name__ == "__main__":
    driver()
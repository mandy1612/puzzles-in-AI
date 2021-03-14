from environment import puzzle,Node
from agent import agent
import numpy as np

def driver():
    # -1 for blank space
    initial= np.array([[4,8,-1],[6,1,5],[7,3,2]])
    final= np.array([[1,2,3],[4,5,6],[7,8,-1]])
    puzz=puzzle(initial)
    agnt=agent(puzz,final)

    node=agnt.BFS()

    if not node:
        print("\n no sol")

    
    agnt.printPath(node)
    
if __name__ == "__main__":
    driver()
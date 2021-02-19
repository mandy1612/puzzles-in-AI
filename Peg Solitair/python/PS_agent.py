from PS_environment import PegSolitare
import numpy as np
from queue import PriorityQueue

class Agent:

    def __init__(self):
        self.puzzle=PegSolitare()
        self.goal=[False]*34
        self.goal[17]=True
        self.frontier=PriorityQueue()
        self.explored={}
    
    def heuristic1(self,node):
        """"This heuristic is almost similar as manhattan distance exepct here we are using some base^(manhattan distance) instead of manhattan distance only"""
        config = node.config
        base = 2
        dist = np.array([base**0,base**1,base**2,base**3])
        coeff = np.zeros((4))
        d = {0:[17],1:[9,10,11,16,18,23,24,25],2:[4,5,6,8,12,15,19,22,26,28,29,30],3:[1,2,3,7,13,14,20,21,27,31,32,33]}

        for i in d:
            toCheck = d[i]
            count = 0
            for j in toCheck:
                if config[j]:
                    count += 1
            coeff[i] = count
        dist = dist.reshape((1,4))
        coeff = coeff.reshape((4,1))
        return np.dot(dist,coeff).squeeze()

    def heuristic2(self,node):
        """This heuristic counts no. of mismatching empty postions"""
        return 32-node.config[1:].count(False)

    def cal_cost(self,node,search):
        if search == "manhattan":
            h1 = self.heuristic1(node)
            return h1
        elif search == "mismatching":
            h2 = self.heuristic2(node)
            return h2
        elif search == "a*" or search == "astar" or search == "A*":
            return node.level + self.heuristic2(node)

    def printPath(self,node):
        if(node != None):
            self.printPath(node.parent)
            print(node,"\n")

    def isGoal(self,node):
        return node.config[1:] == self.goal[1:]
        

    def search(self,optimizer="manhattan"):
        frontier = self.frontier
        explored = self.explored
        self.puzzle.root.cost = self.cal_cost(self.puzzle.root,optimizer)
        frontier.put(self.puzzle.root)
        counter=0

        while not frontier.empty():
            counter+=1
            node = frontier.get()
            conf = node.config
            confStr = str(list(map(int,conf))).replace(",","").replace("[","").replace("]","").replace(" ","")
            explored[confStr]=node
            
            if self.isGoal(node):
                return node,counter

            neighbours=self.puzzle.moves(node)

            for neighbour in neighbours:
              neighbour.cost = self.cal_cost(neighbour,optimizer)
              configuration = neighbour.config
              configurationStr = str(list(map(int,configuration))).replace(",","").replace("[","").replace("]","").replace(" ","")
              if configurationStr not in explored:
                  frontier.put(neighbour)
              else:
                  del(neighbour)

        return None
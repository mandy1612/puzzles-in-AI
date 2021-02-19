# 8-Puzzle

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Approach](#app)

## About <a name = "about"></a>

The 8-puzzle problem is a puzzle invented and popularized by Noyes Palmer Chapman in the 1870s. It is played on a 3-by-3 grid with 8 square blocks labeled 1 through 8 and a blank square. Your goal is to rearrange the blocks so that they are in order. You are permitted to slide blocks horizontally or vertically into the blank square. The following shows a sequence of legal moves from an initial board position (left) to the goal position (right).


    _  1  3        1  _  3        1  2  3        1  2  3        1  2  3
    4  2  5   =>   4  2  5   =>   4  _  5   =>   4  5  _    =>  4  5  6
    7  8  6        7  8  6        7  8  6        7  8  6        7  8  _

    initial                                                      goal

Note:- While coding blank space '_' is denoted by '-1'.
## Getting Started <a name = "getting_started"></a>

Pull this repository or just download it as zip on your computer.

### Prerequisites

Knowledge of data structures like *Priority queue* , and *Hash table* are required. Some knowledge of graph searching algorithms like breadth first search are plus.

## Approach <a name = "app"></a>

We define a state of the game to be the board position, the number of moves made to reach the board position, and the previous state. First, insert the initial state (the initial board, 0 moves, and a null previous state) into a priority queue. Then, delete from the priority queue the state with the minimum priority, and insert onto the priority queue all neighboring states (those that can be reached in one move). Repeat this procedure until the state dequeued is the goal state. The success of this approach hinges on the choice of priority function for a state. We consider two priority functions:

**Hamming priority:** The number of blocks in the wrong position, plus the number of moves made so far to get to the state. Intutively, a state with a small number of blocks in the wrong position is close to the goal state, and we prefer a state that have been reached using a small number of moves.

**Manhattan priority:** The sum of the distances (sum of the vertical and horizontal distance) from the blocks to their goal positions, plus the number of moves made so far to get to the state.

Consequently, as soon as we dequeue a state, we have not only discovered a sequence of moves from the initial board to the board associated with the state, but one that makes the fewest number of moves.

#### Critical optimization
After implementing best-first search, you will notice one annoying feature: states corresponding to the same board position are enqueued on the priority queue many times. To prevent unnecessary exploration of useless states, when considering the neighbors of a state, don't enqueue the neighbor if it is already present in the visited hash table.


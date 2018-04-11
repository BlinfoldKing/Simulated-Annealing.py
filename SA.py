import random
import math
import matplotlib.pyplot as plt

def f (x1, x2):
    return (((2 * (x1 ** 2)) + ((x2 ** 4) / 3)) * (x1 ** 2)) 
    - (x1 * x2)
    + ((4 * (x2 ** 2)) * (x2 ** 2)) 

def P (d, T):
    return math.exp ((-d)/T)

if __name__ == '__main__':

    solutions = []
    currState = [0, 0]
    T1, T2 = 10000, 0
    coolingRate = 0.9
    currEval = f (*currState)
    solutions.append (currEval)
    while T1 != T2:
        newState = [random.uniform(-1, 1), random.uniform(-1, 1)]
        Dif = f (*currState) - f (*newState)
        if Dif > 0:
            currState = newState
            currEval = f (*currState)
            solutions.append (currEval)
        else:
            R = random.random ()
            if P (Dif, T1) > R:
                currState = newState
                currEval = f (*currState)
                solutions.append (currEval)
        T1 = math.floor (T1 * coolingRate)

    print (currState)
    print (f (*currState))

    plt.plot (solutions)
    plt.show ()

    
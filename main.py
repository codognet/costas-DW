from dwave_qbsolv import QBSolv
import numpy as np
import pickle
import string
import math

def isCostas(list):
    n = len(list)
    for i in range(n):
        for k in range(1,n-i):
            for j in range(i+1,n-i):
                if j+k == n:
                    break
                if list[i+k] - list[i] == list[j+k] - list[j]:
                    return 0
    return 1


# QBSolv Parameter
num_repeats = 50
seed = None
algorithm = None
verbosity = 0
timeout = 2592000
solver_limit = None
target = None
find_max = False
solver = 'tabu'
#problem size, etc
n = 5
num = int(n*((n-1)/2)*(n-1)) + n*n #number of variables
penalty=10.0
penalty2=100.0
penalty3=1000.0

file = open("costas" + str(n) + ".QUBO", "rb")
QUBO = pickle.load(file)
file.close()

# Call QBSolv
result = QBSolv().sample_qubo(QUBO, num_repeats=num_repeats, seed=seed, algorithm=algorithm, verbosity=verbosity,
                               timeout=timeout, solver_limit=solver_limit, solver=solver, target=target,
                               find_max=find_max).record

#print the solution
#energy = result.energy.min()
energy = result.energy[0]
print("energy:", energy)
# print("energies", result.energy)
print("sample of size:", len(result.sample[0]))
sol = result.sample[0]

# print solution as permutation
costas=[]
for i in range(n):
    for j in range(n):
        if sol[i*n+j]:
            costas.append(j)
print(costas, end=' ')
if isCostas(costas):
        print("is  costas !")




#sol = [3,4,2,1,5] = [2,3,1,0,4]
# sol = [1, 2, 6, 14, 9, 3, 15, 13, 5, 10, 12, 11, 8, 4, 7]
#       [0, 1, 5, 13, 8, 2, 14, 12, 4, 9, 11, 10, 7, 3, 6]
#l = [0, 1, 5, 13, 8, 2, 14, 12, 4, 9, 11, 10, 7, 6, 3]
#sol = isCostas(l)
#print("sol:", sol)






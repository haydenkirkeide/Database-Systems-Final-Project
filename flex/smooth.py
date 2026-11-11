import math, numpy as np
from flex.sensitivity import elasticSensitivity

def smoothSensitivity(tree, metrics, epsilon, delta, maxK):
    beta = epsilon / (2 * math.log(2 / delta))
    return max(math.exp(-beta * k) * elasticSensitivity(tree, k, metrics) for k in range(maxK + 1))

def noisyAnswer(trueCount, tree, metrics, epsilon, delta, maxK):
    smooth = smoothSensitivity(tree, metrics, epsilon, delta, maxK)
    return trueCount + np.random.laplace(0, 2 * smooth / epsilon)

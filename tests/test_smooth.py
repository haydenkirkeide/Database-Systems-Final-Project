import math
from flex.tree import Node
from flex.smooth import smoothSensitivity

def makeJoin(leftTable, rightTable, leftKey, rightKey):
    return Node([leftTable, rightTable], Node([leftTable]), Node([rightTable]), leftKey, rightKey)

def testSmoothAtLeastLocal():
    metrics = {"a.id": 3, "b.id": 5}
    tree = makeJoin("a", "b", "a.id", "b.id")
    assert smoothSensitivity(tree, metrics, 1.0, 1e-6, 100) >= 5

def testSmoothMatchesManualMax():
    metrics = {"a.id": 3, "b.id": 5}
    tree = makeJoin("a", "b", "a.id", "b.id")
    beta = 1.0 / (2 * math.log(2 / 1e-6))
    expected = max(math.exp(-beta * k) * (5 + k) for k in range(101))
    assert abs(smoothSensitivity(tree, metrics, 1.0, 1e-6, 100) - expected) < 1e-9

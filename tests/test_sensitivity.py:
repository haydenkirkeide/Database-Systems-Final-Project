from flex.tree import Node
from flex.sensitivity import elasticSensitivity

def makeJoin(leftTable, rightTable, leftKey, rightKey):
    left = Node([leftTable])
    right = Node([rightTable])
    return Node([leftTable, rightTable], left, right, leftKey, rightKey)

def testDistinctTableJoin():
    metrics = {"a.id": 3, "b.id": 5}
    tree = makeJoin("a", "b", "a.id", "b.id")
    assert elasticSensitivity(tree, 0, metrics) == 5
    assert elasticSensitivity(tree, 2, metrics) == 7

def testSelfJoin():
    metrics = {"a.id": 3}
    tree = makeJoin("a", "a", "a.id", "a.id")
    assert elasticSensitivity(tree, 0, metrics) == 7

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

def testThreeTableChain():
    metrics = {"a.id": 2, "b.id": 3, "c.id": 4}
    inner = makeJoin("a", "b", "a.id", "b.id")
    outer = Node(["a", "b", "c"], inner, Node(["c"]), "b.id", "c.id")
    assert elasticSensitivity(inner, 0, metrics) == 3
    assert elasticSensitivity(outer, 0, metrics) == 12
    assert elasticSensitivity(outer, 1, metrics) == 20

def testChainWhereJoinedKeyDominates():
    metrics = {"a.id": 2, "b.id": 3, "c.id": 1}
    inner = makeJoin("a", "b", "a.id", "b.id")
    outer = Node(["a", "b", "c"], inner, Node(["c"]), "b.id", "c.id")
    assert elasticSensitivity(outer, 0, metrics) == 6
    assert elasticSensitivity(outer, 1, metrics) == 12

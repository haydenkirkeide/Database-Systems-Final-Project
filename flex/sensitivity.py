def elasticSensitivity(node, k, metrics):
    if node.isTable:
        return 1
    leftSens = elasticSensitivity(node.left, k, metrics)
    rightSens = elasticSensitivity(node.right, k, metrics)
    leftFreq = metrics[node.leftKey] + k
    rightFreq = metrics[node.rightKey] + k
    if set(node.left.tables) & set(node.right.tables):
        return leftFreq * rightSens + rightFreq * leftSens + leftSens * rightSens
    return max(leftFreq * rightSens, rightFreq * leftSens)

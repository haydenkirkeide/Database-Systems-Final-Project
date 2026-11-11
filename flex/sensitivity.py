def maxFreq(node, key, k, metrics):
    if node.isTable:
        return metrics[key] + k
    if key.split(".")[0] in node.left.tables:
        return maxFreq(node.left, key, k, metrics) * maxFreq(node.right, node.rightKey, k, metrics)
    return maxFreq(node.left, node.leftKey, k, metrics) * maxFreq(node.right, key, k, metrics)

def elasticSensitivity(node, k, metrics):
    if node.isTable:
        return 1
    leftSens = elasticSensitivity(node.left, k, metrics)
    rightSens = elasticSensitivity(node.right, k, metrics)
    leftFreq = maxFreq(node.left, node.leftKey, k, metrics)
    rightFreq = maxFreq(node.right, node.rightKey, k, metrics)
    if set(node.left.tables) & set(node.right.tables):
        return leftFreq * rightSens + rightFreq * leftSens + leftSens * rightSens
    return max(leftFreq * rightSens, rightFreq * leftSens)

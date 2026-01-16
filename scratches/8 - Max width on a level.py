from turtledemo.forest import tree


def BST(tree):
    if tree is None:
        return 0

    def getheight(node):
        if node is None:
            return 0
        return 1 + max(getheight(node.get('left')), getheight(node.get('right')))

    def widthAtLevel(node,level ):
        if node is None:
            return 0
        if level==0:
            return 1
        return widthAtLevel(node.get('left'), level-1) + widthAtLevel(node.get('right'), level-1)

    def findMaxWidth(currentLevel, height):
        if currentLevel>= height:
            return 0
        current = widthAtLevel(tree, currentLevel)
        return max(current,findMaxWidth(currentLevel+1, height))

    return findMaxWidth(0, getheight(tree))


binary_tree_dict = {
        'value': 1,
        'left': {
            'value': 2,
            'left': {
                'value': 4,
                'left': {'value':7, 'left':None, 'right':None},
                'right': None
            },
            'right': {'value': 5, 'left': None, 'right': None}
        },
        'right': {
            'value': 3,
            'left': {'value': 99, 'left': None, 'right': None},
            'right': {
                'value': 6,
                'left':None,
                'right': None}
        }
    }

print(BST(binary_tree_dict))